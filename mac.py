"""Reference implementation of the MAC used in the challenge "MACs in Orbit".

Put your key candidate into KEY_CANDIDATE at the bottom and run this file to
check it against the intercepted pair.
"""

from code_and_decode import string_to_code
from consts import INTERCEPTED_COMMAND, INTERCEPTED_TAG, KEY_CANDIDATE


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
