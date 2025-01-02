# type: ignore
# ignore name conflict

from doctest import debug
from ply import yacc

from incc_interpreter_ue08.lexer.lexer import helper_lexer, lexer, tokens
from incc_interpreter_ue08.LSP import LSP_CONFIGS
from incc_interpreter_ue08.parser.controlflow import *
from incc_interpreter_ue08.parser.functions import *
from incc_interpreter_ue08.parser.literals import *
from incc_interpreter_ue08.parser.operators import *
from incc_interpreter_ue08.parser.sequences import *
from incc_interpreter_ue08.parser.struct_parser import *
from incc_interpreter_ue08.parser.variables import *
from incc_interpreter_ue08.parser.incc_lsp import *

precedence = [
    ["nonassoc", "THEN"],
    ["nonassoc", "ELSE", "DO", "WHILE", "IN"],
    ["left", "COMMA"],
    ["right", "ASSIGN"],
    ["right", "RIGHT_ARROW"],
    ["left", "OR", "NOR", "XOR"],
    ["left", "IMP"],
    ["left", "AND", "NAND"],
    ["left", "EQS", "NEQS", "EQ", "NEQ"],
    ["left", "LT", "GT", "LE", "GE"],
    ["left", "PLUS", "MINUS"],
    ["left", "TIMES", "DIVIDE"],
    ["right", "NOT", "UMINUS", "UPLUS"],
    ["right", "LPAREN", "LBRACKET", "DOT"],
]


# def p_error(p):
#     raise SyntaxError(f"XXX Syntax error at token {p}")


def p_error(p):
    last_token = parser.symstack[-1] if parser.symstack else None
    if last_token:
        raise SyntaxError(f"Syntax error after token {last_token}")
    raise SyntaxError(f"Syntax error at token {p}")


parser = yacc.yacc(start="expression")


def parse_expr(text: str, reset_lineno=True) -> Expression:
    LSP_CONFIGS.FILE_TEXT = text
    if reset_lineno:
        lexer.lineno = 0

    if LSP_CONFIGS.PRINT_TOKENS:
        help_print_tokens(text)
        # items = parser.parse(input=text, lexer=lexer)
        items = parser.parse(input=text, lexer=lexer, tracking=True)
        print(
            "START:PARSETREE=========================================================================",
            flush=True,
        )
        print(
            "START:PARSETREE=========================================================================",
            flush=True,
        )
        if type(items) is not SequenceExpression:
            print(items)
        else:
            for i, item in enumerate(items):
                print(str(i) + ":", item, flush=True)
        print(
            "END:PARSETREE=========================================================================",
            flush=True,
        )
        print(
            "END:PARSETREE=========================================================================",
            flush=True,
        )
        exit()
    else:
        # exit()
        # return parser.parse(input=text, lexer=lexer)
        return parser.parse(input=text, lexer=lexer, tracking=True)


def help_print_tokens(text):
    if LSP_CONFIGS.PRINT_TOKENS:
        helper_lexer(text)
        # exit()


def find_column(input, lexpos):
    line_start = input.rfind("\n", 0, lexpos) + 1
    return (lexpos - line_start) + 1


if __name__ == "__main__":
    # fname = "/Users/dominik/HOME/BA/DEV/MAIN/tests/incc_files/struct_sem.incc24"
    # with open(fname, "r") as f:
    #     data = f.read()
    data = """
    {
aaa=123;
 bbb=123;
  ccc=123;
   aaa
}
    """
    a = find_column(data, 28)
    print(a)
    x = parser.parse(input=data, lexer=lexer, tracking=True)
