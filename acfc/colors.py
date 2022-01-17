import configparser
from acfc.helpers import unpound

class Normal:
    black = ''
    blue = ''
    cyan = ''
    green = ''
    magenta = ''
    red = ''
    yellow = ''
    white = ''

class Bright:
    black = ''
    blue = ''
    cyan = ''
    green = ''
    magenta = ''
    red = ''
    yellow = ''
    white = ''

class Primary:
    background = ''
    foreground = ''

class Cursor:
    background = ''
    foreground = ''

class Selection:
    background = ''
    foreground = ''

class Colors:
    normal = Normal
    bright = Bright
    primary = Primary
    selection = Selection
    cursor = Cursor

    def try_find(self, colors: dict, group: str, field: str):
        try:
            return unpound(colors['colors'][group][field])
        except KeyError:
            if group == 'bright':
                return unpound(colors['colors']['normal'][field])
            else:
                return ''

    def __init__(self, colors: dict):
        if not colors:
            return None
        
        self.normal.black = self.try_find(colors, 'normal', 'black')
        self.normal.red = self.try_find(colors, 'normal', 'red')
        self.normal.green = self.try_find(colors, 'normal', 'green')
        self.normal.yellow = self.try_find(colors, 'normal', 'yellow')
        self.normal.blue  = self.try_find(colors, 'normal', 'blue')
        self.normal.magenta = self.try_find(colors, 'normal', 'magenta')
        self.normal.cyan  = self.try_find(colors, 'normal', 'cyan')
        self.normal.white = self.try_find(colors, 'normal', 'white')

        self.bright.black = self.try_find(colors, 'bright', 'black')
        self.bright.red = self.try_find(colors, 'bright', 'red')
        self.bright.green = self.try_find(colors, 'bright', 'green')
        self.bright.yellow = self.try_find(colors, 'bright', 'yellow')
        self.bright.blue  = self.try_find(colors, 'bright', 'blue')
        self.bright.magenta = self.try_find(colors, 'bright', 'magenta')
        self.bright.cyan  = self.try_find(colors, 'bright', 'cyan')
        self.bright.white = self.try_find(colors, 'bright', 'white')

        self.primary.background = self.try_find(colors, 'primary', 'background')
        self.primary.foreground = self.try_find(colors, 'primary', 'foreground')

        self.cursor.background = self.try_find(colors, 'cursor', 'background')
        self.cursor.foreground = self.try_find(colors, 'cursor', 'foreground')

        self.selection.background = self.try_find(colors, 'selection', 'background')
        self.selection.foreground = self.try_find(colors, 'selection', 'foreground')

    def as_foot(self, config: configparser.ConfigParser):
        """
        Populates a given `config` with its appropriate values
        """
        config['cursor'] = {
            'color': self.cursor.foreground + ' ' + self.cursor.background
        }
        config['colors'] = {
            'foreground': self.primary.foreground,
            'background': self.primary.background,
            'regular0': self.normal.black,
            'regular1': self.normal.red,
            'regular2': self.normal.green,
            'regular3': self.normal.yellow,
            'regular4': self.normal.blue,
            'regular5': self.normal.magenta,
            'regular6': self.normal.cyan,
            'regular7': self.normal.white,
            'bright0': self.bright.black,
            'bright1': self.bright.red,
            'bright2': self.bright.green,
            'bright3': self.bright.yellow,
            'bright4': self.bright.blue,
            'bright5': self.bright.magenta,
            'bright6': self.bright.cyan,
            'bright7': self.bright.white,
            'selection-foreground': self.selection.foreground,
            'selection-background': self.selection.background,
        }

        return config
