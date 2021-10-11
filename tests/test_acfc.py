from acfc import __version__
from acfc.colors import Colors
import os


def assert_bright(colors: Colors, black: str, blue: str, cyan: str, green: str, magenta: str, red: str, white: str, yellow: str):
    assert colors.bright_black == black
    assert colors.bright_blue == blue
    assert colors.bright_cyan == cyan
    assert colors.bright_green == green
    assert colors.bright_magenta == magenta
    assert colors.bright_red == red
    assert colors.bright_white == white
    assert colors.bright_yellow == yellow

def test_version():
    assert __version__ == '2.0.4'


def test_atom_yml():
    import yaml

    file = open(os.path.dirname(__file__) + "/themes/Atom.yml", 'r')
    with file as stream:
        assert_bright(
            Colors(yaml.safe_load(stream)),
            '000000',
            '96cbfe',
            '85befd',
            '94fa36',
            'b9b6fc',
            'fd5ff1',
            'e0e0e0',
            'f5ffa8'
        )


def test_dracula_yml():
    import yaml

    file = open(os.path.dirname(__file__) + "/themes/Dracula.yml", 'r')
    with file as stream:
        assert_bright(
            Colors(yaml.safe_load(stream)),
            '555555',
            'bd93f9',
            '8be9fd',
            '50fa7b',
            'ff79c6',
            'ff5555',
            'ffffff',
            'f1fa8c'
        )
