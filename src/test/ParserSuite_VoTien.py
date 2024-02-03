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
        
    def test_411(self):
        input = """ 
            ##12
            ##12
            
            func main(number a) var c <- 1
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 411))
        
    def test_412(self):
        input = """ 
            func main(string a) 
                begin 
                    break ## 12
                end
            func main(dynamic a) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 412))
        
    def test_413(self):
        input = """ 
            func main(number a[1,2,3]) ##12
                break
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 413))
        
    def test_414(self):
        input = """ 
            ##12
            func main(number a) 
                ##12
                
                begin 
                    break
                end
                
                ##12
                ##12
            func main(number a)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 414))
        
    def test_415(self):
        input = """ 
            ## 12
            
            var a <- 1 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 415))
        
    def test_416(self):
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 416))
        
    def test_417(self):
        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 417))
        
    def test_418(self):
        input = """ var VoTien <- "Vo" ... "Tien" 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 418))
        
    def test_419(self):
        input = """ var VoTien <- "Vo" ... 1 ... "Tien" 
        """
        expect = "Error on line 1 col 26: ..."
        self.assertTrue(TestParser.test(input, expect, 419))
        
    def test_420(self):
        input = """ 
            var VoTien <- true > "true" 
            var VoTien <- true >= "true"
            var VoTien <- true = "true"
            var VoTien <- true == "true"
            var VoTien <- true < "true"
            var VoTien <- true <= "true"
            var VoTien <- true >= "true" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 420))
        
    def test_421(self):
        input = """ var VoTien <- true > x >= z 
        """
        expect = "Error on line 1 col 24: >="
        self.assertTrue(TestParser.test(input, expect, 421))
        
    def test_422(self):
        input = """ 
            var VoTien <- true and "true" or 1 
            var VoTien <- 1 and 2 and 3 or 4 or 4
            var VoTien <- 1 + 2 - 2 + 3 and 3
            var VoTien <- 1 / 2 * 3 % 4
            var VoTien <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 422))
        
    def test_423(self):
        input = """var VoTien <- true >= "true" and 1 > 2
        """
        expect = "Error on line 1 col 35: >"
        self.assertTrue(TestParser.test(input, expect, 423))
        
    def test_424(self):
        input = """ 
            var VoTien <- -1 * not 1
            var VoTien <- not not not----C
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 424))
        
    def test_425(self):
        input = """var VoTien <- - not 1
        """
        expect = "Error on line 1 col 16: not"
        self.assertTrue(TestParser.test(input, expect, 425))
        
    def test_426(self):
        input = """ 
            var VoTien <- a[1] + 1
            var VoTien <- array[1,1+2][1][2,3]
            var VoTien <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var VoTien <- a[1] + fun()[1,fun()] 
            var VoTien <- 1[1]
        """
        expect = "Error on line 3 col 38: ["
        self.assertTrue(TestParser.test(input, expect, 426))
        
    def test_427(self):
        input = """var VoTien <- a[]
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 427))
        
    def test_428(self):
        input = """ 
            var VoTien <- a()
            var VoTien <- a(1,2)
            var VoTien <- a(x,array[2])[2]
            var VoTien <- a(z,k[3] ... 2)[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 428))
        
    def test_429(self):
        input = """var VoTien <- a()()
        """
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 429))
        
    def test_430(self):
        input = """ 
            var VoTien <- a() + ++1 / 2 *3 <= 3 ... "v" >= 2
            var VoTien <- a(1,2)[1,2,3 ... 2] + false + true
            var VoTien <- a(z,k[2,3,"2"] ... 2)[true]
            var VoTien <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
            var VoTien <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            var VoTien <- a(x,array[2])[2,3+2,true,false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 430))