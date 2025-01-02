from icecream import ic

import incc_interpreter_ue08.interpreter as interpreter
from incc_interpreter_ue08.lexer import lexer


def print_all_entries(keys):
    for x in keys:
        print(x, lexer_dict[x])


import_env = interpreter.set_up_env()
# ic(import_env.vars)

import_function_names = [item for item in import_env.vars]
# ic(import_function_names)

import_toks_to_translate = [x for x in import_function_names if str.isupper(x)]
# ic(import_toks_to_translate)

arr = []
arr += lexer.reserved_words
lexer_dict = lexer.__dict__
NOT_IMPORTANT_REST = [
    "LSP_ALL",
    "LSP_CONFIGS",
    "helper_lexer",
    "lex",
    "lexer",
    "lsp_lexer",
    "print_tok_lsp",
]
t_keys = [
    "t_ASSIGN",
    "t_BACKSLASH",
    "t_CHAR",
    "t_COMMA",
    "t_DIVIDE",
    "t_DOT",
    "t_EQS",
    "t_GE",
    "t_GT",
    "t_IDENT",
    "t_LBRACE",
    "t_LBRACKET",
    "t_LE",
    "t_LPAREN",
    "t_LT",
    "t_MINUS",
    "t_NEQS",
    "t_NUMBER",
    "t_PLUS",
    "t_RBRACE",
    "t_RBRACKET",
    "t_RIGHT_ARROW",
    "t_RPAREN",
    "t_SEMICOLON",
    "t_STRING",
    "t_TIMES",
    "t_ignore",
    "t_ignore_COMMENT",
]
reserved = [
    "controlflow_reserved_words",
    "expr_reserved_words",
    "expr_tokens",
    "functions_reserved_words",
    "functions_tokens",
    "lit_reserved_words",
    "lit_tokens",
    "reserved_words",
    "seq_tokens",
    "struct_reserved_words",
    "struct_tokens",
    "tokens",
    "var_reserved_words",
    "var_tokens",
]
print_all_entries(reserved)
