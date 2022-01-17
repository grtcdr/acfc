#!/usr/bin/env python3

import sys
import yaml
import configparser
from acfc import __version__
from acfc.colors import Colors


def not_blank(text: str):
    return bool(text and not text.isspace())


def print_ini(colors, config):
    for section in colors.sections():
        print('[' + section + ']')
        for item, value in config[section].items():
            if not_blank(value):
                print(item + '=' + value)


def main():
    config = configparser.ConfigParser()

    print('acfc, version ' + __version__)
    print()
    print('Paste in the Alacritty color configuration and press Ctrl+D as soon as you\'re finished:')
    print()
    colors = Colors(yaml.safe_load(sys.stdin.read())).as_foot(config)
    sys.exit(print_ini(colors, config))


if __name__ == '__main__':
    main()
