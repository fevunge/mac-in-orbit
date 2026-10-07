from consts import ALLOWED_CHARS


def string_to_code(text):
    """Turn a string into the list of its character indices, "a" -> 0, " " -> 67."""
    if type(text) is not str:
        raise TypeError("Input is not a string")

    code = []
    for char in text:
        if char not in ALLOWED_CHARS:
            raise ValueError(f'Character "{char}" in {text} is not allowed')
        code += [ALLOWED_CHARS.index(char)]

    return code


def code_to_string(code):
    """Turn a list of character indices back into a string."""
    if not all(isinstance(i, int) for i in code):
        raise TypeError("A code must be a list of integers")

    try:
        return "".join([ALLOWED_CHARS[i] for i in code])
    except IndexError:
        raise ValueError("The code contains an invalid index")
