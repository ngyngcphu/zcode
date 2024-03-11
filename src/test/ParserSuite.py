import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
## P9yB~M^r<KV%}&R/Y
string hA[516.790e31]
bool aY_w <- [DjF(I8c(), [- 29.242e-21]), NA] ## 8$%0JC6.x+e "xSUx
bool oF[269] ## W| l` =^+1X&.99dWns
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
func Ohf (string Qf6)	return
## Y=5>zQmuT3i2N
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
number P9i ## )!AAFXmjD+Y{$/1v
## >RbKSCT1lEtTmI$?,
## 2{LU!eu(!Aj7NA
func hDz (bool pUvZ[469E+35])
	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
## T&GGD$|f*i[Q~3~W,<E
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
## nffR.wp4h.o}KW]/
## 0ngD$8[Nkk
number bn[76.367e53,6E+90] ## !t 7}
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
func zvX (dynamic RfW)	return jL_

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
## t&BUj7j`S$;
## ePrhgYp3he7N,}GJDkQ
string o8 ## T>/
func sJ4x (string yXB)	begin
		## M#OlkMrj*+"]D~Tfc
		psn("q")
		## )[7}Bm$jw78
	end
## GyBjR/5Lq} ]tc(;i<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
func yd (bool xC, var FJgS, bool w46[8E-54])	return

func ghYA (dynamic ztyT, string I0oX[9.048e+38], string x52d[9e+99,516,98.812])
	return false
dynamic xX <- true
'''
		expect = '''Error on line 2 col 18: var'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
func Iw ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
## I
func CnrP (var LXw[0,7.984E20])	return false
func ES (bool yAF_[9.036,395,363.858], number sa66[30E-32], string wLo[1e-11,174e00])
	begin
		break
	end

'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
func G2 (var p700[949.529,6.477e-19,896e+56])
	return
func xVe (dynamic Qi0, string S2[87,9.996,86], dynamic nI[9.070e-55,180.438,3e81])
	begin
		## A^|S:/6p-,iDhh-^tR
		## A.+wW?QR/
	end
## ilyn!Z-dRvdW-Q51n] 
## Yt
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
func Rc (number Ud0F)
	return

func tz8 (string Wb, number foLP[68,976,4e-93])
	return "'"'""
func BZ ()	begin
		## zA,cy0/;{z+ J
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
number zKWK ## TRT43U%rf2n|1zNc3ak5
## 3eUD*#l~/Le-V~!nF<0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
dynamic ZcHA <- true
func h3p ()	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
## jn!MMzY.A
func Ym9q (dynamic Aumw)	begin
	end

bool q_ <- Nq ## }
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
func jGr ()
	begin
		## L#t]YvqJr
		break
		## zA075_T,
	end

## AbC4)+!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
## 4gGi1z+
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
number Xii <- false ## @h
## O<! Du"+22nT8f
bool kkiu[0.988E-85,0.228]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
number L2[0.964,9,8.740E91]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
bool LZ <- 463.146e98
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
func K3T (dynamic Vrm)
	return

## ykO:r44IbC0zvwF
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func znhO (var xCh, bool ef, dynamic WkD[520,541.976])	return
func RFt (bool d_t, bool KK0[0e33])
	return
func MS81 (dynamic QuFj, var D_, dynamic ep[0.342])
	return fDBP

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
var PJnL
## {b
## N>sE"IV
'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
var O2PJ[0,9.996E40] <- false ## ixeyPC`SGX( %>|N}
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
string t6mM[5.004] <- m_
func DYPh (dynamic cNF, string TPax, dynamic AIz)	begin
	end
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
bool YM <- yTws ## JWq)
## JzUuS&A-z]e
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
##  qZ!Ty2$
## @3UG_"bI(
number jXRV ## 4/{-3CkCO`a"%P
dynamic mPJx[301.561,10.599,7e+16] <- 912 ## w=f0{@c91Inqw&O)
'''
		expect = '''Error on line 5 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
dynamic FR3L[5E-50] ## o..AD]F$:8M(e{{9a`n
## sK
func BX3y ()	begin
		## KsfAlPhcx(%e
	end

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
## <wrr|T
func p8 (string PNJo[4.656,222.327], number os[67e-84,238.226E-05], string itC[58.885])
	return "'"p'""
func yx0 (dynamic PW, string Cn1[51.437,364.970E+05])	begin
	end

func vK (string ipp)
	return r7
func a2Rg (string NY)	begin
		## ,8
		## kW#qQ5
		## em<%{GP:J-7:v-<
	end

'''
		expect = '''Error on line 5 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
number hLo <- true ## mV0
## h[?vYrvW|]~>U
dynamic kH
## v{w#t
## G,r]F%+30; {!Zce]"l-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
##  B9cB7h]yrg*xkH}|b
bool RzU[101.982e36] ## *sU-(I[wa
func YX (dynamic G8, bool BW[96e-47,362], string jI[77.488E07])	begin
		begin
			break
		end
		break
		Wo(96e+05, 10E+03)
	end

