import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_501(self):
		input = '''
bool L5e
var Xqq <- [((EP))]
bool tq
func jXe0 (bool vjj, bool qDLJ[72.33])	return 38.47 == 76.74

func Khbv (number E1, number RwfH, string CW)	begin
		continue
		return V3M
		break
	end
'''
		expect = '''Program([VarDecl(Id(L5e), BoolType, None, None), VarDecl(Id(Xqq), None, var, ArrayLit(Id(EP))), VarDecl(Id(tq), BoolType, None, None), FuncDecl(Id(jXe0), [VarDecl(Id(vjj), BoolType, None, None), VarDecl(Id(qDLJ), ArrayType([72.33], BoolType), None, None)], Return(BinaryOp(==, NumLit(38.47), NumLit(76.74)))), FuncDecl(Id(Khbv), [VarDecl(Id(E1), NumberType, None, None), VarDecl(Id(RwfH), NumberType, None, None), VarDecl(Id(CW), StringType, None, None)], Block([Continue, Return(Id(V3M)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 501))

	def test_502(self):
		input = '''
func I8oI (bool fML[15.23,98.54], number im, bool r5)
	return true

string yP[55.73,21.43,97.23]
bool OHVL[88.14,12.77,34.17]
func Txx (bool pB[63.08,32.01], number P4m[92.17,26.81])	return "gFON"
func d7 ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(I8oI), [VarDecl(Id(fML), ArrayType([15.23, 98.54], BoolType), None, None), VarDecl(Id(im), NumberType, None, None), VarDecl(Id(r5), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(yP), ArrayType([55.73, 21.43, 97.23], StringType), None, None), VarDecl(Id(OHVL), ArrayType([88.14, 12.77, 34.17], BoolType), None, None), FuncDecl(Id(Txx), [VarDecl(Id(pB), ArrayType([63.08, 32.01], BoolType), None, None), VarDecl(Id(P4m), ArrayType([92.17, 26.81], NumberType), None, None)], Return(StringLit(gFON))), FuncDecl(Id(d7), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 502))

	def test_503(self):
		input = '''
func OlhB (bool tD[15.49,46.51], number T5)	return "ki"
number rLXp
func Uvlv ()
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(OlhB), [VarDecl(Id(tD), ArrayType([15.49, 46.51], BoolType), None, None), VarDecl(Id(T5), NumberType, None, None)], Return(StringLit(ki))), VarDecl(Id(rLXp), NumberType, None, None), FuncDecl(Id(Uvlv), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 503))

	def test_504(self):
		input = '''
