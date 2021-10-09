#!/usr/bin/env python

import sys
import yaml

if __name__ == "__main__":

    with open(sys.argv[1], "r") as stream:
        try:
            color_dict = yaml.safe_load(stream)
            as_ini = "[cursor]\n" \
                "color=" + color_dict['colors']['cursor']['text'].replace('0x', '').replace('#', '') + " " + color_dict['colors']['cursor']['cursor'].replace('0x', '').replace('#', '') + "\n\n" \
                "[colors]\n" \
                "foreground=" + color_dict['colors']['primary']['foreground'].replace('0x', '').replace('#', '') + "\n" \
                "background=" + color_dict['colors']['primary']['background'].replace('0x', '').replace('#', '') + "\n" \
                "regular0=" + color_dict['colors']['normal']['black'].replace('0x', '').replace('#', '') + "\n" \
                "regular1=" + color_dict['colors']['normal']['red'].replace('0x', '').replace('#', '') + "\n" \
                "regular2=" + color_dict['colors']['normal']['green'].replace('0x', '').replace('#', '') + "\n"\
                "regular3=" + color_dict['colors']['normal']['yellow'].replace('0x', '').replace('#', '') + "\n"\
                "regular4=" + color_dict['colors']['normal']['blue'].replace('0x', '').replace('#', '') + "\n"\
                "regular5=" + color_dict['colors']['normal']['magenta'].replace('0x', '').replace('#', '') + "\n"\
                "regular6=" + color_dict['colors']['normal']['cyan'].replace('0x', '').replace('#', '') + "\n"\
                "regular7=" + color_dict['colors']['normal']['white'].replace('0x', '').replace('#', '') + "\n"\
                "bright0=" + color_dict['colors']['bright']['black'].replace('0x', '').replace('#', '') + "\n"\
                "bright1=" + color_dict['colors']['bright']['red'].replace('0x', '').replace('#', '') + "\n"\
                "bright2=" + color_dict['colors']['bright']['green'].replace('0x', '').replace('#', '') + "\n"\
                "bright3=" + color_dict['colors']['bright']['yellow'].replace('0x', '').replace('#', '') + "\n"\
                "bright4=" + color_dict['colors']['bright']['blue'].replace('0x', '').replace('#', '') + "\n"\
                "bright5=" + color_dict['colors']['bright']['magenta'].replace('0x', '').replace('#', '') + "\n"\
                "bright6=" + color_dict['colors']['bright']['cyan'].replace('0x', '').replace('#', '') + "\n"\
                "bright7=" + \
                color_dict['colors']['bright']['white'].replace(
                    '0x', '').replace('#', '') + "\n" \
                "selection-foreground=" + color_dict['colors']['selection']['text'].replace('0x', '').replace('#', '') + "\n" \
                "selection-background=" + \
                color_dict['colors']['selection']['background'].replace(
                    '0x', '').replace('#', '') + "\n"

            print(as_ini)
        except yaml.YAMLError as exc:
            print(exc)
