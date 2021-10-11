#!/usr/bin/env python3

import sys, os, yaml, configparser
from acfc.colors import Colors


def main():
    if not len(sys.argv) > 1:
        print('I need a YAML file to parse.')
        sys.exit(1)

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
            config = configparser.ConfigParser()
            colors = Colors(yaml.safe_load(stream)).as_foot(config)
                
            for section in colors.sections():
                print('[' + section + ']')
                for item, value in config[section].items():
                    print(item + '=' + value)

        except yaml.YAMLError as exc:
            print(exc)


if __name__ == '__main__':
    main()
