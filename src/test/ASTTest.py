import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *


class ASTTest(unittest.TestCase):
    def test_902(self):
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestAST.test(input, expect, 902))
