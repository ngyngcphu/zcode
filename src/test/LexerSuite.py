import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("TwcvtuQ", "TwcvtuQ,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("7.268e-36", "7.268e-36,<EOF>", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''"p	='"
U"''', '''p	='"
U,<EOF>''', 104))

	def test_105(self):
		self.assertTrue(TestLexer.test("5.418", "5.418,<EOF>", 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''"'"'"SN'""''', '''\'"'"SN'",<EOF>''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("8E25", "8E25,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''## 3FZ_q+sU0;f$5P(|l''', '''Error Token #''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''##  c/TS.F?$2MxOwup''', '''Error Token #''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test("47.000E+69", "47.000E+69,<EOF>", 111))

	def test_112(self):
		self.assertTrue(TestLexer.test("^r", "Error Token ^", 112))

	def test_113(self):
		self.assertTrue(TestLexer.test('''## TW<WN:y%c"$V&t1''', '''Error Token #''', 113))

	def test_114(self):
		self.assertTrue(TestLexer.test('''## 3''', '''Error Token #''', 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("gdltQn", "gdltQn,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 116))

	def test_117(self):
		self.assertTrue(TestLexer.test("&VbXm", "Error Token &", 117))

	def test_118(self):
		self.assertTrue(TestLexer.test("9e-76", "9e-76,<EOF>", 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''"R"''', '''R,<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''## ~X NfS$bdm&wS>(1LbQ''', '''Error Token #''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("539", "539,<EOF>", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test('''"'"'"'""''', '''\'"'"'",<EOF>''', 123))

	def test_124(self):
		self.assertTrue(TestLexer.test('''## IHEar-7=BRNgK}9,7lHq''', '''Error Token #''', 124))

	def test_125(self):
		self.assertTrue(TestLexer.test('''## #/5 ''', '''Error Token #''', 125))

	def test_126(self):
		self.assertTrue(TestLexer.test('''## uaJ*#":00H2}Nta''', '''Error Token #''', 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("^", "Error Token ^", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test("45.499", "45.499,<EOF>", 128))

	def test_129(self):
		self.assertTrue(TestLexer.test('''"V ''', '''Unclosed String: V ''', 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''## "(d:`kTP''', '''Error Token #''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test("461", "461,<EOF>", 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''## y%(e2r/;lnet]''', '''Error Token #''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test("Z", "Z,<EOF>", 133))

	def test_134(self):
		self.assertTrue(TestLexer.test("751.030E+39", "751.030E+39,<EOF>", 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("a", "a,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("4@SCDMz", "4,Error Token @", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("$", "Error Token $", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 138))

	def test_139(self):
		self.assertTrue(TestLexer.test('''"
(Y"''', '''
(Y,<EOF>''', 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("3e+26", "3e+26,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("29.317E43", "29.317E43,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## 9qiw%@BNp''', '''Error Token #''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''## a18xc$JJ|7!s''', '''Error Token #''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''"'"'"'"p'""''', '''\'"'"'"p'",<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("8fLJ@aq", "8,fLJ,Error Token @", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("39", "39,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test('''"~ "''', '''~ ,<EOF>''', 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''"'"'"'"\\x;{"''', '''"'"'"'"\\x,Error Token ;''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''## |p03|X^dEqC''', '''Error Token #''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test('''"1'"T+
'""''', '''1'"T+
'",<EOF>''', 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("SgGEBT3Nf", "SgGEBT3Nf,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''## EbS-C,>?x!tEgN''', '''Error Token #''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''## BKkGcgIjAkOGEx''', '''Error Token #''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test('''"_\\v'"t"''', '''"_\\v,Error Token '''', 159))

	def test_160(self):
		self.assertTrue(TestLexer.test("&hXP7PCC5Y", "Error Token &", 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("493.043E+65", "493.043E+65,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test("36.037", "36.037,<EOF>", 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("U$q", "U,Error Token $", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''## Xn''', '''Error Token #''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test('''"'"'"'" ''', '''Unclosed String: '"'"'" ''', 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("GPoj", "GPoj,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("196", "196,<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test("RAuV_Fb", "RAuV_Fb,<EOF>", 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("44", "44,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 170))

	def test_171(self):
		self.assertTrue(TestLexer.test("0.475", "0.475,<EOF>", 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("69", "69,<EOF>", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("75.847", "75.847,<EOF>", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("IufP4", "IufP4,<EOF>", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("BDa&", "BDa,Error Token &", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''## F/9g''', '''Error Token #''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''## ] kz*AjMEa''', '''Error Token #''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''## pAs@x,`oa/,''', '''Error Token #''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''## bg(2=-#&''', '''Error Token #''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''## @W}>(''', '''Error Token #''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("P6D", "P6D,<EOF>", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("967.451", "967.451,<EOF>", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''"\\gOxJ'""''', '''"\\g,OxJ,Error Token '''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test("739", "739,<EOF>", 187))

	def test_188(self):
		self.assertTrue(TestLexer.test('''"'"J'"oW ''', '''Unclosed String: '"J'"oW ''', 188))

	def test_189(self):
		self.assertTrue(TestLexer.test("lV", "lV,<EOF>", 189))

	def test_190(self):
		self.assertTrue(TestLexer.test("1.450", "1.450,<EOF>", 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("68.992", "68.992,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test("Dh_RJ", "Dh_RJ,<EOF>", 192))

	def test_193(self):
		self.assertTrue(TestLexer.test("9YDFdhmiiL", "9,YDFdhmiiL,<EOF>", 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''## bg^9)7d|>_ ,T.gY''', '''Error Token #''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test('''"\\y uP("''', '''"\\y,uP,(,Unclosed String: ''', 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("IV3Xy", "IV3Xy,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("Mm6$", "Mm6,Error Token $", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("$3$o@0WY", "Error Token $", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test('''## d{HPj%SVO0H%tf2''', '''Error Token #''', 200))
