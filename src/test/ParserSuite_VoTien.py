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
        expect = "Error on line 3 col 16: break"
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
            var VoTien <- a() + 1 / 2 *3 <= 3 ... "v" >= 2
            var VoTien <- a(1,2)[1,2,3 ... 2] + false + true
            var VoTien <- a(z,k[2,3,"2"] ... 2)[true]
            var VoTien <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
            var VoTien <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            var VoTien <- a(x,array[2])[2,3+2,true,false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 430))
        
    def test_431(self):
        input = """var VoTien <- a[1]()
        """
        expect = "Error on line 1 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 431))
        
    def test_432(self):
        input = """
        ## comment
        func main()

            ## comment
            begin
            aPI <- 3.14
            end
            ## comment
            
        ## comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 432))
        
    def test_433(self):
        input = """
        func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        func main()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                VoTien <- 1 + 2 + fun()
                VoTien[1+a] <- 1
                
                ## comment4
                VoTien[3+4,2,4] <- 1
                
                ## comment5
            end
            ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 433))
        
    def test_434(self):
        input = """
        func main()
            begin
            aPI + 1 <- 3.14
            end
        """
        expect = "Error on line 4 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 434))
        
    def test_435(self):
        input = """
        func main()
            begin
            aPI()<- 3.14
            end
        """
        expect = "Error on line 4 col 17: <-"
        self.assertTrue(TestParser.test(input, expect, 435))
        
    def test_436(self):
        input = """
        func main()
            begin
            (aPI)[2]<- 3.14
            end
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 436))
        
    def test_437(self):
        input = """
        func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if (1) api <- 1
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 437))
        
    def test_438(self):
        input = """
        func main()
            begin   
                if (api <- 1)
            end
        """
        expect = "Error on line 4 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 438))
        
    def test_439(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                
                a <- 1
            ## comment
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 439))
        
    def test_440(self):
        input = """
        func main()
            begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 440))
        
    def test_441(self):
        input = """
        func main()
            begin
            for i+1 until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 441))
        
    def test_442(self):
        input = """
        func main()
        begin 
            break
            continue
            for i until i >= 10 by 1 + 1 ... 3 / 2
                begin
                    break
                    continue
                end
                
            for i until i >= 10 by 1 print(1)
            for i until i >= 10 by 1 
                print(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 442))
        
    def test_443(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 443))
        
    def test_444(self):
        input = """
        func main()
            return 1 + 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 444))
        
    def test_445(self):
        input = """
        func main()
            begin
            main()
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 445))
        
    def test_446(self):
        input = """
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 446))
        
    def test_447(self):
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 447))
        
    def test_448(self):
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 448))
        
    def test_449(self):
        input = """
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 449))
        
    def test_450(self):
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 450))
        
    def test_451(self):
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 451))
        
    def test_452(self):
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false
            end
            return true
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 452))
        
    def test_453(self):
        input = """ func areDivisors(number num1, number num2)
                        return ((num1 % num2 = 0) or (num2 % num1 = 0))

                    func main()
                        begin
                            var num1 <- readNumber()
                            var num2 <- readNumber()
                            if (areDivisors(num1, num2)) writeString("Yes")
                            else writeString("No")
                        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 453))
        
    def test_454(self):
        input = """ func isPrime(number x)

                    func main()
                        begin
                            number x <- readNumber()
                            if (isPrime(x)) writeString("Yes")
                            else writeString("No")
                        end

                    func isPrime(number x)
                        begin
                            if (x <= 1) return false
                            var i <- 2
                            for i until i > x / 2 by 1
                            begin
                                if (x % i = 0) return false
                            end
                            return true
                        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 454))
        
    def test_455(self):
        input = """ func foo(number a[5], string b)
                    begin
                        var i <- 0
                        for i until i >= 5 by 1
                        begin
                            a[i] <- i * i + 5
                        end
                        return -1
                    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 455))
        
    def test_456(self):
        input = """
        number a[5] <- [1, 2, 3, 4, 5]
        number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 456))