from incc_interpreter_ue08.lexer import lexer
from incc_interpreter_ue08.LSP.LSP_ENV import (
    get_lsp_ref,
    get_lsp_def,
)
from incc_interpreter_ue08.parser import parser as PARSER


def parse_for_def_ref(text):
    PARSER.parse_expr(text)
    def_ = get_lsp_def()
    ref_ = get_lsp_ref()
    print(def_)
    print(ref_)
    # reset_lsp_ref()
    # reset_lsp_def()
    return def_, ref_


if __name__ == "__main__":
    text = """{a=1;b=2;b=123}"""
    parse_for_def_ref(text)
