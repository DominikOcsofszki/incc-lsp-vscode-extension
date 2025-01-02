from incc_interpreter_ue08.syntaxtree.sequences import *


def p_expressions(p):
    """
    sequence : sequence SEMICOLON expression
             | expression
    """
    p[0] = [p[1]] if len(p) == 2 else [*p[1], p[3]]


def p_sequence(p):
    """
    expression : LBRACE sequence RBRACE
    """
    p[0] = SequenceExpression(p[2])
