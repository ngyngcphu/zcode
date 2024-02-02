import unittest
from TestUtils import TestLexer

# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013  
class LexerSuite_VoTien(unittest.TestCase):

    def test_KeyWord_Operators_Separators(self):
        """test KeyWord Op# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013   erators Separators"""
        
        ##^ test KeyWord
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,301))
        
        ##^ test Operators
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,302))

        
    def test_Identifiers(self):
        """test Identifiers"""
        ##^ test true ID
        self.assertTrue(TestLexer.test("A _ a az AZ aZ _a a_ a1 _1 A1", "A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>", 306))     

        ##^ test false ID
        self.assertTrue(TestLexer.test("1Tienc", "1,Tienc,<EOF>", 307))
        self.assertTrue(TestLexer.test("11Tienc", "11,Tienc,<EOF>", 308))
        
    def test_Literal(self):
        """test Identifiers"""   
        
        ##^ test NUMBER_LIT    
        input = "0 -0 199 001 012. 12. 0. 12.3 12.3e3 12.3e-30 2.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,199,001,012.,12.,0.,12.3,12.3e3,12.3e-30,2.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,309))
        ##^ fail NUMBER_LIT
        self.assertTrue(TestLexer.test(".12e-3","Error Token .",310))
        self.assertTrue(TestLexer.test("12.2h-3","12.2,h,-,3,<EOF>",311))
        
        ##^ test STRING_LIT 
        input = """ "Vo  Tien" """ # kiểm tra bình thường
        expect = "Vo  Tien,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,312))
        self.assertTrue(TestLexer.test(""" "" """,",<EOF>",313)) # chuỗi rỗng
        
        ##^ kiểm tra các kí tự cho phép
        input = """ "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\" """
        expect = "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,314))
        self.assertTrue(TestLexer.test(""" "'"Vo '" Tien '' '"" ""","'\"Vo '\" Tien '' '\",<EOF>",315))
        
        ##^ kiểm tra lỗi Unclosed String
        self.assertTrue(TestLexer.test(""" "Vo \n" """, "Unclosed String: Vo ", 316))
        self.assertTrue(TestLexer.test(""" "Vo \n Tien" """, "Unclosed String: Vo ", 317))
        self.assertTrue(TestLexer.test(""" "Vo  """, "Unclosed String: Vo  ", 318))
        self.assertTrue(TestLexer.test(""" "Vo \\n \n """, "Unclosed String: Vo \\n ", 319))
        self.assertTrue(TestLexer.test(""" "Vo ' \\n \\b """, "Unclosed String: Vo ' \\n \\b ", 320))
        
        ##^ kiểm tra lỗi Illegal Escape
        self.assertTrue(TestLexer.test(""" "Tien ' \\1  """, "Illegal Escape In String: Tien ' \\1", 323))
        self.assertTrue(TestLexer.test(""" "Tien \\2 \\n \n """, "Illegal Escape In String: Tien \\2", 324))
        self.assertTrue(TestLexer.test(""" "Tien \\e \\n \\r """, "Illegal Escape In String: Tien \\e", 325))        

    
    def test_Comments_newline(self):
        """test Comments và newline""" 
        self.assertTrue(TestLexer.test("## Vo tien","<EOF>",330))    
        self.assertTrue(TestLexer.test("###","<EOF>",331)) 
        self.assertTrue(TestLexer.test("a##1","a,<EOF>",332)) 
        self.assertTrue(TestLexer.test("a#","a,Error Token #",333))    
        self.assertTrue(TestLexer.test("a\n##1\nb","a,\n,\n,b,<EOF>",334))  
        self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",335))
        input = """a
                    ## comment
                """
        expect = """a,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,336))   


    def test_complex(self): # test case 140 ->
                
        input = "."
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input,expect,340))
        
        input = ";"
        expect = "Error Token ;"
        self.assertTrue(TestLexer.test(input,expect,341))
        
        input = "{"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input,expect,342))       
        
        self.assertTrue(TestLexer.test("+1-2","+,1,-,2,<EOF>",343)) 
        self.assertTrue(TestLexer.test(""" "Tien \t \n" """, "Unclosed String: Tien 	 ", 344))
        self.assertTrue(TestLexer.test(""" "Tien \\" """, "Illegal Escape In String: Tien \\\"", 345))
        self.assertTrue(TestLexer.test(""" "Tien \\\n """, "Illegal Escape In String: Tien \\\n", 346))
        self.assertTrue(TestLexer.test(""" "Tien '\\ """, "Illegal Escape In String: Tien '\\ ", 347))
        self.assertTrue(TestLexer.test(""" "Tien \'" " """, "Tien '\" ,<EOF>", 348))
        self.assertTrue(TestLexer.test(""" "Tien \\\'" " """, "Tien \\',Unclosed String:  ", 349))
        self.assertTrue(TestLexer.test(""" "Tien 
                                       " """, "Unclosed String: Tien ", 350))
