
from icecream import ic


def helper_lsp_check(p):
    p_dict = p.__dict__
    # for x in p_dict:
    # print(x)
    # ic(p_dict[x])
    check = ["lexer", "parser"]
    # check = ["lexer", "parser"]
    for x in check:
        ic(p_dict[x].__dict__)
    # exit()


def init_helper_lsp(p):
    # TODO:
    return
    # helper_lsp(p)
    if p and p.__dict__:
        lexer_dict = p.__dict__.get("lexer").__dict__
    else:
        ic("P WAS NOT PASSED!")
        raise RuntimeError("P WAS NOT PASSED!")
    important(lexer_dict)
    # exit()


def helper_lsp(p):
    # print(p)
    if p and p.__dict__:
        lexer_dict = p.__dict__.get("lexer").__dict__
        helper_lexer_dict(lexer_dict)

    # exit()
    ic("ONE RUN")


def not_important(lexer_dict):
    lexre = lexer_dict.get("lexre")
    lexretext = lexer_dict.get("lexretext")
    lexstatere = lexer_dict.get("lexstatere")
    lexstateretext = lexer_dict.get("lexstateretext")
    lexerrorf = lexer_dict.get("lexerrorf")
    lexeoff = lexer_dict.get("lexeoff")
    lexre = ic(lexre)
    lexretext = ic(lexretext)
    lexstatere = ic(lexstatere)
    lexstateretext = ic(lexstateretext)
    lexerrorf = ic(lexerrorf)
    lexeoff = ic(lexeoff)


def maybe_helpful(lexer_dict):
    lexstate = lexer_dict.get("lexstate")
    lexstatestack = lexer_dict.get("lexstatestack")
    lexstateinfo = lexer_dict.get("lexstateinfo")
    lexstateignore = lexer_dict.get("lexstateignore")
    lexstateerrorf = lexer_dict.get("lexstateerrorf")
    lexstateeoff = lexer_dict.get("lexstateeoff")
    lexreflags = lexer_dict.get("lexreflags")
    lexstate = ic(lexstate)
    lexstatestack = ic(lexstatestack)
    lexstateinfo = ic(lexstateinfo)
    lexstateignore = ic(lexstateignore)
    lexstateerrorf = ic(lexstateerrorf)
    lexstateeoff = ic(lexstateeoff)
    lexreflags = ic(lexreflags)


def helper_lexer_dict(lexer_dict):
    lexstaterenames = lexer_dict.get("lexstaterenames")
    lextokens = lexer_dict.get("lextokens")
    lexignore = lexer_dict.get("lexignore")
    lexliterals = lexer_dict.get("lexliterals")
    lexmodule = lexer_dict.get("lexmodule")
    lexoptimize = lexer_dict.get("lexoptimize")
    lextokens_all = lexer_dict.get("lextokens_all")

    lextokens = ic(lextokens)
    lexignore = ic(lexignore)
    lexliterals = ic(lexliterals)
    lexmodule = ic(lexmodule)
    lexoptimize = ic(lexoptimize)
    lextokens_all = ic(lextokens_all)
    lexstaterenames = ic(lexstaterenames)


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