func KHvI (string KW[0,538,39.013], number Mc[8e+87,248E-55,28.145], string TqY[254e-80])
	return
var aNo
'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
bool tn
## Qa
func njOI ()	return true

func W7 (bool KK, bool Zur[1.435,9e11])
	return

func B_H (var NY_J[5.017E45,55.050E51,549], var tsa[20.970E+66,3.787,784E36])	begin
	end

'''
		expect = '''Error on line 9 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
func mdI (string NN[63], string bb, var BKX[2E+66,72.638e13,7.456])	return false

'''
		expect = '''Error on line 2 col 36: var'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
string pk ## Q
func Dc (string a5)
	return true

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
func sez (number NMv[7.519E-79,60.985E-77], var MQJd, var BQ[7.237])	return "B'"'""
dynamic PB <- zVM2
'''
		expect = '''Error on line 2 col 44: var'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
number Qcw[485E-91] <- "'"G" ## 03nKvv/Nk0kXIQU l,-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
string iuXs[111,758e-50,0] <- in
number rFs[8e-31,2]
## `>sgh4"l55eA_(+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
var jfN <- tg
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
## B3cuJGSGiy`"L[e&8zK
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
## )ysQo+j~p oHK*Pg6Nn{
var hGT[5E45,229.384e-48] ## 9sS# U/Vz
func qn (var Ky, bool fh)	return
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
func wn7q (bool vi)
	return "k'"'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
func MT (var uAI, dynamic na)
	return
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
func Nv (string JV[69,4.634e+71], var o5ta[639.946e-44,927,97.650E+34])
	return
## u/&p74TO{Q <waIy
## FtgDVW0kL
func kPs (string WGz)
	return
'''
		expect = '''Error on line 2 col 34: var'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
number yVV ## :-_=@lc/
func q5rq (dynamic dWon)
	return "C'"4'""
func Ov (bool HI[1e11,155.318,45])
	begin
		## LoPA_IY3:5
		N6G(589e80)[bu4, aG6] <- true
		## KqW|f;@EA,@&ZB9a|Du
	end
func DLlV (dynamic UuB, number hRE)	return true
func Pcx (bool AnjS, var J7_r[642.738E82,4,710E05])
	return

'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
var Jsy[37.900E31] <- false
dynamic OR[461.418,1.246E25] ## h
number dFv[6.424,170E-38] ## q
## z2Lt*TCy2/`
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
## Sa,dZfKqhw0V
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
func dW (number Y0, dynamic MfWf[58,7.535])	return "'"@L'""
'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
string uPFz <- false ## t~p1b2;%
## _.T`P/ay/% mbl%?1Uu
var jx2l ## #,eCn1A:PI[d^N=
func tm (var EpJ5[92])
	begin
		## w]<uT*E,GYRVJYH@]d
	end
## G(:"xLIWEwc
'''
		expect = '''Error on line 4 col 27: 
'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
string oc[95.072]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
var Xwi <- false
## JC4J^
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
## 79)FHI3&
number pzWF[70e-20] <- s_
## `ZNsV%&&nf
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
## |Mx
func ve ()	begin
		## E>hUGnvJk7]J
		## 3-ZUy)b%OOpeBw@
	end
func Vp (string SyJ, dynamic tbt)
	begin
		jO <- Xeep
		## WlqgtX31yqYYE
		## >f>(u{l=$F4%4
	end

'''
		expect = '''Error on line 7 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
