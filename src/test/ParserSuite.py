import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
## ?I_-+]_
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
func Ry ()	return [- ([not false]), Yz8]
number pn0Z[309E+91,2,4] ## a/I^$7f:c^9C,2s
func np (number Rdy, var ROU[8e+44,86.003e70,3.091e+48], bool ufN4)
	return WUw0

'''
		expect = '''Error on line 4 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
func zkWA ()	begin
		tiX("F")
		## ~R4u ^5
	end
func Ulg (string dEs9[2.246,4.370E-89,23e38])	return

number pX2i <- 2.445
func KBVC (number qs[9,4,4.099], dynamic FjWj[278e-70,9.229,61.536])
	return
## `+3sxz3r8z
'''
		expect = '''Error on line 9 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
func MVvg ()
	return
func VX7Y (var Ew[77.971e+72,51,152])
	return
## _+,9n!>G6s6WhyD<MvX
dynamic jD
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
func FZlT ()
	begin
		for ux until false by "'"L'"'""
			return Z6OG
		continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
## +&Z%x^%1pAP2K+
string pLvK <- false
func OOZ (bool Auu[6.354E50,814.578e93], var rS)
	return
## eN5)q{:2wwA^g-=XjRo
'''
		expect = '''Error on line 4 col 41: var'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
func RiH (bool RVG[85.327E11,165E57,986E+21], number dK7R)	return tEsR

func ABZ6 (bool Hl)	begin
	end
## D]
## X
number P0[78.511E65,5.106]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
var SDw <- 8e54 ## [[9Eb(Lz,VJf
number YG[504e47,88.376] ## wQu~6R
func uq ()
	begin
	end
func QT ()
	begin
		begin
			continue
			number r4st <- "'"'"-O'""
		end
		## O
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
var l63I[9.605,66.419] ## <9)19*&l%Q*;V4UH;O
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
dynamic zGxR <- false ## kS^L
string yR <- "J" ## >
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
## _YV}
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
bool QXs[79.255,92] ## H4g@<;Y/o2ylj@ME6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
## nC
var hfQs[181E+35] <- true ## 6HLfJ6a4>1;MB.G9r
number zmoa ## )VXJM
func QMPw ()
	begin
		## 5f:EL9S
		Eo9 <- "U1"
		dLMI()
	end
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
bool hV[95.522e-69,50e+29,671.262e+17] <- true
## L!na<V"4YCB&:B88f
number uYN <- false ## T`Hn(zLfu= 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
number d_[23.290,0,416]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
## "Bp>u2-/jCvH
var Vv
number NUC[467E87,54] <- ".'"'"'"" ## fjO
## cPsbkxvf~bs`0
## )lhcVvV[~@sNz#40
'''
		expect = '''Error on line 3 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
## BzOD>AZN&@PNwS[
number ZkRt[96.621E+29] <- true
func ScHT (number hmR, string t3H[307.993,19,1], string NAy)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
func cgRN (number vro[4,443.085E+26], number aH, var zH1[21,1E+83,52.766])	return

## ~AJnQ?NKtiDX
func HC2 ()	return true

func UWDB (var qZv, dynamic K2LW[3,7])	return

'''
		expect = '''Error on line 2 col 49: var'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
## kZk#?>rBb3lj
func WI (number IzNZ, number PzI)
	begin
		## j_|F3bsU
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
## |r3,W,>R|7OdeIv{5(
number lzo[688E+99,386.590E13,617.652E-07] ## RiZB8_^b
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
func R0e ()	return
func GOg (dynamic w3G[21.447,2.184,6.743])	begin
		if (8E-06) begin
		end
		elif (983.634) U7qx(41.643E47, b3, 2.621)
		continue
	end
## sh"bPUmkkR<h3`"&7?q
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func acO (var j7M[475.716E-22,495.873,7E-17])
	return

func xV0s (var IN[7E-21])
	return
func g3ha (bool MK2[22.037E-31], bool Qnw[158.858e+10,21,301], string Pgi[11.240e67,7.730E-64,1e14])
	return

func bM ()	begin
		## 1:[$;w@1
	end

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
## vs`i_7>RCw,j;G
var O2d[3.025] <- 4.768 ## BK->b
func oz0 ()	begin
		## $X} H^Y<LBI997)x5
	end
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
bool FA_p[8,1.237E-97,94.261] ## p35%&>J
func QXVz ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
func gpsB ()
	begin
		## e PVkOGv?
		continue
		## c51PCPmj|p,!{
	end

