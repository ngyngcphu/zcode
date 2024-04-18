import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *


class ASTTest(unittest.TestCase):
    def test_902(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestAST.test(input, expect, 902))
