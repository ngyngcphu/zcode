import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *


class ASTTest(unittest.TestCase):
    def test_902(self):
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestAST.test(input, expect, 902))
