from icecream import ic
from incc_interpreter_ue08.LSP.LSP_CONFIGS import PRINT_LOG_LEVEL


def mlogger_func(text, print_level, extra=""):
    if print_level <= PRINT_LOG_LEVEL:
        if extra:
            ic(str(text) + " |=>|" + str(extra) + "|<=|")
        else:
            ic(text)


try:
    builtins = __import__("__builtin__")
except ImportError:
    builtins = __import__("builtins")


def install(glob_func_name="mlog"):
    setattr(builtins, glob_func_name, mlogger_func)


def uninstall(glob_func_name="mlog"):
    delattr(builtins, glob_func_name, mlogger_func)


# globals().update(dict(mlog=mlogger_func))
install()