func tCx (dynamic VL[9.619], var XB[22])	return myrK
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
string r7
func Vz (string XyF[3.320,8])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
string WAh[40.902] <- 14e38
## fPZH*P
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
func Fd (var rwqZ, var dV[566,35E+54,962e+98])	begin
		## QSlx,-4:g|G!IK=%
		## a
	end
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
dynamic q5[61.227,430.990] <- true ## VD(
var cZPm[512E+03] <- ldxq ## "AcwS
func kFUX (string TCbO, dynamic AXWN)	return true
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
func e3R (bool MJ, var HQ[132,857E66])
	begin
		PnQR(true, "'"'"")
		## O~9C4M)l2h<Xq~_bZ#
	end
## v^9M
number lZRO[67.116e13,93] <- d7
## r;P1oCF6(%
func US (number C9[4.500E+14])
	return

'''
		expect = '''Error on line 2 col 19: var'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
func v_Q2 ()	return

dynamic LCGy[2] <- false
func Xi (number Cf)
	return YtmH

var tp[47.311,708.295,4.420] <- FP
func D7 (string AO6G[2.005,732.758])	begin
	end
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
func zBC (bool oysY[90E-58,34], var g720)	return "<~'""
## LhKF5Yk`h|6D]m"cm."W
func U17 (string S80, bool CVzN[5,12.152,11.139e-96])	begin
		break
		## ot%!R3{/
		if (857.311)
		Zc <- 8.894e+33
		elif (930.065e-40)
		aPs <- 8.558e-94
		elif ("e'"") continue
		elif (Jn) BFe <- vl
		elif (1e55)
		if (4)
		begin
		end
		elif (bG8) lKc("o ", hoJ)
		elif (false)
		string VKw[62.717E-30] <- 1.868E63
	end

'''
		expect = '''Error on line 2 col 32: var'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
string GUsE ## r$TDFM,8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
func iMDR (number Pve, dynamic xz[91.223,1.013,1.995E-12], number gjd[77e-32,10e+16,51])
	begin
		return "t8'"'""
		## kD~Z"]`_XT(Lv}k(IC
		if ("k'"dZ'"")
		continue
		elif (9) return "Az'"'"'""
		elif (true)
		if (41e-30) lT()
		elif ("'"w1'"z")
		for ZO2l until false by true
			return 4.811e57
		elif ("?$'"'"") if (n9kg)
		var iPU <- Hy
		else if ("'"'"'"") return "'""
		elif (lTFG) for WCQd until IK by "'"e'"a'""
			if (";'"'"'"")
			s4[Q0B, 8.676E97, Ifyn] <- "'"'"7'"["
			elif (998e+02)
			break
			else begin
				continue
				if (oVmx)
				if ("|'"m") jt(7.434e-86)
				elif (true)
				if ("A'"A'"'"") EU <- 849.396E-11
				elif ("x")
				break
				else VLjZ(px, false)[13E01] <- ",'"S'"("
				else begin
					## BZYi8e 7Ez-:RtGp[k
					## [0`wmjg)z:vij`{!Hm./
					## k09W44&qs;I
				end
			end
		elif ("X{") continue
		elif (true)
		HB(okHu, true)
		elif (false)
		iJH0 <- "@"
		elif (90.993)
		return "t'""
		elif ("'"'"i'"W") bool kSmB
		elif ("'"|'"") Y1Um <- false
		elif (7E03) break
		else return "f"
	end

'''
		expect = '''Error on line 2 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
## qe
bool rtqv[99,4.552E-79,76.030] <- "9'"'""
func D7lD (string kQm7)
	begin
		R6nQ(988.545e77, 830E+67)
		## "oJ-
		## XVKRR
	end

func s6c (dynamic oGj)
	return

func YJR (string hHG[20,72e94], bool B3[3.526e36,369.738,40.943])
	return EH

'''
		expect = '''Error on line 11 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
func pq (var tk[4,977e+73,30e+25])
	return 5.076

## :74=4!x2]"hskAu8%C*
dynamic WXR ## vtHJ$r@{&Aic_W
## +F
## .)E&b95`
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
func PKs (number gO[1.163,138e+77], dynamic tJUS, var nRS)
	return

'''
		expect = '''Error on line 2 col 36: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
func kKcG (string k0[832.102,4E+46])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
## A?#
string XXPw[99E+55] <- vV3L ## 2kn~v/N
bool gXZd[983E00] ## h%
## ?7+hH>D^?<U#JH>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
func nUh (var Nu)
	begin
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
## O0w<M:^IheGQ`<#,6s
number SSro[89E85,0,752.468e-05]
func pkf (number A0F4[1e+42,4.194,152], var dsS, string vZW[2E+52,34.379,9.774])	return true
'''
		expect = '''Error on line 4 col 40: var'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
## D_SanY:Wi;g
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
func eCvg ()
	return 7e-84
func YUit (dynamic m3l, bool vwrb)	return false
bool uFl[27.529E83,811e25] <- false
bool PGR ## N$;l#:.{5q |
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
## jmaA_j E9ivq
var zmYt[852.883,86.514] ## *f$o,alZY
## a7`[0WfCdKIc-8$E)
func sLX4 (dynamic XL[2.671,730,8])
	begin
		## 9IqRK)L f(7wYN{}YCy
		bool iUB
		## l:hy#D >$n$g$Z@N)+pY
	end
func VR0V (bool QE[3.358E+47,1.352e+24])	return 0.385e45
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
number jC[0.868,436.148,46] <- fSu ## .>Ppv,O2H
## {>wQDXdyS4Zs9/PT2zYQ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
func mOnt (number MM6F, string wBn[1.634,41.451,82.032])
	return

bool xEkf[0,2.438,1]
func u7 (string ae, number Fe)	return

string vd[82e+55,74.928E-59,75.717e-05]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
## g4,t&!F[aG=~uC)
func EBon (string Y1[7.054e-92], dynamic ds)
	return 77
'''
		expect = '''Error on line 3 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
## Lo-67J/y
## +rR1h
## AR=7^r(NsYBUCCPq
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
dynamic oA[372.200E25,11.010E-75] <- 301.944e+09
number Syt ## %CmTUW4&
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
## qiF{fiT0q8AQ
func PyJ4 (string UO)
	return fscE

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
number Bxf1 <- jy
func eD (bool lW9[65.586,529])	begin
	end

func O37U (bool LMh)
	return "g h"
func bb (number FJm)
	return

func GP ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
func vKuE (var Rez[51.003e88], number A4)
	return
string Bpv <- 4e+81 ## lz:WLG?ft+T](7IMM
func Xrl (dynamic SA, string qRP9, number GUi)	return 7e-93

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
string gmw2 <- 2E+74 ## Vv.%pg
## ">
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
number vs[54]
number Eq <- zIa ## e
func NM (bool m3, bool PYdy)
	return g_Pw

dynamic Vv[293.998e+58,8.034] <- "'"&" ## XbjP4DMo")3gAG>!Mk*z
func NM (bool Aml, dynamic rR, bool jW3U)
	return "'"x'"'""
'''
		expect = '''Error on line 7 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
func N8I (string OEX0)
	begin
		continue
		continue
		begin
			begin
			end
		end
	end
string Aq[512] <- H4C ## /vi<lTHPvt.NYJ)!l_
func wW (var ra, string Kp, var oQ[379])	begin
		## UTjjMr
		Z8t(false, Ik, 4e-43)
	end
string JPuP <- "'"(" ## X$zYKG:Tg
func Si (var U6oG, bool lS)	begin
		## `,=fjTs
	end
'''
		expect = '''Error on line 12 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
var QW <- 15.539E-69 ## tz(
func MaJ (var JnI, number d8se, string nx[192.829,256,5.355])	begin
		## =1
		for tpnL until "@'"'"'"" by "/2"
			break
		continue
	end
func Fo (bool hSB[877], number O5SP, bool Ol)
	begin
		## jQ[tEF8^?Sw>JWsq(`Z(
		## 2+2s
		## Hm]5V!R_Cy$R^t
	end

func eBA (dynamic kBO[70E84,41E-94,9], bool u_dt)	return
## Jk/Ah
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
dynamic pL
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
## I?s
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
## R
## Kp]UO
var MLc3 <- jIq ## IKvh6
dynamic V8 <- "'"o" ## f
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
func AnAt (var N7I[88.267e-40], var FaW[65.528,854], var vA[38E-56,33.523,9])	begin
		## ?)XA;iNv6{05B_6O[
		Pa(82.453, 198.099, false)
	end
## +?ki["Xf.
dynamic enSN <- 324
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
## v`dpuX%FN4!"JF
dynamic oOa ## 4%DN#2ksw
func aNC (var r7)
	return 584.110E+61
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
## R,#
func VA (number dcj8)	begin
		## zlOgY
		break
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
## n@=bu~kY,v
## 1`JMOEqXsd
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
string WiL[8.587,8.111,212.627e18] ## >]&!.or],i#3iVp(rK
func jsjb (dynamic s5vu[9,4.053,31e64])	return

func Ix8 (bool aM[1e00], bool y24[47,715e-43], number cji)
	begin
		## f71!]rSoR
	end
func r7 ()	begin
		## [U^SLGYGkoDSK
		break
		## ; 
	end
## _@sR{6+=9
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
func iDnX (dynamic qGEu, dynamic XF, dynamic Iub[872.794e-45,23.944e17])
	return 95

## Ezjq0sJyS89
## h
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
string qo
number F8 <- 8 ## i
var XNwk <- "j'"4}" ## g(G%J*<,j.ftCau
number XcC ## zqFu*q3Y<$~V
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
number n7 <- DI
## -+
## S"yj~(g$I/
number KJVh[5,0.125]
## ^P,SgjPmrO:vL2uH&l~b
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
dynamic Cw1L[3] <- true
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
dynamic VxC[3.860E-71] <- 8e-93 ## ~I!Ez#.jN"f23++}}
## D:SwK
number qC <- tgo
func uq (number o5w1, var m1J[854.834], dynamic g3j[130.784E62,298e+09,105])	return
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
## [(fYLrPK><
string FN
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
## S|_D0U/}
number bd[8.156e29,340E-85] <- wnv ## ;T+
func Ga (number HGG, string jurI, number WB[270e74,4E-65])
	begin
	end
## {TW?qxc
func W7WI (dynamic mo[289e+95])	return 79.450E-89
'''
		expect = '''Error on line 8 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
var zz[53.309,15E14] ## ~vg
var QLTX <- "9E7[" ## cSYk$ytA@fL
## >}BuvS
var cWp
func T8 (dynamic xm[76,4,3.466])
	return
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 300))
