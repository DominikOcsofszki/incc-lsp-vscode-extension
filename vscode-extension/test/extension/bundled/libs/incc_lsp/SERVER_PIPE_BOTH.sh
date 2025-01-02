#!/bin/sh

# cat - | tee /Users/dominik/HOME/BA/DEV/MAIN/src/incc_lsp/log.txt | /Users/dominik/HOME/BA/DEV/MAIN/.venv/bin/python /Users/dominik/HOME/BA/DEV/MAIN/src/incc_lsp/lsp_server/LSP_SERVER.py | tee -a /Users/dominik/HOME/BA/DEV/MAIN/src/incc_lsp/log.txt

# cat - | tee /Users/dominik/HOME/BA/DEV/MAIN/PIPES/log_client.pipe | /Users/dominik/HOME/BA/DEV/MAIN/.venv/bin/python /Users/dominik/HOME/BA/DEV/MAIN/src/incc_lsp/lsp_server/LSP_SERVER.py | tee /Users/dominik/HOME/BA/DEV/MAIN/PIPES/log_server.pipe
cat - | tee /Users/dominik/HOME/BA/DEV/MAIN/PIPES/log_both.pipe | /Users/dominik/HOME/BA/DEV/MAIN/.venv/bin/python /Users/dominik/HOME/BA/DEV/MAIN/src/incc_lsp/lsp_server/LSP_SERVER.py | tee /Users/dominik/HOME/BA/DEV/MAIN/PIPES/log_both.pipe

