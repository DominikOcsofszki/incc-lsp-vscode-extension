# incc-lsp-vscode-extension


# Install
```sh
sh install_extension.sh
```
# Uninstall
```sh
sh uninstall_extension.sh
```

# Restart Server:
- open commandPalette
`shift+cmd+p`

- restart:
```
lsp-incc-vscode.restart
```

# Issues:
- COMMENTS
- 

-example.incc
```incc
- before:
```incc
{
missing_semi ="ERROR"
  s = struct {
    .x = 7;
    .set_x = \x -> .x = x
  };
  t = extend s {
    .x = 5;
#   ..x = 2; #! disallowed
#   .set_px = \x -> ..x = x; #! disallowed
    .set_px = \x -> ..set_x(x);
    .set_x = \x -> .x = x
  };
  t.set_x(2);
  print(t.x); #2
  print(t..x); #7
  t..set_x(1);
  print(t..x); #1
# t.x = 1; #! disallowed
  print(t.x); #2

  f = 3;
  r = struct {
    .g = \ -> f;
    .h = \x -> f = x
  };
  print(r.g()); #3
  r.h(5);
  print(r.g()); #5

  # hinzugefügt: assign member of parent not known in child
  u = struct {
    .x = 1
  };
  v = extend u {
    .set_x = \x -> .x = x
  };
# v.set_x(5); #!disallowed

  # optional:
  {
    a = struct {
      set .x = 1;
#     .set_x = \x -> .x = x; # generated
      .y = 2
    };
    a.set_x(5); # allowed
#   a.set_y(2); #! disallowed, set_y not generated
    print(a.x); #5, allowed
    print(a.y) #2, allowed
  }

}

```

![vscode.incc](img/vscode.incc.png)

- before:
![vscode.incc before](img/vscode.incc.before.png)

