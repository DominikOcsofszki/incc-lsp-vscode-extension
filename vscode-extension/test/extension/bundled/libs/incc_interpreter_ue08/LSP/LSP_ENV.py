from typing import override


def find_column(input, lexpos):
    line_start = input.rfind("\n", 0, lexpos) + 1
    return (lexpos - line_start) + 1


class InfoLsp:
    def __init__(self, lineno: int, lexpos: int, *rest: any):
        self.lexpos: int = lexpos
        self.lineno: int = lineno
        self.rest: any = rest

    @override
    def __repr__(self):
        # if self.rest:
        #     return f"|lineno:{self.lineno} lexpos:{self.lexpos} ... {self.rest}|"
        # else:
        #     return f"|lineno:{self.lineno} lexpos:{self.lexpos}|"
        if self.rest:
            return f"{self.lineno}:{self.lexpos} ... {self.rest}"
        else:
            return f"{self.lineno}:{self.lexpos}"


class EnvLsp:
    def __init__(self):
        self.entries: dict[str, list[InfoLsp]] = {}

    def __contains__(self, name: str):
        return name in self.entries.keys()

    def __getitem__(self, name: str):
        return self.entries.get(name)

    def __setitem__(self, key: str, info: list[int]):
        if key in self.entries:
            self.entries[key].append(InfoLsp(*info))
        else:
            self.entries[key] = [InfoLsp(*info)]

    # def __setitem__(self, key: str, info: list[InfoLsp]):
    #     if key in self.entries:
    #         self.entries[key].append(info)
    #     else:
    #         self.entries[key] = [info]

    # def push(self, *names):
    #
    # def pop(self):

    @override
    def __repr__(self):
        return str(self.entries)


lsp_ref = EnvLsp()
lsp_def = EnvLsp()


def get_lsp_ref():
    return lsp_ref


def get_lsp_def():
    return lsp_def


if __name__ == "__main__":
    env = EnvLsp()
    # env["t"] = [InfoLsp(1, 2)]
    # env["t"] = [InfoLsp(1, 3)]
    env["t"] = [1, 3]
    env["t"] = [1, 3, 5]
    env["t"] = [1, 3, "ASDADSD"]
    print(env)
