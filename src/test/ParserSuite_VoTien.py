import unittest
from TestUtils import TestParser
 
class ParserSuite_VoTien(unittest.TestCase):
    def test_401(self):
        input = """
            var VoTien <- true and "true" or 1 
            var VoTien <- 1 and 2 and 3 or 4 or 4
            var VoTien <- 1 + 2 - 2 + 3 and 3
            var VoTien <- 1 / 2 * 3 % 4
            var VoTien <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 401))
        
    def test_402(self):
        input = """ 
            number VoTien
            
            ## VO Tien
            number VoTien <- 0
            bool a[122,15]
            bool a[122,15] <- 1 + 1 / 2 * 3
            string b[3]
            ## 12 
            
            string b[3] <- 2 ... " tring"
            var i <- 0
            dynamic i
            dynamic i <- 0
            ## VO Tien
             
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 402))
        
    def test_403(self):
        input = """ 
            var VoTien
        """
        expect = "Error on line 2 col 22: \n"
        self.assertTrue(TestParser.test(input, expect, 403))
        
    def test_404(self):
        input = """ 
            dynamic VoTien[5] <- 3
        """
        expect = "Error on line 2 col 26: ["
        self.assertTrue(TestParser.test(input, expect, 404))
        
    def test_405(self):
        input = """ 
            bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 405))
        
    def test_406(self):
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 406))
        
    def test_407(self):
        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 407))
        
    def test_408(self):
        input = """ 
            func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var VoTien <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 7 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 408))
        
    def test_409(self):
        input = """ 
            func main()
            ## VO Tien
            func main() func main(dynamic a) ## VO Tien
        """
        expect = "Error on line 4 col 24: func"
        self.assertTrue(TestParser.test(input, expect, 409))
        
    def test_410(self):
        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 410))