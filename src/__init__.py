import configparser

from helpers import unpound as up


class Colors:
    normal_black = ''
    normal_blue = ''
    normal_cyan = ''
    normal_green = ''
    normal_magenta = ''
    normal_red = ''
    normal_yellow = ''
    normal_white = ''

    bright_black = ''
    bright_blue = ''
    bright_cyan = ''
    bright_green = ''
    bright_magenta = ''
    bright_red = ''
    bright_yellow = ''
    bright_white = ''

    primary_background = ''
    primary_foreground = ''
    selection_background = ''
    selection_foreground = ''
    cursor_background = ''
    cursor_foreground = ''

    def __init__(self, _dict: dict):
        self.normal_black = up(_dict['colors']['normal']['black'])
        self.normal_blue = up(_dict['colors']['normal']['blue'])
        self.normal_cyan = up(_dict['colors']['normal']['cyan'])
        self.normal_green = up(_dict['colors']['normal']['green'])
        self.normal_magenta = up(_dict['colors']['normal']['magenta'])
        self.normal_red = up(_dict['colors']['normal']['red'])
        self.normal_yellow = up(_dict['colors']['normal']['yellow'])
        self.normal_white = up(_dict['colors']['normal']['white'])

        try:
            self.bright_black = up(_dict['colors']['bright']['black'])
            self.bright_blue = up(_dict['colors']['bright']['blue'])
            self.bright_cyan = up(_dict['colors']['bright']['cyan'])
            self.bright_green = up(_dict['colors']['bright']['green'])
            self.bright_magenta = up(_dict['colors']['bright']['magenta'])
            self.bright_red = up(_dict['colors']['bright']['red'])
            self.bright_yellow = up(_dict['colors']['bright']['yellow'])
            self.bright_white = up(_dict['colors']['bright']['white'])
        except KeyError:
            print("Bright values were not specified, so I will default to normal values.")
            self.bright_black = up(_dict['colors']['normal']['black'])
            self.bright_blue = up(_dict['colors']['normal']['blue'])
            self.bright_cyan = up(_dict['colors']['normal']['cyan'])
            self.bright_green = up(_dict['colors']['normal']['green'])
            self.bright_magenta = up(_dict['colors']['normal']['magenta'])
            self.bright_red = up(_dict['colors']['normal']['red'])
            self.bright_yellow = up(_dict['colors']['normal']['yellow'])
            self.bright_white = up(_dict['colors']['normal']['white'])

        try:
            self.primary_background = up(
                _dict['colors']['primary']['background'])
            self.primary_foreground = up(
                _dict['colors']['primary']['foreground'])
            self.selection_background = up(
                _dict['colors']['selection']['background'])
            self.selection_foreground = up(
                _dict['colors']['selection']['text'])
            self.cursor_background = up(_dict['colors']['cursor']['cursor'])
            self.cursor_foreground = up(_dict['colors']['cursor']['text'])
        except KeyError:
            raise Exception(
                "This configuration file does not set some required keys.")

    def as_foot(self, config: configparser.ConfigParser):
        """
        Populates a given ``config`` with proper color values

        :param config: An object containing foot's configuration
        :return: configparser.ConfigParser
        """
        config['cursor'] = {
            'color': self.cursor_foreground + ' ' + self.cursor_background
        }
        config['colors'] = {
            'foreground': self.primary_foreground,
            'background': self.primary_background,
            'regular0': self.normal_black,
            'regular1': self.normal_red,
            'regular2': self.normal_green,
            'regular3': self.normal_yellow,
            'regular4': self.normal_blue,
            'regular5': self.normal_magenta,
            'regular6': self.normal_cyan,
            'regular7': self.normal_white,
            'bright0': self.bright_black,
            'bright1': self.bright_red,
            'bright2': self.bright_green,
            'bright3': self.bright_yellow,
            'bright4': self.bright_blue,
            'bright5': self.bright_magenta,
            'bright6': self.bright_cyan,
            'bright7': self.bright_white,
            'selection-foreground': self.selection_foreground,
            'selection-background': self.selection_background,
        }

        return config
