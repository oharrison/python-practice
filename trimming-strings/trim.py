""" This module trims strings """

def left_trim(string):
    """
    Args:
        string (str): The string to be left trimmed.

    Returns:
        str: string with empty spaces at the start of the string removed

    Examples:
        >>> left_trim('   the quick brown fox jumped over the lazy dog')
        >>> left_trim(' the quick brown fox jumped over the lazy dog')
    """
    for i, char in enumerate(string):
        if char != ' ':
            return string[i:]

def right_trim(string):
    """
    Args:
        string (str): The string to be left trimmed.

    Returns:
        str: string with empty spaces at the end of the string removed

    Examples:
        >>> right_trim('the quick brown fox jumped over the lazy dog    ')
        >>> right_trim('the quick brown fox jumped over the lazy dog  ')
    """
    end = len(string) - 1
    while string[end] == ' ':
        end -= 1
    return string[:end + 1]

def left_and_right_trim(string):
    """
    Args:
        string (str): The string to be left trimmed.

    Returns:
        str: string with empty spaces at the start and end of the string removed

    Examples:
        >>> left_and_right_trim('    the quick brown fox jumped over the lazy dog    ')
        >>> left_and_right_trim('  the quick brown fox jumped over the lazy dog  ')
    """
    return right_trim(left_trim(string))

if __name__ == '__main__':
    assert left_trim('    left trim') == 'left trim'
    assert right_trim('right trim    ') == 'right trim'
    assert left_and_right_trim('    trim both sides    ') == 'trim both sides'
    print('All tests passed.')
    