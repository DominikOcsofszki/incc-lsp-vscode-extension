# from lsp_text_import import TEXT_HOVER

from incc_lsp.extracts_from_interpreter import LEXER_TOKS
from incc_lsp.lsp_server.lsp_server_logging import LOGGING
from incc_lsp.lsp_text_document_server_features.import_lsp_text_document import (
    InCCLanguageServer,
    add_all_reserved_word,
    types,
)
from incc_lsp.lsp_text_import import HOVER_ALL


def get_hoover_CompletionItem():
    auto_completion = add_all_reserved_word()
    return [types.Hover(contents=x) for x in auto_completion]


comments_json_hover = HOVER_ALL.get_all_tasks_json_hover()
comments_json_hover_keys = comments_json_hover.keys()


def create(SERVER: InCCLanguageServer):
    @SERVER.feature(types.TEXT_DOCUMENT_HOVER)
    def completions(params: types.CompletionParams):
        document = SERVER.workspace.get_text_document(params.text_document.uri)
        current_line = document.lines[params.position.line]
        tok_hover = LEXER_TOKS.from_line_match_get_id(
            current_line, params.position.character
        )
        # LOGGING.info(tok_hover)
        if tok_hover:
            hover_content = ""
            # LOGGING.info(tok_hover.startswith("#"))
            if tok_hover.startswith("#"):
                # LOGGING.info("it's a comment")
                for key in comments_json_hover_keys:
                    if key in tok_hover:
                        # LOGGING.info(f"contains {key}")
                        hover_content: str = comments_json_hover.get(
                            f"{str.lower(key)}", ""
                        )
                        hover_content = f"# {key}  \n - {hover_content}"

                        break
            else:
                hover_content: str = HOVER_ALL.hover_dict_lower_case.get(
                    f"{str.lower(tok_hover)}", ""
                )
                if hover_content:
                    hover_content = f"# {tok_hover}  \n - {hover_content}"

            return types.Hover(
                contents=types.MarkupContent(
                    kind=types.MarkupKind.Markdown, value=hover_content
                )
            )
            # return types.Hover(
            #     contents=TEXT_HOVER.reserved_hover_helper_dict.get(
            #         f"{str.upper(tok_hover)}",
            #         f"NO HOVER YET for token: '{tok_hover}' yet",
            #     )
            # )
