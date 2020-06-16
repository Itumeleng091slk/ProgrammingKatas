import unittest
from hello import hello

class Test(unittest.TestCase):
    def test_hello_code(self):
        self.assertAlmostEqual(hello("Tshepo"),"Hello Tshepo!")
        self.assertAlmostEqual(hello("Sam"),"Hello Sam!")
        self.assertAlmostEqual(hello("Catherine"),"Hello Catherine!")
