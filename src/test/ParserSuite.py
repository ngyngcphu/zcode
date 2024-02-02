import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
## "2p]rC{^jQ197$<o4
bool OZ7[8.469e-18,145] <- K0("2khs&", RREQ(5))["'"L"] == 69 ## iu}T
number oB8[893,8.484]
## A>dKyD$>ccZ<y6f37
var zI[9.735]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
## ;/wGB:XKiXD`W
## LE
func j9 (var sF[61,442.384e94,2.577E78])
	return

string Cab ## yR"
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
## lOwx%#hl
bool ys[2.468] <- "'"z"
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
number wB[6.216E12,564.250,28] <- false
func EI0C (string V5ja[7.245e-11], var sB1, number xdO5[307E+54,51e50,269.136])
	return

func KRD (string d9s[23,17,30.817E+31])
	return

bool jh <- 992 ## qRNfU53#H4)5
string ttO[8.707,0.761,6e-26] <- 978.969 ## `
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
var idXN
## 6&~Uv5`1]&jY
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
bool N39Z[76e38,71.631E+07,0.875] <- WI ## ,!oGx.k[5VC@tL
func p7 (bool Ta[4e-83,17e+57])	begin
		return "*"
		## 3r#us4t`YU"p~979:%r
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
func a_lR (bool mi, dynamic mH[264,5.035])
	return 223.276E42

dynamic to5b[7.136] ## Ljj4*b8O
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
## vm4;pC+0,y$
## WL.
func uTGW (bool DgA[32.031,711])	begin
		return 44E-16
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
## /
string uScU[1E60]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
number gwva[9.723e-48,75.717E-86,1]
func VNNM (dynamic ZZb, string IME)
	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
## ~)O
func QN (number le[205.835E+31,904.947e+64])
	return true

var ut8V[25e+51,78.598,84.614]
func epQ1 ()	return he

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
func hl_O (var qH)
	return 32
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
var LF
## "vO
string UUR
var eDa[0.781E-83] <- Am4L
dynamic rD
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
## _Z5wbFGx"h
func XIyM (dynamic ngLG, number SqS)	return "C_'"'""

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
dynamic dd77 ## g@3k&v^@$*!bhQ^
func XxH (bool OO, string ymy[0e-86,36.971,256], string wBPu)	begin
		## <#"JZ4)ONj/5|J|q2]
		## KA,CwzepI(h+0g@
		## NE
	end
number cqp
## }I:rid+xFEN
func G9m (bool wAR[806.481], var Tc7Z)
	return "}*'"5"

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
func M4d6 (dynamic ldgQ, bool Uf[2.626,84.848e+35], var V9FJ[7e+86,134.394E-90,18.270])
	begin
	end
func fO (var gJXJ[7,97])
	return true

string XjbA[8.257e-06,9.328E69,0.163] <- FQkZ ## a^t:EG
dynamic vA <- 897.305 ## jKlb.- [
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
func TPn (dynamic reb, bool sP[483E+21])	return XD

## yr3/
func aqHn (var S2[15.715e-34], dynamic CGb, string bcl[9.506,9,1E+42])	begin
		begin
			## .r"4kKh10:Fk-B;W:VN
			## c79}38oA%L+|NA
			VfQ <- 1.119
		end
		begin
			continue
			rj("'"'"'"{", false, "'"")
			## V^(0VN
		end
	end

string YDDX ## ,uTDV={F"LGUoc
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
var ezH <- false ## N1G5kFzOxTV;#O_b_Z
## P I-+_yQ!,e<DF
func wbJ (var YY[9.877E-47,93.982e-49], number GZx[458])	begin
		break
	end

var HHI[4.404E01] ## 5:
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
bool Soc[0] <- Kg4 ## ){pQd
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
func Pd (bool Gt, number odSQ, string uld2[57.433e02,318])
	begin
		break
		## y+LUP-AYoW7*;QftJvB
	end

var bn ## #0Z+Zw7)D6ZbA3g*w
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
func Ei (number RW[802.024E11,4,35.434])	return 802

dynamic skWw[834E-29,0.131,1.766e+65] <- "y"
number xSn[46.061,5E-55] <- x1o
func P7tw (var eDt, string dlhZ)	begin
		## ttJ]MlR
		for E8 until 91.317 by 8e-95
			continue
		## >}9
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func w1lN (number pjZ[6.061E-19,689.960,73E+54])	begin
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
string DPO3[1e+99,61.230E-36,51e+89] <- "/"
## i8a
var TIb[615E+01,33.218] <- j1 ## h gq!1j;B 8<|.OhlQn
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
string lX[87,522.809]
func PAsA (string dBa, var s3[3.856], dynamic dJ[33.105E15])	begin
		break
		continue
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
func WCpR (number pOm[73.515], string RS_)
	return jUB

## $]3M+{fOwzG.t
## <sfA/[Y
string N6g[5.755,20.758,844.456e-12] ## XNq{E5IXBnjh9
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
var oVnl <- 49.239E+87
func Rd ()
	begin
		## 4OCQlW4[/}M^^*BLVS
		## sc$7aid;]<?n:SeQ*
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
## 3SqVe&(F~$"y
func vqSD (dynamic Stx0[368.378E-80,50.914E+69,62.687E-53], var zI)	return

## >S^O0!PyCGX{K^TGD
## QR4bqD"+[u"kW#6?6.Vb
dynamic b7 <- true ## Wj;sH7/4eFm(mXoqVF#q
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
## 9z4}ebuH2x7XLCXGNf
## H=HIcXy
func qy ()
	return
## Xgw&!.n4lP14eWo!qr
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
## r8rP2fti`Gygx(%p
dynamic QJ[622.732,10e+20,54.354e-46] <- 0E+00 ## 33IM&
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## Gpk{e.HF4d;T}^
## ^
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
bool LAbG
string yCa[3.571E-65,46.358,0.544E17] <- false
## 8w<Ga`g;oT%Wf
func G6gD (string kyOf[6e33,1E+98], var rR8e[30E60,33.230])
	return

## 69v*Xofl2aeE<F
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
func Ge0 (dynamic eAIn, var UnB, string CZXM)	return true
func Kv (string wRI, var woVh, bool rtV[38.654E-77,8e-85,9e-92])
	return Ah

bool yN[34.900E-91,582.517,2.409] ## JSwUe|qQXU>=_/Qd=<
dynamic en
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
func CNNF ()
	return false

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
## w^1)At1>Ae<JpPFW{]Zo
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
## +r_@xGJ
## 1CfH,<xY
## FbN*tTu}:H<)"U
func Qm6 ()
	return
## 6CX6Vu_1-&LZ}0R2ch
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
string coh[2,4,66e01] <- SU ## ~T__,C.Or7AU}!3L/R_X
func lW1t (var Nt[14e11,8])
	begin
	end

number YM <- "'"'"y" ## --Q
## eDtUxEt9%J8En/
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
func A5 ()	return
func Iy (var oSOp[4.594e29], dynamic E1S, var DNY9)	begin
	end

func Jif (var QMI, string Xsc6)
	begin
		## {Ew4RXOb
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
## @SgapD35!NH
## =t0&~eCh}
## u-I
string jFe <- F0u ## -gZuc@0]ShE_hi+a{+
func BVpU (number jg[93,61e+32], dynamic XLk)	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
func tJ9J (number XP2[0E+91,96], string uU[15.886E+73,7E+18])
	begin
		## _)y
		number IPz[66.916E+85] <- false
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
func sYc (dynamic yw, var FH[861.693])	begin
		## xjrK&}!`FL.1UbDWbLE9
		CIb("B'"~'"(", "7Cu'"", skO)
		continue
	end
## |5u@pH:+q+]KJ?IC
## L::"?6>78
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
number Xue[1E+64,472] <- Rg ## HolQ;B`H
dynamic jrK[5e+81,9.019E-18,518.696e+35] ## k&f|:`Cml
## g
## {Rzl_,
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
## w4d[ilU
func enoA ()
	begin
		for fpFc until 994.369e76 by ":"
			bool ybV[404,2] <- 4E-28 ## ~,OT
		break
	end
bool Lo[86.906,94]
bool FQ <- "'"'"'"'""
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
## aa
## l;+mpWy8QJ@WL:T1uN
dynamic tzmB[931E-46]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
func d0ks (bool iHL[5.829,292.428e+31,9.540e+23])
	begin
		##  o",96jBs0^/$
		if (15E+07) return false
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
## bDUV6kU=Z#0
dynamic U1Vw <- true ## IhzXI3TA
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
func e6bT (dynamic Tck[698.162e29,725.137,96.029E32], var S6Z9[2.932E+63,96.943E-05])
	return MGF

var FT <- pN6 ## =<MjJsT0Ggx_L!ac
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
func AL ()	begin
		begin
			Re2[63.022E-83] <- "'"x+"
			## rtqqWXh
			## <xEvR8_[[$>M@Fe%
		end
		## vfNSZJ($[lAr=QK,+7/
		## D@
	end

number a05 <- true ## plihN6UA}V8z,B
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
func OVAC (number FoV[0,3E96], bool et, var Xfhb[0e76,58.322e-31,85.350e+37])
	return

number KH ## yg8gsed4Jf.Sk{t`w
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
## bTT3D4oj-3n(
func dWj (string FPs[63.940,32.269e32,413.903e62], var OO, bool mj[1e+40])	return false
func ZRk (string OWW[558.021])
	return "CS'""
string Ytsl[54.430] ## hLF~g7W#V]V~Q?
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
func hzpX (bool uOC[637e10])
	begin
		number Cd[5E20,89e-77] <- 1.090E-32
		s4 <- 2e-45
		## _"Tdq?_!h
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
func WE (number yWPh[8], dynamic ot[9E-39,1E+23])
	return false
var Ki_[94.677e-04]
bool K4[18.274E+77,4E-82] <- true ## Sl.&0A$Q
number DzE[32e07]
func Gr (var AO[606], number Ir[5.549,181,6.898E-59], bool YV[76.794,22])
	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
## :KnQ
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
## q6< )Hdx5Y`7`Y"9BU
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
## #7De?d[{[R*8mvWES?3
func lND4 ()
	begin
		## v]M-a.3T2rT{|
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
bool RZn[3.127,0e+07] ## 0,7!&;F
var jT ## @7:=X:/+u
func xgN (string xEcy, number JOU6)
	return oQ

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
dynamic Cj_[8]
func rE (bool ACJg[33E25], string L2[5.538e96,5.183E+31,9E-85])	return

dynamic EsI[653,260]
func Fyb (dynamic iAl[650.001e+28])
	return
dynamic tGAR[974e+87,58E65,35] ## m{E$C?A
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
bool sa[181.367] <- "1'"'"" ## X#Qf<?cW@d
## )
## ("}jg
func lKeb (var pqT[67.489,42E12,82.170E+26])	begin
	end
func rr (var uF[103.061E+88,472,50])
	begin
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
dynamic hi ## )$:q-&Ri=)_)kC&lt*<
dynamic dy
func oP8 (dynamic ve[1e-72])	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
var ZhY <- "'"'""
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
## +[bJC1qWBv
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
bool ERP8 ## :rns3d[YP_UG
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
func WE9 (string aAMu[67.825], number gW, string zLT[29.925e-02])	begin
		kX[false] <- "2'"O"
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
func aX_u ()
	return 0E-06
## `H:?1/ EsD`Hlr#fw
func mfbd (bool lc, bool ctg)
	return false
string hoZF <- "AF" ## sX%B-p*~|R_2x^
## ~ysr7WPZ)Y6n
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
## YP2K^lv: )_Os-qt?rN
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
number j6K[3E+66,519,35e97]
string FEiP[64E75,50.564E87] ## FGiJ(^Zfm<M$@iW0
## HO
func Ya (string Lhfp)	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
var OmK3 <- EA ## uqW:KTi
## r0*d8dmvg>gz
func CU (number HXRm)	begin
		return
	end
string S51[3.345e-13,1] <- "S" ## %>}q5to!GPiYE<
## xydBu/;E&z
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
number mZT
## B?a?8{J:94>PY^Xz@+v
## Se9;RJjzOa^hcJT&j$<{
## NU0DJ=U|3ufm]0t+p[
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
func LHZ (dynamic oO, number t9)	begin
		## zmpgOrA|%}syP<^VT!D
		for Ye until zsV by 9.171E77
			dynamic OoI[8.494,7,8E-67] ## Ds`:*J<
	end

func Sy ()	begin
		for Q2o until SfE by 10
			return ZiV9
	end

string eeVa[257E47]
## j1:k&E;/ @yP/N
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
func kk ()
	return
func xs ()	return

number eIZ[618.969E+82,187,9.598E89] <- true
string bmJN <- 9 ## f""-9!1}laMSJg"o":GJ
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
func E2X (var FVq[1E-20], dynamic Pn, bool Dm)	return "'"'"'""

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
## `T[;USso
## R(+4m-z+j&`jQ
func Sq (number a0fU[64e27,386e+41], var bjBj[4.501,485,3e08])
	return
func GsT (bool QgwW[5.984,5.665], number eF19, dynamic wM8k)	return

func zO ()
	begin
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
func rB ()	begin
		for dHZ until "K'"'"" by cp
			break
		if ("'"'"'"P7") for aKu until "E'"'"'"'"" by "'"t'"'";"
			return
		elif (2.093e+39) if (T7Tv) break
		elif (false) eExG(10, true)[false] <- 45.115E+38
		elif (td)
		for pc until "R]" by false
			begin
				if (true)
				return
				elif ("'"'"4")
				if (false)
				break
				elif ("^") if (Tl4v)
				X9(gm, true, true)["'"'"w"] <- "'""
				elif ("'"/'"")
				continue
				elif (uyd)
				break
				elif (3) begin
					dv()
				end
				elif (true) t1[EIMU, 9.902E-99, le] <- eg
				elif (799e04)
				return
				else IjX_()[1.800, false] <- "C"
				elif (31.218e88)
				begin
					continue
					dynamic EY_o <- false
					## Oz^I{0p@
				end
				elif ("V'".$")
				Na <- 75E+67
				elif (949)
				continue
				elif (sTIa) for XZhM until "OG" by true
					if (false) continue
					elif (true)
					if (true)
					continue
					elif (37.871E-54) break
					elif (6.173E52)
					GGU()
					elif (false) SZDK(885.950E+74)
				elif (QQtz)
				break
				elif (false)
				if (KCn) continue
				elif ("'"'"") if ("q") break
				elif (cn1)
				for Lel until giZx by "O;F'""
					dynamic nCW[7,5] <- 51e08 ## v^#m
				elif (false)
				begin
				end
				elif (wZbf)
				dynamic BYH
				elif (371.113)
				if ("'"'"'"")
				break
				elif (true) zmR(false, NYN, true)[86.199E+97] <- CLxj
				elif ("h") begin
					gO(13.600E-49, true)
				end
				elif (325.787)
				if (24.968E+63)
				if (2)
				return
				else begin
					return
					if (true) Yl(qj)
					else Ayhi("'"'"BM'"")
					break
				end
			end
		else for qK3 until "'"'"|'"" by 4.028e+94
			return
		elif ("'"'"$") begin
			## bctl*zVB_ZOL{yGIB6SS
		end
		## swZ7/
	end
## "TG<Z=~s(cN,M!xy}V`O
func TarY (number TT0[87], string HDvE[1.452,2.342])	begin
		## DG) .sluTy@ F k
		## V27fUe8lGQiwDR;82
		## {@c7ba0:3W
	end
## ?{yLM*s[EQY
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
func XI (bool y4Y)
	return true
func wm (bool Y1qm)
	return
var i6SB ## ">{;?b`
func oq5 ()
	return true
func KXbd (dynamic Zvz)
	return cFB0

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
## i9YsfdwJNj
func j8 (dynamic UP9[8])	begin
	end

## X8_/MKT3e:OMHxuu{
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
dynamic j0[38E45,594] ## h-w#*]c6dLm*[n&G
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
string ZLU[97,4.233e+37] <- saG ## 7n;l$FuX$
func sArZ (number WHN)
	return V4
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
dynamic FyKF[703E+78,8.503]
## b*uF/IeWwMjj;r
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
## [f
dynamic Ms5 <- 0e+02
func kgv (dynamic x7A[6.020e34])	return false
var Gv[0,46.185,928e53] ## *cmyiQ|7{_IB#,
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
var Hut <- 83.242e+23
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
## ?Z?!
dynamic q_w[17] <- "'"us9'"" ## 5P= 
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
## 7AQ^KU!k93lA
## ZV10kCu^5d&<p5
## UsHy(hz*+;"qoG_t,c
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
number Xd[87.622,95E-72,7] <- 72.393
## O SsFIY!rqh~J]dy
func eJ (var DP[2.630,20.552,46E+37])
	return

## !t
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
func yNQr (string M28, string B79I)
	return

## ajRB8B.
func AP8n (bool I_, string f7V[3.438E-06])	return "T'"|o"

## ,C"-ZRvN@Y9ri%^nOf
## 1b^m$
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
func XF19 ()	begin
		if ("Ib('"3") break
		elif (true)
		g24 <- 5E08
		elif (true) string uevY[8E-70]
		elif ("'"i&") if (SE) if (Ne)
		for pjK until 678 by bga
			continue
		elif (DB_4) continue
		elif (fRGL)
		th[UC, "Jt'"", "'"l"] <- GV5K
		elif (287e+37) Gb4g <- "'"v'""
		elif (93E-70)
		begin
			if ("'"C") string D3I4[0e98,2,4.196e97] <- "W"
			elif (true) for sy2 until false by 66.161
				begin
					continue
					## ZOb}pT%(mAP>
				end
			elif (Ae)
			for M0 until C2 by true
				begin
					if (643.576)
					return
					elif (KmuC) for h_ until true by "{L"
						begin
							## J5Kd(7N
						end
					elif ("w'"")
					break
					## BM?M=6B]PH-fUKQaV$TA
				end
			break
			## (8Nk=BgP
		end
		## nU>$LeQs1={K&A9
	end

dynamic yiD ## VGSShQw @b!IKr+OEY
dynamic Sg <- "s('"S"
## X!
func xUrr (string xTDZ, var OQV[1E-65,430e-12,1.484], dynamic sUx[74.121E-94,43.881,527.682E14])	return "'"dd"
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
## |&
func uPL ()
	return false

## 8+z,/r@V(f$*tvL@aCX
func uzz2 (number sSH, var L287, var DyE)	begin
		dynamic EfHN <- 3E+57
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
dynamic rf <- "("
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
func OIvp ()	begin
		if ("(&6'"") ngQ <- 34.479
		elif (false)
		break
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
dynamic s1a[689E+58,96.611E93]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
func LDl (string Mu, bool E5Zq[7.643], dynamic sI)
	begin
		continue
		continue
	end
## h&T!M~2CVtpmZP_CI
func xie (var KQN)	return "3n'""

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
string tMxU[9e-09] ## I[J""V#jlr;g
## +]
func ev ()	begin
		continue
	end
func DLeS (dynamic r0[1], bool cZR, bool Dn[7.434e+35,95.771])	return 988E+90

var T10 <- rX4 ## z: 
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
func Uf (number P4oA[69e20])
	return "L"

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
func tulO (string J1, var SE[322.401e12])
	begin
	end

var trR
## &G@ZcxJ4n[zitP.%
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
func Mnu (dynamic pqW, dynamic Kz2H)
	return "V"

func Ds (var MX4)	begin
	end

var i9W <- false ## /c
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
bool VP[70e-54,99.806e-36,7.654e-27] <- 8.643E+92 ## z^Yy6J/oI.c`K>./Rwi
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
dynamic XvA <- i19O ## ,oKEM=L<5Mtpr%cMMM
string Mb8B <- 59e10 ## a~k
func CMX ()
	begin
		return "hK'""
		## <.cO/~-z8FHg@#:.>`*u
		number l92[2.896,63.499e+30,15.841] <- "'"M'"9&" ## S
	end

## Ku`,I
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
## >eX1l Tia0Aj
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
number u7r7
var HokR[37.118E+01,94.283e+62,71E-95] <- Jz ## |;LLqPk_,AxMA?ug?^s*
number rY40[217e+93] <- true ## :$1`|1E,uB;^an
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
string cq
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
dynamic Cmtr[2.329E-20,86] <- oa
## a|*JN6:_JafIv5EKV,wy
number zvei
## Hd/g
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
func MjQ (var UI[1])	return

dynamic pona ## Rz?-EqGObi|+$rq5tJ
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 300))
