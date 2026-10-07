"""Reference implementation of the MAC used in the challenge "MACs in Orbit".

Put your key candidate into KEY_CANDIDATE at the bottom and run this file to
check it against the intercepted pair.
"""

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-!?. "


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


def mac(text, key):
    """Compute the tag of text under key. Both are lists of character indices."""
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
    for i in range(len(A)):
        M += [(A[i] * A[(i + 1) % len(A)]) + KE[i]]

    return M


def check_mac(text, key, tag):
    """Return True if key produces tag for text."""
    return mac(text, key) == tag


INTERCEPTED_COMMAND = "SONNENSEGEL-AUSFAHREN-869230"
INTERCEPTED_TAG = [
    496, 248, 2060, 1055, 1408, 989, 1178, 2264, 904, 832, 1819, 1218, 2432,
    11944, 5572, 758, 664, 2177, 709, 392, 837, 1768, 3420, 3484, 3538, 3666,
    6856, 12592,
]

KEY_CANDIDATE = "put your key here"

if __name__ == "__main__":
    command = "ENERGIESPARMODUS-EIN-123456"
    key = "Geheim123-456"

    print("command:", command)
    print("encoded:", string_to_code(command))
    print("key:    ", key)
    print("encoded:", string_to_code(key))
    print("tag:    ", mac(string_to_code(command), string_to_code(key)))

    print()
    print("Checking", repr(KEY_CANDIDATE), "against the intercepted pair.")
    if check_mac(
        string_to_code(INTERCEPTED_COMMAND),
        string_to_code(KEY_CANDIDATE),
        INTERCEPTED_TAG,
    ):
        print("The key is correct.")
    else:
        print("The key is wrong.")





