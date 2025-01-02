# from copy import deepcopy
from icecream import ic


class P_Info:
    def __init__(self, p):
        # self.p = deepcopy(p)
        self.lexer_dict = self.setup_lexer_dict(p)
        self.lexmatch = self.lexer_dict.get("lexmatch")
        self.lexdata = self.lexer_dict.get("lexdata")
        self.match_span = self.lexmatch.span()
        self.match_group = self.lexmatch.group()
        self.lineno = self.lexer_dict.get("lineno")
        self.lexpos = self.lexer_dict.get("lexpos")
        self.column = self.lexer_dict.get("column")
        self.type = self.lexer_dict.get("type")
        # ic(self.lexer_dict)
        # print(self.match_group)
        # exit()

    def __repr__(self):
        # return str(self.p) + "\n" + str() + "\n" + str(self.lexmatch)
        # return str(self.lexmatch)

        print_arr = [self.lexpos, self.column, self.type, self.lexmatch]
        print_arr = [self.lexpos, self.lexmatch]
        print_arr = [self.match_span, self.match_group]
        # print_arr = [self.lineno-1, self.column-1, self.type]
        print(":".join(map(str, print_arr)))

        return "var_name:" + str(self.match_group)

    def setup_lexer_dict(self, p):
        if p and p.__dict__:
            lexer_dict = p.__dict__.get("lexer").__dict__
            return lexer_dict
        else:
            raise RuntimeError("P WAS NOT PASSED!")

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
