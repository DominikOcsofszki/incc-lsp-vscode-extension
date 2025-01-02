lit_tokens = {"NUMBER", "STRING", "CHAR", "LBRACKET", "RBRACKET"}
lit_reserved_words = {"TRUE", "FALSE"}

t_NUMBER = r"-?\d+(\.\d*)?|\.\d+"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"


def t_STRING(t):
    r'"([^\n"]|\")*"'
    t.value = t.value[1:-1]
    t.lexpos = t.lexpos + 1
    return t


def t_CHAR(t):
    r"'([^\n']|\')'"
    t.value = t.value[1:-1]
    t.lexpos = t.lexpos + 1
    return t
