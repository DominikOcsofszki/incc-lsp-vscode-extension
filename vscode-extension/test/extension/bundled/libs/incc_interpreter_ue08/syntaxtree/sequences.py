from dataclasses import dataclass

from incc_interpreter_ue08.syntaxtree.syntaxtree import *


@dataclass
class SequenceExpression(Expression):
    expressions: list[Expression]

    def __iter__(self):
        yield from self.expressions
