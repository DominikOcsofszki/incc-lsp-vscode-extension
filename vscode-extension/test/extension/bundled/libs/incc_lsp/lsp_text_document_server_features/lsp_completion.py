from incc_lsp.extracts_from_interpreter import LEXER_TOKS
from incc_lsp.lsp_text_document_server_features.helper_lsp_completions import (
    get_CompletionItem,
    get_helper_CompletionItem,
)
from incc_lsp.lsp_text_document_server_features.import_lsp_text_document import (
    InCCLanguageServer,
)
from lsprotocol import types

from incc_lsp.lsp_server.lsp_server_logging import LOGGING


def get_IDs_from_data(data: str):
    arr = LEXER_TOKS.getTokenFromDataDepth(data)
    arr = set([x.value for x in arr])
    return [types.CompletionItem(label=x, kind=18) for x in arr]


def filter_comp_items(all_comp_items: list[types.CompletionItem]):
    LOGGING.info(all_comp_items)
    all_comp_items.sort(key=lambda x: x.label[0])
    LOGGING.info(all_comp_items)
    return all_comp_items


def create(SERVER: InCCLanguageServer):
    # @SERVER.feature(types.TEXT_DOCUMENT_COMPLETION)
    # def completions(params: types.CompletionParams):
    #     return [types.CompletionItem(label="TEXT", kind=18)]

    @SERVER.feature(types.TEXT_DOCUMENT_COMPLETION)
    def completions(params: types.CompletionParams):
        LOGGING.info("PARAMS:")
        LOGGING.info(params)
        LOGGING.info("PARAMSEND")
        document = SERVER.workspace.get_text_document(params.text_document.uri)
        current_line = document.lines[params.position.line].strip()
        # lines = document.lines
        file_concated = "".join(document.lines)
        # comp_items = get_IDs_from_data_up_to_line(document.source, params.position.line)
        comp_items = get_IDs_from_data(file_concated)

        # if current_line.startswith("T="):
        #     # return get_IDs_from_data(file_concated)
        #     # return []
        #     # TODO
        #     # - this ignores all keywords...
        #
        #     return get_IDs_from_data(document.source)

        # if current_line.startswith("HELP:"):
        #     return get_helper_CompletionItem()

        all_comp_items = get_CompletionItem() + comp_items
        # return all_comp_items
        all_comp_items_sorted = filter_comp_items(all_comp_items)

        return all_comp_items_sorted


if __name__ == "__main__":
    arr = ["tt", "t", "t", "st", "s"]
    arr = [types.CompletionItem(label=x, kind=18) for x in arr]
    print(len(arr))
    arr_sort = filter_comp_items(arr)
    print(len(arr_sort))
    for l in arr_sort:
        print(l.label)
    arr_sort = filter(lambda x: x.label[0] == "t", arr)
    print("=======")
    for l in arr_sort:
        print(l.label)
