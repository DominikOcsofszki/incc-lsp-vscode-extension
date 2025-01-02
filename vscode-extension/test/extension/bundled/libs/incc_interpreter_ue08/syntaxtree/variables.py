from dataclasses import dataclass

from incc_interpreter_ue08.LSP import lexer_lsp
from incc_interpreter_ue08.syntaxtree.syntaxtree import *


@dataclass
class AssignExpression(Expression):
    name: str
    expression: Expression
    p: lexer_lsp.P_Info


@dataclass
class VariableExpression(Expression):
    name: str


@dataclass
class LockExpression(Expression):
    names: list[str]
    body: Expression


@dataclass
class LocalExpression(Expression):
    assignments: list[AssignExpression]
    body: Expression
