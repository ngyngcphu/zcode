import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
## {Xz_2
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
bool VQK[12,34,10.410] <- 18e-16 / X4 == "'"N]w]" ... "#'"b'"|" ## sa
func SYmP (dynamic F9q, number ELR)	begin
		return 931.237
	end

## 2 
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
## [3Dej -#
number iC73[5E30,9] <- TGDp
func kC (var Hd3m)
	return 651

func hL ()	return

dynamic LO[9.925,906.955,950.671]
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
func fubn (string LQ)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
bool t2[364.206E-07] ## {SC
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
## qK.q@]:NL.n]D>ve[
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
## #BW.(J:V;5O7Sok8O
## Loe{
func Gg (string U3[208e-91], var Gkbz[131.121e-93])	return false
string veyb
## +_$NdmX)qx3=P"hRQ
'''
		expect = '''Error on line 4 col 29: var'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
## 6]Q$po02pM!iCMBI|[
func Q2FI (dynamic Zq, bool Bm6[5,637,464], string VTvO[0E06])	return
## /6"0]{G;c 4~N@<7It
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
string H_4G[7.558E83,93,39.639] <- 3.677 ## V YtgXZ#I(A,4Z`
dynamic LkL[8.248e19] <- 28 ## SQk:
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
func Ol (var Tl, dynamic QlT, bool Cqe)
	return "+"

## A
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
var MRe <- 7.522
func pv82 (bool tup[67,204], bool aI)	return Ct

## N<y<O=af^
bool da
string SGQd[40.263E-71,330.118e-74] <- sT7
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
var ao[60E-72,87.007,3.593] <- 4.802
func SQwx ()
	return 9
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
## X:
func b8Iz ()
	begin
		## Iv0sy
		number KEtx ## NRRk ?O>LBft{ZZ
		if (DPqk) break
		else break
	end

func A_Xu (number tLb)	return
## e"[+N-C%1qxP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
func y_Cb (number JF, number mgt)	return
## t_>_Ns`U1iqG7
## dy,a [_= 
bool cSXW <- 542.825
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
var V17 ## 25+U=KR5@*>E>c)J
## q4Vei:%mg:y|
## ]PL
## L9
## RxgzjVW6q~L3,OM
'''
		expect = '''Error on line 2 col 27: 
'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
func qvS (bool Tj6t, var rSZ, var KYnl[0])	begin
	end
'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
func rCi (bool gg2[167.094,919,591.652], string pa2[241.540,790.224,62], dynamic V0gH)
	begin
	end

bool RE2[582e-70,70.730e56] <- 70
'''
		expect = '''Error on line 2 col 73: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
bool eg59 ## K"l<Pt~4bY/+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
## Y`5la)F5sY26hR
func rADO (string ByJ[6e-00], var IH, var q6[85.716])
	return false
## Ek
var QW ## >Xjz:~>.
var D4 <- true ## ?Ac(
'''
		expect = '''Error on line 3 col 30: var'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
bool ktM ## )gOyLEmkR2Pd=[.&.
func DL (number tZu[84,157.865e+01])
	return false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
number Mq
func fjvX (bool i9s)	begin
		return false
		for VJ until true by "U'"'"g'""
			Q4 <- false
	end
dynamic GXg5 ## Vx#7%6~2h
## ]y0`
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func sVh1 (var Eo[692E72], bool xZ3[6])
	return

## }h{N?FLq2i y4_,Q.FK
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
number K1gD[63.148e+74,4.858E43] ## `KH~M2c
## n[
func Bpw ()	return 635.153E-12
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
## Xf|_E)M1
dynamic Fi[2.355e-12]
## {xQn2vTP.17RF},ad_l
string eBu[3,6e-30] <- "l'"'"Wf"
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
func YyT ()
	begin
		continue
		break
	end

string o1e[27,40,3E63] <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
dynamic c0
func qa (var DpXO[133.360E-11], dynamic RFq, bool UtJ[864.557E+17,3E+70,927E+64])
	return
string LV[3.498e-57,6.232e13,8.127e77] <- "E_"
func KEO (string U2po[575.341,34])
	begin
		aTI()
	end
## #MCy8
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
## Y-K
## u9`eH<
bool Er[2.918e+22] <- xX ## :7104"=6F6i@
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
dynamic mw <- 64
func SGm (var uh3O[26.964,89.116,201.632e67], dynamic OC8)
	return
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
## Hj
## D~v}GlUJuJ,_qzq=O
## f;O/lx;]AH8EL6
func Rxc ()	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## a/_`
## jcF$^&k1
func L0 (bool J5[9.733,541.951e78,659.164e43])	return

func v_Qx (dynamic CfD[81.484E37])
	return false
'''
		expect = '''Error on line 6 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
