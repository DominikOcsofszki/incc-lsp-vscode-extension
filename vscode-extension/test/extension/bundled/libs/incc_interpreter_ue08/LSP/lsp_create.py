import re
from copy import deepcopy

from icecream import ic

from incc_interpreter_ue08.LSP import lexer_lsp


def create_p_info_class(p):
    # call1_important(p)
    # return p
    # return deepcopy(p)
    return lexer_lsp.P_Info(p)


def call1_important(p):
    if p and p.__dict__:
        lexer_dict = p.__dict__.get("lexer").__dict__
    else:
        ic("P WAS NOT PASSED!")
        raise RuntimeError("P WAS NOT PASSED!")
    # important(lexer_dict)
    call2_working(lexer_dict)


def call2_working(lexer_dict):
    lexmatch = lexer_dict.get("lexmatch")
    lexdata = lexer_dict.get("lexdata")
    item_range_arr = lexmatch.span()
    match = lexmatch.group()
    match_from_index = lexdata[item_range_arr[0] : item_range_arr[1]]
    # match_from_index = lexdata[item_range_arr[0]-3: item_range_arr[1]+3]
    ic("============")
    # ic(match)
    # ic(item_range_arr)
    ic(match)
    ic(match_from_index)
    # ic(lexdata[31:-1])
    # exit()
    # ic(lexdata)
    # ic(item_range_arr[0])
    # ic(item_range_arr[1])
    # ic(lexdata[2])

    # exit()


def important(lexer_dict):
    lineno = lexer_dict.get("lineno")
    lineno = ic(lineno)
    lexmatch = lexer_dict.get("lexmatch")
    lexdata = lexer_dict.get("lexdata")
    lexpos = lexer_dict.get("lexpos")
    lexlen = lexer_dict.get("lexlen")
    lexdata = ic(lexdata)
    lexpos = ic(lexpos)
    lexlen = ic(lexlen)
    lexmatch = ic(lexmatch)
    item_range_arr = lexmatch.span()
    match = lexmatch.group()
    ic(match)
    ic(item_range_arr)
    # ic(item_range_arr[0])
    # ic(item_range_arr[1])
    # ic(lexdata[2])
    x = lexdata[item_range_arr[0] : item_range_arr[1]]
    ic(match)
    ic(x)
    # exit()
