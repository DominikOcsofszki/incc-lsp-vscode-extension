from dataclasses import dataclass

from incc_interpreter_ue08.syntaxtree.syntaxtree import Expression


@dataclass
class OperatorExpression(Expression):
    operator: str
    operands: list[Expression]
