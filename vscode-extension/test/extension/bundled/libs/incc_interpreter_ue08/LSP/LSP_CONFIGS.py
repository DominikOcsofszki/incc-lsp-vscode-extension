EXIT_BEFORE_EVAL = True
# PRINT_TOKENS = True
PRINT_TOKENS = False
PRINT_P_ASSIGN = True
PRINT_LOG_LEVEL = 1
__FILE_TEXT = "empty"


def set_file_text(text):
    global __FILE_TEXT
    __FILE_TEXT = text


def get_file_text():
    return __FILE_TEXT
