#!/usr/bin/env python

import sys
import configparser
import yaml

class Colors:
    bright_black = ''
    bright_blue = ''
    bright_cyan = ''
    bright_green = ''
    bright_magenta = ''
    bright_red = ''
    bright_yellow = ''
    bright_white = ''
    normal_black = ''
    normal_blue = ''
    normal_cyan = ''
    normal_green = ''
    normal_magenta = ''
    normal_red = ''
    normal_yellow = ''
    normal_white = ''
    primary_background = ''
    primary_foreground = ''
    selection_background = ''
    selection_foreground = ''
    cursor_background=''
    cursor_foreground=''

    def __init__(self, _dict):
        self.bright_black = _dict['colors']['bright']['black'].replace('#','').replace('0x','')
        self.bright_blue = _dict['colors']['bright']['blue'].replace('#','').replace('0x','')
        self.bright_cyan = _dict['colors']['bright']['cyan'].replace('#','').replace('0x','')
        self.bright_green = _dict['colors']['bright']['green'].replace('#','').replace('0x','')
        self.bright_magenta = _dict['colors']['bright']['magenta'].replace('#','').replace('0x','')
        self.bright_red = _dict['colors']['bright']['red'].replace('#','').replace('0x','')
        self.bright_yellow = _dict['colors']['bright']['yellow'].replace('#','').replace('0x','')
        self.bright_white = _dict['colors']['bright']['white'].replace('#','').replace('0x','')
        self.normal_black = _dict['colors']['normal']['black'].replace('#','').replace('0x','')
        self.normal_blue = _dict['colors']['normal']['blue'].replace('#','').replace('0x','')
        self.normal_cyan = _dict['colors']['normal']['cyan'].replace('#','').replace('0x','')
        self.normal_green = _dict['colors']['normal']['green'].replace('#','').replace('0x','')
        self.normal_magenta = _dict['colors']['normal']['magenta'].replace('#','').replace('0x','')
        self.normal_red = _dict['colors']['normal']['red'].replace('#','').replace('0x','')
        self.normal_yellow = _dict['colors']['normal']['yellow'].replace('#','').replace('0x','')
        self.normal_white = _dict['colors']['normal']['white'].replace('#','').replace('0x','')
        self.primary_background = _dict['colors']['primary']['background'].replace('#','').replace('0x','')
        self.primary_foreground = _dict['colors']['primary']['foreground'].replace('#','').replace('0x','')
        self.selection_background = _dict['colors']['selection']['background'].replace('#','').replace('0x','')
        self.selection_foreground = _dict['colors']['selection']['text'].replace('#','').replace('0x','')
        self.cursor_background = _dict['colors']['cursor']['cursor'].replace('#','').replace('0x','')
        self.cursor_foreground = _dict['colors']['cursor']['text'].replace('#','').replace('0x','')

    def as_foot(self, config):
        config['cursor'] = {
            'color': self.cursor_foreground+' '+self.cursor_background
        }
        config['colors'] = {
            'foreground':self.primary_foreground,
            'background':self.primary_background,
            'regular0':self.normal_black,
            'regular1':self.normal_red,
            'regular2':self.normal_green,
            'regular3':self.normal_yellow,
            'regular4':self.normal_blue,
            'regular5':self.normal_magenta,
            'regular6':self.normal_cyan,
            'regular7':self.normal_white,
            'bright0':self.bright_black,
            'bright1':self.bright_red,
            'bright2':self.bright_green,
            'bright3':self.bright_yellow,
            'bright4':self.bright_blue,
            'bright5':self.bright_magenta,
            'bright6':self.bright_cyan,
            'bright7':self.bright_white,
            'selection-foreground':self.selection_foreground,
            'selection-background':self.selection_background,
        }

        return config

if __name__ == "__main__":
    with open(sys.argv[1], "r") as stream:
        try:
            # Instantiate configparser to store foot's values
            config = configparser.ConfigParser()
            # Instantiate Colors to parse alacritty's color object 
            colors = Colors(yaml.safe_load(stream)).as_foot(config)
                
            # Print to console
            for section in colors.sections():
                print('['+section+']')
                for item, value in config[section].items():
                    print(item + "=" + value)

        except yaml.YAMLError as exc:
            print(exc)