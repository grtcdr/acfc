def unpound(input: str) -> str:
    """
    Removes '0x' or '#' prefix from a given string

    :param input: A hexadecimal value.
    :return: str
    """
    return input.replace('#', '').replace('0x', '')
