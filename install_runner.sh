#!/bin/sh

code --install-extension vscode-extension/beta_working_0/lsp-incc-vscode.vsix
echo "INSTALL PIPX for managing python-dependencies"
brew install pipx

pipx install numpy
pipx install https://github.com/DominikOcsofszki/repo/raw/main/py_pip/incc_interpreter_ue08-0.1.0-py3-none-any.whl


