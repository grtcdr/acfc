#!/usr/bin/env python

import sys
import os
import configparser
import yaml
import argparse
import colors

if __name__ == '__main__':
    if len(sys.argv) > 1:
        yaml_file = sys.argv[1]

        if os.path.isfile(yaml_file):
            with open(yaml_file, 'r') as stream:
                try:
                    config = configparser.ConfigParser()
                    colors = Colors(yaml.safe_load(stream)).as_foot(config)

                    # Print to console
                    for section in colors.sections():
                        print('['+section+']')
                        for item, value in config[section].items():
                            print(item + '=' + value)

                except yaml.YAMLError as exc:
                    print(exc)
        else:
            print(yaml_file + ": Not a file.")
    else:
        print("I need a YAML file to parse.")
