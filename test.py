from mac import mac, check_mac
from code_and_decode import string_to_code
from consts import INTERCEPTED_COMMAND, INTERCEPTED_TAG, KEY_CANDIDATE

if __name__ == "__main__":
    print(f"intercepted command: {INTERCEPTED_COMMAND} : {string_to_code(INTERCEPTED_COMMAND)}")
    print(f"intercepted tag:    {INTERCEPTED_TAG}")
    print(f"key:    {KEY_CANDIDATE} : {string_to_code(KEY_CANDIDATE)}")

    print("\nChecking", repr(KEY_CANDIDATE), "against the intercepted pair.")
    if check_mac(
        string_to_code(INTERCEPTED_COMMAND),
        string_to_code(KEY_CANDIDATE),
        INTERCEPTED_TAG,
    ):
        print("The key is correct.")
    else:
        print("The key is wrong.")
