def p_expression_comment_ignore(p):
    """
    expression : COMMENT
    """
    p[0] = p[1]
