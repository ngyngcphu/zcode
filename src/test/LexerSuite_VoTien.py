import unittest
from TestUtils import TestLexer

class LexerSuite_VoTien(unittest.TestCase):
    def test_301(self):
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,301))
        
    def test_302(self):
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,302))
        
    def test_303(self):
        self.assertTrue(TestLexer.test("A _ a az AZ aZ _a a_ a1 _1 A1", "A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>", 303))
        
    def test_304(self):
        self.assertTrue(TestLexer.test("1Tienc", "1,Tienc,<EOF>", 304))
    
    def test_305(self):
        self.assertTrue(TestLexer.test("11Tienc", "11,Tienc,<EOF>", 305))
        
    def test_306(self):
        input = "0 -0 199 001 012. 12. 0. 12.3 12.3e3 12.3e-30 2.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,199,001,012.,12.,0.,12.3,12.3e3,12.3e-30,2.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,306))