from dataclasses import dataclass

from incc_interpreter_ue08.syntaxtree.syntaxtree import *


@dataclass
class NumberLiteral(Expression):
    value: str


@dataclass
class BoolLiteral(Expression):
    value: str


@dataclass
class StringLiteral(Expression):
    value: str


@dataclass
class CharLiteral(Expression):
    value: str


@dataclass
class ArrayLiteral(Expression):
    elements: list[Expression]
