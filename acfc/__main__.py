#!/usr/bin/env python3

import sys
import os
import yaml
import configparser
from acfc import __version__
from acfc.colors import Colors


def print_ini(colors, config):
    for section in colors.sections():
        print('[' + section + ']')
        for item, value in config[section].items():
            print(item + '=' + value)


def main():
    config = configparser.ConfigParser()

    if not len(sys.argv) > 1:
        print('acfc, version ' + __version__)
        print()
        print('Paste in the Alacritty color configuration and press Ctrl+D as soon as you\'re finished:')
        print()
        colors = Colors(yaml.safe_load(sys.stdin.read())).as_foot(config)
        sys.exit(print_ini(colors, config))

    yaml_file = sys.argv[1]
    if not os.path.isfile(yaml_file):
        print('"' + yaml_file + '": Not a file.')
        sys.exit(2)

    extension = os.path.splitext(yaml_file)[1]
    if extension != ".yml" and extension != ".yaml":
        print('"' + yaml_file + '": Not a YAML file.')
        sys.exit(3)

    with open(yaml_file, 'r') as stream:
        try:
            colors = Colors(yaml.safe_load(stream)).as_foot(config)
            print_ini(colors, config)

        except yaml.YAMLError as exc:
            print(exc)


if __name__ == '__main__':
    main()
