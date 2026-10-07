ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-!?. "


def string_to_code(text):
    """Turn a string into the list of its character indices, "a" -> 0"""
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

def mac(text, key):
    """Compute the tag of text under key. Both are lists of character,→ indices."""
    if type(text) is not list or type(key) is not list:
        raise TypeError("Text and key must both be lists")

    if len(text) == 0 or len(key) == 0:
        raise ValueError("Text and key must not be empty")

    if not all(isinstance(i, int) for i in text):
        raise TypeError("The text must be a list of integers")

    if not all(isinstance(i, int) for i in key):
        raise TypeError("The key must be a list of integers")

    I = text
    K = key

    # Repeat the key until it is as long as the text.
    KE = (K * (len(I) // len(K) + 1))[: len(I)]

    A = [KE[i] ^ I[i] for i in range(len(I))]

    # Multiply each element of A with its right neighbour, wrapping around at
    # the end, and add the key character back on top.

    M = []
    for i in range(0, len(A)):
        M += [(A[i] * A[(i + 1) % len(A)]) + KE[i]]

    return M


def check_mac(text, key, tag):
    """Return True if key produces tag for text."""
    return mac(text, key) == tag

tag = mac(string_to_code("hello world"), string_to_code("12e01b7d-148e-44d9-b1ef-80efc907925f"))

print(check_mac(string_to_code("hello world"), string_to_code("12e01b7d-148e-44d9-b1ef-80efc907925f"), tag))





