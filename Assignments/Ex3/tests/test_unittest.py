from Assignments.Ex3.src.inc_dec import *   # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(3), 4)

    def test_decrement(self):
        self.assertEqual(decrement(3), 2)

if __name__ == '__main__':
    unittest.main()