func hI (number m7[44.464E-10,63.781e54], bool bCIf[92.336e+91,3e+39], number YTu[2.723e+10,6.448,86])
	begin
		break
		break
	end
## +nm$s
bool acCs[3.369e+11,46e67] ## g/RwXvB2XLncV2o
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
func zm (string OKM[4.423,86.824,5e83], var wh[359.883e98,7,820.154e+86], var Q5[3E+35,8.196,25])
	begin
		break
		return true
		for DjK until false by crh
			begin
			end
	end
## B]2/l{$Z!`;
'''
		expect = '''Error on line 2 col 40: var'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
func jJ (string ta35[8.202,61.083e+19])	return
number mlR <- IE ## Kin"J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
func a2 ()	return

## UrR:@`qk
func LC ()	return 39
func IY (var bj[41e+78])
	return
'''
		expect = '''Error on line 6 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
dynamic d4 ## &>?
## jsq#qY
## t#qVR1I8`rvm
func lG (number Yfkz)	begin
		## >[]cAbJU[mK
	end
bool Ux
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
string rX[3.385,75]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
func aydf (var ZBR, dynamic AvC, dynamic AFH[57])	return 888.542
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
dynamic rlb8[803.148] ## TB=cv=G/X(|%Gp"G=vm
func jwpK (var pzz[3.198e+60,13.747,222], bool TezP)
	return
## S!SE0!
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
dynamic XFk2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
func oE ()
	return

## |[)A
var bDi <- 875.079 ##  K/l
dynamic PkP[3.232] <- "'"?"
func hb (number zjv[67], string X7)	begin
		## EDSAWphLt;20
	end

'''
		expect = '''Error on line 7 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
dynamic Po[84,8,74.906] <- "<" ## mx_W*&TMbaQDUkh
## mA5<
## 1a5
number Bb <- true ## WLUWDLPsRA
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
## yqn9]03Td
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
string G7x <- "H'"65." ## R?`P3f Uet+0|q
func sr (number NtwE)	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
## !-N<@0T71eet!$KIrS0^
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
string R9s[450E+74,814e-48] ## u:+idf<N10La/oCK
number oFKu ## ;J,~ph_ogB%L$2
## vv6:#&f=Iz
number Gw[23.119,7.622E26,702E+30] ## Yu5"zYrj~!rVg5U,E0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
## %Q&;s^EA@B&mFhec6
string FkzF <- 502.441e66 ## ;P+AZ|ZwzR7NwiQ(pP2
func F9ty (dynamic hgb, bool Hyi[852E65,49e-50,4.536])	return qDzA

'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
## :v p?fg~@m5d`k/Z
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
func zuA9 (string VT, dynamic ZO, bool HTnH)
	return

'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
string HvR5[7.512e76]
## /K:Ey4[S@"=e
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
## ?z4^m7l
func dBFG (number bO, string DVTh)
	return "'"s'""
func PyM (bool PWp, dynamic Ek6, number ct[17.251])
	return Hu

func zChH ()
	begin
	end
'''
		expect = '''Error on line 5 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
dynamic U7qb[863.095,83.470,906E+92] ## (>s;R[+6E$%g|@I`(J:6
func pf2 (string OpF, dynamic Z9zi[312], string W_[640E+19,2.555e89])	return
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
bool SB <- true ## D`ba(g75yef+ty=l3
## xt[X&13i_7P_Y63|q_u-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
var kL[85,4.749,22] ## -C2GrkA_lA2T
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
string MX[29.447]
## TI@Vd
func s74 (number L0cU, number f42[67E12,0.036,56], dynamic GWi[982e-17])
	return
'''
		expect = '''Error on line 4 col 51: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
func pSvP (string ub5l, number LSmj, number cCD[35e-94,159.188e+80,2.744])
	return true
var vb[807.324] <- "s"
## 0rs(R]Jan3
'''
		expect = '''Error on line 4 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
func XNgg ()	begin
	end

func ELas (number swQN[3.689e14,16.954,41.440], bool rKBq[761], bool Od[178.053])	return

func qVQ ()	return rAO
## -eZ`UXCdmRJWz<..w%
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
number AKv[3E-95,315.658,92E+28]
func o56 ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
var Inb
## l
func q_k ()
	begin
		## 7pTn$xgwr.E%>`Y"S
	end

number Ah[56,43.004e+13] ## ]owka d
func wUdi ()
	return

'''
		expect = '''Error on line 2 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
number yj3[80.970E-01] <- er
func Qqs (bool Ap, var MX)	begin
		## zrNV<oN>*us&ERBp
	end

