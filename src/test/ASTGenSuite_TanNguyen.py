import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite_TanNguyen(unittest.TestCase):
	def test_601(self):
		input = '''
func GWR (bool mxaw, bool TCy5[52.92,3.23,54.04])
	return
dynamic AMUl
number Tk[90.9,73.8,63.5]
func Yb (string af[14.49])	return
'''
		expect = '''Program([FuncDecl(Id(GWR), [VarDecl(Id(mxaw), BoolType, None, None), VarDecl(Id(TCy5), ArrayType([52.92, 3.23, 54.04], BoolType), None, None)], Return()), VarDecl(Id(AMUl), None, dynamic, None), VarDecl(Id(Tk), ArrayType([90.9, 73.8, 63.5], NumberType), None, None), FuncDecl(Id(Yb), [VarDecl(Id(af), ArrayType([14.49], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 601))

	def test_602(self):
		input = '''
bool njOP <- "A"
dynamic aCc7 <- [YzK9 % "a", "nXwy", 85.37]
bool mL[37.36,59.72]
func eVzA ()
	begin
		for z290 until 39.88 by OLX
			string ki
		continue
	end
var JR <- "Jq"
'''
		expect = '''Program([VarDecl(Id(njOP), BoolType, None, StringLit(A)), VarDecl(Id(aCc7), None, dynamic, ArrayLit(BinaryOp(%, Id(YzK9), StringLit(a)), StringLit(nXwy), NumLit(85.37))), VarDecl(Id(mL), ArrayType([37.36, 59.72], BoolType), None, None), FuncDecl(Id(eVzA), [], Block([For(Id(z290), NumLit(39.88), Id(OLX), VarDecl(Id(ki), StringType, None, None)), Continue])), VarDecl(Id(JR), None, var, StringLit(Jq))])'''
		self.assertTrue(TestAST.test(input, expect, 602))

	def test_603(self):
		input = '''
func pIYM (string Fq[5.23,74.14], string gKS, bool Iu21)	return
func TAGs ()	begin
	end
