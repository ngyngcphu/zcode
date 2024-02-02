import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
## ~rQ(Ccu/}b
number rnMM[263.708E20] <- l2(rUr["'"uw", 5.982e89], true) = "'"t{U"
## ^5I.]d
## sY70{T8
func Kj ()	begin
		## `qFJ
		begin
		end
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
func qkO1 (dynamic awZ[6.882E+92,73.718,83E-93])	begin
	end
## gON<8T)7f9orju{
dynamic R2l ## e5S:_O2SrE=mceFO01_Y
string VR[63.180e+88,0.901]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
func Tg8I ()	begin
		## T_z*w"x(&eM1L=X^BCd7
		## |msfL
		break
	end
number vh[892e-84] <- "q'"" ## vKaRgC
## yZ=,C
var HNV[50,7e-13,4] <- 487.704E+03 ## /(/p%affo&A
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
## b=TH5A3wShN)zBQzTYL^
## ?@lNtH(T2*XRBGXL[
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
## ^n.QAR#]]J
func lYrV ()
	begin
		## ZU"2]I
		## ^I<^`m&PY=E>nV
		## cIKttFc<Dam%
	end

string qdw[825.802,25.007E-89] <- CUxp
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
## h)z;r)
## lOO(M/0[!*Og/$249W
## bn4W3hW3h!~gvhjR
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
## 4K?T-e9dBZJv9
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
func pj (number rXK[70.404,534.316], string fA[593E-63,3])
	begin
		## qDuwq7s@w
		## |gA"~v)r|5.?K66qu
	end

func mhf (number MQXr)
	begin
		## tgKjOZ"
		## xs
	end
## S=3@9P2pWnG!7!Mt? y
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
dynamic fl8
dynamic zf1e <- false
var CVqt <- false
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
## Eb-mfN
number ii08
func jq (dynamic S5[717], string LaPp, bool WZ)	return
var iNnv ## lyM!3;x0QK
## $7cTiJu&XZ`X5uw
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
## H]D_LEuFI!]"M
dynamic j80c[82,366.111E07] ## 1YzJ
number AO[35,95.624] <- true ## ct]~H]5CMVP3K76uwQ8#
## mK?F
func hG (bool NIB)	return

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
bool uFp[4,545.100]
var LTOP[4,366]
bool tre
bool cu[70] <- true ## ([66a7KA]BQp{PO:^ 
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
func ZFIA (string Z52[863.824e03])
	begin
		continue
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
## $&$Sr)CW
bool ja[24.294E71,33.409] <- "'"gu^"
## jDrd
func gEB (var kNiA, var bdv5, dynamic T9r)
	begin
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
## R/
func r9 (dynamic LEak[157e+50,9.464], string TU[821.938,2.990e66], dynamic N9)	begin
		h2(true, "8'"?y", 5)
		## )m[z
	end
## M>FX
func XZSs (bool yaDY[97,4.385,6.619e-66], string KLb[6.977,6.145E-30], string xYZY)
	return
string urkk <- false ## fHZE
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
func hO9 (dynamic Ra8)
	begin
		if (7.454E38)
		break
		elif (false)
		var a1Ej[583e-28,42]
		elif (lPt) continue
		elif (Te) return 7E-41
		elif (d1Y) HLoH(true, "'"'"'"M'"", w0m)[42e+96] <- 736.941
		else var Eo[446.673e-12,637.629e44] <- "oj-" ## 2Kle
		continue
		## +
	end

func i007 (number kJON[74E-62], string z1j, var dbE)
	return
func hGr ()	return false

## ^
func JEx (string G8mu, dynamic a5vO)	begin
		zz()
		string kHr[18.542e-46,39.755,97.049e+86] ## MyeDeY,Ewh9A
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
## }k(4l_Bxg2XvS
number b5[802.401] <- "@'":'"'""
func g7 ()
	return 542.926e-02

number JH ## gE6y}^{HNcdf1,j
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
func vHQ (bool JL[41.855E+48], var qtP[10], string ZS)	return 8.611e-73
func GnT (number dXx[9.827,6.999e74,553])	begin
	end
## MRHt#X23 ip,rm9
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
dynamic P27m <- ojH
number rFqG <- 3 ## !XB
func YO0 (dynamic gyF)	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
func cUV ()
	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
func qgJ (dynamic UcNt)	return
## #QqF4Zhre-WvL
## zT[
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func TK (string op[74.918e09,41E69], bool jMkl[313.966,0.983E54], bool nC[623.976])	return

func mS (string xF, number gDf[2.212], dynamic YznU)
	return NmkS

func QuDF ()	begin
		## |cJyQ&.*Se
		E4(28.902, "s|'"'"'"")
	end
string Gvc[8e11] <- 85.431
var ANY <- uM
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
string Oq
dynamic Tli[0,93,3] <- 694.236E-00
func ZH (bool VjQu[9e+10,69e62,24.325e+87])	return
string h5[93.912] <- SV ## .d>{.MMPwI9{bR;K9
number v52[7.872] ## ^$D?bSte~8-7PaRT%S%W
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
func qsn (dynamic dOgy, var kM, string yGY[104.684,5.545E+80,162.666E36])	begin
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
var MI6
func Vkq ()
	return
## _C-G
## [3Q&H!%sJ^
## (2ryk4=K._
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
bool p2F[9.546e48,894E+43,6E43] ## L0ZgrW:
## jT
bool cy <- " Nm['""
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
## t6Tl1:&O
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
func Mc ()	begin
	end
## v
## 55
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
string Il[4E89,91.095e91,3] <- EhZZ
## X`|
## ;hk}&xv>aMz"]/DXh
## ZDR16hA1&z
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## V,7HR~O#,l1%U*
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
func Rau (number Od3[88.836,48.053,79e+44], bool lVz[988,921.416,15e62], var aqED)
	return 8.454e51
bool Fki[235.877,3E+99,5E-67] ## >aEB4YvD?N
func Z8 (string Mn[52E+05,31.168e+69], var Sfb[716.576,5E-84,361], dynamic RNX)	begin
	end
dynamic Fcb[8.743,4.921e+38] <- xs
func ic (number YSh)
	return

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
## E>
## AzMY1(p!
## Voae<:B:Y?&m
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
## V=t
## eaU:_k
## {eg&
## ZchL({O3,%1){;3
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
var Vkf <- Xl ## <Nk)c.^J;wxoHbQVF 
## *bRia
string zPE <- false ## B&b2]3`~i$
func Snc ()
	return true
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
## L^2q`KXMz<G1`z&p
bool JBzQ[573,57.026] <- CO1
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
func fS ()	return 8E-62
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
string Zb7Q[51.921e+16] <- JQ ## #1MqZvT.,G m
## dxNh7}(
dynamic UC2V
number WZ5[2.036] <- wYY ## ;3*B/SeM
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
dynamic GXVQ[93.526] ## qY)_1Q!
## mLN<wf.o2y7:s
dynamic LO[4E-20,190.117e67]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
## n~#R"%
func tZ (bool m3l[717.683e-40,27])
	begin
	end

func eCB (dynamic Hf, bool CoBv[759.605e-97,38.667e79,7e-30], var ABF[8E+80,63])	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
var RA[310.482,0E73] <- true ## *_#t2rKiaqsGd{
## PmVO.Z(2m]<
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
func PhYi (dynamic REO[33.581,58,533E-02], var xK, var WJs[881.713])
	return
func Rxep (dynamic y5s)	return
func OIgl (var XvQR)	return

## ;5(pb&2 9I{F<Q
func YZw (dynamic sm, string n7CD[59.320E+78,779.035], dynamic ts[0.228,0,414.150E-18])
	return Kjv

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
func Zxj (bool EXL)
	begin
		var Zq <- false
		## &[DRZH]3nWZ
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
## ~
func Jb (string Rj, bool cW, var nQ4M[9])	return
func X6zL ()
	return true

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
func sx5 (dynamic f_5, bool r23[2e+77,66.161E75,3], number XRh7[1.172E+87,19])
	return

## mzKH
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
## <S= 1E)w]X
## -iI|cntz^=R
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
## n*&2j
string Cwl <- true ## ;
## Kwg=/wUwt>G
func nK ()
	return false
func twQ (number UmEK[218E+64], bool pV[7.949,193.347,42], bool Wmn[6e31,6e-22,431e28])	begin
		begin
			## XqK=822-?
			if (true) break
			elif (true)
			return a3
			elif (54E-37)
			string j_E1[9.133,744,8.640] <- xR1i
			elif ("F")
			OKI(S4J, yQ9)
			elif (281) for agoL until 5e88 by rT_E
				for XT until "'"'"'"" by ZXs
					W68W[true, 189, true] <- 90.904
			elif ("'"")
			for c0f4 until XP by "<{NB"
				begin
					return 69.027E+45
				end
			## n:4nBb{f+%$ rU^{F[P
		end
		sn(false, Jo, "'"'"'"x ")[UB, 428.866] <- false
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
func hhWY ()
	return wVvr

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
func gG (bool upXl, var B7[2.123,169.434], number r29[616.810,431.235])
	begin
		sH9j <- true
	end

var gAbR <- 239 ## _=`fI/qheMv
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
var BJu[8.968E-56]
func CMa (bool RBoa, number WrZE[1e30,59], dynamic sq[34.641E-60,797])	begin
		dynamic LhI ## %e~
	end

func IoHU (string HlI3)	begin
	end
func r3LF (var oU, string ox[92.243,5.523E+93,15.721E-52])
	return
## $/TOm~H$pE6AlaJj
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
dynamic bV6W <- Mcun
func dY (string O7)	return

string IUu4[124.675E+49] <- 0 ## gg7&q|1VKgp2+qi79d
number mE_S
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
var MlZc[4.550,3,890.152] <- F81
func umE (dynamic TxEQ, dynamic v48[66.037,24.390,0e02], bool XVAF[12.702E15,96E-85])	return 382e-67

func dVh (bool F1s)	begin
		return
		## QVUkmgek(]m>
	end
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
func b3 (bool nuQ[736], var rh[98.253e-28,57E-52])
	begin
		for YGkM until "'"'"k2'"" by "'"'""
			for tk until 209.411 by m08t
				WE(48.456, "H'"O'"-", false)
		for iP until 595 by 6.244e84
			break
		break
	end
func f0 (string eG5[8,9e+33], bool A31[853,34.612E-53,0.469], dynamic QTz[65,53.210])
	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
func YE ()	return

## !(3$A3Gp$47%. 
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
number HS5[459.334,3e-56] <- 6
func b9l1 (string ca[2e64,461,941])	return

var Z7L <- true ## pEU2wLLIb)_w:!NL]m
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
## W
dynamic ZA[1.440] <- true ## 0zL,Ye%e8I
string o8r[43.516,86E97,562e22]
func PL4 (string rPC[4.250], dynamic iEL1[75.373e79])	return bPvm

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
## "a]2v@.m:^Qvq)1L
func dn9B (string tmX[103e40])
	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
## z^qm5D"g!iJ(o
## 9AaV_pe?Si8=YN
## *-%:rym?*g<kF?
## >.RJ|:
func kt ()	return 98.207e+39
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
func qAee (string ZsvX[764E-76,29], dynamic YFJ2[35,62.703e88])	return Pkg
## u8$_Nw=>f"O{f9k>
func pRw0 (dynamic Ai[69.500e+67], string ZkX[51.890,661,697], string QHO[309.937e+57,719.415])
	begin
		## `!Sl9djoQ}-w@px,T"
		## 2MBjAbf@[ )}
		## K&z,KT)`$&khE9/Dc6
	end
string UJ <- l1s
number xGt[5.679,164E+75] ## gF1&ORf!7[v:+$%)
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
## B{$
func xN (bool rP, dynamic hnXT, dynamic Pw[11,324.379,65.697])
	begin
		## 7)xpwek=|Q[s(58]vsL`
		## sE=eI^
		bool UNwJ <- 889.595e22
	end

func jTNi (string HcG0, dynamic ZKas[411.469E-81,251E54,49.192E04], dynamic u6k[4.610,3,39.585])
	begin
		## ^SCHwJYt:?feM!y.]a2_
		## F
		## mzb^,p?wavDi
	end
## nBsdVo5$9,9
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
number Vlc[63.273] <- 857
## H
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
## DeOEY@(JM|x{whacuY&
## 1]f<LNkqf v^udJ0*Y
func EO (string NMrU[368.798e08], dynamic Se, bool saF)	return

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
func dh (dynamic rvD[7.554], bool gZ[81])
	begin
		for b5 until true by false
			begin
				## FFi;mdYLN6R7F"2Y
				continue
			end
	end
func o3 (string L2TX)
	begin
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
dynamic TuG <- false ## ONb?z
## 0YbO=,H{[
## kb-P/8SSNWI8
bool H6i <- false
var tF[2E17] ## CT~p.`Or`Hw
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
string l9cn <- "b" ## eTjA 
func U8 (number nfxs[4E09,460.078], dynamic X2H2, bool Rve[694.512,3,431])	return
func HdX (var Jj5[56,5e95,498.150E-03], var m3DM)	return true
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
## G
var YJHP[1,95e+02,90.573] <- mI
bool ew[3.202,6.037E69]
func EE94 (dynamic zau, var lBZ[68.135], bool h3xO)	begin
		## OI%?G,-V $vH]0/[F
		Nn <- "'"'"u:'""
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
## ^}$"y{#)eXX/I_Gm
func aE (number XUi9[37,8,49])	begin
	end
func lqS (string mDF, var DtL, number t6j[5,60e-32,10e62])	return

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
string Dv
number fN ## u31!]]g8P:kl@_= +
## *O41mY VX G/2
var AM[5e-74,6.213E76,0.943] <- "'"zc)'"" ## R
func SA (var vq, number eJ)	begin
		for Box until "'"'"'"'"" by false
			continue
		string kjRi[8.716,8.549e+52] <- true ## RYqJl/+1DK0nrq}]95
		return
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
func SvX (dynamic aWX[346.617], string je[2,5E-96])	return true

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
## 4Ca0"5o
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
func i2qH (string nh, bool ioCw[9,53e-31,3.814], bool YG)
	return 8
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
func TP (var mFq[308.634E-14,548.766E+99,412e+95])	return "('"'"'""

func bcV (number iO)	return

number xT[260,3] <- nH ## )
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
func PJ (string RI3o[136.409E+50], var RtJN, var wO)	return jP1

func so6 (number ZDYB)	begin
		for Ovl until 75e+10 by "'"o'"('""
			continue
		GYM <- R5J
		break
	end

## IyglIjppD
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
## YC|Z-.Y"
## 5p~n`b
string XzUN[930.684,486e12] <- "F"
number f9 ## oHVR6jT*oD;]yRA[
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
## Dm*@re>0BvCkxIG
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
var E39b ## >Z!x1GW8Vs)}XVcHS
string MJ <- 7 ## H<X/__?U1$:/vs.
dynamic daQ2
func c4e ()	return true
func fu0 ()	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
dynamic f8P[4.841] <- "'"'"'"Y" ## I7?N.Ok
## qJ:zU}WTeBm/d
## xM
bool yJ_W[48.264E-62,12]
func BG (bool hssm[332.603], bool jl6[9.547E-70])	return

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
dynamic zr <- 876.382
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
func qQaJ (var Yz)	return false

func Nd (number sct[250,4.190], bool PVFd, dynamic vIh)
	return "w'"'""
## /7p(H~qV<]
dynamic Le ## 0hZJ#7>_a(jL#8ob 3J!
func quLg (string CY[418.083E67,866.569e+13])	begin
		return true
	end

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
string U7J3 <- true ## ^  bVx>2,4>%-yGt7
## Y K7WGH
## K0{P-:Oircd}D
string De4G ## 7Yr#
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
## jN*a)T5*
## KvB,S
string C4qS[1e+76,98,5]
string yP[12,540.443E28] <- "'"'"z" ## .fB3Y4%y5mudx3x0bN=^
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
dynamic Ge[425] <- "m" ## s*T?<;BWO7)s
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
## ma}y
## AWMPMu6
## &b2MIk1
dynamic kS[91.554E+09,239e+37,17] ## j-v6
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
dynamic fs
number NCYX[990e09]
## m
func XhvA (var yHc[35.268E97,2.719], number nLHQ[85.781e+27,4.203e+38], number a91[60E+10])
	return false

dynamic n8d <- false ## rP.Lr:`Po~`vn
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
func oBkE ()
	return

## wA)f1
number Fudw ## S(%tK.
## ,Su
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
number lc4b[812,45e62,467.184E-79] <- false ## xgh>A_I
## 6 o7OoyA@YJ$3?BN/^`
func Fy8 ()	return

string LNyC[748.208E+05,2,6e-59] <- 86e+53 ## Y?V@8}C{&sc~r1P-
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
func LvU (var ky71, dynamic Zu)
	return

dynamic c5 <- 7E-24
func gVPv ()
	begin
	end
func yG57 (dynamic e03, number D30[0,4.684E34], number gVCM[1.530])	return Hn
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
func py (var DZ[78,6e05,7.201])	begin
		## y|=#6h2
	end

number MmaO <- xh9
## K(#_`%.,0$-q9TY!{bV
## L-IM$8N
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
number BAF <- Wkw ## L)B
string LAj
func Dh ()
	return 2.709
## .6)Ws"/lcFgUznz]:/CN
string y6WB[1.744E69,211.567,6.562]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
## e
## XNDPn#+@P]M
## -3$6g
## #jXYho;=;,:_gmj-609
number He[737.499,32e-33] <- IYmG ## 6QIvhR8`8|
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
func GSO (dynamic Yg, bool Z1[74.493E95,4.234E-97])
	return Umt
func Kbf (bool JPI)	return
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
## k*Y9PLC]1)UC
dynamic xsp[458E-83,452] <- 556 ## x;qu1<jwq
## Y+l#f
func T7Lc (string wiL[53,23e-54])	return

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
func Lrw (bool uR[9.677,3,3.208], var tYp[6e+81])	return
func hY0 (bool eaI1, string JNHs)	return "'"iB]'""

var LG[2.027E+70] <- true ## |c}[B
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
bool L5w <- "'"A" ## 9!sbj
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
dynamic cff <- false
bool VTZl <- true ## ~5vBr_~CdSC6=]
func E5 ()
	return

## .j/ x<_tKy%/,G#oC!8
func ur8 (number Qydd)	return

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
## tMtg_W)%+"p4
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
## JDc7h~;:4
number Esk[5] ## iloD#pE]
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
string Mg
func CO (dynamic PL9[18,60e-08], var a6o1, string tM[8])	return
## -jWx-[Pbxz,#R3>u
## HuVTK&dhgf<zw&a)=
var u81[1.583e-98] <- YfI
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
func N0eu (string yAD, dynamic x8)
	return "'"'"_'""

'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
string yf <- 28
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
bool TvMs
## <uu
## i
'''
		expect = '''Error on line 1 col 0: 
'''
		self.assertTrue(TestParser.test(input, expect, 300))