## gyDsjQQt=F@
var ajCV ## eZ2[dd)GL5?vDzfaq(h
'''
		expect = '''Error on line 3 col 19: var'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
func K_W9 (dynamic hu[4.637e-62,7e87,5], dynamic mZr[0.417E13,708e+29], bool Bcz[24.723])	begin
	end

## 2?/,zLb{x1U
var Lw ##  n?F5aycW>$1dA[6f|*
## /s"LJHp]"^8U
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
func hO ()
	return 479.018
number cfJy ## z$L`B3.Vi,U:Eb
## ?T7%$32JNv`p
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
string X4P[45.226] ## !C`EN?*v
## v(TcSZl!QMJT_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
func fzzF ()
	return

## Rp%tt[q~L.IfMxT RO2u
func kGS (bool s6, bool mnmG[56.958e+40,58.886E-95], number Loj[9.531,5.369,10.290])	return

func Onxj (dynamic pyg[6,75], string fr[517], dynamic Mf)	return
dynamic KQm
'''
		expect = '''Error on line 8 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
var xce[1E42,0] <- 9.812 ## Mnct.]h<^[pH
## ".T!=sm<,WL/w=c@b
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
## U3[Bz:~dF
bool zcz1 <- false ## bJwRY`%ROhRFt5t3z
bool Nekc[48.129] <- noNb ## [_RYLa[4ed%R-e,D^,O
func Fcph ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
func K1y (var FC, number w8o[48e-58,8e34], string cWZF[42E57,3.344e71])	begin
		## "*^~p5]KE-A3T
	end

## DQ`
func zk3D (var Rm[44.829E80,3.645,712.429], dynamic CmrG[4E44], bool iF)
	return 4.323E-98
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
## - lX|W>K5$)pUM
func Lt (number JOf[280.846E+23,5,57.862E76], dynamic uli, number Yjw)
	return "'"y"
func Ko (number OG[2e36,2,26.921])
	return

## n}y
'''
		expect = '''Error on line 3 col 46: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
## (.$#+X}%StM
bool ex <- R4 ## af$_gdN Rr5G
func f9mX (string z6Zx[0,97e+01,60E+27], var Ks, number Vw)	return vji

func ZYQg ()
	return false

'''
		expect = '''Error on line 4 col 41: var'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
