#!/bin/sh
echo "IF ERROR:"
echo "vscode has to be enabled as command code. Can be done from vscode"

code --install-extension vscode-extension/lsp-incc-vscode.vsix

echo "Open vscode and create/ open .incc file or .incc24 file"
echo ""
echo ""
echo "IF ERROR:"
echo "numpy has to be installed for python, bundle packaging not working with numpy (it also has 20 mb...)"
echo "todo: python -m pip install numpy"


