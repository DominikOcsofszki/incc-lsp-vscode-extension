# nvim or emacs
- Unzip lsp-incc-vscode.vsix

```sh
unzip lsp-incc-vscode.vsix
```
or
```sh
sh unzip_vsix.sh
```

## run lsp-server:
```sh
sh run_lsp.sh
```


## nvim plugin:

https://github.com/DominikOcsofszki/lsp-incc.nvim

```lua
path = ABSOLUT_PATH/run_lsp.sh  --ABSOLUT PATH
```
---

## Emacs(?):
Schritte wie nvim plugin

incc-lsp = ABSOLUT_PATH/run_lsp.sh ?
gpt:
```
(use-package lsp-mode
  :commands (lsp lsp-deferred)
  :config
  (lsp-register-client
   (make-lsp-client
    :new-connection (lsp-stdio-connection '("incc_lsp")) ;; Use pipx-installed binary
    :major-modes '(incc-mode) ;; Replace with your major mode
    :server-id 'incc-lsp)))
```


