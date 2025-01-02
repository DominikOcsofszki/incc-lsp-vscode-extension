from lsprotocol import types

from incc_lsp.extracts_from_interpreter import (
    # LEXER_TOKS,
    imports_interpreter,
)

III = imports_interpreter.InccInterpreterImported(
    imports_interpreter.reserved_hover_helper_dict
)


def add_all_reserved_word():
    return [str.lower(x) for x in III.LEXER_reserved_words]


def add_helper_reserved_word():
    return ["h." + str.lower(x) for x in III.LEXER_reserved_words]


def get_helper_CompletionItem() -> list[types.CompletionItem]:
    auto_completion = add_helper_reserved_word()
    return [
        types.CompletionItem(label=x, kind=18, detail="TEST") for x in auto_completion
    ]


def get_CompletionItem():
    auto_completion = add_all_reserved_word()
    return [types.CompletionItem(label=x, kind=14) for x in auto_completion]


# def get_IDs_from_data(data: str):
#     arr = LEXER_TOKS.getTokenFromDataDepth(data)
#     arr = set([x.id_name for x in arr])
#     # arr = ["asddasd", "teeeest"]
#     # logging.info(arr)
#     return [types.CompletionItem(label=x, kind=18) for x in arr]