func iP (bool yP[110E+49,90e+65,3], string u6Hs[451.116,656.366E73,436.088e06], var K3)
	return true

bool MoGF <- "'"^'"'"p" ## q3
'''
		expect = '''Error on line 2 col 80: var'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
var Ron ## qxPxX63cL*c|"
number aFl
'''
		expect = '''Error on line 2 col 24: 
'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
number fm ## g+rzd*ufQRC7Gc34>k
## ucfZ=O1V:U<
bool ZzSL <- c8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
func WXP (number FQ[7.626E-56,5e-25])
	begin
	end
func PncA (dynamic MK[266e-65,92,0])	begin
		## <&=9Nt"?
		if (789.330E-40) if (UPf) je[17.023] <- 14
		elif (205) begin
		end
		elif ("y'"Y") return
		elif (975.610E+48)
		break
		else var oqb <- "'"lQ'"'"" ## i)k#JI~I
	end

dynamic Ogrh[978.925]
## 72).Sgu3mhsA+hf_bf^
'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
## R,4q5I.MnnCyy:C_M
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
## <B^e~a[%D_l/w:n,~8u
func x1 (bool NN9, var F1E_)	return
func lon (bool os, var Fb[91,312E73,722.098])
	return 337.373E30

var kCg[82e-15,229.393] <- rO
'''
		expect = '''Error on line 3 col 19: var'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
string pViM ## z
string kc8V <- 1.417e58 ## {tO
func dUj (var owjd, string jzyq[1.592E+13,297.483e41], var Vm2)
	return
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
## B1N1&)J
bool Q7[41.185] ## vsDOH
## 8AUp
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
## nPnX"AE)}"OM
var Lq0F ## 6P((J
func JCS (string OQV, number D2rH[9.737,9,219])	return
'''
		expect = '''Error on line 3 col 17: 
'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
## ^GYH;ej
var et7[530,599.404]
var u4r_
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
string RR[9.537,55.285E09] <- eA ## 4=M|$>oKTET]5|b%
## G1J2Zmr"$6GITYl`
func q9 (string kgG[9.126e-31])	return eF

dynamic AgXs[36,83.866,96.525e+44] ## -k[(
func qxZ (bool bRBl[933,706.974,11])
	return o0
'''
		expect = '''Error on line 6 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
## )dI_|5?3|;UMd
func R7 ()
	return 8e+58
## ?l1 fkp&ZN=[2+7o
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
bool fS[1e+68] <- "'"b"
## F)|?<(0eJ@virKY[
## o]o<>HD%|r
func cjK (bool pIJ)	begin
		## LjAKg_(JvTf Aga
		## Gi.L`a(
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
func BA (bool Y8qQ[925.128E+51,27e90,820.267e-51], var f_Y)
	begin
	end

string V5Bo[1e+84,58e-96] <- "'""
func V1_O ()	return
'''
		expect = '''Error on line 2 col 51: var'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
number jl5[5.338,885e09,405] <- true ## ^u_agl|8ak`=zB/qk
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
## 3~
func lX7 (var lXC[155,1,83E45])	begin
	end

bool e9GI[9.120,8.945,609.940] ## ~Qh;~M`?:
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
func bsce (number a0[6e01])	begin
		string XC
		begin
			## i4:,5Mp
			begin
				return
			end
			begin
				j03 <- "'"'""
				l27(TtlD, EBf)
				## u7-%82BR*T
			end
		end
		begin
			## ":UvZ#R*P5J
			if (true)
			string rr[53e+04,79,30.210]
			elif (5E-93) continue
			elif (36.746) jg[jG, WtNv, Uo] <- " "
			elif (false) return false
			else begin
				## <a.D&JjcGOqx1$
				continue
			end
		end
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
## j,E;c[" 1Kx@]k<%Q
func SH (var YuvM[54.946E09,3.026], bool O1tX[697.246E+12,50E47], dynamic sHc_)
	return

## Bl7#a5GhW2`)qZr0~*
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
## (|OO5
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
var bS_[674.203E-22,3,395] ## x
string xnl[6.321] <- 0.081 ## Pv+iSH
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
bool dmk[87] <- true
func FF (var bnDs[7], var Li3d)	return 4E-29

## 8MQ)"Q7Z|$O!N,=*
func C2Fh (number dYVY[68.843E-25], string h_[87E+42])	begin
	end
func WJ (string Zp1D, dynamic P53)
	return 10.284E63

'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
## $cQXuKN
## kT&fa
string wW <- true ## I8&8Pd7*dC{Mo$Igx
## }I^PI"PT">kTM[Ov
string JlrX[48.722E29,2] <- yPtS ## =&QD6;?[~H=}Ke9UW+G
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
## h
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
## 7/J^pL{z@~q!)
var my
'''
		expect = '''Error on line 3 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
func ELC ()
	return

func dVj (string mQRs, bool w8_e[6E+83,481.563])	begin
		number NBE4[1e26,15.734e82,43] <- true
		## WMx,_u/+exa
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
## AZdJ3A
func vU04 ()
	return 8.636

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
## L[]X9],{CN
var iZR[1.929E-81] <- true
func hjm ()	begin
	end

func kSTp ()	return

func ku (number yKFr)	begin
		continue
		## ^t!I.kydAh,U)qy~s
	end

'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
func ipW (var FH7J, dynamic Cp[7E14])	begin
		## mJX@rnn
		## ?5}GESQf??z/bGjc&
	end

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
func jc (number NT, number ubum)
	return

number ph[967,231e24,2.146e+47] <- false
var bDj[57E-60] ## )SbTC4-Hyk"~F ;*95XQ
number HM[73.136]
'''
		expect = '''Error on line 6 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
number Sbw <- "'"%#'""
func UDg ()
	return 438.013
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
func c3y (var zJlo, number tqf)	begin
		TZF <- true
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
## A
## [&]plWZlwnI<
func HSl (number WkY, bool VfaA[52,215E-96], bool X7M[228])	return

dynamic o6D[5] <- "'"l'"'"(" ## BxN[| $[8 FBm7*h|
'''
		expect = '''Error on line 6 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
## E.3F,UR]M11c"^a%39E=
func wR (number XaS)
	return
## ;)F1:o?|y{YoAgL 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
bool r1[2,14.475e-92] <- 837.968E-62
bool smzd[505,5.259,354E-83]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
## c?2/14TDuj6e,
func wrJ (number rIA[74.681E41], string JO[74.429E-55,5e-88,689e+38])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
func Ir (string il4[4,262,624.054], var XB)
	begin
		for HW until 409.536 by ixs4
			rFD(true, "'"", "q'"]")["K'"'"'"Q", false] <- true
		## `i3
		begin
			## >ldh
			## /v$RCSx
			## pIHST7@pxH`Ly>Kr<
		end
	end

func UQsm (string kPO[47e+32,93e41,125.202E-18])	begin
		## K$|80>]J9#&?mC%P`
	end
'''
		expect = '''Error on line 2 col 36: var'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
func Tp (number EnX[25], dynamic iuBM[8.385E-72,989.862e+30])	begin
		## 8og$-KA
		break
		## ,S:sv.($sw<]Nb|wL!`
	end
bool ui[5,1e62,34.410E48]
'''
		expect = '''Error on line 2 col 25: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
string ZAij ## {/Whq]-%a6{7%Q
## oN@>^l[+}eU]Tj=M
func mUx9 (dynamic Nj[6])
	return nANt

string Bp[6.495]
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
dynamic xzK[338.577E+82,2.925,9.273E04] <- false ## =q_p]iue {
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
string zC
number Voc ## T
## FwNTg]
var okH[6.198e+14,57,9] ## 9plrK
'''
		expect = '''Error on line 5 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
func gDE (number g0S[3.432e-34,96.643], string Gz[2,1.745e-89,55.753e74], dynamic w9c[903.349])	return DKI

number ky <- eUi ## 8ttTu
func LCS (var ph, var ILif[222E+47], number F3)	begin
		## B4q{
		begin
			return
			## IiSPSm&,Ro?9-,skk1
			## uw
		end
		begin
			## "pYN|u
		end
	end

'''
		expect = '''Error on line 2 col 74: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
dynamic HeDh ## Y&G518Z
## ?Z.G>Anhmks
## a!u/iZ+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
dynamic bgW <- "'"R'"" ## +teRzI2FGnz0k?n
func kLe (var jlGY[577.737,7.396], string cr4T)	return Ra

## *ipjnCbGet?2G&
bool aqp ## c{Q+/%P-E/vO^23D#m^
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
string wtD
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
var hc[73,278e47] <- false ## 0SG)n.
dynamic DnhY[7.035E-84,289e-41,4.429] <- "'"'"" ## zF%E*4qg-.vA5zv?
func FH (var pWO[5,218.529E05], bool hbQy[3,7e-32], bool SAU)
	return
func eW7 (string TVk1[17.014], var heQ, dynamic bNn[295])	return

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
func cGH (var zZn)
	return

number LGz ## KV$sm+r?+7%
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
## nF I3##
## A
string ZT ## IJju&c>?2>8
## }tljG1"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
dynamic C_H[529.720] <- 2e+90
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
string tv[3.293,614E-66,392.624E-63] ## ,MaPJ-g/I
bool B5r
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
## dmxrHv~
dynamic GcOf[880e87,705.437]
func f6 ()
	return 26E-20

var QZZk[5E50] <- IoW ## O8J
dynamic Mo[363.996E+26] <- qht ## y|W"A_J
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
func tgX (var Pp[1,11,7])
	return "F)O"
number BsQr
func LL ()	return

## y
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
func mcTC ()
	begin
		## ?
		break
		## <6W?3uPv_*0X+*
	end
## XhV)d=
func LfUU (var j1o[6.409,6.049,984E+25], number fvQ, bool UIh9)	begin
		## 9
		## 6+Z>WrX#s7ce]
	end
'''
		expect = '''Error on line 9 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
bool FCA[61,888] <- false
func Gw ()	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
bool qdl0 <- 2e20 ## GX!cSv,^! D1i
func Nc (bool LQ[778E54,2E+61,1.418])	return

func kA (number Chs, string qM[356.321,359,42.296])
	return true

bool StV3 <- true ## dH$I82ml7)n^|kAGm
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
string vcD <- false ## R$TnaGg4#`~K5dnA}<sM
## yv$not^|)]ZmQ2q Z1_
## ._Y6IlMS)`z
## g*6w:Uh8
## Pvp
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
string vm[9e75,86.471,59] ## gxl{&A)Q(u&>j(R7B(h
## #w|ao6d
bool fz <- 0
## 9;u"W[>>
func DbKL ()
	begin
		## eYKP|}/>
		## 5f-Kij:XbeAQZx
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
number U3E[96.895,5.624E+90,93E-07]
## &1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
## wgzf02x@c<*cG&)o
dynamic BhL[910E-88,828.254]
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
func gzOQ ()
	return false

number cVP <- true ## iBy+ ob
func K0Ja ()	return

var CxZ7 <- 4 ## ._4]o4*Z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
bool Yp
func AT ()
	return 40E+97

## ZYLU$DriR0U(
var Uy2J[26E+59] ## _4H9Ttx
'''
		expect = '''Error on line 7 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
func DuW (bool cYU, bool zS)	begin
		return 76E-99
		continue
		if (true) bool I2
		else for wPp until true by k4m
			continue
	end

dynamic KKi[573.919E+91,6E+17,14.564]
func odm (string eT, var AB7w[23.257,840,163], bool H_2)
	begin
		## VPt6i2*k 
	end
func vD8 (bool fIwb, number NaXW)	begin
		V5()[637.358, "2'"t?"] <- false
		for Sw until true by "#L"
			begin
				## %p-w5Q96gn9%LN,l7:
				break
			end
		## :@/X`uQ
	end
'''
		expect = '''Error on line 10 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
string imX[26,88.142E-40]
## wTe"/Yvgx{-t.A7VH
func XrR1 (var pTC)
	return US

func ZDK (var tw, var PO6, bool yUJV[8])	return ID
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
func hUJt (string Yqi[4.523E80])
	begin
		## =RJ}FCbWbw
		## %h<]SU^%1?{
		## 7BYBDkF93
	end
## x0IE=aHpF&zTLY}cH^
func Bq ()	begin
		## Z?_6U-E
		begin
		end
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
string Xg[7e-76,96.109,578.942E+57] <- 42.007e73
## {wvFkR5/c><qBg=t8N1a
func em ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
dynamic RKJt[33e+12,666,96] ## ^dqG
func XQSu (string PWQe[976.267], number UT[70.456,19.472E-96], var WTHp[25.700E+34,19])
	return "'"'""
func pPA (string XDt)
	return

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
bool zl6_[4,166.954,9.726] ## _^7%L;2vN}1ZRze?Y<@m
number CQHE
func CQzJ (number h5U[90], var TNe[7.955E-05,743.195], dynamic Uoh[49e30])
	begin
		continue
		## D "H@hjz ?P^x$<@si>#
	end
'''
		expect = '''Error on line 4 col 27: var'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
## p=k
func kW ()	begin
		## _$}[+n<sRK]v
		number t4 <- "+'"hm^" ## nvW+"%<a
	end

bool d5G[13.575] ## dyU
number OuL[5,57e29,4.828E-02] <- ug0u ## 1u=@#^1=R%!"~D-@sKD
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
## {tu"As
bool oVYQ[693.499E+40,8e-92,335.535]
dynamic oxG ## H`-e
func J4 (string ZZZD[60,5.476], string aGF, string Oc)
	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
## TUf9s93]sr6k1Z9fw[-
string xvE[46e-89,675E89,29] <- 44.653 ## V*l6{K](!A[F}]e)f/
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
dynamic D7q[491.431,507E98] ## sd/p"L~|g:cf&N
number Xt[847.873,63e+55] ## ^00!]gietE8XnX
func QV ()
	return Hiu
func HK (string o0p, bool kYp[29.727])
	return

'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 300))
