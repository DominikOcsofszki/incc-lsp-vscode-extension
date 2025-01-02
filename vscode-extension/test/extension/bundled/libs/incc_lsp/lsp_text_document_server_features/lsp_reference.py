from incc_lsp.extracts_from_interpreter import LEXER_TOKS
from incc_lsp.extracts_from_interpreter.PARSER_LSP import parse_for_def_ref
from incc_lsp.lsp_server.lsp_server_logging import LOGGING
from incc_lsp.lsp_text_document_server_features.import_lsp_text_document import (
    InCCLanguageServer,
    types,
)


def find_column(input: str, lexpos: int):
    line_start = input.rfind("\n", 0, lexpos) + 1
    return lexpos - line_start


def get_lsp_def(document, tok_under_courser):
    lsp_defs, lsp_refs = parse_for_def_ref(document.source)

    # defined_at = lsp_defs.entries.get(tok_under_courser)
    defined_at = lsp_refs.entries.get(tok_under_courser)
    if defined_at:
        column = find_column(document.source, defined_at[-1].lexpos)
        LOGGING.info(defined_at[-1])
        return [
            types.Location(
                uri=document.uri,
                range=types.Range(
                    start=types.Position(line=defined_at[-1].lineno, character=column),
                    end=types.Position(line=defined_at[-1].lineno, character=column),
                ),
            )
        ]
    else:
        return


def create(SERVER: InCCLanguageServer):

    @SERVER.feature(types.TEXT_DOCUMENT_REFERENCES)
    def goto_reference(ls: InCCLanguageServer, params: types.DefinitionParams):
        document = SERVER.workspace.get_text_document(params.text_document.uri)
        current_line = document.lines[params.position.line]
        tok_under_courser = LEXER_TOKS.from_line_match_get_id(
            current_line, params.position.character
        )
        return get_lsp_def(document, tok_under_courser)


# TODO:
# - check if id or other item


# TODO:
# - RESET lineno after first run!!!!
