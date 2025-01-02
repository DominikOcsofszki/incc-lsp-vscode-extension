from dataclasses import dataclass

from incc_interpreter_ue08.LSP import lexer_lsp
from incc_interpreter_ue08.syntaxtree.syntaxtree import Expression
from incc_interpreter_ue08.syntaxtree.variables import AssignExpression


@dataclass
class StructExpression(Expression):
    initializers: list[AssignExpression]
    parent_expr: Expression = None


@dataclass
class MemberAccessExpression(Expression):
    expr: Expression
    member: str
    up_count: int


@dataclass
class MemberAssignExpression(Expression):
    name: str
    expr: Expression
    p: lexer_lsp.P_Info


@dataclass
class ThisExpression(Expression):
    pass
