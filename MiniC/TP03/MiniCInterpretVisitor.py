# Visitor to *interpret* MiniC files
from typing import Dict, List, cast
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Lib.Errors import MiniCRuntimeError, MiniCInternalError, MiniCTypeError

MINIC_VALUE = int | str | bool | float | List['MINIC_VALUE']


class MiniCInterpretVisitor(MiniCVisitor):

    _memory: Dict[str, MINIC_VALUE]

    def __init__(self):
        self._memory = dict()  # store all variable ids and values.
        self.has_main = False

    # visitors for variable declarations

    def visitVarDecl(self, ctx) -> None:
        # Initialise all variables in self._memory
        type_str: str = ctx.typee().getText()
        vars_l: List[str] = self.visit(ctx.id_l())
        for name in vars_l:
            if name in self._memory:
                raise MiniCRuntimeError(
                    "Variable {0} has already been declared.".format(name)
                )
            if type_str == 'int':
                self._memory[name] = 0
            elif type_str == 'float':
                self._memory[name] = 0.0
            elif type_str == 'bool':
                self._memory[name] = False
            elif type_str == 'string':
                self._memory[name] = ""

    def visitIdList(self, ctx) -> List[str]:
        list_variables = self.visit(ctx.id_l())
        list_variables.append(ctx.ID().getText())
        return list_variables

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # visitors for atoms --> value

    def visitParExpr(self, ctx) -> MINIC_VALUE:
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx) -> int:
        return int(ctx.getText())  # return int(var);

    def visitFloatAtom(self, ctx) -> float:
        return float(ctx.getText())  # return float(var);

    def visitBooleanAtom(self, ctx) -> bool:
        return ctx.getText() == "true"  # return true rule.

    def visitIdAtom(self, ctx) -> MINIC_VALUE:
        variable_name: str = ctx.getText()
        return self._memory[variable_name]  # find value of x and return it.

    def visitStringAtom(self, ctx) -> str:
        return ctx.getText()[1:-1]  # Remove the ""

    # visit expressions

    def visitAtomExpr(self, ctx) -> MINIC_VALUE:
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx) -> bool:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval | rval

    def visitAndExpr(self, ctx) -> bool:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval & rval

    def visitEqualityExpr(self, ctx) -> bool:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        # be careful for float equality
        if ctx.myop.type == MiniCParser.EQ:
            return lval == rval
        else:
            return lval != rval

    def visitRelationalExpr(self, ctx) -> bool:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.LT:
            return lval < rval  # equivalent to rule return e1.visit()<e2.visit()
        elif ctx.myop.type == MiniCParser.LTEQ:
            return lval <= rval
        elif ctx.myop.type == MiniCParser.GT:
            return lval > rval
        elif ctx.myop.type == MiniCParser.GTEQ:
            return lval >= rval
        else:
            raise MiniCInternalError(
                f"Unknown comparison operator '{ctx.myop}'"
            )

    def visitAdditiveExpr(self, ctx) -> MINIC_VALUE:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.PLUS:
            if any(isinstance(x, str) for x in (lval, rval)):
                return '{}{}'.format(lval, rval)
            else:
                return lval + rval
        elif ctx.myop.type == MiniCParser.MINUS:
            return lval - rval
        else:
            raise MiniCInternalError(
                f"Unknown additive operator '{ctx.myop}'")

    def visitMultiplicativeExpr(self, ctx) -> MINIC_VALUE:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.MULT:
            return lval * rval
        elif ctx.myop.type == MiniCParser.DIV:
            if rval == 0 or rval == 0.0 or rval == 0.00:
                raise MiniCRuntimeError("Division by 0")
            elif isinstance(lval, int):  # integer division
                return lval // rval
            else:  # float division
                return lval / rval
        elif ctx.myop.type == MiniCParser.MOD:
            if rval == 0 or rval == 0.0 or rval == 0.00:
                raise MiniCRuntimeError("Division by 0")
            else:
                return lval % rval
        else:
            raise MiniCInternalError(
                f"Unknown multiplicative operator '{ctx.myop}'")

    def visitNotExpr(self, ctx) -> bool:
        return not self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx) -> MINIC_VALUE:
        return -self.visit(ctx.expr())

    # visit statements

    def visitPrintlnintStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        print(val)

    def visitPrintlnfloatStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        val = f"{val:.2f}"
        print(val)

    def visitPrintlnboolStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        print('1' if val else '0')

    def visitPrintlnstringStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        print(val)

    def visitAssignStat(self, ctx) -> None:
        variable_name = ctx.ID().getText()
        # recursively visit the expression to get the value.
        value = self.visit(ctx.expr())
        self._memory[variable_name] = value

    def visitIfStat(self, ctx) -> None:
        # We don't need to check IF token is here because ANTLR already recognized it.
        # evaluate the expression inside parenthesis
        result_if_eval_expr = self.visit(ctx.expr())
        if result_if_eval_expr:  # if evaluation of the expression is true
            # recursively visit the then block.
            self.visit(ctx.then_block)
        else:
            # Continue if else statement here.
            is_else = ctx.ELSE() is not None
            if is_else:
                self.visit(ctx.else_block)
            # if no else block or if false continue execution and do nothing.

    def visitWhileStat(self, ctx) -> None:
        result_while_eval_expr = self.visit(ctx.expr())
        # While this expression is true, we execute the body of the while.
        while result_while_eval_expr:
            self.visit(ctx.body)
            # We reevalutate the expr to see if we need to break the wile loop.
            result_while_eval_expr = self.visit(ctx.expr())
        # We continue the execution of the program by doing nothing here.

    def visitForStat(self, ctx) -> None:
        # if assignement passed and then update it in memory.
        if (ctx.index_assign is not None):
            self.visit(ctx.index_assign)
        # default is true if no expr is put, in this case we need to add a div by 0 to stop program with counter to set limit.
        result_for_eval_expr = True
        if (ctx.expr() is not None):
            result_for_eval_expr = self.visit(ctx.expr())
        # While this expression is true, we execute the body of the for.
        while result_for_eval_expr:
            # We execute the body of the for loop.
            self.visit(ctx.body)
            # Increment the index to be re-evaluate by following for_expr.
            if ctx.index_mutation() is not None:
                self.visit(ctx.index_mutation())
            # re-evaulation of the for expression at the end.
            if (ctx.expr() is not None):
                result_for_eval_expr = self.visit(ctx.expr())
        # We continue the execution of the program by doing nothing here.

    def visitIndexPlusPlus(self, ctx) -> None:
        index_name = ctx.ID().getText()
        index_to_update = self._memory[index_name]
        if isinstance(index_to_update, int):
            self._memory[index_name] = index_to_update + int(1)
        else:
            raise MiniCTypeError("Index is not an integer")

    def visitIndexMinusMinus(self, ctx) -> None:
        index_name = ctx.ID().getText()
        index_to_update = self._memory[index_name]
        if isinstance(index_to_update, int):
            self._memory[index_name] = index_to_update - int(1)
        else:
            raise MiniCTypeError("Index is not an integer")

    def visitIndexOperatorAssignment(self, ctx) -> None:
        assert ctx.myop is not None
        index_name = ctx.ID().getText()
        op = ctx.myop.type
        value = self.visit(ctx.expr())
        index_to_update = self._memory[index_name]
        if value is not int:
            raise MiniCTypeError("Index is not an integer")
        if (op == MiniCParser.PLUS):
            if isinstance(index_to_update, int):
                self._memory[index_name] = index_to_update + int(value)
            else:
                raise MiniCTypeError("Index is not an integer")
        if (op == MiniCParser.MINUS):
            if isinstance(index_to_update, int):
                self._memory[index_name] = index_to_update + int(value)
            else:
                raise MiniCTypeError("Index is not an integer")

    def visitProgRule(self, ctx) -> None:
        self.visitChildren(ctx)
        if not self.has_main:
            # A program without a main function is compilable (hence
            # it's not a typing error per se), but not executable,
            # hence we consider it a runtime error.
            raise MiniCRuntimeError("No main function in file")

    # Visit a function: ignore if non main!
    def visitFuncDef(self, ctx) -> None:
        funname = ctx.ID().getText()
        if funname == "main":
            self.has_main = True
            self.visit(ctx.vardecl_l())
            self.visit(ctx.block())
        else:
            raise MiniCRuntimeError(
                "Functions are not supported in evaluation mode")

    def visitFuncCall(self, ctx) -> None:  # pragma: no cover
        raise MiniCRuntimeError(
            "Functions are not supported in evaluation mode")
