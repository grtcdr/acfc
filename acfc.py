#!/usr/bin/env python

import sys
import yaml

with open(sys.argv[1], "r") as stream:
    try:
        color_dict = yaml.safe_load(stream)
        as_ini = "[colors]\n" \
            "alpha=1\n" \
            "foreground=" + color_dict['colors']['primary']['foreground'].replace('0x', '').replace('#', '') + "\n" \
            "background=" + color_dict['colors']['primary']['background'].replace('0x', '').replace('#', '') + "\n" \
            "regular0=" + color_dict['colors']['normal']['black'].replace('0x', '').replace('#', '') + " #black\n" \
            "regular1=" + color_dict['colors']['normal']['red'].replace('0x', '').replace('#', '') + " #red\n" \
            "regular2=" + color_dict['colors']['normal']['green'].replace('0x', '').replace('#', '') + " #green\n"\
            "regular3=" + color_dict['colors']['normal']['yellow'].replace('0x', '').replace('#', '') + " #yellow\n"\
            "regular4=" + color_dict['colors']['normal']['blue'].replace('0x', '').replace('#', '') + " #blue\n"\
            "regular5=" + color_dict['colors']['normal']['magenta'].replace('0x', '').replace('#', '') + " #magenta\n"\
            "regular6=" + color_dict['colors']['normal']['cyan'].replace('0x', '').replace('#', '') + " #cyan\n"\
            "regular7=" + color_dict['colors']['normal']['white'].replace('0x', '').replace('#', '') + " #white\n"\
            "bright0=" + color_dict['colors']['bright']['black'].replace('0x', '').replace('#', '') + " #bright black\n"\
            "bright1=" + color_dict['colors']['bright']['red'].replace('0x', '').replace('#', '') + " #bright red\n"\
            "bright2=" + color_dict['colors']['bright']['green'].replace('0x', '').replace('#', '') + " #bright green\n"\
            "bright3=" + color_dict['colors']['bright']['yellow'].replace('0x', '').replace('#', '') + " #bright yellow\n"\
            "bright4=" + color_dict['colors']['bright']['blue'].replace('0x', '').replace('#', '') + " #bright blue\n"\
            "bright5=" + color_dict['colors']['bright']['magenta'].replace('0x', '').replace('#', '') + " #bright magenta\n"\
            "bright6=" + color_dict['colors']['bright']['cyan'].replace('0x', '').replace('#', '') + " #bright cyan\n"\
            "bright7=" + \
            color_dict['colors']['bright']['white'].replace(
                '0x', '').replace('#', '') + " #bright white\n"
        print(as_ini)
    except yaml.YAMLError as exc:
        print(exc)
