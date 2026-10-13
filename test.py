from mac import mac, check_mac

if __name__ == "__main__":
    # command = "ENERGIESPARMODUS-EIN-123456"
    key = "123"

    # print("command:", INTERCEPTED_COMMAND)
    print("command encoded:", string_to_code(INTERCEPTED_COMMAND))
    print("key:    ", KEY_CANDIDATE)
    print("key encoded:", string_to_code(KEY_CANDIDATE))
    print("tag:    ", INTERCEPTED_TAG)
    print("computed tag:", mac(string_to_code(INTERCEPTED_COMMAND), string_to_code(KEY_CANDIDATE)))

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
