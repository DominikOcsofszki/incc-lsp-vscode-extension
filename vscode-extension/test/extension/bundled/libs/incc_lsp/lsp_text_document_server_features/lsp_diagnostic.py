from incc_interpreter_ue08.LSP.LSP_ENV import get_lsp_def
from incc_lsp.extracts_from_interpreter.PARSER_LSP import parse_for_def_ref
from incc_lsp.lsp_text_document_server_features.import_lsp_text_document import (
    InCCLanguageServer,
    types,
)


def find_column(input, lexpos):
    line_start = input.rfind("\n", 0, lexpos) + 1
    return lexpos - line_start


def empty_diagnostic_msg(ls, document):
    ls.text_document_publish_diagnostics(
        types.PublishDiagnosticsParams(
            uri=document.uri,
            version=1,
            diagnostics=[],
        )
    )


def diagnostic_msg(ls, document, line, character, msg):
    diagnostics = types.Diagnostic(
        message=msg,
        severity=types.DiagnosticSeverity.Error,
        range=types.Range(
            start=types.Position(line=line, character=character),
            end=types.Position(line=line, character=character),
        ),
    )
    ls.text_document_publish_diagnostics(
        types.PublishDiagnosticsParams(
            uri=document.uri,
            version=1,
            diagnostics=[diagnostics],
        )
    )


def EXTRACT_INFO(message):
    import re

    pattern = r"LexToken\((\w+),'(.*?)',(\d+),(\d+)\)"
    match = re.search(pattern, message)

    if match:
        token_type = match.group(1)
        token_value = match.group(2)
        line_number = int(match.group(3))
        column_number = int(match.group(4))
        return line_number, column_number
    return line_number, column_number


def create_on_open(SERVER: InCCLanguageServer):
    @SERVER.feature(types.TEXT_DOCUMENT_DID_OPEN)
    def did_open(ls: InCCLanguageServer, params: types.DidOpenTextDocumentParams):
        """Parse each document when it is changed"""
        document = SERVER.workspace.get_text_document(params.text_document.uri)
        try:
            parse_for_def_ref(document.source)
            empty_diagnostic_msg(ls, document)
        except SyntaxError as err:
            error_msg = err.msg
            if error_msg:
                linenr, column = EXTRACT_INFO(err.msg)
                diagnostic_msg(
                    # ls, document, linenr, params.position.character, error_msg
                    ls,
                    document,
                    linenr,
                    column,
                    error_msg,
                )
                return


def create(SERVER: InCCLanguageServer):
    @SERVER.feature(types.TEXT_DOCUMENT_DID_CHANGE)
    def did_change(ls: InCCLanguageServer, params: types.DidOpenTextDocumentParams):
        """Parse each document when it is changed"""
        document = SERVER.workspace.get_text_document(params.text_document.uri)
        try:
            parse_for_def_ref(document.source)
            empty_diagnostic_msg(ls, document)
        except SyntaxError as err:
            error_msg = err.msg
            if error_msg:
                linenr, column = EXTRACT_INFO(err.msg)
                diagnostic_msg(
                    # ls, document, linenr, params.position.character, error_msg
                    ls,
                    document,
                    linenr,
                    column,
                    error_msg,
                )
                return
