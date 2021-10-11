from acfc import __version__
from acfc.colors import Colors
import os


def test_version():
    assert __version__ == '2.0.4'


def test_themes_before_conversion():
    """ Compares the parsed YML values for each theme in the 'themes' directory"""
    import yaml

    themes = ["Atom", "Dracula"]
    for i in themes:
        theme_suffix = "/themes/" + i + ".yml"
        file = open(os.path.dirname(__file__) + theme_suffix, 'r')
        with file as stream:
            colors = Colors(yaml.safe_load(stream))
        
            assert isinstance(int(colors.bright_black, 16), int) == True
            assert isinstance(int(colors.bright_blue, 16), int) == True
            assert isinstance(int(colors.bright_cyan, 16), int) == True
            assert isinstance(int(colors.bright_green, 16), int) == True
            assert isinstance(int(colors.bright_magenta, 16), int) == True
            assert isinstance(int(colors.bright_red, 16), int) == True
            assert isinstance(int(colors.bright_white, 16), int) == True
            assert isinstance(int(colors.bright_yellow, 16), int) == True


def test_themes_after_conversion():
    """ Compares YML and INI values for each theme in the 'themes' directory"""
    import yaml
    import configparser

    themes = ["Atom", "Dracula"]
    for i in themes:
        theme_suffix = "/themes/" + i + ".yml"
        file = open(os.path.dirname(__file__) + theme_suffix, 'r')
        with file as stream:
            config = configparser.ConfigParser()
            colors_yml = Colors(yaml.safe_load(stream))
            colors_ini = colors_yml.as_foot(config)

            assert colors_ini['colors']['bright0'] == colors_yml.bright_black
            assert colors_ini['colors']['bright1'] == colors_yml.bright_red
            assert colors_ini['colors']['bright2'] == colors_yml.bright_green
            assert colors_ini['colors']['bright3'] == colors_yml.bright_yellow
            assert colors_ini['colors']['bright4'] == colors_yml.bright_blue
            assert colors_ini['colors']['bright5'] == colors_yml.bright_magenta
            assert colors_ini['colors']['bright6'] == colors_yml.bright_cyan
            assert colors_ini['colors']['bright7'] == colors_yml.bright_white
