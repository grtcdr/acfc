# acfc
[Alacritty](https://github.com/alacritty/alacritty) Colors to [Foot](https://codeberg.org/dnkl/foot) Colors

This tool converts Alacritty's YAML color configuration to Foot's INI color configuration.

## Usage:

acfc accepts only one argument, i.e. a path to a YAML file. It'll then chuck out
its INI equivalent to the terminal.

```
acfc.py input.yml
```

- Input:
```yaml
# Colors (Dracula)
colors:
  bright:
    black: '#555555'
    blue: '#bd93f9'
    cyan: '#8be9fd'
    green: '#50fa7b'
    magenta: '#ff79c6'
    red: '#ff5555'
    white: '#ffffff'
    yellow: '#f1fa8c'
  cursor:
    cursor: '#bbbbbb'
    text: '#ffffff'
  normal:
    black: '#000000'
    blue: '#bd93f9'
    cyan: '#8be9fd'
    green: '#50fa7b'
    magenta: '#ff79c6'
    red: '#ff5555'
    white: '#bbbbbb'
    yellow: '#f1fa8c'
  primary:
    background: '#1e1f29'
    foreground: '#f8f8f2'
  selection:
    background: '#44475a'
    text: '#ffffff'
```

- Output:
```ini
[colors]
alpha=1
foreground=f8f8f2
background=1e1f29
regular0=000000 #black
regular1=ff5555 #red
regular2=50fa7b #green
regular3=f1fa8c #yellow
regular4=bd93f9 #blue
regular5=ff79c6 #magenta
regular6=8be9fd #cyan
regular7=bbbbbb #white
bright0=555555 #bright black
bright1=ff5555 #bright red
bright2=50fa7b #bright green
bright3=f1fa8c #bright yellow
bright4=bd93f9 #bright blue
bright5=ff79c6 #bright magenta
bright6=8be9fd #bright cyan
bright7=ffffff #bright white
```

# License

This tool is licensed under the MIT license.
