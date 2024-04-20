import unittest
from TestUtils import TestChecker
from main.zcode.utils.AST import *


class CheckSuite(unittest.TestCase):
    def test_801(self):
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 801))

    def test_802_No_entry_point(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 802))
    
    def test_803_No_entry_point(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 803))

    def test_804_No_entry_point(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 804))

    def test_805_No_entry_point(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 805))
        
    def test_806_No_entry_point(self):
        input = """
            number VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 806))

    def test_807_NoDefinition(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 807))
        
    def test_808_NoDefinition(self):
        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 808))
        
    def test_809_NoDefinition(self):
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 809))

    def test_810_Redeclared(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 810))
        
    def test_811_Redeclared(self):
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 811))
        
    def test_812_Redeclared(self):
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 812))
        
    def test_813_Redeclared(self):
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 813))
        
    def test_814_Redeclared(self):
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 814))
        
    def test_815_Redeclared(self):
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 815))
        
    def test_816_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                number c
                string VoTien
                begin
                    number c
                    string VoTien
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 816))
        
    def test_817_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 817))

    def test_818_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 818))
        
    def test_819_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 819))

    def test_820_Redeclared(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 820))

    def test_821_Redeclared(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 821))

    def test_822_Redeclared(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 822))
        
    def test_823_Redeclared(self):
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 823))

    def test_824_Redeclared(self):
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 824))
        
    def test_825_Redeclared(self):
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 825))

    def test_826_Redeclared(self):
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 826))

    def test_827_Undeclared(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 827))
        
    def test_828_Undeclared(self):
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 828))

    def test_829_Undeclared(self):
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 829))

    def test_830_Undeclared(self):
        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 830))

    def test_831_Undeclared(self):
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 831))

    def test_832_Undeclared(self):
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 832))

    def test_833_MustInLoop(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 833))

    def test_834_MustInLoop(self):
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 834))

    def test_835_MustInLoop(self):
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 835))

    def test_836_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            var a <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 836))

    def test_837_TypeCannotBeInferred(self):
        input = """
            number VoTien
            var a <- VoTien
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 837))

    def test_838_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 838))

    def test_839_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 839))

    def test_840_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 840))

    def test_841_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 841))

    def test_842_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 842))

    def test_843_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 843))

    def test_844_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 844))

    def test_845_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 845))

    def test_846_TypeMismatchInStatement(self):
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 846))

    def test_847_TypeMismatchInStatement(self):
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 847))

    def test_848_TypeMismatchInStatement(self):
        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 848))

    def test_849_TypeMismatchInStatement(self):
        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 849))

    def test_850_TypeMismatchInStatement(self):
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 850))

    def test_851_TypeMismatchInStatement(self):
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 851))

    def test_852_TypeMismatchInStatement(self):
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 852))

    def test_853_TypeMismatchInStatement(self):
        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 853))

    def test_854_TypeMismatchInStatement(self):
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 854))

    def test_855_TypeMismatchInStatement(self):
        input = """
            func main()begin
                dynamic a
                if (a) number a
                elif (a)  return
                else number a
                
                if(true) number a
                elif (1) number a
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), VarDecl(Id(a), NumberType, None, None)), [(NumLit(1.0), VarDecl(Id(a), NumberType, None, None))], None)"
        self.assertTrue(TestChecker.test(input, expect, 855))

    def test_856_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 856))

    def test_857_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 857))

    def test_858_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 858))

    def test_859_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 859))

    def test_860_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        self.assertTrue(TestChecker.test(input, expect, 860))

    def test_861_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 861))

    def test_862_TypeMismatchInExpression(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 862))

    def test_863_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 863))

    def test_864_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 864))

    def test_865_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 865))

    def test_866_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 866))

    def test_867_TypeMismatchInExpression(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 867))

    def test_868_TypeMismatchInExpression(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 868))

    def test_869_TypeMismatchInExpression(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 869))

    def test_870_TypeMismatchInExpression(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 870))

    def test_871_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 871))

    def test_872_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 872))

    def test_873_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 873))

    def test_874_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 874))

    def test_875_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 875))

    def test_876_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 876))

    def test_877_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 877))

    def test_878_TypeMismatchInExpression(self):
        input = """
            func VoTien()
            func main() begin
                number VoTien_ <- VoTien()
            end
            func VoTien() begin
            end
        """
        # expect = "???"
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 878))

    def test_879_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            var x <- VoTien and (VoTien > VoTien)
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(VoTien), Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 879))

    def test_880_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            var x <- VoTien + VoTien * VoTien
            number y <- VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 880))

    def test_881_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            var x <- VoTien > VoTien ... VoTien < VoTien
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., BinaryOp(>, Id(VoTien), Id(VoTien)), BinaryOp(<, Id(VoTien), Id(VoTien)))"
        self.assertTrue(TestChecker.test(input, expect, 881))

    def test_882_full(self):
        input = """
            func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 882))

    def test_883_full(self):
        input = """
func isPrime(number x)
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 883))

    def test_884_full(self):
        input = """
            var VoTien <- VoTien
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(VoTien), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 884))

    def test_885_full(self):
        input = """
            func main() return main()
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input, expect, 885))

    def test_886_arraylit(self):
        input = """
            dynamic x
            number a <- [x]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 886))

    def test_887_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x]
            func f()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 887))

    def test_888_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, 2]
            func  main()
            begin
                x <- 1
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 888))

    def test_889_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, x, x]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 889))

    def test_890_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, x, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 890))

    def test_891_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 891))

    def test_892_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, [x,x], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 892))

    def test_893_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 893))

    def test_894_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 894))

    def test_895_arraylit(self):
        input = """
            dynamic x
            number a[3,3] <- [[1,2,3], x, x]
            func  main()
            begin
                x <- [1,2,3]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 895))

    def test_896_arraylit(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 896))

    def test_897_arraylit(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 897))

    def test_898_arraylit(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 898))

    def test_899_arraylit(self):
        input = """
            dynamic x
            number a[1,1,1,1] <- [[[x]]]
            func  main()
            begin
                x <- [1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 899))

    def test_900_arraylit(self):
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[[1,2], x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 900))

    def test_901_arraylit(self):
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[x, x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 901))

    def test_902_arraylit(self):
        input = """
            dynamic x
            var a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 902))

    def test_903_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                return [x]                
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 903))

    def test_904_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                return [x, [1,2]]                
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 904))

    def test_905_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 905))

    def test_906_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, y]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 906))

    def test_907_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, [y]]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 907))

    def test_908_arraylit(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo(x)
                x <- [[2,2], [2,3]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 908))

    def test_909_arraylit(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x])
                x <- [1]
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 909))

    def test_910_arraylit(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 910))

    def test_911_arraylit(self):
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 911))

    def test_912_arraylit(self):
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo(x)
                x <- [1,2]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 912))

    def test_913_return(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 913))

    def test_914_return(self):
        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 914))

    def test_915_return(self):
        input = """
            func main() begin 
                return 1
                begin
                    return "string"
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 915))

    def test_916_return(self):
        input = """
            func main() begin 
                dynamic i
                return 1
                return i
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 916))

    def test_917_return(self):
        input = """
            func fun() begin
                return 
                return
                return 1
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 917))

    def test_918_return(self):
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 918))

    def test_919_return(self):
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 919))

    def test_920_return(self):
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 920))

    def test_921_return(self):
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 921))

    def test_922_return(self):
        input = """
            func fun() begin
                number a[2,2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 922))

    def test_923_return(self):
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 923))

    def test_924_return(self):
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 924))

    def test_925_return(self):
        input = """
            func fun() begin
                string a[1,1,1,1,1]
                return a
                return [[[[["1"]]]]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 925))

    def test_926_return(self):
        input = """
            func fun() begin
                return [1,2]
                return [3,4]
            end
            
            func fun1() begin
                return [[1,2], [3,4]]
                return [[1,5], [3,4]]
            end
            
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 926))

    def test_927_return(self):
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 927))

    def test_928_return(self):
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun1()
            end
            func fun3() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 928))

    def test_929_return(self):
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               number a <- fun3()
            end
            func fun3() return "1"  
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 929))

    def test_930_return(self):
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 930))

    def test_931_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 931))

    def test_932_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 932))

    def test_933_Assign(self):
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                a <- c
                c <- b

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 933))

    def test_934_Assign(self):
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                c <- a
                b <- c

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 934))

    def test_935_Assign(self):
        input = """
            func main() begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 935))

    def test_936_Assign(self):
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                c <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 936))

    def test_937_Assign(self):
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [[1,2,3]]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 937))

    def test_938_Assign(self):
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 938))