func msQS (bool TV[0.0,31.68,89.11], string QwKd[48.8,64.26,88.58], string Cta)	return
func JTG (number de[9.14,3.27,38.71])
	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(msQS), [VarDecl(Id(TV), ArrayType([0.0, 31.68, 89.11], BoolType), None, None), VarDecl(Id(QwKd), ArrayType([48.8, 64.26, 88.58], StringType), None, None), VarDecl(Id(Cta), StringType, None, None)], Return()), FuncDecl(Id(JTG), [VarDecl(Id(de), ArrayType([9.14, 3.27, 38.71], NumberType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 504))

	def test_505(self):
		input = '''
func PdNi (bool pdp)
	return

'''
		expect = '''Program([FuncDecl(Id(PdNi), [VarDecl(Id(pdp), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 505))

	def test_506(self):
		input = '''
func yb ()
	return "e"
number o4ZB[1.88] <- Xww
func x3g2 (string LHK)
	begin
		continue
		return false
	end
dynamic sw5l <- 45.87
'''
		expect = '''Program([FuncDecl(Id(yb), [], Return(StringLit(e))), VarDecl(Id(o4ZB), ArrayType([1.88], NumberType), None, Id(Xww)), FuncDecl(Id(x3g2), [VarDecl(Id(LHK), StringType, None, None)], Block([Continue, Return(BooleanLit(False))])), VarDecl(Id(sw5l), None, dynamic, NumLit(45.87))])'''
		self.assertTrue(TestAST.test(input, expect, 506))

	def test_507(self):
		input = '''
func MiVF ()	return

number A8
func eHq3 (number Q0jg[71.98,7.43], bool xsK[53.25,51.73,7.67])
	return 91.93
number WneJ
func rt (string ljb[39.26,43.64,5.76], number V0[84.22,65.62])	return

'''
		expect = '''Program([FuncDecl(Id(MiVF), [], Return()), VarDecl(Id(A8), NumberType, None, None), FuncDecl(Id(eHq3), [VarDecl(Id(Q0jg), ArrayType([71.98, 7.43], NumberType), None, None), VarDecl(Id(xsK), ArrayType([53.25, 51.73, 7.67], BoolType), None, None)], Return(NumLit(91.93))), VarDecl(Id(WneJ), NumberType, None, None), FuncDecl(Id(rt), [VarDecl(Id(ljb), ArrayType([39.26, 43.64, 5.76], StringType), None, None), VarDecl(Id(V0), ArrayType([84.22, 65.62], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 507))

	def test_508(self):
		input = '''
func DYX (number seS[93.28,34.75,9.41], bool so)
	return
number Yobg[49.56] <- false
'''
		expect = '''Program([FuncDecl(Id(DYX), [VarDecl(Id(seS), ArrayType([93.28, 34.75, 9.41], NumberType), None, None), VarDecl(Id(so), BoolType, None, None)], Return()), VarDecl(Id(Yobg), ArrayType([49.56], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 508))

	def test_509(self):
		input = '''
func fZT (bool wV)
	begin
		begin
		end
	end

func Oa ()	return false
func qcp_ (bool ssL[27.01,80.97,34.55])	return
var MmjY <- JXY
func T5O (bool S2i)	return

'''
		expect = '''Program([FuncDecl(Id(fZT), [VarDecl(Id(wV), BoolType, None, None)], Block([Block([])])), FuncDecl(Id(Oa), [], Return(BooleanLit(False))), FuncDecl(Id(qcp_), [VarDecl(Id(ssL), ArrayType([27.01, 80.97, 34.55], BoolType), None, None)], Return()), VarDecl(Id(MmjY), None, var, Id(JXY)), FuncDecl(Id(T5O), [VarDecl(Id(S2i), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 509))

	def test_510(self):
		input = '''
string nY[77.92,87.05,33.23] <- "MxwXg"
'''
		expect = '''Program([VarDecl(Id(nY), ArrayType([77.92, 87.05, 33.23], StringType), None, StringLit(MxwXg))])'''
		self.assertTrue(TestAST.test(input, expect, 510))

	def test_511(self):
		input = '''
func VQ (string KFl, string IT, string jZ)	begin
	end
func Wz (number KT2T[45.63,31.09], number In6V)	begin
		wb()
		return true
	end

'''
		expect = '''Program([FuncDecl(Id(VQ), [VarDecl(Id(KFl), StringType, None, None), VarDecl(Id(IT), StringType, None, None), VarDecl(Id(jZ), StringType, None, None)], Block([])), FuncDecl(Id(Wz), [VarDecl(Id(KT2T), ArrayType([45.63, 31.09], NumberType), None, None), VarDecl(Id(In6V), NumberType, None, None)], Block([CallStmt(Id(wb), []), Return(BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 511))

	def test_512(self):
		input = '''
func OG (string AB1E)	begin
		continue
		break
	end
'''
		expect = '''Program([FuncDecl(Id(OG), [VarDecl(Id(AB1E), StringType, None, None)], Block([Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 512))

	def test_513(self):
		input = '''
func J8T9 (number VN[42.1,51.09], bool U02b)
	return "LXSN"
func IfT ()	begin
	end

string IgY[2.33,14.81,87.69] <- Cuw9
func thKW (bool He)
	return If

'''
		expect = '''Program([FuncDecl(Id(J8T9), [VarDecl(Id(VN), ArrayType([42.1, 51.09], NumberType), None, None), VarDecl(Id(U02b), BoolType, None, None)], Return(StringLit(LXSN))), FuncDecl(Id(IfT), [], Block([])), VarDecl(Id(IgY), ArrayType([2.33, 14.81, 87.69], StringType), None, Id(Cuw9)), FuncDecl(Id(thKW), [VarDecl(Id(He), BoolType, None, None)], Return(Id(If)))])'''
		self.assertTrue(TestAST.test(input, expect, 513))

	def test_514(self):
		input = '''
var J37 <- "x"
var Ln <- "K"
func sE ()	return "WpOR"
bool O6uX[54.69,71.4,46.64]
'''
		expect = '''Program([VarDecl(Id(J37), None, var, StringLit(x)), VarDecl(Id(Ln), None, var, StringLit(K)), FuncDecl(Id(sE), [], Return(StringLit(WpOR))), VarDecl(Id(O6uX), ArrayType([54.69, 71.4, 46.64], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 514))

	def test_515(self):
		input = '''
number nGb[98.97,33.8]
number MB4[30.06,47.64] <- false
bool K3[85.76]
dynamic RWl <- "OjnPT"
'''
		expect = '''Program([VarDecl(Id(nGb), ArrayType([98.97, 33.8], NumberType), None, None), VarDecl(Id(MB4), ArrayType([30.06, 47.64], NumberType), None, BooleanLit(False)), VarDecl(Id(K3), ArrayType([85.76], BoolType), None, None), VarDecl(Id(RWl), None, dynamic, StringLit(OjnPT))])'''
		self.assertTrue(TestAST.test(input, expect, 515))

	def test_516(self):
		input = '''
func i86S (number NPIu)
	return "L"

func PfP4 (string Sm)	return 49.26
bool MGjR[36.04,3.13,2.38]
func zam (string XMT[84.29,4.41], number WBS[86.16], string avfe)	return true
func SpR ()	return

'''
		expect = '''Program([FuncDecl(Id(i86S), [VarDecl(Id(NPIu), NumberType, None, None)], Return(StringLit(L))), FuncDecl(Id(PfP4), [VarDecl(Id(Sm), StringType, None, None)], Return(NumLit(49.26))), VarDecl(Id(MGjR), ArrayType([36.04, 3.13, 2.38], BoolType), None, None), FuncDecl(Id(zam), [VarDecl(Id(XMT), ArrayType([84.29, 4.41], StringType), None, None), VarDecl(Id(WBS), ArrayType([86.16], NumberType), None, None), VarDecl(Id(avfe), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(SpR), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 516))

	def test_517(self):
		input = '''
string xr2 <- a0dw
number TvK
func MiV (number f6kD[64.57,27.96], string TTTU, bool rYRp)	return
'''
		expect = '''Program([VarDecl(Id(xr2), StringType, None, Id(a0dw)), VarDecl(Id(TvK), NumberType, None, None), FuncDecl(Id(MiV), [VarDecl(Id(f6kD), ArrayType([64.57, 27.96], NumberType), None, None), VarDecl(Id(TTTU), StringType, None, None), VarDecl(Id(rYRp), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 517))

	def test_518(self):
		input = '''
number Yb[76.7] <- "RugkN"
func WWi (string BOe)	begin
		dynamic PXes <- false
	end
func co7 (bool FjaP, number brT, bool rNP)	return true
var nc <- "rFmVx"
bool a7 <- "pQAM"
'''
		expect = '''Program([VarDecl(Id(Yb), ArrayType([76.7], NumberType), None, StringLit(RugkN)), FuncDecl(Id(WWi), [VarDecl(Id(BOe), StringType, None, None)], Block([VarDecl(Id(PXes), None, dynamic, BooleanLit(False))])), FuncDecl(Id(co7), [VarDecl(Id(FjaP), BoolType, None, None), VarDecl(Id(brT), NumberType, None, None), VarDecl(Id(rNP), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(nc), None, var, StringLit(rFmVx)), VarDecl(Id(a7), BoolType, None, StringLit(pQAM))])'''
		self.assertTrue(TestAST.test(input, expect, 518))

	def test_519(self):
		input = '''
func Ci (string fnQG[80.43], bool og)	begin
		return
	end

number kXyg <- true
func w3 ()	return 78.26
string Ey4o[71.07,47.43,24.98]
'''
		expect = '''Program([FuncDecl(Id(Ci), [VarDecl(Id(fnQG), ArrayType([80.43], StringType), None, None), VarDecl(Id(og), BoolType, None, None)], Block([Return()])), VarDecl(Id(kXyg), NumberType, None, BooleanLit(True)), FuncDecl(Id(w3), [], Return(NumLit(78.26))), VarDecl(Id(Ey4o), ArrayType([71.07, 47.43, 24.98], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 519))

	def test_520(self):
		input = '''
func a6 (bool PR[37.52,26.65], number o3f6)	begin
	end
number w4X8[77.34,8.04] <- true
func M3B ()
	return true

'''
		expect = '''Program([FuncDecl(Id(a6), [VarDecl(Id(PR), ArrayType([37.52, 26.65], BoolType), None, None), VarDecl(Id(o3f6), NumberType, None, None)], Block([])), VarDecl(Id(w4X8), ArrayType([77.34, 8.04], NumberType), None, BooleanLit(True)), FuncDecl(Id(M3B), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 520))

	def test_521(self):
		input = '''
string ss[2.89,23.27,92.34] <- "F"
dynamic xH <- 11.26
string Jm_S
'''
		expect = '''Program([VarDecl(Id(ss), ArrayType([2.89, 23.27, 92.34], StringType), None, StringLit(F)), VarDecl(Id(xH), None, dynamic, NumLit(11.26)), VarDecl(Id(Jm_S), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 521))

	def test_522(self):
		input = '''
bool hMx
func Upp ()	return "Srau"
'''
		expect = '''Program([VarDecl(Id(hMx), BoolType, None, None), FuncDecl(Id(Upp), [], Return(StringLit(Srau)))])'''
		self.assertTrue(TestAST.test(input, expect, 522))

	def test_523(self):
		input = '''
bool f6Gd[51.39,67.02]
dynamic gQ
var Cz <- "BD"
number Z4_R[60.01]
func N1T (string kss)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(f6Gd), ArrayType([51.39, 67.02], BoolType), None, None), VarDecl(Id(gQ), None, dynamic, None), VarDecl(Id(Cz), None, var, StringLit(BD)), VarDecl(Id(Z4_R), ArrayType([60.01], NumberType), None, None), FuncDecl(Id(N1T), [VarDecl(Id(kss), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 523))

	def test_524(self):
		input = '''
func qkn (string Wr[70.56,58.68], bool EC[64.36,14.09,42.65], bool WpW)	return true
func DHp5 (bool X5[50.8,34.56,82.01], bool Vu)	return

string rZ1Y <- false
bool AT <- "hNhSc"
'''
		expect = '''Program([FuncDecl(Id(qkn), [VarDecl(Id(Wr), ArrayType([70.56, 58.68], StringType), None, None), VarDecl(Id(EC), ArrayType([64.36, 14.09, 42.65], BoolType), None, None), VarDecl(Id(WpW), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(DHp5), [VarDecl(Id(X5), ArrayType([50.8, 34.56, 82.01], BoolType), None, None), VarDecl(Id(Vu), BoolType, None, None)], Return()), VarDecl(Id(rZ1Y), StringType, None, BooleanLit(False)), VarDecl(Id(AT), BoolType, None, StringLit(hNhSc))])'''
		self.assertTrue(TestAST.test(input, expect, 524))

	def test_525(self):
		input = '''
func RcEP (number qw[92.93,87.22], string Uc9, bool Hm)	return

'''
		expect = '''Program([FuncDecl(Id(RcEP), [VarDecl(Id(qw), ArrayType([92.93, 87.22], NumberType), None, None), VarDecl(Id(Uc9), StringType, None, None), VarDecl(Id(Hm), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 525))

	def test_526(self):
		input = '''
func eBj ()
	begin
		continue
		begin
			return
		end
	end
func Ucew (number CmQ[28.37,4.34,74.51], bool WzT[21.77,74.84], bool DzPI)	begin
	end
string W1
bool Fh
func biP (string Tc[52.46])	return

'''
		expect = '''Program([FuncDecl(Id(eBj), [], Block([Continue, Block([Return()])])), FuncDecl(Id(Ucew), [VarDecl(Id(CmQ), ArrayType([28.37, 4.34, 74.51], NumberType), None, None), VarDecl(Id(WzT), ArrayType([21.77, 74.84], BoolType), None, None), VarDecl(Id(DzPI), BoolType, None, None)], Block([])), VarDecl(Id(W1), StringType, None, None), VarDecl(Id(Fh), BoolType, None, None), FuncDecl(Id(biP), [VarDecl(Id(Tc), ArrayType([52.46], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 526))

	def test_527(self):
		input = '''
func ia (number vp4[14.1,42.83,73.16], number OKXM, number AAW[5.38,86.16,23.45])
	return
dynamic Md
func Re ()
	return false

func tb (bool cKl, string DGx)
	return

number S6[32.87]
'''
		expect = '''Program([FuncDecl(Id(ia), [VarDecl(Id(vp4), ArrayType([14.1, 42.83, 73.16], NumberType), None, None), VarDecl(Id(OKXM), NumberType, None, None), VarDecl(Id(AAW), ArrayType([5.38, 86.16, 23.45], NumberType), None, None)], Return()), VarDecl(Id(Md), None, dynamic, None), FuncDecl(Id(Re), [], Return(BooleanLit(False))), FuncDecl(Id(tb), [VarDecl(Id(cKl), BoolType, None, None), VarDecl(Id(DGx), StringType, None, None)], Return()), VarDecl(Id(S6), ArrayType([32.87], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 527))

	def test_528(self):
		input = '''
func HT (bool F9m[50.67,67.09,5.94])
	return
func qCKs (string ppfS[38.25,46.87])	return true

func seg (bool yvZj, bool Hot)
	begin
		bool qm <- "d"
	end

func PQ (number WYC, bool WEa[50.98])
	return "GABoT"

func H_ (number vbGT, bool Hpk, bool Rv[21.79,6.33,66.15])	return er

'''
		expect = '''Program([FuncDecl(Id(HT), [VarDecl(Id(F9m), ArrayType([50.67, 67.09, 5.94], BoolType), None, None)], Return()), FuncDecl(Id(qCKs), [VarDecl(Id(ppfS), ArrayType([38.25, 46.87], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(seg), [VarDecl(Id(yvZj), BoolType, None, None), VarDecl(Id(Hot), BoolType, None, None)], Block([VarDecl(Id(qm), BoolType, None, StringLit(d))])), FuncDecl(Id(PQ), [VarDecl(Id(WYC), NumberType, None, None), VarDecl(Id(WEa), ArrayType([50.98], BoolType), None, None)], Return(StringLit(GABoT))), FuncDecl(Id(H_), [VarDecl(Id(vbGT), NumberType, None, None), VarDecl(Id(Hpk), BoolType, None, None), VarDecl(Id(Rv), ArrayType([21.79, 6.33, 66.15], BoolType), None, None)], Return(Id(er)))])'''
		self.assertTrue(TestAST.test(input, expect, 528))

	def test_529(self):
		input = '''
func OAz7 (string e0HL[47.44,72.77,83.91], number gSg)	return pK
'''
		expect = '''Program([FuncDecl(Id(OAz7), [VarDecl(Id(e0HL), ArrayType([47.44, 72.77, 83.91], StringType), None, None), VarDecl(Id(gSg), NumberType, None, None)], Return(Id(pK)))])'''
		self.assertTrue(TestAST.test(input, expect, 529))

	def test_530(self):
		input = '''
func F92 (number IE, string mzMn[35.7,10.0])	return false

bool F7[46.35]
number DE <- false
func cFMD ()	return
number tT[1.13,35.27,96.84]
'''
		expect = '''Program([FuncDecl(Id(F92), [VarDecl(Id(IE), NumberType, None, None), VarDecl(Id(mzMn), ArrayType([35.7, 10.0], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(F7), ArrayType([46.35], BoolType), None, None), VarDecl(Id(DE), NumberType, None, BooleanLit(False)), FuncDecl(Id(cFMD), [], Return()), VarDecl(Id(tT), ArrayType([1.13, 35.27, 96.84], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 530))

	def test_531(self):
		input = '''
func rLe ()	return xa
dynamic vgt
'''
		expect = '''Program([FuncDecl(Id(rLe), [], Return(Id(xa))), VarDecl(Id(vgt), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 531))

	def test_532(self):
		input = '''
func k5 ()	begin
		if (zR)
		return
		else bool Yu[93.85,41.41]
		for rP until "GDm" by true
			mQ("TUPlp", 41.89, "lqu")
	end
'''
		expect = '''Program([FuncDecl(Id(k5), [], Block([If((Id(zR), Return()), [], VarDecl(Id(Yu), ArrayType([93.85, 41.41], BoolType), None, None)), For(Id(rP), StringLit(GDm), BooleanLit(True), CallStmt(Id(mQ), [StringLit(TUPlp), NumLit(41.89), StringLit(lqu)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 532))

	def test_533(self):
		input = '''
func sj (bool P1w)	return

var dlL <- false
func Fb8N ()	return

number TbG9[71.73,94.06,94.5] <- Rd0k
bool uVc[66.33,56.8,53.51]
'''
		expect = '''Program([FuncDecl(Id(sj), [VarDecl(Id(P1w), BoolType, None, None)], Return()), VarDecl(Id(dlL), None, var, BooleanLit(False)), FuncDecl(Id(Fb8N), [], Return()), VarDecl(Id(TbG9), ArrayType([71.73, 94.06, 94.5], NumberType), None, Id(Rd0k)), VarDecl(Id(uVc), ArrayType([66.33, 56.8, 53.51], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 533))

	def test_534(self):
		input = '''
func put (string R_L)	begin
		begin
			OPw <- TH
			continue
		end
		return "FQjs"
		if (PY) break
		else ORN(43.96)
	end

func YA (number IkBI)
	return
number wQw8 <- Kto
'''
		expect = '''Program([FuncDecl(Id(put), [VarDecl(Id(R_L), StringType, None, None)], Block([Block([AssignStmt(Id(OPw), Id(TH)), Continue]), Return(StringLit(FQjs)), If((Id(PY), Break), [], CallStmt(Id(ORN), [NumLit(43.96)]))])), FuncDecl(Id(YA), [VarDecl(Id(IkBI), NumberType, None, None)], Return()), VarDecl(Id(wQw8), NumberType, None, Id(Kto))])'''
		self.assertTrue(TestAST.test(input, expect, 534))

	def test_535(self):
		input = '''
number II
string ylS[12.47,97.78]
func nPgG (string z97, string NG[36.35])
	begin
	end
'''
		expect = '''Program([VarDecl(Id(II), NumberType, None, None), VarDecl(Id(ylS), ArrayType([12.47, 97.78], StringType), None, None), FuncDecl(Id(nPgG), [VarDecl(Id(z97), StringType, None, None), VarDecl(Id(NG), ArrayType([36.35], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 535))

	def test_536(self):
		input = '''
func JuvG (bool gxU[36.11], bool F7wh[38.05,57.0,71.6])	return
func ZRY ()
	return 78.15
func c5 ()	return
bool T0wt[19.9]
'''
		expect = '''Program([FuncDecl(Id(JuvG), [VarDecl(Id(gxU), ArrayType([36.11], BoolType), None, None), VarDecl(Id(F7wh), ArrayType([38.05, 57.0, 71.6], BoolType), None, None)], Return()), FuncDecl(Id(ZRY), [], Return(NumLit(78.15))), FuncDecl(Id(c5), [], Return()), VarDecl(Id(T0wt), ArrayType([19.9], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 536))

	def test_537(self):
		input = '''
func ZI ()	return
'''
		expect = '''Program([FuncDecl(Id(ZI), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 537))

	def test_538(self):
		input = '''
number xR[85.65,10.11,10.28] <- 24.57
number dfp[27.7] <- "QjQuT"
'''
		expect = '''Program([VarDecl(Id(xR), ArrayType([85.65, 10.11, 10.28], NumberType), None, NumLit(24.57)), VarDecl(Id(dfp), ArrayType([27.7], NumberType), None, StringLit(QjQuT))])'''
		self.assertTrue(TestAST.test(input, expect, 538))

	def test_539(self):
		input = '''
func DOCW (bool qxw, string Spoh[84.33,54.33,49.6], bool I93[94.08])	begin
		dynamic fj <- hT4k
		yTZ(23.76, "qdnTa", PW)
		break
	end
bool mPwr <- 28.35
'''
		expect = '''Program([FuncDecl(Id(DOCW), [VarDecl(Id(qxw), BoolType, None, None), VarDecl(Id(Spoh), ArrayType([84.33, 54.33, 49.6], StringType), None, None), VarDecl(Id(I93), ArrayType([94.08], BoolType), None, None)], Block([VarDecl(Id(fj), None, dynamic, Id(hT4k)), CallStmt(Id(yTZ), [NumLit(23.76), StringLit(qdnTa), Id(PW)]), Break])), VarDecl(Id(mPwr), BoolType, None, NumLit(28.35))])'''
		self.assertTrue(TestAST.test(input, expect, 539))

	def test_540(self):
		input = '''
func Vq (bool BP[1.74,69.47,17.81], bool Nqbu[63.27,8.41])	return
'''
		expect = '''Program([FuncDecl(Id(Vq), [VarDecl(Id(BP), ArrayType([1.74, 69.47, 17.81], BoolType), None, None), VarDecl(Id(Nqbu), ArrayType([63.27, 8.41], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 540))

	def test_541(self):
		input = '''
var v7 <- 96.09
string YN_g[58.89,80.62]
number r8[58.82,24.77]
'''
		expect = '''Program([VarDecl(Id(v7), None, var, NumLit(96.09)), VarDecl(Id(YN_g), ArrayType([58.89, 80.62], StringType), None, None), VarDecl(Id(r8), ArrayType([58.82, 24.77], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 541))

	def test_542(self):
		input = '''
bool tf[18.88]
func BnY (number qk, number l2aD[38.86,35.11])
	return
func MWO (bool fk0j[0.23], number FRjt, bool D3[88.6])
	begin
		continue
		return 89.86
	end
'''
		expect = '''Program([VarDecl(Id(tf), ArrayType([18.88], BoolType), None, None), FuncDecl(Id(BnY), [VarDecl(Id(qk), NumberType, None, None), VarDecl(Id(l2aD), ArrayType([38.86, 35.11], NumberType), None, None)], Return()), FuncDecl(Id(MWO), [VarDecl(Id(fk0j), ArrayType([0.23], BoolType), None, None), VarDecl(Id(FRjt), NumberType, None, None), VarDecl(Id(D3), ArrayType([88.6], BoolType), None, None)], Block([Continue, Return(NumLit(89.86))]))])'''
		self.assertTrue(TestAST.test(input, expect, 542))

	def test_543(self):
		input = '''
func F0K (string C8Ga[76.19,18.95], string ie)
	return 29.6

string sxA1[45.5] <- false
'''
		expect = '''Program([FuncDecl(Id(F0K), [VarDecl(Id(C8Ga), ArrayType([76.19, 18.95], StringType), None, None), VarDecl(Id(ie), StringType, None, None)], Return(NumLit(29.6))), VarDecl(Id(sxA1), ArrayType([45.5], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 543))

	def test_544(self):
		input = '''
number YL[38.97,22.19,24.31]
'''
		expect = '''Program([VarDecl(Id(YL), ArrayType([38.97, 22.19, 24.31], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 544))

	def test_545(self):
		input = '''
func ciB (bool emij, bool eW, string jkB)	begin
		for mE until ifv by "b"
			UHx(Ks5R)
		for NrsP until QAg5 by true
			return
		break
	end

func U5 (bool tQb9[37.97,44.19,75.49], number c_[46.26])
	begin
	end

func XnGD (string vQfJ, number J5p8)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(ciB), [VarDecl(Id(emij), BoolType, None, None), VarDecl(Id(eW), BoolType, None, None), VarDecl(Id(jkB), StringType, None, None)], Block([For(Id(mE), Id(ifv), StringLit(b), CallStmt(Id(UHx), [Id(Ks5R)])), For(Id(NrsP), Id(QAg5), BooleanLit(True), Return()), Break])), FuncDecl(Id(U5), [VarDecl(Id(tQb9), ArrayType([37.97, 44.19, 75.49], BoolType), None, None), VarDecl(Id(c_), ArrayType([46.26], NumberType), None, None)], Block([])), FuncDecl(Id(XnGD), [VarDecl(Id(vQfJ), StringType, None, None), VarDecl(Id(J5p8), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 545))

	def test_546(self):
		input = '''
func c3m (string lw, number LlyD)
	begin
		nLSZ["CBM"] <- "FyC"
		break
		return 87.42
	end

'''
		expect = '''Program([FuncDecl(Id(c3m), [VarDecl(Id(lw), StringType, None, None), VarDecl(Id(LlyD), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(nLSZ), [StringLit(CBM)]), StringLit(FyC)), Break, Return(NumLit(87.42))]))])'''
		self.assertTrue(TestAST.test(input, expect, 546))

	def test_547(self):
		input = '''
func SG7U (bool NF9[9.85,8.28,56.42], number OEe)	begin
		TXo(hM, true)
		return
	end

dynamic uP <- 61.55
'''
		expect = '''Program([FuncDecl(Id(SG7U), [VarDecl(Id(NF9), ArrayType([9.85, 8.28, 56.42], BoolType), None, None), VarDecl(Id(OEe), NumberType, None, None)], Block([CallStmt(Id(TXo), [Id(hM), BooleanLit(True)]), Return()])), VarDecl(Id(uP), None, dynamic, NumLit(61.55))])'''
		self.assertTrue(TestAST.test(input, expect, 547))

	def test_548(self):
		input = '''
func H4 (bool w4)	begin
		EW_(ny, DUzk, 33.69)
		for dfR until tD4M by pQiD
			return true
		begin
			return
			break
			Bn <- true
		end
	end

var euE <- false
dynamic LL
number AL[87.67,93.53] <- false
'''
		expect = '''Program([FuncDecl(Id(H4), [VarDecl(Id(w4), BoolType, None, None)], Block([CallStmt(Id(EW_), [Id(ny), Id(DUzk), NumLit(33.69)]), For(Id(dfR), Id(tD4M), Id(pQiD), Return(BooleanLit(True))), Block([Return(), Break, AssignStmt(Id(Bn), BooleanLit(True))])])), VarDecl(Id(euE), None, var, BooleanLit(False)), VarDecl(Id(LL), None, dynamic, None), VarDecl(Id(AL), ArrayType([87.67, 93.53], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 548))

	def test_549(self):
		input = '''
number II[0.95]
bool l4E
'''
		expect = '''Program([VarDecl(Id(II), ArrayType([0.95], NumberType), None, None), VarDecl(Id(l4E), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 549))

	def test_550(self):
		input = '''
number js7
func XJ (string eMC1)	return
number Om[57.58,83.32]
'''
		expect = '''Program([VarDecl(Id(js7), NumberType, None, None), FuncDecl(Id(XJ), [VarDecl(Id(eMC1), StringType, None, None)], Return()), VarDecl(Id(Om), ArrayType([57.58, 83.32], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 550))

	def test_551(self):
		input = '''
dynamic n_Y <- false
bool WRLv
func m99X ()	return
'''
		expect = '''Program([VarDecl(Id(n_Y), None, dynamic, BooleanLit(False)), VarDecl(Id(WRLv), BoolType, None, None), FuncDecl(Id(m99X), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 551))

	def test_552(self):
		input = '''
func Y4Jp ()	return
func YV9 (bool nal[0.82,5.96], number SZh[31.58,77.39,98.47], bool pOE[79.2])	return "RH"

func kw ()
	begin
		if (E0ho)
		continue
		elif ("gbD") return
		elif (true)
		Quvi <- 71.54
		else s22(false)
	end

func r9H ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(Y4Jp), [], Return()), FuncDecl(Id(YV9), [VarDecl(Id(nal), ArrayType([0.82, 5.96], BoolType), None, None), VarDecl(Id(SZh), ArrayType([31.58, 77.39, 98.47], NumberType), None, None), VarDecl(Id(pOE), ArrayType([79.2], BoolType), None, None)], Return(StringLit(RH))), FuncDecl(Id(kw), [], Block([If((Id(E0ho), Continue), [(StringLit(gbD), Return()), (BooleanLit(True), AssignStmt(Id(Quvi), NumLit(71.54)))], CallStmt(Id(s22), [BooleanLit(False)]))])), FuncDecl(Id(r9H), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 552))

	def test_553(self):
		input = '''
string h5w
'''
		expect = '''Program([VarDecl(Id(h5w), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 553))

	def test_554(self):
		input = '''
func nIrY (number nb[11.77,77.68], number GG[82.74,48.18])
	return 4.06
dynamic a0ra
func Ljqc ()	return false

func mYKO (number rQcX)
	begin
		for RY until 8.65 by 80.5
			return
	end
string Dk[79.47] <- true
'''
		expect = '''Program([FuncDecl(Id(nIrY), [VarDecl(Id(nb), ArrayType([11.77, 77.68], NumberType), None, None), VarDecl(Id(GG), ArrayType([82.74, 48.18], NumberType), None, None)], Return(NumLit(4.06))), VarDecl(Id(a0ra), None, dynamic, None), FuncDecl(Id(Ljqc), [], Return(BooleanLit(False))), FuncDecl(Id(mYKO), [VarDecl(Id(rQcX), NumberType, None, None)], Block([For(Id(RY), NumLit(8.65), NumLit(80.5), Return())])), VarDecl(Id(Dk), ArrayType([79.47], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 554))

	def test_555(self):
		input = '''
func LC (bool BY3[66.67,87.79], string vKo, number IyH[36.34,51.2])
	return Odi
func Uc ()
	begin
	end
func bPdX ()
	begin
	end
bool oN[71.4,89.89]
'''
		expect = '''Program([FuncDecl(Id(LC), [VarDecl(Id(BY3), ArrayType([66.67, 87.79], BoolType), None, None), VarDecl(Id(vKo), StringType, None, None), VarDecl(Id(IyH), ArrayType([36.34, 51.2], NumberType), None, None)], Return(Id(Odi))), FuncDecl(Id(Uc), [], Block([])), FuncDecl(Id(bPdX), [], Block([])), VarDecl(Id(oN), ArrayType([71.4, 89.89], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 555))

	def test_556(self):
		input = '''
bool inL8[67.18,11.89] <- Nkt
func iE8 ()
	return Oa

func GS ()
	return

func OS (number bf47[4.94,23.32,2.93], bool d5m)
	return

func zs (number MW[90.05], number fFIH, bool x9)	begin
		begin
			t81[6.98] <- true
			break
			return
		end
		if ("VUuTS") return
		elif ("EK") begin
		end
		elif ("qqOE")
		continue
		else dCE(true)
	end

'''
		expect = '''Program([VarDecl(Id(inL8), ArrayType([67.18, 11.89], BoolType), None, Id(Nkt)), FuncDecl(Id(iE8), [], Return(Id(Oa))), FuncDecl(Id(GS), [], Return()), FuncDecl(Id(OS), [VarDecl(Id(bf47), ArrayType([4.94, 23.32, 2.93], NumberType), None, None), VarDecl(Id(d5m), BoolType, None, None)], Return()), FuncDecl(Id(zs), [VarDecl(Id(MW), ArrayType([90.05], NumberType), None, None), VarDecl(Id(fFIH), NumberType, None, None), VarDecl(Id(x9), BoolType, None, None)], Block([Block([AssignStmt(ArrayCell(Id(t81), [NumLit(6.98)]), BooleanLit(True)), Break, Return()]), If((StringLit(VUuTS), Return()), [(StringLit(EK), Block([])), (StringLit(qqOE), Continue)], CallStmt(Id(dCE), [BooleanLit(True)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 556))

	def test_557(self):
		input = '''
bool ZOGf[83.04,54.19] <- "Z"
func qBnX (bool Zg)
	return

func AjKd (string sGP6[79.02,14.55,21.62], bool xN, number Leb[18.67,27.65,13.36])
	begin
	end

func LxaE (string oMgG, string zxU4[94.05,48.98,72.36], string vs)
	return
'''
		expect = '''Program([VarDecl(Id(ZOGf), ArrayType([83.04, 54.19], BoolType), None, StringLit(Z)), FuncDecl(Id(qBnX), [VarDecl(Id(Zg), BoolType, None, None)], Return()), FuncDecl(Id(AjKd), [VarDecl(Id(sGP6), ArrayType([79.02, 14.55, 21.62], StringType), None, None), VarDecl(Id(xN), BoolType, None, None), VarDecl(Id(Leb), ArrayType([18.67, 27.65, 13.36], NumberType), None, None)], Block([])), FuncDecl(Id(LxaE), [VarDecl(Id(oMgG), StringType, None, None), VarDecl(Id(zxU4), ArrayType([94.05, 48.98, 72.36], StringType), None, None), VarDecl(Id(vs), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 557))

	def test_558(self):
		input = '''
number iP[1.05,12.56] <- false
bool y4[84.64,36.87,58.87] <- 88.72
string QTS4[54.37,30.96] <- "UtdqA"
number Vi[47.15] <- zF4
'''
		expect = '''Program([VarDecl(Id(iP), ArrayType([1.05, 12.56], NumberType), None, BooleanLit(False)), VarDecl(Id(y4), ArrayType([84.64, 36.87, 58.87], BoolType), None, NumLit(88.72)), VarDecl(Id(QTS4), ArrayType([54.37, 30.96], StringType), None, StringLit(UtdqA)), VarDecl(Id(Vi), ArrayType([47.15], NumberType), None, Id(zF4))])'''
		self.assertTrue(TestAST.test(input, expect, 558))

	def test_559(self):
		input = '''
func wd (string uWK[10.22])
	return false
number b0cp
func WPu (number v2m, bool l4[7.81,89.15,72.5], bool WR)	return
func ALh (number jv, number UvXr[78.99])	return

number cF[85.44] <- 33.52
'''
		expect = '''Program([FuncDecl(Id(wd), [VarDecl(Id(uWK), ArrayType([10.22], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(b0cp), NumberType, None, None), FuncDecl(Id(WPu), [VarDecl(Id(v2m), NumberType, None, None), VarDecl(Id(l4), ArrayType([7.81, 89.15, 72.5], BoolType), None, None), VarDecl(Id(WR), BoolType, None, None)], Return()), FuncDecl(Id(ALh), [VarDecl(Id(jv), NumberType, None, None), VarDecl(Id(UvXr), ArrayType([78.99], NumberType), None, None)], Return()), VarDecl(Id(cF), ArrayType([85.44], NumberType), None, NumLit(33.52))])'''
		self.assertTrue(TestAST.test(input, expect, 559))

	def test_560(self):
		input = '''
func re9I ()
	return

func cE (bool uva[34.69], number hD[11.69,36.4], string fX[74.85])
	begin
		break
		number uSt[88.51,16.38] <- "bnlg"
		begin
			for OSVj until "Os" by 58.8
				dynamic ZPLe <- ke
			return
			for z_c5 until UmC by eLlK
				for eBHh until true by "fISJ"
					for K0 until ujNV by true
						break
		end
	end

dynamic WLf
bool LvD[61.15,1.15] <- dK
'''
		expect = '''Program([FuncDecl(Id(re9I), [], Return()), FuncDecl(Id(cE), [VarDecl(Id(uva), ArrayType([34.69], BoolType), None, None), VarDecl(Id(hD), ArrayType([11.69, 36.4], NumberType), None, None), VarDecl(Id(fX), ArrayType([74.85], StringType), None, None)], Block([Break, VarDecl(Id(uSt), ArrayType([88.51, 16.38], NumberType), None, StringLit(bnlg)), Block([For(Id(OSVj), StringLit(Os), NumLit(58.8), VarDecl(Id(ZPLe), None, dynamic, Id(ke))), Return(), For(Id(z_c5), Id(UmC), Id(eLlK), For(Id(eBHh), BooleanLit(True), StringLit(fISJ), For(Id(K0), Id(ujNV), BooleanLit(True), Break)))])])), VarDecl(Id(WLf), None, dynamic, None), VarDecl(Id(LvD), ArrayType([61.15, 1.15], BoolType), None, Id(dK))])'''
		self.assertTrue(TestAST.test(input, expect, 560))

	def test_561(self):
		input = '''
bool Rlo[2.07] <- Xf7
number vK[62.15] <- true
var Pt <- true
func gCMB (bool uc[52.34,85.45], bool NUge)
	return

func iMdm ()
	return
'''
		expect = '''Program([VarDecl(Id(Rlo), ArrayType([2.07], BoolType), None, Id(Xf7)), VarDecl(Id(vK), ArrayType([62.15], NumberType), None, BooleanLit(True)), VarDecl(Id(Pt), None, var, BooleanLit(True)), FuncDecl(Id(gCMB), [VarDecl(Id(uc), ArrayType([52.34, 85.45], BoolType), None, None), VarDecl(Id(NUge), BoolType, None, None)], Return()), FuncDecl(Id(iMdm), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 561))

	def test_562(self):
		input = '''
func bEK ()	begin
		continue
		break
		OlZ("J")
	end
'''
		expect = '''Program([FuncDecl(Id(bEK), [], Block([Continue, Break, CallStmt(Id(OlZ), [StringLit(J)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 562))

	def test_563(self):
		input = '''
func nw (number lQ2Y[15.91])	begin
	end
func DqP (bool l0ov[81.75,61.22,39.94], number lRK[28.57,13.86])	begin
	end
number Od <- 59.2
'''
		expect = '''Program([FuncDecl(Id(nw), [VarDecl(Id(lQ2Y), ArrayType([15.91], NumberType), None, None)], Block([])), FuncDecl(Id(DqP), [VarDecl(Id(l0ov), ArrayType([81.75, 61.22, 39.94], BoolType), None, None), VarDecl(Id(lRK), ArrayType([28.57, 13.86], NumberType), None, None)], Block([])), VarDecl(Id(Od), NumberType, None, NumLit(59.2))])'''
		self.assertTrue(TestAST.test(input, expect, 563))

	def test_564(self):
		input = '''
bool bm <- 19.9
func hZ1v (string vS[26.53])	begin
		continue
	end
number YEa6 <- "caZG"
func OFYq (bool u6[1.86,21.07], string s7t)	begin
		E5(mRh, false)
	end

func r0 ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(bm), BoolType, None, NumLit(19.9)), FuncDecl(Id(hZ1v), [VarDecl(Id(vS), ArrayType([26.53], StringType), None, None)], Block([Continue])), VarDecl(Id(YEa6), NumberType, None, StringLit(caZG)), FuncDecl(Id(OFYq), [VarDecl(Id(u6), ArrayType([1.86, 21.07], BoolType), None, None), VarDecl(Id(s7t), StringType, None, None)], Block([CallStmt(Id(E5), [Id(mRh), BooleanLit(False)])])), FuncDecl(Id(r0), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 564))

	def test_565(self):
		input = '''
func luF (number Kv, string tBpY[30.6,98.53], bool XN[63.69,28.43])
	begin
		b5Y <- 95.94
		for ObK until "OmpF" by 92.22
			return
		for puDx until true by gik
			rFx1 <- NI
	end
'''
		expect = '''Program([FuncDecl(Id(luF), [VarDecl(Id(Kv), NumberType, None, None), VarDecl(Id(tBpY), ArrayType([30.6, 98.53], StringType), None, None), VarDecl(Id(XN), ArrayType([63.69, 28.43], BoolType), None, None)], Block([AssignStmt(Id(b5Y), NumLit(95.94)), For(Id(ObK), StringLit(OmpF), NumLit(92.22), Return()), For(Id(puDx), BooleanLit(True), Id(gik), AssignStmt(Id(rFx1), Id(NI)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 565))

	def test_566(self):
		input = '''
func gfuA (number Vsr)
	return Yw
number Rq <- true
'''
		expect = '''Program([FuncDecl(Id(gfuA), [VarDecl(Id(Vsr), NumberType, None, None)], Return(Id(Yw))), VarDecl(Id(Rq), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 566))

	def test_567(self):
		input = '''
var fdr <- true
'''
		expect = '''Program([VarDecl(Id(fdr), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 567))

	def test_568(self):
		input = '''
func zSS ()	begin
		begin
			eOl()
			for T1as until tTOM by 53.65
				return
			for OQ until 78.75 by 12.45
				ocw(bnB, 87.15, false)
		end
		return 32.89
	end
func ga (string Ob[28.16,8.72])	return FU

'''
		expect = '''Program([FuncDecl(Id(zSS), [], Block([Block([CallStmt(Id(eOl), []), For(Id(T1as), Id(tTOM), NumLit(53.65), Return()), For(Id(OQ), NumLit(78.75), NumLit(12.45), CallStmt(Id(ocw), [Id(bnB), NumLit(87.15), BooleanLit(False)]))]), Return(NumLit(32.89))])), FuncDecl(Id(ga), [VarDecl(Id(Ob), ArrayType([28.16, 8.72], StringType), None, None)], Return(Id(FU)))])'''
		self.assertTrue(TestAST.test(input, expect, 568))

	def test_569(self):
		input = '''
string Ue[85.48,44.64,51.31] <- "Y"
'''
		expect = '''Program([VarDecl(Id(Ue), ArrayType([85.48, 44.64, 51.31], StringType), None, StringLit(Y))])'''
		self.assertTrue(TestAST.test(input, expect, 569))

	def test_570(self):
		input = '''
func WW_X (string tQnM, bool Xv5[1.45,97.44])
	return

func dU ()
	return
func UfrE (bool o4IB)	return

func ik (string kJhi[68.61], string on, bool AR[23.51])	return 49.27
'''
		expect = '''Program([FuncDecl(Id(WW_X), [VarDecl(Id(tQnM), StringType, None, None), VarDecl(Id(Xv5), ArrayType([1.45, 97.44], BoolType), None, None)], Return()), FuncDecl(Id(dU), [], Return()), FuncDecl(Id(UfrE), [VarDecl(Id(o4IB), BoolType, None, None)], Return()), FuncDecl(Id(ik), [VarDecl(Id(kJhi), ArrayType([68.61], StringType), None, None), VarDecl(Id(on), StringType, None, None), VarDecl(Id(AR), ArrayType([23.51], BoolType), None, None)], Return(NumLit(49.27)))])'''
		self.assertTrue(TestAST.test(input, expect, 570))

	def test_571(self):
		input = '''
dynamic ii
func er (number YFaC[88.77,83.18])
	return true
string R_b[35.18,52.99,92.39]
'''
		expect = '''Program([VarDecl(Id(ii), None, dynamic, None), FuncDecl(Id(er), [VarDecl(Id(YFaC), ArrayType([88.77, 83.18], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(R_b), ArrayType([35.18, 52.99, 92.39], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 571))

	def test_572(self):
		input = '''
bool pq
string Q9[6.88]
'''
		expect = '''Program([VarDecl(Id(pq), BoolType, None, None), VarDecl(Id(Q9), ArrayType([6.88], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 572))

	def test_573(self):
		input = '''
func q82l (bool niD, number leW)
	begin
		begin
			string CwhX[74.64,33.2,77.56] <- "je"
			for bE until t_V by nq
				begin
					if (true)
					break
					elif (false) tre <- false
					elif (I0q)
					break
					elif (xcV6) if (26.07)
					bool l_ <- 20.51
					elif (Mq8L)
					return false
					elif (true) kuF <- "TX"
					else dynamic Cda <- true
					elif (true) xc()
				end
			var PS7 <- "gUg"
		end
		GoA <- "HAo"
	end
number Rq[18.92,33.06,75.59] <- "Gqqx"
number QCP7
bool KkH[53.7,13.18,5.91] <- 48.66
'''
		expect = '''Program([FuncDecl(Id(q82l), [VarDecl(Id(niD), BoolType, None, None), VarDecl(Id(leW), NumberType, None, None)], Block([Block([VarDecl(Id(CwhX), ArrayType([74.64, 33.2, 77.56], StringType), None, StringLit(je)), For(Id(bE), Id(t_V), Id(nq), Block([If((BooleanLit(True), Break), [(BooleanLit(False), AssignStmt(Id(tre), BooleanLit(False))), (Id(I0q), Break), (Id(xcV6), If((NumLit(26.07), VarDecl(Id(l_), BoolType, None, NumLit(20.51))), [(Id(Mq8L), Return(BooleanLit(False))), (BooleanLit(True), AssignStmt(Id(kuF), StringLit(TX)))], VarDecl(Id(Cda), None, dynamic, BooleanLit(True)))), (BooleanLit(True), CallStmt(Id(xc), []))], None)])), VarDecl(Id(PS7), None, var, StringLit(gUg))]), AssignStmt(Id(GoA), StringLit(HAo))])), VarDecl(Id(Rq), ArrayType([18.92, 33.06, 75.59], NumberType), None, StringLit(Gqqx)), VarDecl(Id(QCP7), NumberType, None, None), VarDecl(Id(KkH), ArrayType([53.7, 13.18, 5.91], BoolType), None, NumLit(48.66))])'''
		self.assertTrue(TestAST.test(input, expect, 573))

	def test_574(self):
		input = '''
bool ReMJ[15.77,46.74] <- "GS"
'''
		expect = '''Program([VarDecl(Id(ReMJ), ArrayType([15.77, 46.74], BoolType), None, StringLit(GS))])'''
		self.assertTrue(TestAST.test(input, expect, 574))

	def test_575(self):
		input = '''
func oN ()	return

'''
		expect = '''Program([FuncDecl(Id(oN), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 575))

	def test_576(self):
		input = '''
func Eo ()
	begin
		for dBEv until 84.48 by true
			xMl(SoVL, JfN)
		Qox("ejNPS")
		begin
			if (50.81)
			ZasR()
			elif (ZN)
			if ("s") return
			elif (Y9) begin
				for gjtH until 86.1 by JB
					begin
						begin
							VG(67.86)
						end
						D821(false, 71.12)
						string yR[52.37,35.56,92.46] <- "IBh"
					end
			end
			elif (true) return dE
			elif (O_AF)
			if (78.02) return
			elif (89.84) begin
				return 53.51
			end
			elif ("mst") continue
			else for KP until ucJs by YF
				string X0 <- 20.73
			else return
			if (true)
			continue
			elif (82.52)
			if (false)
			return
			elif (Fe) number SI
			elif ("EC")
			for WKKW until 85.24 by "Mgae"
				for BY3 until "wT" by 89.28
					if (true) var DVL <- soW
					elif (zPX) break
					elif (false) Q9("Us", g3)
					elif (true)
					continue
					elif (37.9) begin
						string o1[68.66,53.12]
						bool tu[19.83,28.22,70.06]
					end
					else for mS08 until z6A by 44.56
						return
			elif ("PEM") cm8U(false)
			elif (pt)
			begin
			end
			elif (Ft1F) KaL("pnK", 89.3, 46.76)
			elif ("zAag") continue
			elif ("YS")
			begin
			end
			elif ("E")
			return
			elif (24.12) continue
		end
	end
func AIv (number fIyH[39.36,25.07,31.39], string LAh)	begin
		for o7U until "oHQX" by "mccJk"
			O9w()
		Gt <- "Onhsv"
		y3V7["udUZM", "Tkj", true] <- true
	end
number dW
func zwTV ()
	return

'''
		expect = '''Program([FuncDecl(Id(Eo), [], Block([For(Id(dBEv), NumLit(84.48), BooleanLit(True), CallStmt(Id(xMl), [Id(SoVL), Id(JfN)])), CallStmt(Id(Qox), [StringLit(ejNPS)]), Block([If((NumLit(50.81), CallStmt(Id(ZasR), [])), [(Id(ZN), If((StringLit(s), Return()), [(Id(Y9), Block([For(Id(gjtH), NumLit(86.1), Id(JB), Block([Block([CallStmt(Id(VG), [NumLit(67.86)])]), CallStmt(Id(D821), [BooleanLit(False), NumLit(71.12)]), VarDecl(Id(yR), ArrayType([52.37, 35.56, 92.46], StringType), None, StringLit(IBh))]))])), (BooleanLit(True), Return(Id(dE))), (Id(O_AF), If((NumLit(78.02), Return()), [(NumLit(89.84), Block([Return(NumLit(53.51))])), (StringLit(mst), Continue)], For(Id(KP), Id(ucJs), Id(YF), VarDecl(Id(X0), StringType, None, NumLit(20.73)))))], Return()))], None), If((BooleanLit(True), Continue), [(NumLit(82.52), If((BooleanLit(False), Return()), [(Id(Fe), VarDecl(Id(SI), NumberType, None, None)), (StringLit(EC), For(Id(WKKW), NumLit(85.24), StringLit(Mgae), For(Id(BY3), StringLit(wT), NumLit(89.28), If((BooleanLit(True), VarDecl(Id(DVL), None, var, Id(soW))), [(Id(zPX), Break), (BooleanLit(False), CallStmt(Id(Q9), [StringLit(Us), Id(g3)])), (BooleanLit(True), Continue), (NumLit(37.9), Block([VarDecl(Id(o1), ArrayType([68.66, 53.12], StringType), None, None), VarDecl(Id(tu), ArrayType([19.83, 28.22, 70.06], BoolType), None, None)]))], For(Id(mS08), Id(z6A), NumLit(44.56), Return()))))), (StringLit(PEM), CallStmt(Id(cm8U), [BooleanLit(False)])), (Id(pt), Block([])), (Id(Ft1F), CallStmt(Id(KaL), [StringLit(pnK), NumLit(89.3), NumLit(46.76)])), (StringLit(zAag), Continue), (StringLit(YS), Block([])), (StringLit(E), Return()), (NumLit(24.12), Continue)], None))], None)])])), FuncDecl(Id(AIv), [VarDecl(Id(fIyH), ArrayType([39.36, 25.07, 31.39], NumberType), None, None), VarDecl(Id(LAh), StringType, None, None)], Block([For(Id(o7U), StringLit(oHQX), StringLit(mccJk), CallStmt(Id(O9w), [])), AssignStmt(Id(Gt), StringLit(Onhsv)), AssignStmt(ArrayCell(Id(y3V7), [StringLit(udUZM), StringLit(Tkj), BooleanLit(True)]), BooleanLit(True))])), VarDecl(Id(dW), NumberType, None, None), FuncDecl(Id(zwTV), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 576))

	def test_577(self):
		input = '''
func FJAb (number Ii, string Tm6I, number n5h)	return

string pYC[51.63]
func GXY (number mMMc[49.59])	return "qSEM"

'''
		expect = '''Program([FuncDecl(Id(FJAb), [VarDecl(Id(Ii), NumberType, None, None), VarDecl(Id(Tm6I), StringType, None, None), VarDecl(Id(n5h), NumberType, None, None)], Return()), VarDecl(Id(pYC), ArrayType([51.63], StringType), None, None), FuncDecl(Id(GXY), [VarDecl(Id(mMMc), ArrayType([49.59], NumberType), None, None)], Return(StringLit(qSEM)))])'''
		self.assertTrue(TestAST.test(input, expect, 577))

	def test_578(self):
		input = '''
func vyS ()
	return

var xJ <- 23.45
func jHT (string B43R[57.71,92.29,49.05])	return
bool Tbg4[86.02]
'''
		expect = '''Program([FuncDecl(Id(vyS), [], Return()), VarDecl(Id(xJ), None, var, NumLit(23.45)), FuncDecl(Id(jHT), [VarDecl(Id(B43R), ArrayType([57.71, 92.29, 49.05], StringType), None, None)], Return()), VarDecl(Id(Tbg4), ArrayType([86.02], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 578))

	def test_579(self):
		input = '''
bool y2[62.31]
func V9XQ (number A_[89.04,69.83,76.94])	begin
		return
	end

func Zy0 (string Ug9, number yiVb, number wy4a)	return

'''
		expect = '''Program([VarDecl(Id(y2), ArrayType([62.31], BoolType), None, None), FuncDecl(Id(V9XQ), [VarDecl(Id(A_), ArrayType([89.04, 69.83, 76.94], NumberType), None, None)], Block([Return()])), FuncDecl(Id(Zy0), [VarDecl(Id(Ug9), StringType, None, None), VarDecl(Id(yiVb), NumberType, None, None), VarDecl(Id(wy4a), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 579))

	def test_580(self):
		input = '''
var Bx <- true
number pZE3[15.53,12.57]
func y_ (string J39[71.51,88.49], bool Ma, bool G6[32.68])
	begin
		continue
		break
	end
func Drvj ()	return "Rz"

'''
		expect = '''Program([VarDecl(Id(Bx), None, var, BooleanLit(True)), VarDecl(Id(pZE3), ArrayType([15.53, 12.57], NumberType), None, None), FuncDecl(Id(y_), [VarDecl(Id(J39), ArrayType([71.51, 88.49], StringType), None, None), VarDecl(Id(Ma), BoolType, None, None), VarDecl(Id(G6), ArrayType([32.68], BoolType), None, None)], Block([Continue, Break])), FuncDecl(Id(Drvj), [], Return(StringLit(Rz)))])'''
		self.assertTrue(TestAST.test(input, expect, 580))

	def test_581(self):
		input = '''
func BR (string OX, number gjC)	return

func LE ()
	return false
bool LZb[90.31,72.14,77.21]
func VyQ ()
	return "fqFM"
func CRR (string Kd[83.58,21.77], string mAOT, bool V29[58.96])
	return
'''
		expect = '''Program([FuncDecl(Id(BR), [VarDecl(Id(OX), StringType, None, None), VarDecl(Id(gjC), NumberType, None, None)], Return()), FuncDecl(Id(LE), [], Return(BooleanLit(False))), VarDecl(Id(LZb), ArrayType([90.31, 72.14, 77.21], BoolType), None, None), FuncDecl(Id(VyQ), [], Return(StringLit(fqFM))), FuncDecl(Id(CRR), [VarDecl(Id(Kd), ArrayType([83.58, 21.77], StringType), None, None), VarDecl(Id(mAOT), StringType, None, None), VarDecl(Id(V29), ArrayType([58.96], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 581))

	def test_582(self):
		input = '''
func ETJ7 (bool wZH9)
	return true
func T_s7 (bool mFgl, number eGM, string q4nc[49.03,58.73])	return
func d4Uq ()	return
'''
		expect = '''Program([FuncDecl(Id(ETJ7), [VarDecl(Id(wZH9), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(T_s7), [VarDecl(Id(mFgl), BoolType, None, None), VarDecl(Id(eGM), NumberType, None, None), VarDecl(Id(q4nc), ArrayType([49.03, 58.73], StringType), None, None)], Return()), FuncDecl(Id(d4Uq), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 582))

	def test_583(self):
		input = '''
bool dqlw <- SZwb
func KTO (string GK[41.95,62.91])
	begin
	end
'''
		expect = '''Program([VarDecl(Id(dqlw), BoolType, None, Id(SZwb)), FuncDecl(Id(KTO), [VarDecl(Id(GK), ArrayType([41.95, 62.91], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 583))

	def test_584(self):
		input = '''
number pyb
dynamic Kjt <- true
'''
		expect = '''Program([VarDecl(Id(pyb), NumberType, None, None), VarDecl(Id(Kjt), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 584))

	def test_585(self):
		input = '''
func heR ()	begin
	end
bool qeV[54.55] <- JEgE
number MJt
bool lc
'''
		expect = '''Program([FuncDecl(Id(heR), [], Block([])), VarDecl(Id(qeV), ArrayType([54.55], BoolType), None, Id(JEgE)), VarDecl(Id(MJt), NumberType, None, None), VarDecl(Id(lc), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 585))

	def test_586(self):
		input = '''
string mT
number Wdlx
func uizn (bool D3Z)	return

number O01[2.65,35.75,49.15] <- "oC"
bool hQrJ[89.69,31.84]
'''
		expect = '''Program([VarDecl(Id(mT), StringType, None, None), VarDecl(Id(Wdlx), NumberType, None, None), FuncDecl(Id(uizn), [VarDecl(Id(D3Z), BoolType, None, None)], Return()), VarDecl(Id(O01), ArrayType([2.65, 35.75, 49.15], NumberType), None, StringLit(oC)), VarDecl(Id(hQrJ), ArrayType([89.69, 31.84], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 586))

	def test_587(self):
		input = '''
string Gd <- 15.09
func QvFA ()	return "sCX"

'''
		expect = '''Program([VarDecl(Id(Gd), StringType, None, NumLit(15.09)), FuncDecl(Id(QvFA), [], Return(StringLit(sCX)))])'''
		self.assertTrue(TestAST.test(input, expect, 587))

	def test_588(self):
		input = '''
func izQ ()
	return
string xK[46.25,10.86]
func tUm ()
	return "O"

'''
		expect = '''Program([FuncDecl(Id(izQ), [], Return()), VarDecl(Id(xK), ArrayType([46.25, 10.86], StringType), None, None), FuncDecl(Id(tUm), [], Return(StringLit(O)))])'''
		self.assertTrue(TestAST.test(input, expect, 588))

	def test_589(self):
		input = '''
func w76i (bool sgo, number HnSA[56.01])	begin
	end
func HGv (number wvl[32.77,65.26,36.9])	begin
		continue
	end

var aVF <- "ozEL"
'''
		expect = '''Program([FuncDecl(Id(w76i), [VarDecl(Id(sgo), BoolType, None, None), VarDecl(Id(HnSA), ArrayType([56.01], NumberType), None, None)], Block([])), FuncDecl(Id(HGv), [VarDecl(Id(wvl), ArrayType([32.77, 65.26, 36.9], NumberType), None, None)], Block([Continue])), VarDecl(Id(aVF), None, var, StringLit(ozEL))])'''
		self.assertTrue(TestAST.test(input, expect, 589))

	def test_590(self):
		input = '''
number PA[4.18,97.46,63.65]
number V3C[50.11,47.37,27.78] <- "BhRq"
number XI7N[84.0,81.42]
func Va5F (bool D7n[99.77,81.06], string JE2A, bool HfLh[34.93,4.36])	return JfD

'''
		expect = '''Program([VarDecl(Id(PA), ArrayType([4.18, 97.46, 63.65], NumberType), None, None), VarDecl(Id(V3C), ArrayType([50.11, 47.37, 27.78], NumberType), None, StringLit(BhRq)), VarDecl(Id(XI7N), ArrayType([84.0, 81.42], NumberType), None, None), FuncDecl(Id(Va5F), [VarDecl(Id(D7n), ArrayType([99.77, 81.06], BoolType), None, None), VarDecl(Id(JE2A), StringType, None, None), VarDecl(Id(HfLh), ArrayType([34.93, 4.36], BoolType), None, None)], Return(Id(JfD)))])'''
		self.assertTrue(TestAST.test(input, expect, 590))

	def test_591(self):
		input = '''
func FNsz (number AP3l, bool QS)
	return true

func vav ()
	return true
number nwrB <- true
func Sdx (number jr[97.86,45.35])
	return

func sT (bool ryh, string Ym[58.81,15.98,45.16], number MWV)
	return 32.94

'''
		expect = '''Program([FuncDecl(Id(FNsz), [VarDecl(Id(AP3l), NumberType, None, None), VarDecl(Id(QS), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(vav), [], Return(BooleanLit(True))), VarDecl(Id(nwrB), NumberType, None, BooleanLit(True)), FuncDecl(Id(Sdx), [VarDecl(Id(jr), ArrayType([97.86, 45.35], NumberType), None, None)], Return()), FuncDecl(Id(sT), [VarDecl(Id(ryh), BoolType, None, None), VarDecl(Id(Ym), ArrayType([58.81, 15.98, 45.16], StringType), None, None), VarDecl(Id(MWV), NumberType, None, None)], Return(NumLit(32.94)))])'''
		self.assertTrue(TestAST.test(input, expect, 591))

	def test_592(self):
		input = '''
func v9SG (string GgP, number HQP[43.91,70.11], number qU[0.56,48.28])
	begin
		b1k["NOogO", "G", 29.38] <- 89.73
		begin
		end
		for FeNk until "ybnjt" by false
			return
	end

'''
		expect = '''Program([FuncDecl(Id(v9SG), [VarDecl(Id(GgP), StringType, None, None), VarDecl(Id(HQP), ArrayType([43.91, 70.11], NumberType), None, None), VarDecl(Id(qU), ArrayType([0.56, 48.28], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(b1k), [StringLit(NOogO), StringLit(G), NumLit(29.38)]), NumLit(89.73)), Block([]), For(Id(FeNk), StringLit(ybnjt), BooleanLit(False), Return())]))])'''
		self.assertTrue(TestAST.test(input, expect, 592))

	def test_593(self):
		input = '''
func xR (string i8W[11.36,5.37,45.78])	return "x"

func suT (string smQ)
	begin
		string uHd[33.35,60.93]
		number ilqS[12.47,17.63,57.59]
		for Hp9 until 40.42 by YY8r
			number NsM[95.36] <- true
	end
func NG_J (number iYI)	return "C"

func vj75 (bool Drm[56.05,29.09], string wG1[55.88])	return

'''
		expect = '''Program([FuncDecl(Id(xR), [VarDecl(Id(i8W), ArrayType([11.36, 5.37, 45.78], StringType), None, None)], Return(StringLit(x))), FuncDecl(Id(suT), [VarDecl(Id(smQ), StringType, None, None)], Block([VarDecl(Id(uHd), ArrayType([33.35, 60.93], StringType), None, None), VarDecl(Id(ilqS), ArrayType([12.47, 17.63, 57.59], NumberType), None, None), For(Id(Hp9), NumLit(40.42), Id(YY8r), VarDecl(Id(NsM), ArrayType([95.36], NumberType), None, BooleanLit(True)))])), FuncDecl(Id(NG_J), [VarDecl(Id(iYI), NumberType, None, None)], Return(StringLit(C))), FuncDecl(Id(vj75), [VarDecl(Id(Drm), ArrayType([56.05, 29.09], BoolType), None, None), VarDecl(Id(wG1), ArrayType([55.88], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 593))

	def test_594(self):
		input = '''
number QCR[52.58,58.72]
'''
		expect = '''Program([VarDecl(Id(QCR), ArrayType([52.58, 58.72], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 594))

	def test_595(self):
		input = '''
bool ksQ[22.97,35.58]
dynamic qb
'''
		expect = '''Program([VarDecl(Id(ksQ), ArrayType([22.97, 35.58], BoolType), None, None), VarDecl(Id(qb), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 595))

	def test_596(self):
		input = '''
func MN (number Fbm8[38.63,76.11])	begin
	end

'''
		expect = '''Program([FuncDecl(Id(MN), [VarDecl(Id(Fbm8), ArrayType([38.63, 76.11], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 596))

	def test_597(self):
		input = '''
func az ()	return
func P3C ()	return
string st[3.25] <- 25.76
func Ke3 (number uv[70.57,16.37,8.9], number kG[80.12,10.05,47.18], string FZP[94.43])
	return "X"
func AK (string lb5T)
	return
'''
		expect = '''Program([FuncDecl(Id(az), [], Return()), FuncDecl(Id(P3C), [], Return()), VarDecl(Id(st), ArrayType([3.25], StringType), None, NumLit(25.76)), FuncDecl(Id(Ke3), [VarDecl(Id(uv), ArrayType([70.57, 16.37, 8.9], NumberType), None, None), VarDecl(Id(kG), ArrayType([80.12, 10.05, 47.18], NumberType), None, None), VarDecl(Id(FZP), ArrayType([94.43], StringType), None, None)], Return(StringLit(X))), FuncDecl(Id(AK), [VarDecl(Id(lb5T), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 597))

	def test_598(self):
		input = '''
number hLPS[43.45]
func oop (bool ZYj)	return "jJKP"

string CJ[71.52,26.19] <- 66.35
func PX (string yEkw[91.37,99.19], number UbE[66.06])
	return false
'''
		expect = '''Program([VarDecl(Id(hLPS), ArrayType([43.45], NumberType), None, None), FuncDecl(Id(oop), [VarDecl(Id(ZYj), BoolType, None, None)], Return(StringLit(jJKP))), VarDecl(Id(CJ), ArrayType([71.52, 26.19], StringType), None, NumLit(66.35)), FuncDecl(Id(PX), [VarDecl(Id(yEkw), ArrayType([91.37, 99.19], StringType), None, None), VarDecl(Id(UbE), ArrayType([66.06], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 598))

	def test_599(self):
		input = '''
func cO (bool KNp[76.56], string xweM, string k0)
	return LH6

func gq ()
	begin
		begin
			ty <- "djr"
			if ("goZ")
			continue
			elif (qfZM) OuZ[P6rH, 6.12] <- false
			elif (61.17) return true
			elif (true) for LmLb until "CQXx" by 96.85
				F8WT[true] <- 14.46
			elif (false) if (false)
			if (58.41) if (Al9J) continue
			elif ("On")
			break
			elif (true)
			begin
			end
			elif (LB)
			begin
				al <- "Bjs"
				bool ZJ
			end
			elif (true) if (55.76) return
			elif (lNzy) continue
			elif (lJfv)
			IUc[12.55, true, mtZt] <- "H"
			elif (QN)
			break
			elif ("bGl")
			begin
			end
			elif (frtK)
			string L0H
			break
		end
		G2F[Pd, "RoRGH"] <- 62.13
		return WJMc
	end

bool HIg[55.82]
'''
		expect = '''Program([FuncDecl(Id(cO), [VarDecl(Id(KNp), ArrayType([76.56], BoolType), None, None), VarDecl(Id(xweM), StringType, None, None), VarDecl(Id(k0), StringType, None, None)], Return(Id(LH6))), FuncDecl(Id(gq), [], Block([Block([AssignStmt(Id(ty), StringLit(djr)), If((StringLit(goZ), Continue), [(Id(qfZM), AssignStmt(ArrayCell(Id(OuZ), [Id(P6rH), NumLit(6.12)]), BooleanLit(False))), (NumLit(61.17), Return(BooleanLit(True))), (BooleanLit(True), For(Id(LmLb), StringLit(CQXx), NumLit(96.85), AssignStmt(ArrayCell(Id(F8WT), [BooleanLit(True)]), NumLit(14.46)))), (BooleanLit(False), If((BooleanLit(False), If((NumLit(58.41), If((Id(Al9J), Continue), [(StringLit(On), Break)], None)), [(BooleanLit(True), Block([]))], None)), [(Id(LB), Block([AssignStmt(Id(al), StringLit(Bjs)), VarDecl(Id(ZJ), BoolType, None, None)])), (BooleanLit(True), If((NumLit(55.76), Return()), [(Id(lNzy), Continue), (Id(lJfv), AssignStmt(ArrayCell(Id(IUc), [NumLit(12.55), BooleanLit(True), Id(mtZt)]), StringLit(H))), (Id(QN), Break), (StringLit(bGl), Block([])), (Id(frtK), VarDecl(Id(L0H), StringType, None, None))], None))], None))], None), Break]), AssignStmt(ArrayCell(Id(G2F), [Id(Pd), StringLit(RoRGH)]), NumLit(62.13)), Return(Id(WJMc))])), VarDecl(Id(HIg), ArrayType([55.82], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 599))

	def test_600(self):
		input = '''
func Ra (string tnAN[68.23,83.98], number dXj[12.69,23.42], string Mt[39.83,47.94,56.32])
	return TT

func NI (bool qT[70.64,38.41])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Ra), [VarDecl(Id(tnAN), ArrayType([68.23, 83.98], StringType), None, None), VarDecl(Id(dXj), ArrayType([12.69, 23.42], NumberType), None, None), VarDecl(Id(Mt), ArrayType([39.83, 47.94, 56.32], StringType), None, None)], Return(Id(TT))), FuncDecl(Id(NI), [VarDecl(Id(qT), ArrayType([70.64, 38.41], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 600))
