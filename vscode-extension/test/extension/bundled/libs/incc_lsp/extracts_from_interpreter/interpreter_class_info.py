from lsprotocol import types as types

from incc_lsp.extracts_from_interpreter import (
    import_keys,
    imported_helper,
    interpreter_tokens,
)

reserved_help = {}


class InccInterpreterImported:
    # def __init__(self, reserved_help):
    def __init__(self, res):
        self.reserved_help = reserved_help
        self.import_toks_to_translate = import_keys.import_toks_to_translate
        self.import_toks_literal = import_keys.import_toks_literal
        self.t_keys = interpreter_tokens.t_keys
        self.LEXER_import_modul = interpreter_tokens.lexer
        self.LEXER_reserved_words = self.LEXER_import_modul.reserved_words
        self.LEXER_tokens = self.LEXER_import_modul.tokens
        self.COMPLETION_ITEMS_reserved_words_with_help_info = (
            self.add_info_to_reserved_words(self.reserved_help)
        )

    def printm(self, print_f=print):
        print_f(self.LEXER_reserved_words)
        print_f(self.LEXER_tokens)

    def print_all_infos(self, print_f=print):
        for key in self.__dict__:
            print_f(self.__dict__[key])
            # interpreter_tokens.lexer_dict.get(key)

    def check_for_reserved_words(self, x):
        return x in self.LEXER_reserved_words

    def check_for_tokens(self, x):
        return x in self.LEXER_tokens

    def add_info_to_reserved_words(self, reserved):
        return [
            types.CompletionItem(label=x, kind=14, detail=self.reserved_help.get(x))
            for x in self.LEXER_reserved_words
        ]


if __name__ == "__main__":
    III = InccInterpreterImported(imported_helper.reserved_hover_helper_dict)
    # III.print_all_infos()
    # iii.printm(ic)
    # print(III.LEXER_tokens)
    print(III.LEXER_reserved_words)
    # print(iii.LEXER_reserved_words)
    # print(iii.COMPLETION_ITEMS_reserved_words_with_help_info)
{
    "do",
    "extend",
    "and",
    "while",
    "loop",
    "false",
    "imp",
    "struct",
    "this",
    "true",
    "xor",
    "or",
    "eq",
    "lock",
    "nand",
    "local",
    "fun",
    "set",
    "neq",
    "if",
    "then",
    "in",
    "not",
    "nor",
    "for",
    "else",
}

######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
# for key in iii.t_keys:
#     print(interpreter_tokens.lexer_dict[key])

#
# if __name__ == "__main__":
#     iii = InccInterpreterImported()
#     # iii.print_all_infos(ic)
#     # for key in iii.t_keys:
#     #     print(interpreter_tokens.lexer_dict[key])
#     t_ = [x for x in iii.lexer_dict if str.startswith(x, "t_")]
#     reserved = [x for x in iii.lexer_dict if check_for_reserved_words(x)]
#     # ic(reserved)
#     all_reserved = [iii.lexer_dict[x] for x in reserved]
#     ic(all_reserved)
#     # keys, values = zip(*reserved.items())
#     reserved2 = [x for x in iii.lexer_dict.items() if check_for_reserved_words(x)]
#     ic(reserved2)
#     ic(iii.lexer_dict)

# reserved_words = set(
#     lit_reserved_words
#     | expr_reserved_words
#     | var_reserved_words
#     | controlflow_reserved_words
#     | functions_reserved_words
#     | struct_reserved_words
# )
# tokens = list(
#     lit_tokens
#     | expr_tokens
#     | var_tokens
#     | seq_tokens
#     | functions_tokens
#     | struct_tokens
#     | reserved_words
# )
