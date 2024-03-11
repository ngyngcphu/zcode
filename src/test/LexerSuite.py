import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test("0.086", "0.086,<EOF>", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test('''"'"v'""''', '''\'"v'",<EOF>''', 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''## Y6sD!*d1V"cN2^''', '''<EOF>''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("Hc0Uh4eNm", "Hc0Uh4eNm,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''## l<~.''', '''<EOF>''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test("Mpw7Jzez^", "Mpw7Jzez,Error Token ^", 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("80", "80,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test('''## 4Lbe__<LAuKUbE"''', '''<EOF>''', 108))

	def test_109(self):
		self.assertTrue(TestLexer.test("619E-68", "619E-68,<EOF>", 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test("93", "93,<EOF>", 111))

	def test_112(self):
		self.assertTrue(TestLexer.test("192.230E-56", "192.230E-56,<EOF>", 112))

	def test_113(self):
		self.assertTrue(TestLexer.test('''"'"
h'""''', '''Unclosed String: '"''', 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("bcO", "bcO,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test('''## n<''', '''<EOF>''', 115))

	def test_116(self):
		self.assertTrue(TestLexer.test('''## z?P}U?B=rWJY''', '''<EOF>''', 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''"'"M"''', '''\'"M,<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test("80", "80,<EOF>", 119))

	def test_120(self):
		self.assertTrue(TestLexer.test("12.226e45", "12.226e45,<EOF>", 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''## c!''', '''<EOF>''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''## eloq5''', '''<EOF>''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("hQyoKLHw", "hQyoKLHw,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("28.282", "28.282,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("ML4hDJDu", "ML4hDJDu,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''"\\xr"''', '''Illegal Escape In String: \\x''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test('''## /{''', '''<EOF>''', 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''## EO%A#&V''', '''<EOF>''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## I''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("152", "152,<EOF>", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''## 5W^G''', '''<EOF>''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"'""''', '''\'"'"'"'"'",<EOF>''', 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("wTeW6H^", "wTeW6H,Error Token ^", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 137))

	def test_138(self):
		self.assertTrue(TestLexer.test("37.708", "37.708,<EOF>", 138))

	def test_139(self):
		self.assertTrue(TestLexer.test('''"'"'"'"\\p'"$"''', '''Illegal Escape In String: '"'"'"\\p''', 139))

	def test_140(self):
		self.assertTrue(TestLexer.test('''"H'"'"-Q"''', '''H'"'"-Q,<EOF>''', 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("0dBJ8XXtX", "0,dBJ8XXtX,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## s{u''', '''<EOF>''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test("40.402", "40.402,<EOF>", 143))

	def test_144(self):
		self.assertTrue(TestLexer.test("64", "64,<EOF>", 144))

	def test_145(self):
		self.assertTrue(TestLexer.test('''## =H,Fkv?S''', '''<EOF>''', 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("91.221E+55", "91.221E+55,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("40.132e84", "40.132e84,<EOF>", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("45E-20", "45E-20,<EOF>", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test("814e-40", "814e-40,<EOF>", 149))

	def test_150(self):
		self.assertTrue(TestLexer.test("94.771", "94.771,<EOF>", 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''## C,1z%`m4''', '''<EOF>''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("HMJr_$b", "HMJr_,Error Token $", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("7J", "7,J,<EOF>", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test('''## =oy/lEaa(}(67>Pa_LZ%''', '''<EOF>''', 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''"'"'"	1"''', '''\'"'"	1,<EOF>''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''## (5;ax%!+8!@aH4v5An''', '''<EOF>''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("6R", "6,R,<EOF>", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("dYqu9Zu4", "dYqu9Zu4,<EOF>", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("Vy&QG3KnI", "Vy,Error Token &", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## "vU9piZA%;''', '''<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("42E27", "42E27,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''## -A&V2vmeX;~H''', '''<EOF>''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("hlWsWzcL", "hlWsWzcL,<EOF>", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test("7.906e21", "7.906e21,<EOF>", 164))

	def test_165(self):
		self.assertTrue(TestLexer.test('''"Q'"|"''', '''Q'"|,<EOF>''', 165))

	def test_166(self):
		self.assertTrue(TestLexer.test('''## rA<Y5|X''', '''<EOF>''', 166))

	def test_167(self):
		self.assertTrue(TestLexer.test('''"'"-G'"' ''', '''Unclosed String: '"-G'"' ''', 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''## 4QC8dcXP7''', '''<EOF>''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("445E37", "445E37,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("32.667e90", "32.667e90,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test("I7I&bc2^bk", "I7I,Error Token &", 171))

	def test_172(self):
		self.assertTrue(TestLexer.test("21.155", "21.155,<EOF>", 172))

	def test_173(self):
		self.assertTrue(TestLexer.test('''## T+gZW69VRk`*z''', '''<EOF>''', 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("KqBGpA", "KqBGpA,<EOF>", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test('''## <16HJ1''', '''<EOF>''', 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''## {$s|:W_$rw''', '''<EOF>''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("6.148e-32", "6.148e-32,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''## `#''', '''<EOF>''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test("560", "560,<EOF>", 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''"
v7"''', '''Unclosed String: ''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''"'"'"?'"'""''', '''\'"'"?'"'",<EOF>''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("Z@m3", "Z,Error Token @", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("PlUQ", "PlUQ,<EOF>", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("5e-45", "5e-45,<EOF>", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## a1:KVNRQu:QQaF''', '''<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("265.017", "265.017,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test("888.299E+03", "888.299E+03,<EOF>", 189))

	def test_190(self):
		self.assertTrue(TestLexer.test("9.339E+34", "9.339E+34,<EOF>", 190))

	def test_191(self):
		self.assertTrue(TestLexer.test('''## zp[JxGcG~@`''', '''<EOF>''', 191))

	def test_192(self):
		self.assertTrue(TestLexer.test("224.038e+83", "224.038e+83,<EOF>", 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''"O'"'""''', '''O'"'",<EOF>''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''## 9d?7h|X::23Hq2%Q%''', '''<EOF>''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("td", "td,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test('''"\\zW"''', '''Illegal Escape In String: \\z''', 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("28", "28,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("1VaAj&", "1,VaAj,Error Token &", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test('''## D''', '''<EOF>''', 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("54.257E49", "54.257E49,<EOF>", 200))
