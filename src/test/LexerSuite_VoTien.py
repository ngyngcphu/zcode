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
        
    def test_307(self):
        self.assertTrue(TestLexer.test(".12e-3","Error Token .",307))
    
    def test_308(self):
        self.assertTrue(TestLexer.test("12.2h-3","12.2,h,-,3,<EOF>",308))
        
    def test_309(self):
        input = """ "Vo  Tien" """
        expect = "Vo  Tien,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,309))
        
    def test_310(self):
        self.assertTrue(TestLexer.test(""" "" """,",<EOF>",310))
        
    def test_311(self):
        input = """ "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\" """
        expect = "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,311))
        
    def test_312(self):
        self.assertTrue(TestLexer.test(""" "'"Vo '" Tien '' '"" ""","'\"Vo '\" Tien '' '\",<EOF>",312))
        
    def test_313(self):
        self.assertTrue(TestLexer.test(""" "Vo \n" """, "Unclosed String: Vo ", 313))
        
    def test_314(self):
        self.assertTrue(TestLexer.test(""" "Vo \n Tien" """, "Unclosed String: Vo ", 314))
        
    def test_315(self):
        self.assertTrue(TestLexer.test(""" "Vo  """, "Unclosed String: Vo  ", 315))
        
    def test_316(self):
        self.assertTrue(TestLexer.test(""" "Vo \\n \n """, "Unclosed String: Vo \\n ", 316))
        
    def test_317(self):
        self.assertTrue(TestLexer.test(""" "Vo ' \\n \\b """, "Unclosed String: Vo ' \\n \\b ", 317))
        
    def test_318(self):
        self.assertTrue(TestLexer.test(""" "Tien ' \\1  """, "Illegal Escape In String: Tien ' \\1", 318))
        
    def test_319(self):
        self.assertTrue(TestLexer.test(""" "Tien \\2 \\n \n """, "Illegal Escape In String: Tien \\2", 319))
        
    def test_320(self):
        self.assertTrue(TestLexer.test(""" "Tien \\e \\n \\r """, "Illegal Escape In String: Tien \\e", 320))
        
    def test_321(self):
        self.assertTrue(TestLexer.test("## Vo tien","<EOF>",321))
    
    def test_322(self):
        self.assertTrue(TestLexer.test("###","<EOF>",322))
        
    def test_323(self):
        self.assertTrue(TestLexer.test("a##1","a,<EOF>",323))
        
    def test_324(self):
        self.assertTrue(TestLexer.test("a#","a,Error Token #",324))
        
    def test_325(self):
        self.assertTrue(TestLexer.test("a\n##1\nb","a,\n,\n,b,<EOF>",325))
        
    def test_326(self):
        self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",326))
        
    def test_327(self):
        input = """a
                    ## comment
                """
        expect = """a,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,327))
        
    def test_328(self):
        input = "."
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input,expect,328))
        
    def test_329(self):
        input = ";"
        expect = "Error Token ;"
        self.assertTrue(TestLexer.test(input,expect,329))
        
    def test_330(self):
        input = "{"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input,expect,330))
        
    def test_331(self):
        self.assertTrue(TestLexer.test("+1-2","+,1,-,2,<EOF>",331))
        
    def test_332(self):
        self.assertTrue(TestLexer.test(""" "Tien \t \n" """, "Unclosed String: Tien 	 ", 332))
        
    def test_333(self):
        self.assertTrue(TestLexer.test(""" "Tien \\" """, "Illegal Escape In String: Tien \\\"", 333))
        
    def test_334(self):
        self.assertTrue(TestLexer.test(""" "Tien \\\n """, "Illegal Escape In String: Tien \\\n", 334))
        
    def test_335(self):
        self.assertTrue(TestLexer.test(""" "Tien '\\ """, "Illegal Escape In String: Tien '\\ ", 335))
        
    def test_336(self):
        self.assertTrue(TestLexer.test(""" "Tien \'" " """, "Tien '\" ,<EOF>", 336))
        
    def test_337(self):
        self.assertTrue(TestLexer.test(""" "Tien \\\'" " """, "Tien \\',Unclosed String:  ", 337))
        
    def test_338(self):
        self.assertTrue(TestLexer.test(""" "Tien 
                                       " """, "Unclosed String: Tien ", 338))