func NfW (number L0v, bool HA)
	begin
		begin
			break
			for jT7v until zB by true
				sX("'"lK'"%", "z'"'"")
		end
	end

dynamic jjE <- 874 ## )|ckWgn9DzF"|Q.v8G
bool Kf[32.872E92,132.898,36.028] <- 184.527e-57
bool JKD[68e13,34E-08]
## !9>"O"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
## O8dIvYu
func dTt (dynamic Ipw, string pyv[44], var vcn[974E63])
	return dd2Q

func fl (number da9[969E+34])
	return 888.770
dynamic Fd0[3E07,561.671,0]
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
## F{+#|%->?r8p8{?"&S
func NqB ()	begin
		## LG?bxYfHw2r|v
		number nxH[81e+27,2.392e03,37] <- false
		## `0~Q$w_PR}t./"GX5w?
	end
dynamic EK
string N4UR <- "S'"R'"" ## w}2N~&UQ:bLT
string g8t[799e-60] ## m;+u2*{8L7:X3UdG1 $
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
func wRj (string DrBN[909,1.082])
	begin
		bh(true, vs)
	end
## 7m}`>
## o~{I27O7D[bd
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
## )xI
bool hHg ## `5^!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
dynamic oW[2e+25] <- 6.561 ## @;oB`1N="7
func qf5 ()
	return

'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
func tt (string waj4[899,2.864e+07,27.074e64])	begin
		begin
		end
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
func NDA ()	return 837.428
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
dynamic k6 <- true ## L?WB
func j8 (dynamic pG, bool rgyn)
	begin
		## J^$MTqHH;n`|r%(E$]
		## dqV%$pssy.dLW=@
	end

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
## =P.U
## Y:_V{+>Aiv6*o_W#<
string tZgA
func LjU (var Bwh, dynamic fMp[10.423e-79], string ux)	return true
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
## w
var iz <- 6.609E-46 ## JIytgr,yRRqtuYn
## BeXgOxM.^[v"+-[s=6
## 9w;piBY8)(jD?+sCLVg
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
func x8z (number rk[26])	begin
		## -Cq
	end

bool Qic1 <- true ## )%tSHC_&_J#qSRES
## Nc
## c%LnOIieFTa[
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
func fvx (number pk, var VL6C, number He[172.420e-30,789e+22])
	return 82.408
bool Ezs <- true ## =(
func d_s ()
	begin
		continue
	end
func SrqF (dynamic Jy, string C3, bool Cr[83.613E-71,7.954E07])
	begin
		for nOA until "t" by joDn
			begin
				if (b5)
				break
				elif (true)
				if (z6ak)
				begin
					## gS."H Z1T!*T
					## CDon
				end
				elif (Pmh6) for jZ until Em0 by 4.094
					begin
						## H,=BneX!(J7r&
						return true
						rQR <- 870.318
					end
				elif (298E-11) EL(3e28, 23E63, false)[244e22, uH, 30.731e-15] <- true
				elif (false) dynamic zz9[43E28,0,2.207]
				continue
				## @n
			end
		## Rv!3}ojb<tc;RUjE
		break
	end

'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
func tiXV (dynamic YB)
	begin
		## yE
	end
dynamic yZH[48.464E+54,5.017]
func QMh (number nGV[0.820,729])	begin
		## 2nR2|[DDkJOY(xZ
		## pl`
		return
	end

## JiS/i)bT"Bd"JPKE%~
## I],/!$3lW*-f^
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
var MLiH <- false ## Fje`/?GP<D:+e
dynamic gU
## Y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
## LhTTSARw+2
## ;r>th+i#v>HM;rUpzf^2
dynamic SVDh
func LOR (bool KU[8], bool fE[437.015e46,23e-16,5e33])
	begin
		raqZ(3.128, vLG, 804e+05)
		zC0(fv, U0kD, oHYm)
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
number aFWq <- false ## *pWNEJ/
## pr`0zar}nc%28^z+[a~
bool pYTd[96E+82,7.097]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
dynamic LYX[3.993e-93,8e+14,560.792]
bool ZqxQ[7E-29,47E-68,72E49]
## ~S*wX
func atU ()
	return
dynamic Y_w7[35.734,8E+02] <- 4.134 ## 0./*|Q6t
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
## W;x2[sqvmb[v
func LM6q ()	begin
		## 9r)uZwiS%?0mg(
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
## AN
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
func oU (var M8xj)
	return
func WTU2 ()	return
## OsJAsDU2!a[//
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
func Jqu ()	return "'"'"I'"M"

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
## w?#=9T0v[ao4t_g
var Tl2i
## UW*q !6i7I/Fyf
func XoXh (var lUci, string gACv[9E47,32])	return
'''
		expect = '''Error on line 3 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
dynamic Sm ## +W
## fx%KeR>Y)0*S7T;c
func P9 ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
## uo ra#J/r%<
## l)O8}y2_.xhkj)52iF
dynamic EMV ##  5Z{4k~A
## K2P
## vw>kzMxYZT,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
func Am (number E0eJ[84e97], bool Z4qT[45e50,3.320e-82])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
func rZ (bool cmV[81.680,37,21], var S3P, var eNsC)
	return "'"Q"
'''
		expect = '''Error on line 2 col 33: var'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
number ox[36e-11,943E-73,882] <- 4.540e-21
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
## 9&`)M5W;FU
## 7[dQpMzGz#,=WmndN]I
## M%H6_l3W<d0"e
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
var QNMx[228.307,5.455,9e+35] <- true
func Qice (string xf, string QPAR)	return "'"'"q'""

var Ht[764.001E53,90,133.873]
func Pgl (var chcr[69.724], number v3C5[462E54,760.411])
	return
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
## |@
func czxY (bool c6p, number N36b, string KZo[43.076e+58,408.909E+56])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
number i8[2e+26,11E85,16.290] ## #u~
bool z3[49.010,3E+01] <- 36 ## ;]h,8X>zxlQfjVlmE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
## .vWZu/R,q1
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
## f9>>,Q`?Ek?
## )TipTVYN9j=pBKQc
func zvai (number eQ[0E+52,292.685e19,1.788E-82])
	return Wiw

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
## 3<$8npfuAXD
func GF (number BTS[0.278e04,57.908,9])	begin
	end

## /QAO:
## ypY7Fnj-C*h0E+^
var Qual
'''
		expect = '''Error on line 8 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
func Ggc (dynamic SyZd, number xsl)
	return ph3

func uohy ()
	return "X"

func ngo (bool Y71l, number tSJ[994.940E-43])
	return

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
func mU (bool g1[40.497,2.082e+45])
	begin
		vPW(true, 677, "'"'"3'"'"")
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
## ^D
## 4N+T@g
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 300))
