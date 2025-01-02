from icecream import ic

from incc_interpreter_ue08.lexer.lexer import *

glob = globals()


def check_lexer():
    for x in globals():
        print(x)


# check_lexer()


def lexer_reserved():
    ic(glob.get("struct_reserved_words"))
    ic(glob.get("var_reserved_words"))
    ic(glob.get("reserved_words"))
    ic(glob.get("lit_reserved_words"))
    ic(glob.get("functions_reserved_words"))
    ic(glob.get("expr_reserved_words"))
    ic(glob.get("controlflow_reserved_words"))


def lexer_all_tokens():
    tokkens = glob.get("tokens")
    ic(tokkens)
    return tokens


def lexer_infos():

    ic(glob.get("check_lexer"))
    ic(glob.get("expr_tokens"))
    ic(glob.get("functions_tokens"))
    ic(glob.get("ic"))
    ic(glob.get("lex"))
    ic(glob.get("lexer"))
    ic(glob.get("lit_tokens"))
    ic(glob.get("seq_tokens"))
    ic(glob.get("struct_tokens"))
    ic(glob.get("tokens"))
    ic(glob.get("var_tokens"))


def lexer_t_():
    ic(glob.get("t_ASSIGN"))
    ic(glob.get("t_BACKSLASH"))
    ic(glob.get("t_CHAR"))
    ic(glob.get("t_COMMA"))
    ic(glob.get("t_DIVIDE"))
    ic(glob.get("t_DOT"))
    ic(glob.get("t_EQS"))
    ic(glob.get("t_GE"))
    ic(glob.get("t_GT"))
    ic(glob.get("t_IDENT"))
    ic(glob.get("t_LBRACE"))
    ic(glob.get("t_LBRACKET"))
    ic(glob.get("t_LE"))
    ic(glob.get("t_LPAREN"))
    ic(glob.get("t_LT"))
    ic(glob.get("t_MINUS"))
    ic(glob.get("t_NEQS"))
    ic(glob.get("t_NUMBER"))
    ic(glob.get("t_PLUS"))
    ic(glob.get("t_RBRACE"))
    ic(glob.get("t_RBRACKET"))
    ic(glob.get("t_RIGHT_ARROW"))
    ic(glob.get("t_RPAREN"))
    ic(glob.get("t_SEMICOLON"))
    ic(glob.get("t_STRING"))
    ic(glob.get("t_TIMES"))
    ic(glob.get("t_ignore"))
    ic(glob.get("t_ignore_COMMENT"))
    ic(glob.get("t_newline"))


lexer_t_()

for x in lexer_all_tokens():
    ic(glob.get("t_" + x))
