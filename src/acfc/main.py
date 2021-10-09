#!/usr/bin/env python

import sys
import configparser
import yaml
import argparse
from colors import Colors

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as stream:
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
