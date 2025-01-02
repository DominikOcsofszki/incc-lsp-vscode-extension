from incc_interpreter_ue08.interpreter import set_up_env

_import_env = set_up_env()


_all_import_keys = [x for x in _import_env.vars.keys()]
import_toks_to_translate = [x for x in _all_import_keys if str.isupper(x)]
import_toks_literal = [x for x in _all_import_keys if not str.isupper(x)]