'''
		expect = '''Program([FuncDecl(Id(pIYM), [VarDecl(Id(Fq), ArrayType([5.23, 74.14], StringType), None, None), VarDecl(Id(gKS), StringType, None, None), VarDecl(Id(Iu21), BoolType, None, None)], Return()), FuncDecl(Id(TAGs), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 603))

	def test_604(self):
		input = '''
func x5V ()
	return "NH"
number FjVl
func Kp3 (string OuWV)
	return
'''
		expect = '''Program([FuncDecl(Id(x5V), [], Return(StringLit(NH))), VarDecl(Id(FjVl), NumberType, None, None), FuncDecl(Id(Kp3), [VarDecl(Id(OuWV), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 604))

	def test_605(self):
		input = '''
number DQ <- false
'''
		expect = '''Program([VarDecl(Id(DQ), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 605))

	def test_606(self):
		input = '''
bool jaE
func V9D ()
	begin
	end

func gfC ()	return
func zqHO ()
	begin
		for wxLc until xNN by false
			begin
			end
		hX5t(true, ZK1p)
	end
func DjG ()	return

'''
		expect = '''Program([VarDecl(Id(jaE), BoolType, None, None), FuncDecl(Id(V9D), [], Block([])), FuncDecl(Id(gfC), [], Return()), FuncDecl(Id(zqHO), [], Block([For(Id(wxLc), Id(xNN), BooleanLit(False), Block([])), CallStmt(Id(hX5t), [BooleanLit(True), Id(ZK1p)])])), FuncDecl(Id(DjG), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 606))

	def test_607(self):
		input = '''
func bFu (number uMc[1.79,49.76,18.32], number kG2[54.68], bool yaV)	begin
		break
		XVl(Yxm5, false, 99.4)
		continue
	end

bool nuHv
bool cY
func F9 (bool apD)
	begin
		for NPXd until u6 by 47.36
			continue
		break
		kd[false] <- "Vv"
	end
'''
		expect = '''Program([FuncDecl(Id(bFu), [VarDecl(Id(uMc), ArrayType([1.79, 49.76, 18.32], NumberType), None, None), VarDecl(Id(kG2), ArrayType([54.68], NumberType), None, None), VarDecl(Id(yaV), BoolType, None, None)], Block([Break, CallStmt(Id(XVl), [Id(Yxm5), BooleanLit(False), NumLit(99.4)]), Continue])), VarDecl(Id(nuHv), BoolType, None, None), VarDecl(Id(cY), BoolType, None, None), FuncDecl(Id(F9), [VarDecl(Id(apD), BoolType, None, None)], Block([For(Id(NPXd), Id(u6), NumLit(47.36), Continue), Break, AssignStmt(ArrayCell(Id(kd), [BooleanLit(False)]), StringLit(Vv))]))])'''
		self.assertTrue(TestAST.test(input, expect, 607))

	def test_608(self):
		input = '''
string Ks[93.19]
'''
		expect = '''Program([VarDecl(Id(Ks), ArrayType([93.19], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 608))

	def test_609(self):
		input = '''
func uPO ()
	return "HgS"

'''
		expect = '''Program([FuncDecl(Id(uPO), [], Return(StringLit(HgS)))])'''
		self.assertTrue(TestAST.test(input, expect, 609))

	def test_610(self):
		input = '''
func fN (number AUU7, number b0[90.62,42.2])
	begin
		if (true) break
		elif ("JTN")
		break
		elif (false) if (80.84) O_UJ()
		elif (76.07) for nIsm until Wj by false
			continue
	end
func Af3R (number sH, string r9[88.82,99.31,33.79], bool p7JD[23.55])	return

'''
		expect = '''Program([FuncDecl(Id(fN), [VarDecl(Id(AUU7), NumberType, None, None), VarDecl(Id(b0), ArrayType([90.62, 42.2], NumberType), None, None)], Block([If((BooleanLit(True), Break), [(StringLit(JTN), Break), (BooleanLit(False), If((NumLit(80.84), CallStmt(Id(O_UJ), [])), [(NumLit(76.07), For(Id(nIsm), Id(Wj), BooleanLit(False), Continue))], None))], None)])), FuncDecl(Id(Af3R), [VarDecl(Id(sH), NumberType, None, None), VarDecl(Id(r9), ArrayType([88.82, 99.31, 33.79], StringType), None, None), VarDecl(Id(p7JD), ArrayType([23.55], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 610))

	def test_611(self):
		input = '''
func Kgm ()	return "ZwPDa"
number Jy[2.16,26.15,44.63] <- "ah"
'''
		expect = '''Program([FuncDecl(Id(Kgm), [], Return(StringLit(ZwPDa))), VarDecl(Id(Jy), ArrayType([2.16, 26.15, 44.63], NumberType), None, StringLit(ah))])'''
		self.assertTrue(TestAST.test(input, expect, 611))

	def test_612(self):
		input = '''
string kTh <- "HH"
func jF (number o1X)	return "pRcNw"
number aN[13.68,65.3,67.45] <- KA70
func v5I (number q6l)
	return 38.9

'''
		expect = '''Program([VarDecl(Id(kTh), StringType, None, StringLit(HH)), FuncDecl(Id(jF), [VarDecl(Id(o1X), NumberType, None, None)], Return(StringLit(pRcNw))), VarDecl(Id(aN), ArrayType([13.68, 65.3, 67.45], NumberType), None, Id(KA70)), FuncDecl(Id(v5I), [VarDecl(Id(q6l), NumberType, None, None)], Return(NumLit(38.9)))])'''
		self.assertTrue(TestAST.test(input, expect, 612))

	def test_613(self):
		input = '''
func A4Tm (string X8J[62.57], bool iqwv[1.21,29.43,22.09])
	return 42.24

bool uR
bool Dqg[66.7,23.4] <- false
'''
		expect = '''Program([FuncDecl(Id(A4Tm), [VarDecl(Id(X8J), ArrayType([62.57], StringType), None, None), VarDecl(Id(iqwv), ArrayType([1.21, 29.43, 22.09], BoolType), None, None)], Return(NumLit(42.24))), VarDecl(Id(uR), BoolType, None, None), VarDecl(Id(Dqg), ArrayType([66.7, 23.4], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 613))

	def test_614(self):
		input = '''
number h3iG[3.6] <- L8
func uO ()	return 70.38
number Q_
func eW (string L6Lx, bool UO)
	return
bool oBzr[24.69,75.95,89.2]
'''
		expect = '''Program([VarDecl(Id(h3iG), ArrayType([3.6], NumberType), None, Id(L8)), FuncDecl(Id(uO), [], Return(NumLit(70.38))), VarDecl(Id(Q_), NumberType, None, None), FuncDecl(Id(eW), [VarDecl(Id(L6Lx), StringType, None, None), VarDecl(Id(UO), BoolType, None, None)], Return()), VarDecl(Id(oBzr), ArrayType([24.69, 75.95, 89.2], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 614))

	def test_615(self):
		input = '''
func YQt ()	return sB

number xA[50.88,74.82,95.84]
string vRT <- "qm"
number yCx[80.72,76.82,22.66] <- "Z"
bool ZAu[17.56,52.61]
'''
		expect = '''Program([FuncDecl(Id(YQt), [], Return(Id(sB))), VarDecl(Id(xA), ArrayType([50.88, 74.82, 95.84], NumberType), None, None), VarDecl(Id(vRT), StringType, None, StringLit(qm)), VarDecl(Id(yCx), ArrayType([80.72, 76.82, 22.66], NumberType), None, StringLit(Z)), VarDecl(Id(ZAu), ArrayType([17.56, 52.61], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 615))

	def test_616(self):
		input = '''
string TzF[74.08,67.39]
var yP <- "JaH"
func E9K (string yhh, bool jL[63.5,45.69,72.46])	return 14.51

func kU ()
	return

'''
		expect = '''Program([VarDecl(Id(TzF), ArrayType([74.08, 67.39], StringType), None, None), VarDecl(Id(yP), None, var, StringLit(JaH)), FuncDecl(Id(E9K), [VarDecl(Id(yhh), StringType, None, None), VarDecl(Id(jL), ArrayType([63.5, 45.69, 72.46], BoolType), None, None)], Return(NumLit(14.51))), FuncDecl(Id(kU), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 616))

	def test_617(self):
		input = '''
func J7 ()	return true
func qEi (bool g4u, number It)	return
dynamic RZD <- c1cO
'''
		expect = '''Program([FuncDecl(Id(J7), [], Return(BooleanLit(True))), FuncDecl(Id(qEi), [VarDecl(Id(g4u), BoolType, None, None), VarDecl(Id(It), NumberType, None, None)], Return()), VarDecl(Id(RZD), None, dynamic, Id(c1cO))])'''
		self.assertTrue(TestAST.test(input, expect, 617))

	def test_618(self):
		input = '''
func JO (number Lxgv)
	begin
		begin
			continue
		end
		for h3 until "vJU" by ZA4g
			return true
		break
	end
number yP[84.96,98.43]
var PlB <- "YnvdM"
'''
		expect = '''Program([FuncDecl(Id(JO), [VarDecl(Id(Lxgv), NumberType, None, None)], Block([Block([Continue]), For(Id(h3), StringLit(vJU), Id(ZA4g), Return(BooleanLit(True))), Break])), VarDecl(Id(yP), ArrayType([84.96, 98.43], NumberType), None, None), VarDecl(Id(PlB), None, var, StringLit(YnvdM))])'''
		self.assertTrue(TestAST.test(input, expect, 618))

	def test_619(self):
		input = '''
bool TH <- "A"
func NYp (number M5[79.84])
	return "WwLWB"

bool W0[35.64] <- "VjRxf"
func EM (bool pw7e[8.52], number Lo[17.09,79.35], string xe8[64.63,98.29])	begin
	end
'''
		expect = '''Program([VarDecl(Id(TH), BoolType, None, StringLit(A)), FuncDecl(Id(NYp), [VarDecl(Id(M5), ArrayType([79.84], NumberType), None, None)], Return(StringLit(WwLWB))), VarDecl(Id(W0), ArrayType([35.64], BoolType), None, StringLit(VjRxf)), FuncDecl(Id(EM), [VarDecl(Id(pw7e), ArrayType([8.52], BoolType), None, None), VarDecl(Id(Lo), ArrayType([17.09, 79.35], NumberType), None, None), VarDecl(Id(xe8), ArrayType([64.63, 98.29], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 619))

	def test_620(self):
		input = '''
func xaqW (string Lkj)	begin
		return
		bool am <- true
	end
func NK8S ()
	begin
		g5LE(true, "VgNoA", false)
		break
		return
	end

bool Ae[4.61,50.58]
func AUis ()	return

string lfI[35.86] <- 70.03
'''
		expect = '''Program([FuncDecl(Id(xaqW), [VarDecl(Id(Lkj), StringType, None, None)], Block([Return(), VarDecl(Id(am), BoolType, None, BooleanLit(True))])), FuncDecl(Id(NK8S), [], Block([CallStmt(Id(g5LE), [BooleanLit(True), StringLit(VgNoA), BooleanLit(False)]), Break, Return()])), VarDecl(Id(Ae), ArrayType([4.61, 50.58], BoolType), None, None), FuncDecl(Id(AUis), [], Return()), VarDecl(Id(lfI), ArrayType([35.86], StringType), None, NumLit(70.03))])'''
		self.assertTrue(TestAST.test(input, expect, 620))

	def test_621(self):
		input = '''
var ahn <- true
'''
		expect = '''Program([VarDecl(Id(ahn), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 621))

	def test_622(self):
		input = '''
var Lr6 <- yv
'''
		expect = '''Program([VarDecl(Id(Lr6), None, var, Id(yv))])'''
		self.assertTrue(TestAST.test(input, expect, 622))

	def test_623(self):
		input = '''
dynamic Z6P <- true
number aN <- "NPxd"
func j8CX ()
	begin
		return "e"
	end
bool xB[75.09,18.86]
'''
		expect = '''Program([VarDecl(Id(Z6P), None, dynamic, BooleanLit(True)), VarDecl(Id(aN), NumberType, None, StringLit(NPxd)), FuncDecl(Id(j8CX), [], Block([Return(StringLit(e))])), VarDecl(Id(xB), ArrayType([75.09, 18.86], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 623))

	def test_624(self):
		input = '''
func peZ (number vs, bool hfyW[84.47,75.28,26.83])	return

func SQV0 (bool sZPE[55.57,41.94])	begin
		break
		TM_[false, true, 19.33] <- "njUtZ"
		return "VTFp"
	end

'''
		expect = '''Program([FuncDecl(Id(peZ), [VarDecl(Id(vs), NumberType, None, None), VarDecl(Id(hfyW), ArrayType([84.47, 75.28, 26.83], BoolType), None, None)], Return()), FuncDecl(Id(SQV0), [VarDecl(Id(sZPE), ArrayType([55.57, 41.94], BoolType), None, None)], Block([Break, AssignStmt(ArrayCell(Id(TM_), [BooleanLit(False), BooleanLit(True), NumLit(19.33)]), StringLit(njUtZ)), Return(StringLit(VTFp))]))])'''
		self.assertTrue(TestAST.test(input, expect, 624))

	def test_625(self):
		input = '''
func JFKu (string cL)	begin
		string ZMz2[54.16,4.29] <- mK
		return
	end
func f1 (string vH3Q, string I7[35.81,81.88], number qqg[84.56,95.75,44.29])
	return false

'''
		expect = '''Program([FuncDecl(Id(JFKu), [VarDecl(Id(cL), StringType, None, None)], Block([VarDecl(Id(ZMz2), ArrayType([54.16, 4.29], StringType), None, Id(mK)), Return()])), FuncDecl(Id(f1), [VarDecl(Id(vH3Q), StringType, None, None), VarDecl(Id(I7), ArrayType([35.81, 81.88], StringType), None, None), VarDecl(Id(qqg), ArrayType([84.56, 95.75, 44.29], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 625))

	def test_626(self):
		input = '''
var Oz <- n7k
func lZzW ()
	return
'''
		expect = '''Program([VarDecl(Id(Oz), None, var, Id(n7k)), FuncDecl(Id(lZzW), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 626))

	def test_627(self):
		input = '''
string eC
string EcK[57.29]
'''
		expect = '''Program([VarDecl(Id(eC), StringType, None, None), VarDecl(Id(EcK), ArrayType([57.29], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 627))

	def test_628(self):
		input = '''
func suo (number OMq[70.77,61.15,24.59])	return

var lc <- 53.4
func GG0p (string Oni[49.86,35.81,2.78], string OXY)
	begin
		number nPJh[91.36,20.28,86.4]
	end
func Y2 (number LYrh)	return 72.19

func ps (bool D61, string jNE[68.3,73.6,96.2], string ArJ)	return

'''
		expect = '''Program([FuncDecl(Id(suo), [VarDecl(Id(OMq), ArrayType([70.77, 61.15, 24.59], NumberType), None, None)], Return()), VarDecl(Id(lc), None, var, NumLit(53.4)), FuncDecl(Id(GG0p), [VarDecl(Id(Oni), ArrayType([49.86, 35.81, 2.78], StringType), None, None), VarDecl(Id(OXY), StringType, None, None)], Block([VarDecl(Id(nPJh), ArrayType([91.36, 20.28, 86.4], NumberType), None, None)])), FuncDecl(Id(Y2), [VarDecl(Id(LYrh), NumberType, None, None)], Return(NumLit(72.19))), FuncDecl(Id(ps), [VarDecl(Id(D61), BoolType, None, None), VarDecl(Id(jNE), ArrayType([68.3, 73.6, 96.2], StringType), None, None), VarDecl(Id(ArJ), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 628))

	def test_629(self):
		input = '''
func GN5t ()
	return "of"
func he (number jtt, number YMI)	begin
		bool bPRs <- "SpW"
		continue
		E3RV[true, false, 68.89] <- "c"
	end

number S5ra <- 14.9
'''
		expect = '''Program([FuncDecl(Id(GN5t), [], Return(StringLit(of))), FuncDecl(Id(he), [VarDecl(Id(jtt), NumberType, None, None), VarDecl(Id(YMI), NumberType, None, None)], Block([VarDecl(Id(bPRs), BoolType, None, StringLit(SpW)), Continue, AssignStmt(ArrayCell(Id(E3RV), [BooleanLit(True), BooleanLit(False), NumLit(68.89)]), StringLit(c))])), VarDecl(Id(S5ra), NumberType, None, NumLit(14.9))])'''
		self.assertTrue(TestAST.test(input, expect, 629))

	def test_630(self):
		input = '''
func tl (string wS, number my5A[32.98], string YiQM[67.89,40.36])	return 64.31

func gb7 (number vtTh)	return 74.97
dynamic WY3l
'''
		expect = '''Program([FuncDecl(Id(tl), [VarDecl(Id(wS), StringType, None, None), VarDecl(Id(my5A), ArrayType([32.98], NumberType), None, None), VarDecl(Id(YiQM), ArrayType([67.89, 40.36], StringType), None, None)], Return(NumLit(64.31))), FuncDecl(Id(gb7), [VarDecl(Id(vtTh), NumberType, None, None)], Return(NumLit(74.97))), VarDecl(Id(WY3l), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 630))

	def test_631(self):
		input = '''
string Cx[75.9,40.71,11.0] <- kEFy
bool MUSD[82.32,38.38] <- "uTMNg"
func ds25 (number oLzj, string xn7[49.75,2.88,81.74])
	return

func qj ()
	return UVFY

'''
		expect = '''Program([VarDecl(Id(Cx), ArrayType([75.9, 40.71, 11.0], StringType), None, Id(kEFy)), VarDecl(Id(MUSD), ArrayType([82.32, 38.38], BoolType), None, StringLit(uTMNg)), FuncDecl(Id(ds25), [VarDecl(Id(oLzj), NumberType, None, None), VarDecl(Id(xn7), ArrayType([49.75, 2.88, 81.74], StringType), None, None)], Return()), FuncDecl(Id(qj), [], Return(Id(UVFY)))])'''
		self.assertTrue(TestAST.test(input, expect, 631))

	def test_632(self):
		input = '''
func m7KP (number i8y[26.62], string EzAl, string lDn[82.24])	begin
		if (false)
		for VSO until 26.93 by b3
			continue
		elif (false) number hi[71.73,28.71] <- false
		elif ("ILY") if ("kFSYL") if (dRR) continue
		elif (true) number Vnd <- true
		elif (58.05) continue
		elif (false)
		if (eW)
		EGj["GB"] <- Lrh
		elif (false)
		return
		else wEA5("cKG", 53.85, Qo)
		elif (aKA)
		number XBW4[60.75,25.67,94.17]
		elif (4.43) for aa until 24.16 by W20
			if ("L") begin
				return "CCqxx"
				for Fmr9 until 94.75 by R0g
					continue
				continue
			end
			elif ("zWDR") number MY[22.93,17.14] <- "jyYv"
			elif (GGGp) break
			elif ("iD") if (kA) for Fen until false by true
				FJHP(false, 16.49, CE)
			elif (false)
			continue
			elif (29.2) begin
				kqjA[false, 63.67, 44.62] <- false
			end
			elif (83.49)
			for N9H until 67.79 by "sEB"
				zM_ <- qfY
			elif (false) continue
			else begin
				if ("MGm") continue
				elif (SvD)
				begin
				end
				elif (31.79)
				begin
					Qc <- false
					for cQ until zm by "pjuZA"
						sW[84.39, vt] <- 22.99
					FF0p <- true
				end
				elif (true) return X_
				else if (98.49) continue
				elif (false)
				return
				elif (false)
				bool jk0w[2.09,9.33,73.35]
				else return
				for jOtv until JS by "Er"
					begin
						break
						begin
							for M9 until ww0w by qW9R
								K_7(Z8Z, "TxX", vTo)
							bool J7Y[0.96,99.0,60.39]
						end
					end
				uL6(NQ2, true, "vLZeR")
			end
		else return 2.97
	end
func m5gf (string aK)
	return
func lX (string aBy, bool IQm)
	begin
		fHrv("sxDBR", true)
		continue
		PuDx(false)
	end
func F3N (bool xOrS[24.73], string XHkf)
	return true
'''
		expect = '''Program([FuncDecl(Id(m7KP), [VarDecl(Id(i8y), ArrayType([26.62], NumberType), None, None), VarDecl(Id(EzAl), StringType, None, None), VarDecl(Id(lDn), ArrayType([82.24], StringType), None, None)], Block([If((BooleanLit(False), For(Id(VSO), NumLit(26.93), Id(b3), Continue)), [(BooleanLit(False), VarDecl(Id(hi), ArrayType([71.73, 28.71], NumberType), None, BooleanLit(False))), (StringLit(ILY), If((StringLit(kFSYL), If((Id(dRR), Continue), [(BooleanLit(True), VarDecl(Id(Vnd), NumberType, None, BooleanLit(True))), (NumLit(58.05), Continue), (BooleanLit(False), If((Id(eW), AssignStmt(ArrayCell(Id(EGj), [StringLit(GB)]), Id(Lrh))), [(BooleanLit(False), Return())], CallStmt(Id(wEA5), [StringLit(cKG), NumLit(53.85), Id(Qo)]))), (Id(aKA), VarDecl(Id(XBW4), ArrayType([60.75, 25.67, 94.17], NumberType), None, None)), (NumLit(4.43), For(Id(aa), NumLit(24.16), Id(W20), If((StringLit(L), Block([Return(StringLit(CCqxx)), For(Id(Fmr9), NumLit(94.75), Id(R0g), Continue), Continue])), [(StringLit(zWDR), VarDecl(Id(MY), ArrayType([22.93, 17.14], NumberType), None, StringLit(jyYv))), (Id(GGGp), Break), (StringLit(iD), If((Id(kA), For(Id(Fen), BooleanLit(False), BooleanLit(True), CallStmt(Id(FJHP), [BooleanLit(False), NumLit(16.49), Id(CE)]))), [(BooleanLit(False), Continue), (NumLit(29.2), Block([AssignStmt(ArrayCell(Id(kqjA), [BooleanLit(False), NumLit(63.67), NumLit(44.62)]), BooleanLit(False))])), (NumLit(83.49), For(Id(N9H), NumLit(67.79), StringLit(sEB), AssignStmt(Id(zM_), Id(qfY)))), (BooleanLit(False), Continue)], Block([If((StringLit(MGm), Continue), [(Id(SvD), Block([])), (NumLit(31.79), Block([AssignStmt(Id(Qc), BooleanLit(False)), For(Id(cQ), Id(zm), StringLit(pjuZA), AssignStmt(ArrayCell(Id(sW), [NumLit(84.39), Id(vt)]), NumLit(22.99))), AssignStmt(Id(FF0p), BooleanLit(True))])), (BooleanLit(True), Return(Id(X_)))], If((NumLit(98.49), Continue), [(BooleanLit(False), Return()), (BooleanLit(False), VarDecl(Id(jk0w), ArrayType([2.09, 9.33, 73.35], BoolType), None, None))], Return())), For(Id(jOtv), Id(JS), StringLit(Er), Block([Break, Block([For(Id(M9), Id(ww0w), Id(qW9R), CallStmt(Id(K_7), [Id(Z8Z), StringLit(TxX), Id(vTo)])), VarDecl(Id(J7Y), ArrayType([0.96, 99.0, 60.39], BoolType), None, None)])])), CallStmt(Id(uL6), [Id(NQ2), BooleanLit(True), StringLit(vLZeR)])])))], Return(NumLit(2.97)))))], None)), [], None))], None)])), FuncDecl(Id(m5gf), [VarDecl(Id(aK), StringType, None, None)], Return()), FuncDecl(Id(lX), [VarDecl(Id(aBy), StringType, None, None), VarDecl(Id(IQm), BoolType, None, None)], Block([CallStmt(Id(fHrv), [StringLit(sxDBR), BooleanLit(True)]), Continue, CallStmt(Id(PuDx), [BooleanLit(False)])])), FuncDecl(Id(F3N), [VarDecl(Id(xOrS), ArrayType([24.73], BoolType), None, None), VarDecl(Id(XHkf), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 632))

	def test_633(self):
		input = '''
func FE (string M8JY)
	begin
		BPz <- le
	end

bool bh5Y <- false
func BR (number Ch[27.53,35.26])
	return P8X3

func uv7 (number lk)	return

func I6 (number GO[59.1,76.02,94.1])
	return
'''
		expect = '''Program([FuncDecl(Id(FE), [VarDecl(Id(M8JY), StringType, None, None)], Block([AssignStmt(Id(BPz), Id(le))])), VarDecl(Id(bh5Y), BoolType, None, BooleanLit(False)), FuncDecl(Id(BR), [VarDecl(Id(Ch), ArrayType([27.53, 35.26], NumberType), None, None)], Return(Id(P8X3))), FuncDecl(Id(uv7), [VarDecl(Id(lk), NumberType, None, None)], Return()), FuncDecl(Id(I6), [VarDecl(Id(GO), ArrayType([59.1, 76.02, 94.1], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 633))

	def test_634(self):
		input = '''
number nXJ <- true
func TJPD (bool q1Yf[51.06], string G6u[63.59,39.14], bool jDC[95.07,17.85])
	begin
		continue
		RZb9 <- 8.45
		dynamic j07 <- "IKAZ"
	end

func Qju9 (number KG)	return

dynamic BwPJ <- 31.85
func kMz5 ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(nXJ), NumberType, None, BooleanLit(True)), FuncDecl(Id(TJPD), [VarDecl(Id(q1Yf), ArrayType([51.06], BoolType), None, None), VarDecl(Id(G6u), ArrayType([63.59, 39.14], StringType), None, None), VarDecl(Id(jDC), ArrayType([95.07, 17.85], BoolType), None, None)], Block([Continue, AssignStmt(Id(RZb9), NumLit(8.45)), VarDecl(Id(j07), None, dynamic, StringLit(IKAZ))])), FuncDecl(Id(Qju9), [VarDecl(Id(KG), NumberType, None, None)], Return()), VarDecl(Id(BwPJ), None, dynamic, NumLit(31.85)), FuncDecl(Id(kMz5), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 634))

	def test_635(self):
		input = '''
func oA (bool o0R[37.93,79.28])	return ejs

dynamic a5
func JXfs (bool ghs2)
	return
'''
		expect = '''Program([FuncDecl(Id(oA), [VarDecl(Id(o0R), ArrayType([37.93, 79.28], BoolType), None, None)], Return(Id(ejs))), VarDecl(Id(a5), None, dynamic, None), FuncDecl(Id(JXfs), [VarDecl(Id(ghs2), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 635))

	def test_636(self):
		input = '''
func u98 ()
	return

func gU ()
	begin
		nwe(false)
	end

string IRRy <- 95.82
string DT[38.16,63.43]
'''
		expect = '''Program([FuncDecl(Id(u98), [], Return()), FuncDecl(Id(gU), [], Block([CallStmt(Id(nwe), [BooleanLit(False)])])), VarDecl(Id(IRRy), StringType, None, NumLit(95.82)), VarDecl(Id(DT), ArrayType([38.16, 63.43], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 636))

	def test_637(self):
		input = '''
number JkMi <- XbpM
func DV7 (string HSBr, number fH[1.11], string eou)	begin
	end

'''
		expect = '''Program([VarDecl(Id(JkMi), NumberType, None, Id(XbpM)), FuncDecl(Id(DV7), [VarDecl(Id(HSBr), StringType, None, None), VarDecl(Id(fH), ArrayType([1.11], NumberType), None, None), VarDecl(Id(eou), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 637))

	def test_638(self):
		input = '''
number AW
bool oo3g[37.44]
string Nh6K[13.52] <- 85.87
'''
		expect = '''Program([VarDecl(Id(AW), NumberType, None, None), VarDecl(Id(oo3g), ArrayType([37.44], BoolType), None, None), VarDecl(Id(Nh6K), ArrayType([13.52], StringType), None, NumLit(85.87))])'''
		self.assertTrue(TestAST.test(input, expect, 638))

	def test_639(self):
		input = '''
func OBT7 ()
	return 72.26

'''
		expect = '''Program([FuncDecl(Id(OBT7), [], Return(NumLit(72.26)))])'''
		self.assertTrue(TestAST.test(input, expect, 639))

	def test_640(self):
		input = '''
string gg
number rb[87.43,38.3,80.08]
bool XFP0[75.16] <- "zTupi"
'''
		expect = '''Program([VarDecl(Id(gg), StringType, None, None), VarDecl(Id(rb), ArrayType([87.43, 38.3, 80.08], NumberType), None, None), VarDecl(Id(XFP0), ArrayType([75.16], BoolType), None, StringLit(zTupi))])'''
		self.assertTrue(TestAST.test(input, expect, 640))

	def test_641(self):
		input = '''
dynamic WdG <- true
func eLk ()
	return

func yda (bool BT8[50.44], string Fef[10.88,64.69])	return

bool lL <- "UQKHi"
func T_h (bool bIsq[36.23,15.22], number cjM[22.76,41.83])
	return
'''
		expect = '''Program([VarDecl(Id(WdG), None, dynamic, BooleanLit(True)), FuncDecl(Id(eLk), [], Return()), FuncDecl(Id(yda), [VarDecl(Id(BT8), ArrayType([50.44], BoolType), None, None), VarDecl(Id(Fef), ArrayType([10.88, 64.69], StringType), None, None)], Return()), VarDecl(Id(lL), BoolType, None, StringLit(UQKHi)), FuncDecl(Id(T_h), [VarDecl(Id(bIsq), ArrayType([36.23, 15.22], BoolType), None, None), VarDecl(Id(cjM), ArrayType([22.76, 41.83], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 641))

	def test_642(self):
		input = '''
func nOHX (bool uA3, bool QgQ[17.56,95.1])	begin
		if (true)
		string tLb[73.15,9.73,74.36]
		elif ("Ty")
		uN(true, VBir, true)
		elif ("Il")
		rwW()
		elif (true) return 31.3
		elif ("P") if (true)
		continue
		elif (56.19)
		continue
		elif (98.09) if ("mDOH")
		for gDd8 until "Lxq" by n8
			continue
		elif (false) return
		elif (true) for Dp until 27.25 by nNZN
			Z5D[false, 92.38] <- 17.72
		elif (47.36)
		for EQdz until false by false
			L_ <- tj7
		elif (27.09)
		break
		elif ("iC")
		lxEY <- 75.26
		elif (false) zp <- false
		else for qZ until true by false
			zDU7(false, Xwp, "vEL")
		return 55.89
		EB(true, wP, "pKmGE")
	end

func oav ()	return jr
func LZwH (number PW_n[22.3,22.52,70.86])	return 54.91
string y6Es[17.76,17.21]
'''
		expect = '''Program([FuncDecl(Id(nOHX), [VarDecl(Id(uA3), BoolType, None, None), VarDecl(Id(QgQ), ArrayType([17.56, 95.1], BoolType), None, None)], Block([If((BooleanLit(True), VarDecl(Id(tLb), ArrayType([73.15, 9.73, 74.36], StringType), None, None)), [(StringLit(Ty), CallStmt(Id(uN), [BooleanLit(True), Id(VBir), BooleanLit(True)])), (StringLit(Il), CallStmt(Id(rwW), [])), (BooleanLit(True), Return(NumLit(31.3))), (StringLit(P), If((BooleanLit(True), Continue), [(NumLit(56.19), Continue), (NumLit(98.09), If((StringLit(mDOH), For(Id(gDd8), StringLit(Lxq), Id(n8), Continue)), [(BooleanLit(False), Return()), (BooleanLit(True), For(Id(Dp), NumLit(27.25), Id(nNZN), AssignStmt(ArrayCell(Id(Z5D), [BooleanLit(False), NumLit(92.38)]), NumLit(17.72)))), (NumLit(47.36), For(Id(EQdz), BooleanLit(False), BooleanLit(False), AssignStmt(Id(L_), Id(tj7)))), (NumLit(27.09), Break), (StringLit(iC), AssignStmt(Id(lxEY), NumLit(75.26))), (BooleanLit(False), AssignStmt(Id(zp), BooleanLit(False)))], For(Id(qZ), BooleanLit(True), BooleanLit(False), CallStmt(Id(zDU7), [BooleanLit(False), Id(Xwp), StringLit(vEL)]))))], None))], None), Return(NumLit(55.89)), CallStmt(Id(EB), [BooleanLit(True), Id(wP), StringLit(pKmGE)])])), FuncDecl(Id(oav), [], Return(Id(jr))), FuncDecl(Id(LZwH), [VarDecl(Id(PW_n), ArrayType([22.3, 22.52, 70.86], NumberType), None, None)], Return(NumLit(54.91))), VarDecl(Id(y6Es), ArrayType([17.76, 17.21], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 642))

	def test_643(self):
		input = '''
func vD ()	return
func Pq0 (string tQHk, string NfH6[41.57,79.6], string Io91[80.12,38.06])
	return false

var O4P <- "X"
func Xy (number IB0[55.27,42.37], bool DqsZ[36.9], string Uc)
	begin
		if (B0b) number Vrcf[85.24,39.83]
		elif (true)
		break
		elif (false)
		return
	end
'''
		expect = '''Program([FuncDecl(Id(vD), [], Return()), FuncDecl(Id(Pq0), [VarDecl(Id(tQHk), StringType, None, None), VarDecl(Id(NfH6), ArrayType([41.57, 79.6], StringType), None, None), VarDecl(Id(Io91), ArrayType([80.12, 38.06], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(O4P), None, var, StringLit(X)), FuncDecl(Id(Xy), [VarDecl(Id(IB0), ArrayType([55.27, 42.37], NumberType), None, None), VarDecl(Id(DqsZ), ArrayType([36.9], BoolType), None, None), VarDecl(Id(Uc), StringType, None, None)], Block([If((Id(B0b), VarDecl(Id(Vrcf), ArrayType([85.24, 39.83], NumberType), None, None)), [(BooleanLit(True), Break), (BooleanLit(False), Return())], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 643))

	def test_644(self):
		input = '''
func t8QF (number cv[13.5,45.93,18.06], string VWB[73.44,63.76,88.8], number cl8J[3.77])
	return

func LT4 (number FiyW, string R2c)
	return 42.22
'''
		expect = '''Program([FuncDecl(Id(t8QF), [VarDecl(Id(cv), ArrayType([13.5, 45.93, 18.06], NumberType), None, None), VarDecl(Id(VWB), ArrayType([73.44, 63.76, 88.8], StringType), None, None), VarDecl(Id(cl8J), ArrayType([3.77], NumberType), None, None)], Return()), FuncDecl(Id(LT4), [VarDecl(Id(FiyW), NumberType, None, None), VarDecl(Id(R2c), StringType, None, None)], Return(NumLit(42.22)))])'''
		self.assertTrue(TestAST.test(input, expect, 644))

	def test_645(self):
		input = '''
func Im (string lm3[85.47,73.68], string aA4I[62.26])
	return gBWE
func DOac (string mp7, bool Qm, number DdG)
	return false

var e3E <- 81.65
func Lkw8 (bool hAx[67.83,18.78], string Pd2[84.09,61.64,79.66], number HE1[67.7,55.98])	return

'''
		expect = '''Program([FuncDecl(Id(Im), [VarDecl(Id(lm3), ArrayType([85.47, 73.68], StringType), None, None), VarDecl(Id(aA4I), ArrayType([62.26], StringType), None, None)], Return(Id(gBWE))), FuncDecl(Id(DOac), [VarDecl(Id(mp7), StringType, None, None), VarDecl(Id(Qm), BoolType, None, None), VarDecl(Id(DdG), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(e3E), None, var, NumLit(81.65)), FuncDecl(Id(Lkw8), [VarDecl(Id(hAx), ArrayType([67.83, 18.78], BoolType), None, None), VarDecl(Id(Pd2), ArrayType([84.09, 61.64, 79.66], StringType), None, None), VarDecl(Id(HE1), ArrayType([67.7, 55.98], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 645))

	def test_646(self):
		input = '''
number aSO[45.07,30.36,46.74] <- 52.8
bool y9[54.58,54.58] <- "HoX"
func oM0 (bool R999, bool S1, bool JrN)	return 45.32
var Yd1 <- "KSy"
func bnx ()	return 95.42

'''
		expect = '''Program([VarDecl(Id(aSO), ArrayType([45.07, 30.36, 46.74], NumberType), None, NumLit(52.8)), VarDecl(Id(y9), ArrayType([54.58, 54.58], BoolType), None, StringLit(HoX)), FuncDecl(Id(oM0), [VarDecl(Id(R999), BoolType, None, None), VarDecl(Id(S1), BoolType, None, None), VarDecl(Id(JrN), BoolType, None, None)], Return(NumLit(45.32))), VarDecl(Id(Yd1), None, var, StringLit(KSy)), FuncDecl(Id(bnx), [], Return(NumLit(95.42)))])'''
		self.assertTrue(TestAST.test(input, expect, 646))

	def test_647(self):
		input = '''
number vai <- Us
number UG
bool cp
var cCF <- true
bool MM
'''
		expect = '''Program([VarDecl(Id(vai), NumberType, None, Id(Us)), VarDecl(Id(UG), NumberType, None, None), VarDecl(Id(cp), BoolType, None, None), VarDecl(Id(cCF), None, var, BooleanLit(True)), VarDecl(Id(MM), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 647))

	def test_648(self):
		input = '''
func GEQC (string qm, number oC3G[7.18,18.62,95.2], bool RP)	begin
	end
dynamic Oc_w
var KS <- o5
'''
		expect = '''Program([FuncDecl(Id(GEQC), [VarDecl(Id(qm), StringType, None, None), VarDecl(Id(oC3G), ArrayType([7.18, 18.62, 95.2], NumberType), None, None), VarDecl(Id(RP), BoolType, None, None)], Block([])), VarDecl(Id(Oc_w), None, dynamic, None), VarDecl(Id(KS), None, var, Id(o5))])'''
		self.assertTrue(TestAST.test(input, expect, 648))

	def test_649(self):
		input = '''
bool Gn[19.08,42.13]
'''
		expect = '''Program([VarDecl(Id(Gn), ArrayType([19.08, 42.13], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 649))

	def test_650(self):
		input = '''
string jBEV <- 82.38
func xQ5T (bool rNR, number jIPK[74.58,7.22,79.58])	return
'''
		expect = '''Program([VarDecl(Id(jBEV), StringType, None, NumLit(82.38)), FuncDecl(Id(xQ5T), [VarDecl(Id(rNR), BoolType, None, None), VarDecl(Id(jIPK), ArrayType([74.58, 7.22, 79.58], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 650))

	def test_651(self):
		input = '''
number UgMJ[22.15,16.52,61.85] <- false
number Lx[64.69,28.91,3.36]
func Mg (bool CoZ0, string feNd[7.03,40.36])	return false

func cHo7 (number tB, number JXR)	return true
bool lv0[83.3] <- iSd
'''
		expect = '''Program([VarDecl(Id(UgMJ), ArrayType([22.15, 16.52, 61.85], NumberType), None, BooleanLit(False)), VarDecl(Id(Lx), ArrayType([64.69, 28.91, 3.36], NumberType), None, None), FuncDecl(Id(Mg), [VarDecl(Id(CoZ0), BoolType, None, None), VarDecl(Id(feNd), ArrayType([7.03, 40.36], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(cHo7), [VarDecl(Id(tB), NumberType, None, None), VarDecl(Id(JXR), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(lv0), ArrayType([83.3], BoolType), None, Id(iSd))])'''
		self.assertTrue(TestAST.test(input, expect, 651))

	def test_652(self):
		input = '''
string ne_z
bool RjRx <- ie0
number Cfhj
func gRlG (bool PdgT[57.79,75.94,69.93], number N_)	return

'''
		expect = '''Program([VarDecl(Id(ne_z), StringType, None, None), VarDecl(Id(RjRx), BoolType, None, Id(ie0)), VarDecl(Id(Cfhj), NumberType, None, None), FuncDecl(Id(gRlG), [VarDecl(Id(PdgT), ArrayType([57.79, 75.94, 69.93], BoolType), None, None), VarDecl(Id(N_), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 652))

	def test_653(self):
		input = '''
string kV7C[12.12,26.05,10.58]
func GVKr ()
	return

func PcH (number NkLE[6.59,94.27,45.77], bool wGqn[17.7,1.15,37.96])	begin
	end

dynamic tqhG
number nLmt[69.35]
'''
		expect = '''Program([VarDecl(Id(kV7C), ArrayType([12.12, 26.05, 10.58], StringType), None, None), FuncDecl(Id(GVKr), [], Return()), FuncDecl(Id(PcH), [VarDecl(Id(NkLE), ArrayType([6.59, 94.27, 45.77], NumberType), None, None), VarDecl(Id(wGqn), ArrayType([17.7, 1.15, 37.96], BoolType), None, None)], Block([])), VarDecl(Id(tqhG), None, dynamic, None), VarDecl(Id(nLmt), ArrayType([69.35], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 653))

	def test_654(self):
		input = '''
func Wv (bool BA[67.35])
	begin
		return
		return
	end
func H4tC (string h3, string DGo[24.5,35.26])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Wv), [VarDecl(Id(BA), ArrayType([67.35], BoolType), None, None)], Block([Return(), Return()])), FuncDecl(Id(H4tC), [VarDecl(Id(h3), StringType, None, None), VarDecl(Id(DGo), ArrayType([24.5, 35.26], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 654))

	def test_655(self):
		input = '''
string ml <- "Zx"
'''
		expect = '''Program([VarDecl(Id(ml), StringType, None, StringLit(Zx))])'''
		self.assertTrue(TestAST.test(input, expect, 655))

	def test_656(self):
		input = '''
func o03 ()	return Yv
'''
		expect = '''Program([FuncDecl(Id(o03), [], Return(Id(Yv)))])'''
		self.assertTrue(TestAST.test(input, expect, 656))

	def test_657(self):
		input = '''
string zx[16.63] <- "ftdYd"
func Ja6 (number f3[71.13,41.59])	return

'''
		expect = '''Program([VarDecl(Id(zx), ArrayType([16.63], StringType), None, StringLit(ftdYd)), FuncDecl(Id(Ja6), [VarDecl(Id(f3), ArrayType([71.13, 41.59], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 657))

	def test_658(self):
		input = '''
func EL4R (number Ez[54.76,77.16], string eGu[3.37,15.22,11.64])	return
var d0 <- Aafw
var mx2u <- false
func Hu ()
	return 68.53

bool Xb[36.59,35.89,15.63]
'''
		expect = '''Program([FuncDecl(Id(EL4R), [VarDecl(Id(Ez), ArrayType([54.76, 77.16], NumberType), None, None), VarDecl(Id(eGu), ArrayType([3.37, 15.22, 11.64], StringType), None, None)], Return()), VarDecl(Id(d0), None, var, Id(Aafw)), VarDecl(Id(mx2u), None, var, BooleanLit(False)), FuncDecl(Id(Hu), [], Return(NumLit(68.53))), VarDecl(Id(Xb), ArrayType([36.59, 35.89, 15.63], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 658))

	def test_659(self):
		input = '''
bool i2
func mPZ ()	return

'''
		expect = '''Program([VarDecl(Id(i2), BoolType, None, None), FuncDecl(Id(mPZ), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 659))

	def test_660(self):
		input = '''
dynamic ZoKR <- false
func rRP (bool Jf[67.35,73.62], string RF, bool ihp8[35.98,39.3,93.42])
	return 18.85
string p9R[94.75,16.98]
bool kaaP[20.45]
bool MCX <- 99.85
'''
		expect = '''Program([VarDecl(Id(ZoKR), None, dynamic, BooleanLit(False)), FuncDecl(Id(rRP), [VarDecl(Id(Jf), ArrayType([67.35, 73.62], BoolType), None, None), VarDecl(Id(RF), StringType, None, None), VarDecl(Id(ihp8), ArrayType([35.98, 39.3, 93.42], BoolType), None, None)], Return(NumLit(18.85))), VarDecl(Id(p9R), ArrayType([94.75, 16.98], StringType), None, None), VarDecl(Id(kaaP), ArrayType([20.45], BoolType), None, None), VarDecl(Id(MCX), BoolType, None, NumLit(99.85))])'''
		self.assertTrue(TestAST.test(input, expect, 660))

	def test_661(self):
		input = '''
dynamic WC <- R9
'''
		expect = '''Program([VarDecl(Id(WC), None, dynamic, Id(R9))])'''
		self.assertTrue(TestAST.test(input, expect, 661))

	def test_662(self):
		input = '''
func AAb (string lo, number x3B[89.42,51.61,79.65], bool y8[56.34,92.48,67.44])
	return

func Yt ()
	return Ze6
func V9 (bool x2[43.8,0.68], number uVt[41.24,33.2])
	return

'''
		expect = '''Program([FuncDecl(Id(AAb), [VarDecl(Id(lo), StringType, None, None), VarDecl(Id(x3B), ArrayType([89.42, 51.61, 79.65], NumberType), None, None), VarDecl(Id(y8), ArrayType([56.34, 92.48, 67.44], BoolType), None, None)], Return()), FuncDecl(Id(Yt), [], Return(Id(Ze6))), FuncDecl(Id(V9), [VarDecl(Id(x2), ArrayType([43.8, 0.68], BoolType), None, None), VarDecl(Id(uVt), ArrayType([41.24, 33.2], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 662))

	def test_663(self):
		input = '''
number ZB[32.23,15.41]
number UiZ[85.58,49.96] <- jv
bool kWQ[34.92]
'''
		expect = '''Program([VarDecl(Id(ZB), ArrayType([32.23, 15.41], NumberType), None, None), VarDecl(Id(UiZ), ArrayType([85.58, 49.96], NumberType), None, Id(jv)), VarDecl(Id(kWQ), ArrayType([34.92], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 663))

	def test_664(self):
		input = '''
func vKk (bool CE[90.24], string P0[91.17,88.72,69.3])	begin
		bool zG[95.26,73.61]
	end

func ZRbi (bool I4g[67.24,20.24])	return
func i6K (bool LYHP, string lP[58.3])	return PGNK

'''
		expect = '''Program([FuncDecl(Id(vKk), [VarDecl(Id(CE), ArrayType([90.24], BoolType), None, None), VarDecl(Id(P0), ArrayType([91.17, 88.72, 69.3], StringType), None, None)], Block([VarDecl(Id(zG), ArrayType([95.26, 73.61], BoolType), None, None)])), FuncDecl(Id(ZRbi), [VarDecl(Id(I4g), ArrayType([67.24, 20.24], BoolType), None, None)], Return()), FuncDecl(Id(i6K), [VarDecl(Id(LYHP), BoolType, None, None), VarDecl(Id(lP), ArrayType([58.3], StringType), None, None)], Return(Id(PGNK)))])'''
		self.assertTrue(TestAST.test(input, expect, 664))

	def test_665(self):
		input = '''
string Jpt[45.39,40.77,42.76] <- 0.06
string l0[69.56,26.54,49.2] <- YM
bool DU[52.93]
func L5 (bool rq5c)	return "w"

dynamic N0k
'''
		expect = '''Program([VarDecl(Id(Jpt), ArrayType([45.39, 40.77, 42.76], StringType), None, NumLit(0.06)), VarDecl(Id(l0), ArrayType([69.56, 26.54, 49.2], StringType), None, Id(YM)), VarDecl(Id(DU), ArrayType([52.93], BoolType), None, None), FuncDecl(Id(L5), [VarDecl(Id(rq5c), BoolType, None, None)], Return(StringLit(w))), VarDecl(Id(N0k), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 665))

	def test_666(self):
		input = '''
dynamic wkV
'''
		expect = '''Program([VarDecl(Id(wkV), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 666))

	def test_667(self):
		input = '''
func c9 (string qz, string bzhd[93.56], number lEZ[17.45,5.98,72.05])	return

'''
		expect = '''Program([FuncDecl(Id(c9), [VarDecl(Id(qz), StringType, None, None), VarDecl(Id(bzhd), ArrayType([93.56], StringType), None, None), VarDecl(Id(lEZ), ArrayType([17.45, 5.98, 72.05], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 667))

	def test_668(self):
		input = '''
string tR[18.24]
func ARFq ()	return
bool klp[89.57] <- false
func YO (string fHp[78.86,98.5])	begin
	end

func lC8i (bool Cqu)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(tR), ArrayType([18.24], StringType), None, None), FuncDecl(Id(ARFq), [], Return()), VarDecl(Id(klp), ArrayType([89.57], BoolType), None, BooleanLit(False)), FuncDecl(Id(YO), [VarDecl(Id(fHp), ArrayType([78.86, 98.5], StringType), None, None)], Block([])), FuncDecl(Id(lC8i), [VarDecl(Id(Cqu), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 668))

	def test_669(self):
		input = '''
dynamic ihF
number e5DW <- true
func Wl3 (string Tnh)	begin
		begin
			oO[false, true, DU6i] <- "KD"
		end
		return
		break
	end

func Db (string qa7[95.06], number Tl8q[20.26,31.62,81.79])
	begin
		break
	end

func ZAG (string pK, string kP[10.07], string jB)	begin
	end
'''
		expect = '''Program([VarDecl(Id(ihF), None, dynamic, None), VarDecl(Id(e5DW), NumberType, None, BooleanLit(True)), FuncDecl(Id(Wl3), [VarDecl(Id(Tnh), StringType, None, None)], Block([Block([AssignStmt(ArrayCell(Id(oO), [BooleanLit(False), BooleanLit(True), Id(DU6i)]), StringLit(KD))]), Return(), Break])), FuncDecl(Id(Db), [VarDecl(Id(qa7), ArrayType([95.06], StringType), None, None), VarDecl(Id(Tl8q), ArrayType([20.26, 31.62, 81.79], NumberType), None, None)], Block([Break])), FuncDecl(Id(ZAG), [VarDecl(Id(pK), StringType, None, None), VarDecl(Id(kP), ArrayType([10.07], StringType), None, None), VarDecl(Id(jB), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 669))

	def test_670(self):
		input = '''
func d7_U (bool BST[55.3,42.8])
	begin
		begin
		end
		continue
		BM(88.03, 85.83)
	end

number zD
number fnk8[92.68,57.32,84.61] <- "VAw"
'''
		expect = '''Program([FuncDecl(Id(d7_U), [VarDecl(Id(BST), ArrayType([55.3, 42.8], BoolType), None, None)], Block([Block([]), Continue, CallStmt(Id(BM), [NumLit(88.03), NumLit(85.83)])])), VarDecl(Id(zD), NumberType, None, None), VarDecl(Id(fnk8), ArrayType([92.68, 57.32, 84.61], NumberType), None, StringLit(VAw))])'''
		self.assertTrue(TestAST.test(input, expect, 670))

	def test_671(self):
		input = '''
string LT[36.12] <- 28.17
'''
		expect = '''Program([VarDecl(Id(LT), ArrayType([36.12], StringType), None, NumLit(28.17))])'''
		self.assertTrue(TestAST.test(input, expect, 671))

	def test_672(self):
		input = '''
var cTN <- p9HJ
func GFN (number wR8k[0.73,85.34])	begin
	end
number Iq[17.02,76.46]
func GMbm ()
	return

'''
		expect = '''Program([VarDecl(Id(cTN), None, var, Id(p9HJ)), FuncDecl(Id(GFN), [VarDecl(Id(wR8k), ArrayType([0.73, 85.34], NumberType), None, None)], Block([])), VarDecl(Id(Iq), ArrayType([17.02, 76.46], NumberType), None, None), FuncDecl(Id(GMbm), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 672))

	def test_673(self):
		input = '''
func gZ (bool Nq)	return

'''
		expect = '''Program([FuncDecl(Id(gZ), [VarDecl(Id(Nq), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 673))

	def test_674(self):
		input = '''
var R9qR <- 79.38
bool KK[40.5,13.27,77.77] <- Chd
func G0M (string Qu5)
	return xQ

'''
		expect = '''Program([VarDecl(Id(R9qR), None, var, NumLit(79.38)), VarDecl(Id(KK), ArrayType([40.5, 13.27, 77.77], BoolType), None, Id(Chd)), FuncDecl(Id(G0M), [VarDecl(Id(Qu5), StringType, None, None)], Return(Id(xQ)))])'''
		self.assertTrue(TestAST.test(input, expect, 674))

	def test_675(self):
		input = '''
string op[27.25]
number jw[38.38]
'''
		expect = '''Program([VarDecl(Id(op), ArrayType([27.25], StringType), None, None), VarDecl(Id(jw), ArrayType([38.38], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 675))

	def test_676(self):
		input = '''
func Zo (number Ccu, bool TvpX[24.62,98.8,75.09])
	return
string bGc2[15.25] <- true
'''
		expect = '''Program([FuncDecl(Id(Zo), [VarDecl(Id(Ccu), NumberType, None, None), VarDecl(Id(TvpX), ArrayType([24.62, 98.8, 75.09], BoolType), None, None)], Return()), VarDecl(Id(bGc2), ArrayType([15.25], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 676))

	def test_677(self):
		input = '''
string vo[85.2,11.41] <- "g"
func MZU (number zAUs[42.85,9.06,76.14])	return
'''
		expect = '''Program([VarDecl(Id(vo), ArrayType([85.2, 11.41], StringType), None, StringLit(g)), FuncDecl(Id(MZU), [VarDecl(Id(zAUs), ArrayType([42.85, 9.06, 76.14], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 677))

	def test_678(self):
		input = '''
var ro4R <- XU
func qT (string J_[63.99], bool dK[95.54,63.82], number xyc)
	return "gN"

bool CWql <- true
func hYMM (string ieO0[91.84,51.89,74.38], bool y7H)	begin
		continue
		break
	end

string xQ6[50.35,26.1]
'''
		expect = '''Program([VarDecl(Id(ro4R), None, var, Id(XU)), FuncDecl(Id(qT), [VarDecl(Id(J_), ArrayType([63.99], StringType), None, None), VarDecl(Id(dK), ArrayType([95.54, 63.82], BoolType), None, None), VarDecl(Id(xyc), NumberType, None, None)], Return(StringLit(gN))), VarDecl(Id(CWql), BoolType, None, BooleanLit(True)), FuncDecl(Id(hYMM), [VarDecl(Id(ieO0), ArrayType([91.84, 51.89, 74.38], StringType), None, None), VarDecl(Id(y7H), BoolType, None, None)], Block([Continue, Break])), VarDecl(Id(xQ6), ArrayType([50.35, 26.1], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 678))

	def test_679(self):
		input = '''
func i6z (string bG4, string wJs[59.4,72.93,79.52])
	return

func dt (string cTE1[82.56], number lJaX, bool pfFi)	return

func RL (number uUK1[38.07], string gh, string cWTv)	return false
'''
		expect = '''Program([FuncDecl(Id(i6z), [VarDecl(Id(bG4), StringType, None, None), VarDecl(Id(wJs), ArrayType([59.4, 72.93, 79.52], StringType), None, None)], Return()), FuncDecl(Id(dt), [VarDecl(Id(cTE1), ArrayType([82.56], StringType), None, None), VarDecl(Id(lJaX), NumberType, None, None), VarDecl(Id(pfFi), BoolType, None, None)], Return()), FuncDecl(Id(RL), [VarDecl(Id(uUK1), ArrayType([38.07], NumberType), None, None), VarDecl(Id(gh), StringType, None, None), VarDecl(Id(cWTv), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 679))

	def test_680(self):
		input = '''
func s5M (string ma, bool R0)
	begin
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(s5M), [VarDecl(Id(ma), StringType, None, None), VarDecl(Id(R0), BoolType, None, None)], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 680))

	def test_681(self):
		input = '''
bool fO[30.58]
func ouM ()	begin
	end
'''
		expect = '''Program([VarDecl(Id(fO), ArrayType([30.58], BoolType), None, None), FuncDecl(Id(ouM), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 681))

	def test_682(self):
		input = '''
bool EIKU <- "ZIgFT"
func OIE ()
	return "rPT"
func vh ()	return
func wxtK (string E_, bool NLxT[14.58,10.13,33.91], bool Ow)	return
'''
		expect = '''Program([VarDecl(Id(EIKU), BoolType, None, StringLit(ZIgFT)), FuncDecl(Id(OIE), [], Return(StringLit(rPT))), FuncDecl(Id(vh), [], Return()), FuncDecl(Id(wxtK), [VarDecl(Id(E_), StringType, None, None), VarDecl(Id(NLxT), ArrayType([14.58, 10.13, 33.91], BoolType), None, None), VarDecl(Id(Ow), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 682))

	def test_683(self):
		input = '''
number NBo[77.15,63.73]
number m9[42.69,14.25,58.16] <- false
'''
		expect = '''Program([VarDecl(Id(NBo), ArrayType([77.15, 63.73], NumberType), None, None), VarDecl(Id(m9), ArrayType([42.69, 14.25, 58.16], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 683))

	def test_684(self):
		input = '''
func WyY (number Hil7[16.59,12.49])
	begin
		for kRnr until K3Of by gT
			break
	end
'''
		expect = '''Program([FuncDecl(Id(WyY), [VarDecl(Id(Hil7), ArrayType([16.59, 12.49], NumberType), None, None)], Block([For(Id(kRnr), Id(K3Of), Id(gT), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 684))

	def test_685(self):
		input = '''
var jzus <- "aNpFy"
func tF ()
	return false

dynamic Q7uC
'''
		expect = '''Program([VarDecl(Id(jzus), None, var, StringLit(aNpFy)), FuncDecl(Id(tF), [], Return(BooleanLit(False))), VarDecl(Id(Q7uC), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 685))

	def test_686(self):
		input = '''
dynamic E2
func xx (bool Sqt[65.43,39.26,5.3], bool EI[46.23,56.78,78.65])
	return 10.98
func S2 (number tal)	return

dynamic jKw0
'''
		expect = '''Program([VarDecl(Id(E2), None, dynamic, None), FuncDecl(Id(xx), [VarDecl(Id(Sqt), ArrayType([65.43, 39.26, 5.3], BoolType), None, None), VarDecl(Id(EI), ArrayType([46.23, 56.78, 78.65], BoolType), None, None)], Return(NumLit(10.98))), FuncDecl(Id(S2), [VarDecl(Id(tal), NumberType, None, None)], Return()), VarDecl(Id(jKw0), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 686))

	def test_687(self):
		input = '''
func RVBE (string h8, number rf[85.4,99.3,88.78])
	return
func BMzp (bool u1[42.85,22.58])	return
func oC (bool W33, string DF[81.01], bool d14e)	begin
	end

func PEoU (string Mhm, string EjS[1.15,8.55])
	begin
		if (true)
		KJ4f()
		elif (52.42)
		string XC[18.36]
		elif (61.83) YAzy[true, false, "OB"] <- "x"
		else if (true)
		if (qAQ9)
		continue
		elif (OZ) if ("xz") begin
			return
			begin
			end
		end
		elif ("pcVZ")
		return "QSqbk"
		elif (true) return 5.85
		else Iq <- xJI
		continue
		if (46.45) if (72.83)
		return
		elif ("x")
		string nr[88.67]
		elif (false)
		if ("KCvW")
		if (99.69) return
		else if ("h") for umw until 77.88 by 68.93
			if (true) KIz(false, "DW")
			elif (false) lr(true)
			elif (48.98) VZYu()
			else return
		elif (19.1) bool BG[51.24,60.77,7.26] <- false
		elif ("WAqrk")
		return
		elif (71.9) continue
		elif (81.11) aDws(52.58)
		elif (AS) for ZA until yZz by kIW
			xa(true)
		else dynamic LTG <- xX
		elif (false) c4v2("WPtD", false)
		elif (true)
		break
		elif (false) iza(15.89, false)
		elif (77.09) return "aWXMx"
		elif ("KIVyN")
		break
		else bool HHx[14.61] <- true
		elif (q6Qj)
		if (true) begin
		end
		elif ("sIMab") begin
			if (1.23) r21 <- 19.17
			elif (false)
			fco(49.93, false, false)
			elif ("qw")
			for Ba0Z until false by 45.46
				K25X <- false
			elif (XC5)
			return dI
			else kPW <- false
		end
		elif ("qxq")
		return 90.11
		elif (true) Af_(true, "M", 19.44)
		elif (Gp_u)
		return "RRye"
		elif (Rj) continue
		elif (61.85)
		continue
		else PmLt[mGmC, df5h, "w"] <- 96.47
	end
'''
		expect = '''Program([FuncDecl(Id(RVBE), [VarDecl(Id(h8), StringType, None, None), VarDecl(Id(rf), ArrayType([85.4, 99.3, 88.78], NumberType), None, None)], Return()), FuncDecl(Id(BMzp), [VarDecl(Id(u1), ArrayType([42.85, 22.58], BoolType), None, None)], Return()), FuncDecl(Id(oC), [VarDecl(Id(W33), BoolType, None, None), VarDecl(Id(DF), ArrayType([81.01], StringType), None, None), VarDecl(Id(d14e), BoolType, None, None)], Block([])), FuncDecl(Id(PEoU), [VarDecl(Id(Mhm), StringType, None, None), VarDecl(Id(EjS), ArrayType([1.15, 8.55], StringType), None, None)], Block([If((BooleanLit(True), CallStmt(Id(KJ4f), [])), [(NumLit(52.42), VarDecl(Id(XC), ArrayType([18.36], StringType), None, None)), (NumLit(61.83), AssignStmt(ArrayCell(Id(YAzy), [BooleanLit(True), BooleanLit(False), StringLit(OB)]), StringLit(x)))], If((BooleanLit(True), If((Id(qAQ9), Continue), [(Id(OZ), If((StringLit(xz), Block([Return(), Block([])])), [(StringLit(pcVZ), Return(StringLit(QSqbk))), (BooleanLit(True), Return(NumLit(5.85)))], AssignStmt(Id(Iq), Id(xJI))))], None)), [], None)), Continue, If((NumLit(46.45), If((NumLit(72.83), Return()), [(StringLit(x), VarDecl(Id(nr), ArrayType([88.67], StringType), None, None)), (BooleanLit(False), If((StringLit(KCvW), If((NumLit(99.69), Return()), [], If((StringLit(h), For(Id(umw), NumLit(77.88), NumLit(68.93), If((BooleanLit(True), CallStmt(Id(KIz), [BooleanLit(False), StringLit(DW)])), [(BooleanLit(False), CallStmt(Id(lr), [BooleanLit(True)])), (NumLit(48.98), CallStmt(Id(VZYu), []))], Return()))), [(NumLit(19.1), VarDecl(Id(BG), ArrayType([51.24, 60.77, 7.26], BoolType), None, BooleanLit(False))), (StringLit(WAqrk), Return()), (NumLit(71.9), Continue), (NumLit(81.11), CallStmt(Id(aDws), [NumLit(52.58)])), (Id(AS), For(Id(ZA), Id(yZz), Id(kIW), CallStmt(Id(xa), [BooleanLit(True)])))], VarDecl(Id(LTG), None, dynamic, Id(xX))))), [(BooleanLit(False), CallStmt(Id(c4v2), [StringLit(WPtD), BooleanLit(False)])), (BooleanLit(True), Break), (BooleanLit(False), CallStmt(Id(iza), [NumLit(15.89), BooleanLit(False)])), (NumLit(77.09), Return(StringLit(aWXMx))), (StringLit(KIVyN), Break)], VarDecl(Id(HHx), ArrayType([14.61], BoolType), None, BooleanLit(True)))), (Id(q6Qj), If((BooleanLit(True), Block([])), [(StringLit(sIMab), Block([If((NumLit(1.23), AssignStmt(Id(r21), NumLit(19.17))), [(BooleanLit(False), CallStmt(Id(fco), [NumLit(49.93), BooleanLit(False), BooleanLit(False)])), (StringLit(qw), For(Id(Ba0Z), BooleanLit(False), NumLit(45.46), AssignStmt(Id(K25X), BooleanLit(False)))), (Id(XC5), Return(Id(dI)))], AssignStmt(Id(kPW), BooleanLit(False)))])), (StringLit(qxq), Return(NumLit(90.11))), (BooleanLit(True), CallStmt(Id(Af_), [BooleanLit(True), StringLit(M), NumLit(19.44)])), (Id(Gp_u), Return(StringLit(RRye))), (Id(Rj), Continue), (NumLit(61.85), Continue)], AssignStmt(ArrayCell(Id(PmLt), [Id(mGmC), Id(df5h), StringLit(w)]), NumLit(96.47))))], None)), [], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 687))

	def test_688(self):
		input = '''
bool tY
func fw (number TsSC[18.2,32.7], string q9x1[58.27,36.11,91.72])	return bFHI
bool lq <- "ebhYY"
bool p2[48.0] <- 69.48
'''
		expect = '''Program([VarDecl(Id(tY), BoolType, None, None), FuncDecl(Id(fw), [VarDecl(Id(TsSC), ArrayType([18.2, 32.7], NumberType), None, None), VarDecl(Id(q9x1), ArrayType([58.27, 36.11, 91.72], StringType), None, None)], Return(Id(bFHI))), VarDecl(Id(lq), BoolType, None, StringLit(ebhYY)), VarDecl(Id(p2), ArrayType([48.0], BoolType), None, NumLit(69.48))])'''
		self.assertTrue(TestAST.test(input, expect, 688))

	def test_689(self):
		input = '''
func k_72 (bool YDjd[77.68,91.36,95.77], number FSv[55.11])
	begin
		for luUF until true by "AoXNt"
			for VzZ until 48.03 by "j"
				TuN[47.38, true] <- 39.92
		ey2 <- "GBC"
	end

'''
		expect = '''Program([FuncDecl(Id(k_72), [VarDecl(Id(YDjd), ArrayType([77.68, 91.36, 95.77], BoolType), None, None), VarDecl(Id(FSv), ArrayType([55.11], NumberType), None, None)], Block([For(Id(luUF), BooleanLit(True), StringLit(AoXNt), For(Id(VzZ), NumLit(48.03), StringLit(j), AssignStmt(ArrayCell(Id(TuN), [NumLit(47.38), BooleanLit(True)]), NumLit(39.92)))), AssignStmt(Id(ey2), StringLit(GBC))]))])'''
		self.assertTrue(TestAST.test(input, expect, 689))

	def test_690(self):
		input = '''
func S0Q ()
	return

string HHu[22.39,3.21]
'''
		expect = '''Program([FuncDecl(Id(S0Q), [], Return()), VarDecl(Id(HHu), ArrayType([22.39, 3.21], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 690))

	def test_691(self):
		input = '''
string wY
number UpM <- 58.28
'''
		expect = '''Program([VarDecl(Id(wY), StringType, None, None), VarDecl(Id(UpM), NumberType, None, NumLit(58.28))])'''
		self.assertTrue(TestAST.test(input, expect, 691))

	def test_692(self):
		input = '''
func Tx_ (string OR[48.25], bool tQfD, number ES[52.67,37.13,24.68])	begin
	end

func ts (bool uB)
	return

'''
		expect = '''Program([FuncDecl(Id(Tx_), [VarDecl(Id(OR), ArrayType([48.25], StringType), None, None), VarDecl(Id(tQfD), BoolType, None, None), VarDecl(Id(ES), ArrayType([52.67, 37.13, 24.68], NumberType), None, None)], Block([])), FuncDecl(Id(ts), [VarDecl(Id(uB), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 692))

	def test_693(self):
		input = '''
var sql <- 61.89
string Vs
number R9OV[53.04,75.82] <- true
dynamic Z24m
string R1pm <- 73.26
'''
		expect = '''Program([VarDecl(Id(sql), None, var, NumLit(61.89)), VarDecl(Id(Vs), StringType, None, None), VarDecl(Id(R9OV), ArrayType([53.04, 75.82], NumberType), None, BooleanLit(True)), VarDecl(Id(Z24m), None, dynamic, None), VarDecl(Id(R1pm), StringType, None, NumLit(73.26))])'''
		self.assertTrue(TestAST.test(input, expect, 693))

	def test_694(self):
		input = '''
string Oj6[26.02]
var rY <- 83.97
bool Ce[40.92,76.58,21.15] <- 55.68
'''
		expect = '''Program([VarDecl(Id(Oj6), ArrayType([26.02], StringType), None, None), VarDecl(Id(rY), None, var, NumLit(83.97)), VarDecl(Id(Ce), ArrayType([40.92, 76.58, 21.15], BoolType), None, NumLit(55.68))])'''
		self.assertTrue(TestAST.test(input, expect, 694))

	def test_695(self):
		input = '''
number Rok0 <- uy_I
func Qb (number H4Z)	begin
		break
	end

func Uf ()
	return 99.33
'''
		expect = '''Program([VarDecl(Id(Rok0), NumberType, None, Id(uy_I)), FuncDecl(Id(Qb), [VarDecl(Id(H4Z), NumberType, None, None)], Block([Break])), FuncDecl(Id(Uf), [], Return(NumLit(99.33)))])'''
		self.assertTrue(TestAST.test(input, expect, 695))

	def test_696(self):
		input = '''
number Ko[64.69]
func Ovi (number BdQf, number Wqv[91.48,91.84,72.23], number Wbj)	begin
		break
	end
func c7 (string Jy, bool EP[80.41,64.32,8.86])
	return
'''
		expect = '''Program([VarDecl(Id(Ko), ArrayType([64.69], NumberType), None, None), FuncDecl(Id(Ovi), [VarDecl(Id(BdQf), NumberType, None, None), VarDecl(Id(Wqv), ArrayType([91.48, 91.84, 72.23], NumberType), None, None), VarDecl(Id(Wbj), NumberType, None, None)], Block([Break])), FuncDecl(Id(c7), [VarDecl(Id(Jy), StringType, None, None), VarDecl(Id(EP), ArrayType([80.41, 64.32, 8.86], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 696))

	def test_697(self):
		input = '''
func PV0t ()	return
number SL[65.34] <- 94.51
'''
		expect = '''Program([FuncDecl(Id(PV0t), [], Return()), VarDecl(Id(SL), ArrayType([65.34], NumberType), None, NumLit(94.51))])'''
		self.assertTrue(TestAST.test(input, expect, 697))

	def test_698(self):
		input = '''
string Qgb[23.23] <- true
string fw
'''
		expect = '''Program([VarDecl(Id(Qgb), ArrayType([23.23], StringType), None, BooleanLit(True)), VarDecl(Id(fw), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 698))

	def test_699(self):
		input = '''
func Aw2 (bool uzP[19.03])	return
string R0S
func J7C4 (number VOR[85.01], string xrD)
	begin
		return yCy
	end

'''
		expect = '''Program([FuncDecl(Id(Aw2), [VarDecl(Id(uzP), ArrayType([19.03], BoolType), None, None)], Return()), VarDecl(Id(R0S), StringType, None, None), FuncDecl(Id(J7C4), [VarDecl(Id(VOR), ArrayType([85.01], NumberType), None, None), VarDecl(Id(xrD), StringType, None, None)], Block([Return(Id(yCy))]))])'''
		self.assertTrue(TestAST.test(input, expect, 699))

	def test_700(self):
		input = '''
dynamic H2
string qLDT[25.99,3.2,33.01]
func Yr (bool vCTO, number kWA[11.62,69.2,66.04], string U5xz[27.03])
	return
'''
		expect = '''Program([VarDecl(Id(H2), None, dynamic, None), VarDecl(Id(qLDT), ArrayType([25.99, 3.2, 33.01], StringType), None, None), FuncDecl(Id(Yr), [VarDecl(Id(vCTO), BoolType, None, None), VarDecl(Id(kWA), ArrayType([11.62, 69.2, 66.04], NumberType), None, None), VarDecl(Id(U5xz), ArrayType([27.03], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 700))