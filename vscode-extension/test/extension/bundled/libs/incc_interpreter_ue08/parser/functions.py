from incc_interpreter_ue08.LSP import lsp_create
from incc_interpreter_ue08.syntaxtree.functions import *
from incc_interpreter_ue08.syntaxtree.variables import (
    AssignExpression,
    LocalExpression,
    VariableExpression,
)


def p_ident_list(p):
    """
    ident_list : IDENT
               | IDENT COMMA ident_list
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1], *p[3]]


def p_expr_list(p):
    """
    expr_list : expression
              | expression COMMA expr_list
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1], *p[3]]


def p_expression_lambda(p):
    """
    expression : BACKSLASH RIGHT_ARROW expression
               | BACKSLASH ident_list RIGHT_ARROW expression
               | BACKSLASH ident_list DOT DOT DOT RIGHT_ARROW expression
    """
    match len(p):
        case 4:
            p[0] = LambdaExpression([], p[3])
        case 5:
            p[0] = LambdaExpression(p[2], p[4])
        case 8:
            p[0] = LambdaExpression(p[2], p[7], True)


def p_expression_function(p):
    """
    expression : FUN IDENT RIGHT_ARROW expression
               | FUN IDENT ident_list RIGHT_ARROW expression
               | FUN IDENT ident_list DOT DOT DOT RIGHT_ARROW expression
    """
    #    fun f x -> body
    # => f := local f := \x -> body in f
    match len(p):
        case 5:
            lmbd_expr = LambdaExpression([], p[4])
        case 6:
            lmbd_expr = LambdaExpression(p[3], p[5])
        case 9:
            lmbd_expr = LambdaExpression(p[3], p[8], True)

    local_expr = LocalExpression(
        [AssignExpression(p[2], lmbd_expr, lsp_create.create_p_info_class(p))],
        VariableExpression(p[2]),
    )

    p[0] = AssignExpression(p[2], local_expr, lsp_create.create_p_info_class(p))
    if lsp_configs.print_p_assign:
        lsp_all.assign_expression_parser_work_with_p(p)


def p_expression_call(p):
    """
    expression : expression LPAREN RPAREN
               | expression LPAREN expr_list RPAREN
    """
    if len(p) == 4:
        p[0] = CallExpression(p[1], [])
    else:
        p[0] = CallExpression(p[1], p[3])
