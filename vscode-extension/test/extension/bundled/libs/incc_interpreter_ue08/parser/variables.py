from ply.yacc import YaccProduction
from incc_interpreter_ue08.LSP import LSP_ALL, LSP_CONFIGS, lsp_create
from incc_interpreter_ue08.syntaxtree.variables import *

from incc_interpreter_ue08.LSP.LSP_ENV import lsp_ref, lsp_def


def p_expression_variable(p: YaccProduction):
    """
    expression : IDENT
    """
    p[0] = VariableExpression(p[1])
    lsp_ref[p[0].name] = [p.lineno(1), p.lexpos(1)]


def p_expression_assign(p: YaccProduction):
    """
    expression : assign_expression
    assign_expression : IDENT ASSIGN expression
    """
    p[0] = (
        p[1]
        if len(p) == 2
        else AssignExpression(p[1], p[3], lsp_create.create_p_info_class(p))
    )
    if len(p) == 2 and LSP_CONFIGS.PRINT_P_ASSIGN:
        LSP_ALL.assign_expression_parser_work_with_p(p)
    else:
        lsp_def[p[0].name] = [p.lineno(1), p.lexpos(1)]


def p_assignment_list(p):
    """
    assignment_list : assign_expression
                    | assign_expression COMMA assignment_list
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1], *p[3]]


def p_lock(p):
    """
    expression : LOCK ident_list IN expression
    """
    p[0] = LockExpression(p[2], p[4])


def p_let(p):
    """
    expression : LOCAL assignment_list IN expression
    """
    p[0] = LocalExpression(p[2], p[4])
