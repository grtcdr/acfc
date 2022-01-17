import configparser
import os
import yaml
import acfc
from acfc.colors import Colors

themes = ["Atom", "Dracula", "MaterialDark", "Breeze"]

def get_theme(current):
    theme_suffix = "/themes/" + current + ".yml"
    file = open(os.path.dirname(__file__) + theme_suffix, 'r')
    return file


def test_bright_black():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright0'] == colors_yml.bright.black


def test_bright_red():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright1'] == colors_yml.bright.red


def test_bright_green():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright2'] == colors_yml.bright.green


def test_bright_yellow():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright3'] == colors_yml.bright.yellow


def test_bright_blue():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright4'] == colors_yml.bright.blue


def test_bright_magenta():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright5'] == colors_yml.bright.magenta


def test_bright_cyan():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright6'] == colors_yml.bright.cyan


def test_bright_white():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['bright7'] == colors_yml.bright.white


def test_normal_black():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular0'] == colors_yml.normal.black


def test_normal_red():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular1'] == colors_yml.normal.red


def test_normal_green():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular2'] == colors_yml.normal.green


def test_normal_yellow():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular3'] == colors_yml.normal.yellow


def test_normal_blue():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular4'] == colors_yml.normal.blue


def test_normal_magenta():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular5'] == colors_yml.normal.magenta


def test_normal_cyan():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular6'] == colors_yml.normal.cyan


def test_normal_white():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['regular7'] == colors_yml.normal.white


def test_primary_foreground():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['foreground'] == colors_yml.primary.foreground


def test_primary_background():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['background'] == colors_yml.primary.background


def test_selection_background():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['selection-background'] == colors_yml.selection.background


def test_selection_foreground():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            assert colors_ini['colors']['selection-foreground'] == colors_yml.selection.foreground


def test_cursor_foreground():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            cursor_colors = colors_ini['cursor']['color'].split(' ', 1)
            assert cursor_colors[0] == colors_yml.cursor.foreground


def test_cursor_background():
    for t in themes:
        with get_theme(t) as stream:
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(configparser.ConfigParser())
            cursor_colors = colors_ini['cursor']['color'].split(' ', 1)
            assert cursor_colors[1] == colors_yml.cursor.background
