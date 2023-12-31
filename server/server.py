from typing import Optional
from pygls.lsp.methods import (TEXT_DOCUMENT_DID_CHANGE,HOVER,TEXT_DOCUMENT_PUBLISH_DIAGNOSTICS,TEXT_DOCUMENT_DID_OPEN,SET_TRACE_NOTIFICATION)
from pygls.lsp.types import (Diagnostic,DidChangeTextDocumentParams,Position,
                             Range,MarkupContent,Hover,Position,Range,ConfigurationParams,ConfigurationItem)
                             
from pygls.lsp.types.basic_structures import (DiagnosticSeverity)
from pygls.server import LanguageServer
from qchecker.match import *
from qchecker.substructures import*

EXTENSION_NAME = "PythonPurifier"

class PythonLanguageServer(LanguageServer):
    HOVER = 'textDocument/hover'
    DOCUMENT_HIGHLIGHT = 'textDocument/documentHighlight'
    TEXT_DOCUMENT_PUBLISH_DIAGNOSTICS = 'textDocument/publishDiagnostics'
    WORKSPACE_DID_CHANGE_CONFIGURATION = 'workspace/didChangeConfiguration'
    TEXT_DOCUMENT_DID_OPEN = 'textDocument/didOpen'
    WORKSPACE_CONFIGURATION = 'workspace/Configuration'
    SET_TRACE_NOTIFICATION = '/setTrace'

    def __init__(self):
        super().__init__() # Setting up LanguageServer with pygls defaults
        self.substructures = [] # Stores code checks the client has choosen to run in there workspace settings

# Initializing new instance of PythonLanguageServer
python_server = PythonLanguageServer()

# Adding defualt workspace settings to self.substructures when client opens a new document
@python_server.feature(TEXT_DOCUMENT_DID_OPEN)
def did_open(ls,params):
     get_configuration(ls,params)

# Trigger when client changes 
@python_server.feature(SET_TRACE_NOTIFICATION)
def get_configuration(ls, params):
     ls.get_configuration(
         ConfigurationParams(
             items=[ConfigurationItem(section=f"{EXTENSION_NAME}.substructures")]
             ),
         lambda config, ls=ls: set_config(config[0], ls)
     )

# Updates self.substructures on the sever side with the new list of checks the client wants to run
def set_config(config, ls):
     substructure_names = {substructure.__name__: substructure for substructure in SUBSTRUCTURES}
     active = []
     for name, value in config.items():
         if value:
             active.append(substructure_names[name])
     ls.substructures = active

# Trigger event for code checks - Activated whenever the client changes there current document
@python_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls, params: DidChangeTextDocumentParams):
    """Text document did change notification."""
    _validate(ls, params)

# Sends diagnostics errors identified by ls.substructures checks to the client
@python_server.feature(TEXT_DOCUMENT_PUBLISH_DIAGNOSTICS)
def _validate(ls: python_server, params):
    diagnostics=[]
    text_doc = ls.workspace.get_document(params.text_document.uri)
    ls.publish_diagnostics(text_doc.uri, diagnostics)
    source = text_doc.source
    matches = []
    for substructure in ls.substructures:
        matches += substructure.iter_matches(source)
    diagnostics = _make_diagnostics(ls,matches)

    ls.publish_diagnostics(text_doc.uri, diagnostics) 
    ls.send_notification("workspace/diagnostic/refresh")

# Helper function called from __validate. Creates the list of Diagnostic objects (to send to the client) based on the errors identified by ls.substructures checks
def _make_diagnostics(ls,matches):
    ls.show_message_log('Validating Python...')
    diagnostics = []
    for match in matches:
        msg = match.id
        text_range = match.text_range
        d = Diagnostic(
            range=Range(
                start=Position(line=text_range.from_line - 1, character=text_range.from_offset),
                end=Position(line=text_range.to_line - 1, character=text_range.to_offset)
            ),
            message=msg,
            source="Python Purifier",
            severity= DiagnosticSeverity.Information ,
        )
        diagnostics.append(d)

    return diagnostics

# Three functions below are simular to checks done in _validate. Needed becuase the variables passed into the pygls HOVER feature are restricted   
def code_checks(code):
    matches = []
    for substructure in SUBSTRUCTURES:
        matches += substructure.iter_matches(code)
    return matches
    
def get_markdown(matches):
    return matches.discription

def get_error_cordinates(matches):
    x = []
    for match in matches:
        temp = match.text_range
        x.append([temp.from_line,temp.from_offset,temp.to_line,temp.to_offset])
    return x


# Registers client hover over an error idenified on the sever side and triggers the relevant markdown content for the error. 
@python_server.feature(HOVER)
def hover(ls, params,
) -> Optional[Hover]:
    text_doc = ls.workspace.get_document(params.text_document.uri)
    source = text_doc.source
    matches = code_checks(source)
    ranges = get_error_cordinates(matches)
    lsp_ranges = [Range(start=Position(line=x[0]-1, character=x[1]),end=Position(line=x[2]-1, character=x[3])) for x in ranges]
    
    for i in range(len(ranges)):
        hover_text =  matches[i].description.content
        if params.position.line >= ranges[i][0] -1 and params.position.line <=  ranges[i][2]:
            contents = MarkupContent(kind='markdown', value=hover_text)
            return Hover(contents=contents, range=lsp_ranges[i])
    return        