from ply import lex

from incc_interpreter_ue08.lexer.controlflow import *
from incc_interpreter_ue08.lexer.functions import *
from incc_interpreter_ue08.lexer.literals import *
from incc_interpreter_ue08.lexer.operators import *
from incc_interpreter_ue08.lexer.sequences import *

# from incc_interpreter_ue08.lexer.struct import *
from incc_interpreter_ue08.lexer.struct_lexer import *
from incc_interpreter_ue08.lexer.variables import *
from incc_interpreter_ue08.LSP import LSP_ALL, LSP_CONFIGS

reserved_words = set(
    lit_reserved_words
    | expr_reserved_words
    | var_reserved_words
    | controlflow_reserved_words
    | functions_reserved_words
    | struct_reserved_words
)
tokens = list(
    lit_tokens
    | expr_tokens
    | var_tokens
    | seq_tokens
    | functions_tokens
    | struct_tokens
    | reserved_words
)
tokens.extend(["IDENT", "COMMA"])
tokens.extend(["COMMENT"])


t_COMMA = ","


def t_IDENT(t):
    """
    [_a-zA-Z][_a-zA-Z0-9]*
    """

    valUp = t.value.upper()
    if valUp in reserved_words:
        t.type = valUp
        t.value = valUp
    # t.column = LSP_ALL.find_column(LSP_CONFIGS.get_file_text(), t)
    # t.column = 777
    # t.find_column = ">>>>>>>>>>>>>"

    return t


# Define a rule so we can track line numbers


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.lexer.line_start_pos = t.lexpos + len(t.value)
    t.line_start_pos = t.lexpos + len(t.value)


t_ignore = " \t"
# t_ignore = " \t\n"


# t_ignore_COMMENT = r"\#.*"
def t_COMMENT(t):
    r"\#.*"
    # valUp = t.value.upper()
    # if valUp in reserved_words:
    #     t.type = valUp
    #     t.value = valUp
    print(t)

    return t


lexer = lex.lex()
lsp_lexer = lexer.clone()


def helper_lexer(text):
    lsp_lexer.input(text)
    tok_list = []
    while True:
        tok = lsp_lexer.token()
        if not tok:
            break
        tok.column = LSP_ALL.find_column(text, tok)
        # print(tok.__dict__)
        # exit()
        # print(tok.type)
        tok_list.append(print_tok_lsp(tok))
    ic(tok_list)


def print_tok_lsp(tok):
    # print_arr = [tok.lineno-1, tok.column, tok.type, tok.value, tok.lexpos]
    print_arr = [tok.lineno - 1, tok.column - 1, tok.type]
    print(":".join(map(str, print_arr)))
    return print_arr


if __name__ == "__main__":
    text = """
    { a =  123;
     b = 1
     #asdasd 123i13 j j 

     }
    """
    lsp_lexer.input(text)
    while True:
        tok = lsp_lexer.token()
        if not tok:
            break
        print(tok)
