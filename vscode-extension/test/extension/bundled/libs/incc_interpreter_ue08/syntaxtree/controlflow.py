from dataclasses import dataclass

from incc_interpreter_ue08.syntaxtree.syntaxtree import Expression


@dataclass
class LoopExpression(Expression):
    count: Expression
    body: Expression


@dataclass
class WhileExpression(Expression):
    condition: Expression
    body: Expression


@dataclass
class DoWhileExpression(Expression):
    condition: Expression
    body: Expression


@dataclass
class IfExpression(Expression):
    condition: Expression
    then_body: Expression
    else_body: Expression
