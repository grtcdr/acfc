import configparser
import os

import yaml

from acfc import __version__
from acfc.colors import Colors

themes = ["Atom", "Dracula", "MaterialDark", "Breeze"]


def test_version():
    assert __version__ == '2.2.0'


def theme_file(current):
    theme_suffix = "/themes/" + current + ".yml"
    file = open(os.path.dirname(__file__) + theme_suffix, 'r')
    return file


def test_bright_black():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright0'] == colors_yml.bright_black


def test_bright_red():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright1'] == colors_yml.bright_red


def test_bright_green():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright2'] == colors_yml.bright_green


def test_bright_yellow():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright3'] == colors_yml.bright_yellow


def test_bright_blue():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright4'] == colors_yml.bright_blue


def test_bright_magenta():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright5'] == colors_yml.bright_magenta


def test_bright_cyan():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright6'] == colors_yml.bright_cyan


def test_bright_white():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright7'] == colors_yml.bright_white


def test_normal_black():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular0'] == colors_yml.normal_black


def test_normal_red():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular1'] == colors_yml.normal_red


def test_normal_green():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular2'] == colors_yml.normal_green


def test_normal_yellow():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular3'] == colors_yml.normal_yellow


def test_normal_blue():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular4'] == colors_yml.normal_blue


def test_normal_magenta():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular5'] == colors_yml.normal_magenta


def test_normal_cyan():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular6'] == colors_yml.normal_cyan


def test_normal_white():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular7'] == colors_yml.normal_white


def test_primary_foreground():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['foreground'] == colors_yml.primary_foreground


def test_primary_background():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['background'] == colors_yml.primary_background


def test_selection_background():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['selection-background'] == colors_yml.selection_background


def test_selection_foreground():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['selection-foreground'] == colors_yml.selection_foreground


def test_cursor_foreground():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            cursor_colors = colors_ini['cursor']['color'].split(' ', 1)
            assert cursor_colors[0] == colors_yml.cursor_foreground


def test_cursor_background():
    for i in themes:
        with theme_file(i) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            cursor_colors = colors_ini['cursor']['color'].split(' ', 1)
            assert cursor_colors[1] == colors_yml.cursor_background
