from typing import List, Tuple
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Lib.LinearCode import LinearCode
from Lib import RiscV
from Lib.RiscV import Condition
from Lib import Operands
from antlr4.tree.Trees import Trees
from Lib.Errors import MiniCInternalError, MiniCUnsupportedError

"""
CAP, MIF08, three-address code generation + simple alloc
This visitor constructs an object of type "LinearCode".
"""


class MiniCCodeGen3AVisitor(MiniCVisitor):

    _current_function: LinearCode

    def __init__(self, debug, parser):
        super().__init__()
        self._parser = parser
        self._debug = debug
        self._functions = []
        self._lastlabel = ""

    def get_functions(self) -> List[LinearCode]:
        return self._functions

    def printSymbolTable(self):  # pragma: no cover
        print("--variables to temporaries map--")
        for keys, values in self._symbol_table.items():
            print(keys + '-->' + str(values))

    # handle variable decl

    def visitVarDecl(self, ctx) -> None:
        type_str = ctx.typee().getText()
        vars_l = self.visit(ctx.id_l())
        for name in vars_l:
            if name in self._symbol_table:
                raise MiniCInternalError(
                    "Variable {} has already been declared".format(name))
            else:
                tmp = self._current_function.fdata.fresh_tmp()
                self._symbol_table[name] = tmp
                if type_str not in ("int", "bool"):
                    raise MiniCUnsupportedError("Unsupported type " + type_str)
                # Initialization to 0 or False, both represented with 0
                self._current_function.add_instruction(
                    RiscV.li(tmp, Operands.Immediate(0)))

    def visitIdList(self, ctx) -> List[str]:
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # expressions

    def visitParExpr(self, ctx) -> Operands.Temporary:
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx) -> Operands.Temporary:
        val = Operands.Immediate(int(ctx.getText()))
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.li(dest_temp, val))
        return dest_temp

    def visitFloatAtom(self, ctx) -> Operands.Temporary:
        raise MiniCUnsupportedError("float literal")

    def visitBooleanAtom(self, ctx) -> Operands.Temporary:
        # true is 1 false is 0
        val = Operands.Immediate(1 if ctx.getText() == "true" else 0)
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.li(dest_temp, val))
        return dest_temp

    def visitIdAtom(self, ctx) -> Operands.Temporary:
        try:
            # get the temporary associated to id
            return self._symbol_table[ctx.getText()]
        except KeyError:  # pragma: no cover
            raise MiniCInternalError(
                "Undefined variable {}, this should have failed to typecheck."
                .format(ctx.getText())
            )

    def visitStringAtom(self, ctx) -> Operands.Temporary:
        raise MiniCUnsupportedError("string atom")

    # now visit expressions

    def visitAtomExpr(self, ctx) -> Operands.Temporary:
        return self.visit(ctx.atom())

    def visitAdditiveExpr(self, ctx) -> Operands.Temporary:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        # Je regarde le symbole myop pour savoir quelle opération je fais.
        if ctx.myop.type == MiniCParser.PLUS:
            dest_temp = self._current_function.fdata.fresh_tmp()
            self._current_function.add_instruction(
                RiscV.add(dest_temp, lval, rval))
            return dest_temp
        elif ctx.myop.type == MiniCParser.MINUS:
            dest_temp = self._current_function.fdata.fresh_tmp()
            self._current_function.add_instruction(
                RiscV.sub(dest_temp, lval, rval))
            return dest_temp
        else:
            raise MiniCInternalError(
                "Unknown additive operator " + ctx.myop.getText())

    def visitOrExpr(self, ctx) -> Operands.Temporary:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.li(dest_temp, Operands.Immediate(1))
        )
        val_true = self._current_function.fdata.fresh_tmp()
        end_function = self._current_function.fdata.fresh_label('end_function')
        self._current_function.add_instruction(
            RiscV.li(val_true, Operands.Immediate(1))
        )
        # If lval is at least true then entire expr is true by default.
        self._current_function.add_instruction(
            RiscV.conditional_jump(
                end_function, lval, Condition('beq'), val_true)
        )
        # Since lval is false we need to check rval to see if entire expr is false.
        self._current_function.add_instruction(
            RiscV.conditional_jump(
                end_function, rval, Condition('beq'), val_true)
        )
        self._current_function.add_instruction(
            RiscV.li(dest_temp, Operands.Immediate(0))
        )
        self._current_function.add_label(end_function)
        return dest_temp

    def visitAndExpr(self, ctx) -> Operands.Temporary:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        val_false = self._current_function.fdata.fresh_tmp()
        val_true = self._current_function.fdata.fresh_tmp()
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.li(dest_temp, Operands.Immediate(0))
        )
        end_function = self._current_function.fdata.fresh_label('end_function')
        self._current_function.add_instruction(
            RiscV.li(val_false, Operands.Immediate(0))
        )
        self._current_function.add_instruction(
            RiscV.li(val_true, Operands.Immediate(1))
        )
        self._current_function.add_instruction(
            RiscV.conditional_jump(
                end_function, lval, Condition('beq'), val_false)
        )
        self._current_function.add_instruction(
            RiscV.li(dest_temp, Operands.Immediate(1))
        )
        # We need to check the other expression to see if its still true.
        self._current_function.add_instruction(
            RiscV.conditional_jump(
                end_function, rval, Condition('beq'), val_true)
        )
        self._current_function.add_instruction(
            RiscV.li(dest_temp, Operands.Immediate(0))
        )
        self._current_function.add_label(end_function)
        return dest_temp

    def visitEqualityExpr(self, ctx) -> Operands.Temporary:
        return self.visitRelationalExpr(ctx)

    def visitRelationalExpr(self, ctx) -> Operands.Temporary:
        assert ctx.myop is not None
        c = Condition(ctx.myop.type)
        if self._debug:
            print("relational expression:")
            print(Trees.toStringTree(ctx, None, self._parser))
            print("Condition:", c)
        val_true = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.li(val_true, Operands.Immediate(1)))

        end_function = self._current_function.fdata.fresh_label('end_function')
        else_block = self._current_function.fdata.fresh_label('else_block')

        # Met dest temp à 1 (= true) de base.
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.li(dest_temp, Operands.Immediate(1)))

        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        # Si eval de la condition est vraie alors je peux passer à la fin de la fonction.
        self._current_function.add_instruction(
            RiscV.conditional_jump(end_function, lval, c, rval)
        )
        # add label de else.
        self._current_function.add_label(else_block)
        # je met le dest temp à 0 (= false)
        self._current_function.add_instruction(
            RiscV.li(dest_temp, Operands.Immediate(0)))
        # add label de fin de fonction.
        self._current_function.add_label(end_function)
        # je return le dest temp.
        return dest_temp

    def visitMultiplicativeExpr(self, ctx) -> Operands.Temporary:
        assert ctx.myop is not None
        div_by_zero_lbl = self._current_function.fdata.get_label_div_by_zero()
        raise NotImplementedError()  # TODO (Exercise 8)

    def visitNotExpr(self, ctx) -> Operands.Temporary:
        val = self.visit(ctx.expr())
        dest_temp = self._current_function.fdata.fresh_tmp()
        temp_val_1 = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.li(temp_val_1, Operands.Immediate(1)))
        self._current_function.add_instruction(
            RiscV.xor(dest_temp, val, temp_val_1))
        return dest_temp

    def visitUnaryMinusExpr(self, ctx) -> Operands.Temporary:
        val = self.visit(ctx.expr())
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.sub(dest_temp, Operands.ZERO, val))
        return dest_temp

    def visitProgRule(self, ctx) -> None:
        self.visitChildren(ctx)

    def visitFuncDef(self, ctx) -> None:
        funcname = ctx.ID().getText()
        self._current_function = LinearCode(funcname)
        self._symbol_table = dict()

        self.visit(ctx.vardecl_l())
        self.visit(ctx.block())
        self._current_function.add_comment("Return at end of function:")
        # This skeleton doesn't deal properly with functions, and
        # hardcodes a "return 0;" at the end of function. Generate
        # code for this "return 0;".
        self._current_function.add_instruction(
            RiscV.li(Operands.A0, Operands.Immediate(0)))
        self._functions.append(self._current_function)
        del self._current_function

    def visitAssignStat(self, ctx) -> None:
        if self._debug:
            print("assign statement, rightexpression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        expr_temp = self.visit(ctx.expr())
        name = ctx.ID().getText()
        self._current_function.add_instruction(
            RiscV.mv(self._symbol_table[name], expr_temp))

    def visitIfStat(self, ctx) -> None:
        if self._debug:
            print("if statement")
        exprEval = self.visit(ctx.expr())
        end_if_label = self._current_function.fdata.fresh_label("end_if")
        lelse = self._current_function.fdata.fresh_label("else")
        # Load zero value in a temp
        immZeroTemp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.li(immZeroTemp, Operands.Immediate(0)))
        # if expr is false then go to else block.
        self._current_function.add_instruction(
            RiscV.conditional_jump(
                lelse, exprEval, Condition('beq'), immZeroTemp)
        )
        # Then block
        self.visit(ctx.then_block)
        # Jump to then end to skip else block.
        self._current_function.add_instruction(
            RiscV.jump(end_if_label)
        )
        # Else block
        self._current_function.add_label(lelse)
        # Check if else block is present or not.
        if ctx.ELSE() is not None:
            self.visit(ctx.else_block)
        self._current_function.add_label(end_if_label)

    def visitWhileStat(self, ctx) -> None:
        if self._debug:
            print("while statement, condition is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
            print("and block is:")
            print(Trees.toStringTree(ctx.stat_block(), None, self._parser))

        start_while = self._current_function.fdata.fresh_label(
            "start_while")
        end_while = self._current_function.fdata.fresh_label("end_while")
        immFalseTemp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(
            RiscV.li(immFalseTemp, Operands.Immediate(0)))

        # Start loop.
        self._current_function.add_label(start_while)
        cond = self.visit(ctx.expr())
        # if expr is false then go to end.
        self._current_function.add_instruction(
            RiscV.conditional_jump(
                end_while, cond, Condition('beq'), immFalseTemp)
        )
        # Execute while block.
        self.visit(ctx.body)
        # Jump to start of while.
        self._current_function.add_instruction(
            RiscV.jump(start_while)
        )
        self._current_function.add_label(end_while)

    def visitPrintlnintStat(self, ctx) -> None:
        expr_loc = self.visit(ctx.expr())
        if self._debug:
            print("print_int statement, expression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        self._current_function.add_instruction_PRINTLN_INT(expr_loc)

    def visitPrintlnboolStat(self, ctx) -> None:
        expr_loc = self.visit(ctx.expr())
        self._current_function.add_instruction_PRINTLN_INT(expr_loc)

    def visitPrintlnfloatStat(self, ctx) -> None:
        raise MiniCUnsupportedError("Unsupported type float")

    def visitPrintlnstringStat(self, ctx) -> None:
        raise MiniCUnsupportedError("Unsupported type string")

    def visitStatList(self, ctx) -> None:
        for stat in ctx.stat():
            self._current_function.add_comment(
                Trees.toStringTree(stat, None, self._parser))
            self.visit(stat)
