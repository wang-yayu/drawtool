import unittest
from calculate import calculate

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calculate('1+2'), 3)  # add assertion here

    def test_something(self):
        self.assertEqual(calculate('3-2'), 1)

    def test_something(self):
        self.assertEqual(calculate('1*2'), 2)

    def test_something(self):
        self.assertEqual(calculate('1/2'), 0.5)

if __name__ == '__main__':
    unittest.main()
