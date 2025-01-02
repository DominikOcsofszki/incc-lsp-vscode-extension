from dataclasses import dataclass

from incc_interpreter_ue08.syntaxtree.syntaxtree import *


@dataclass
class LambdaExpression(Expression):
    arg_names: list[str]
    body: Expression
    rest_arg: bool = False


@dataclass
class FunctionExpression(Expression):
    func_name: str
    arg_names: list[str]
    body: Expression


@dataclass
class CallExpression(Expression):
    f: Expression
    arg_exprs: list[Expression]
