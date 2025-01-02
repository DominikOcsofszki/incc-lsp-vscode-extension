from copy import deepcopy
from icecream import ic
from incc_interpreter_ue08.LSP import LSP_CONFIGS
from incc_interpreter_ue08.LSP._mlog import mlogger_func


def get_lex_dict_from_p(p):
    if p and p.__dict__:
        lexer_dict = p.__dict__.get("lexer").__dict__
    else:
        raise RuntimeError("P WAS NOT PASSED!")
    return deepcopy(lexer_dict)


LIST_IDS = []


def assign_expression_parser_work_with_p(p):
    mlogger_func("assign_expression_parser_work_with_p", 5)
    lex_dict = get_lex_dict_from_p(p)
    match = lex_dict.get("lexmatch")
    mlog(lex_dict.get("lexmatch"), 2)
    span = match.span()
    LIST_IDS.append(match)
    # ic(lex_dict.get("lexdata")[span[0] : span[1]])
    # exit()
    mlog(LIST_IDS, 2)


all = [
    "lexre",
    "lexretext",
    "lexstatere",
    "lexstateretext",
    "lexstaterenames",
    "lexstate",
    "lexstatestack",
    "lexstateinfo",
    "lexstateignore",
    "lexstateerrorf",
    "lexstateeoff",
    "lexreflags",
    "lexdata",
    "lexpos",
    "lexlen",
    "lexerrorf",
    "lexeoff",
    "lextokens",
    "lexignore",
    "lexliterals",
    "lexmodule",
    "lineno",
    "lexoptimize",
    "lextokens_all",
    "lexmatch",
]


def get_text():
    print(LSP_CONFIGS.FILE_TEXT)
    return LSP_CONFIGS.FILE_TEXT


def find_column(input, token):
    line_start = input.rfind("\n", 0, token.lexpos) + 1
    column = (token.lexpos - line_start) + 1
    # ic(column)
    return column
