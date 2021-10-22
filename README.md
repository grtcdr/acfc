# acfc

[![downloads/month](https://img.shields.io/pypi/dm/acfc)](https://pypi.org/project/acfc/)

[Alacritty](https://github.com/alacritty/alacritty) colors to
[Foot](https://codeberg.org/dnkl/foot) colors — Convert Alacritty's YAML color
configuration to Foot's INI color configuration.

## Installation

```
pip install acfc
```

## Usage

acfc accepts only one argument, i.e. a path to a YAML file. It'll then chuck out
its INI equivalent to the terminal. It can also read from stdin.

```
python -m acfc input.yml
```

- Input:
```yaml
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
[cursor]
color=ffffff bbbbbb
[colors]
foreground=f8f8f2
background=1e1f29
regular0=000000
regular1=ff5555
regular2=50fa7b
regular3=f1fa8c
regular4=bd93f9
regular5=ff79c6
regular6=8be9fd
regular7=bbbbbb
bright0=555555
bright1=ff5555
bright2=50fa7b
bright3=f1fa8c
bright4=bd93f9
bright5=ff79c6
bright6=8be9fd
bright7=ffffff
selection-foreground=ffffff
selection-background=44475a
```

## Thanks to

- [configparser](https://github.com/jaraco/configparser) by Jason R. Coombs
- [pyaml](https://github.com/mk-fg/pretty-yaml) by Mike Kazantsev

## License

This neat little project is licensed under the MIT license.
