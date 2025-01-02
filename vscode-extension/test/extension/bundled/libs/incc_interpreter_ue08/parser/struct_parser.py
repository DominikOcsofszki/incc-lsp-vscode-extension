from incc_interpreter_ue08.LSP.LSP_IMPORT_ALL import *
from incc_interpreter_ue08.syntaxtree.functions import LambdaExpression
from incc_interpreter_ue08.syntaxtree.struct import (
    MemberAccessExpression,
    MemberAssignExpression,
    StructExpression,
    ThisExpression,
)
from incc_interpreter_ue08.syntaxtree.variables import VariableExpression


def p_initializer_list(p):
    """
    initializer_list : initializer
                     | initializer SEMICOLON initializer_list
    """
    p[0] = p[1] if len(p) == 2 else [*p[1], *p[3]]


def p_initializer(p):
    """
    initializer : member_assign_expression
                | SET member_assign_expression
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        x = p[2].name
        name = f"set_{x}"
        set_lmbd = LambdaExpression(
            [x],
            MemberAssignExpression(x, VariableExpression(x)),
            lsp_create.create_p_info_class(p),
        )
        p[0] = [
            p[2],
            MemberAssignExpression(name, set_lmbd, lsp_create.create_p_info_class(p)),
        ]
    if LSP_CONFIGS.PRINT_P_ASSIGN:
        LSP_ALL.assign_expression_parser_work_with_p(p)


def p_expr_struct(p):
    """
    expression : STRUCT LBRACE RBRACE
               | STRUCT LBRACE initializer_list RBRACE
    """
    p[0] = StructExpression([] if len(p) == 4 else p[3])


def p_struct_extension(p):
    """
    expression : EXTEND expression LBRACE RBRACE
               | EXTEND expression LBRACE initializer_list RBRACE
    """
    p[0] = StructExpression([] if len(p) == 5 else p[4], p[2])


def p_dots(p):
    """
    dots : DOT
         | DOT dots
    """
    if len(p) == 2:
        p[0] = 0
    else:
        p[0] = 1 + p[2]


def p_member_access(p):
    """
    expression : dots IDENT
               | expression dots IDENT
    """
    if len(p) == 3:
        p[0] = MemberAccessExpression(ThisExpression(), p[2], p[1])
    else:
        p[0] = MemberAccessExpression(p[1], p[3], p[2])


def p_member_assign(p):
    """
    expression : member_assign_expression
    member_assign_expression : dots IDENT ASSIGN expression
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[1] != 0:
            raise SyntaxError(f"Syntax error at token '.'")

        p[0] = MemberAssignExpression(p[2], p[4], lsp_create.create_p_info_class(p))


def p_this(p):
    """
    expression : THIS
    """
    p[0] = ThisExpression()
