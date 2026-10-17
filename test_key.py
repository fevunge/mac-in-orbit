from mac import mac
from consts import INTERCEPTED_COMMAND, INTERCEPTED_TAG, KEY_CANDIDATE
import unittest

class TestKey(unittest.TestCase):
    def test_key_candidate(self):
        tag = mac(INTERCEPTED_COMMAND, KEY_CANDIDATE)
        self.assertEqual(tag, INTERCEPTED_TAG)

if __name__ == "__main__":
    unittest.main()