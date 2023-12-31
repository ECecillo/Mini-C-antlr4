from Lib import RiscV
from Lib.Operands import Temporary, Operand, S
from Lib.Statement import Instruction
from Lib.Allocator import Allocator
from typing import List, Dict


class AllInMemAllocator(Allocator):

    def replace(self, old_instr: Instruction) -> List[Instruction]:
        """Replace Temporary operands with the corresponding allocated
        memory location. FP points to the stack."""
        numreg = 1
        before: List[Instruction] = []
        after: List[Instruction] = []
        subst: Dict[Operand, Operand] = {}
        # TODO (Exercise 7): compute before,after,args.
        for arg in old_instr.args():
            if isinstance(arg, Temporary):
                before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                after.append(RiscV.sd(S[numreg], arg.get_alloced_loc()))
                subst[arg] = S[numreg]
                numreg += 1
        # TODO (Exercise 7): and if so, generate ld/sd accordingly. Replace the
        # TODO (Exercise 7): temporary with S[1], S[2] or S[3] physical registers.
        new_instr = old_instr.substitute(subst)
        return before + [new_instr] + after

    def prepare(self) -> None:
        """Allocate all temporaries to memory.
        Invariants:
        - Expanded instructions can use s2 and s3
          (to store the values of temporaries before the actual instruction).
        """
        self._fdata._pool.set_temp_allocation(
            {temp: self._fdata.fresh_offset()
             for temp in self._fdata._pool.get_all_temps()})
