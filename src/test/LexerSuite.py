import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test('''"g'""''', '''g'",<EOF>''', 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("788.364e65", "788.364e65,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("KTga_ow", "KTga_ow,<EOF>", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("184.615e75", "184.615e75,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test("gxpRshAd#", "gxpRshAd,Error Token #", 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''## b.AG''', '''<EOF>''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("874E39", "874E39,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("28e+65", "28e+65,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"'"d ''', '''Unclosed String: '"d ''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''"\\eTC"''', '''Illegal Escape In String: \\e''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''## RR8/i|;kt. r]!V''', '''<EOF>''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("8QPlmA8_", "8,QPlmA8_,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("KkG", "KkG,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("@9Nk", "Error Token @", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("ZTa", "ZTa,<EOF>", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test("90.049", "90.049,<EOF>", 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'","''', '''\'"'"'"'",,<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''"\\u'"'"'"'"Y"''', '''Illegal Escape In String: \\u''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test('''## v"0y|X=$LiI-w<hlL:''', '''<EOF>''', 123))

	def test_124(self):
		self.assertTrue(TestLexer.test('''";'"'"	J ''', '''Unclosed String: ;'"'"	J ''', 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("EZQNgx", "EZQNgx,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test('''":\\l'">"''', '''Illegal Escape In String: :\\l''', 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("JIlh", "JIlh,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''"T
p"''', '''Unclosed String: T''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("aq5e", "aq5e,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''"6'"\\x'""''', '''Illegal Escape In String: 6'"\\x''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## D-G{8RK`b]xxk?=3FK",''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("2E-46", "2E-46,<EOF>", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''## |H~]y%(;q%g''', '''<EOF>''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''"P ''', '''Unclosed String: P ''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test('''## GCo]%}6tW%ip4|JkV''', '''<EOF>''', 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''## h''', '''<EOF>''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("1.003E+42", "1.003E+42,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''## }q 4#H%]g^:%P(=''', '''<EOF>''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("j", "j,<EOF>", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test('''## [e2%I"+v1cufog''', '''<EOF>''', 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("47", "47,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test("$$_^bp3gG", "Error Token $", 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''"'"'")
'"'""''', '''Unclosed String: '"'")''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test("38N#", "38,N,Error Token #", 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("34.083e18", "34.083e18,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("32E00", "32E00,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("Q#VQo#V_", "Q,Error Token #", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("BUH0", "BUH0,<EOF>", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''## -`5iSvN+L^QF1c''', '''<EOF>''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''## hNqzGXJdoHrG]E$''', '''<EOF>''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test("Q6Ep", "Q6Ep,<EOF>", 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("8oB3$", "8,oB3,Error Token $", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test('''## {hIx,=U''', '''<EOF>''', 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("923.851E32", "923.851E32,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''"\\eq"''', '''Illegal Escape In String: \\e''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("889", "889,<EOF>", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## OsQMs.DwFx''', '''<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test('''"'"'"'" ''', '''Unclosed String: '"'"'" ''', 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''"'"\\d--"''', '''Illegal Escape In String: '"\\d''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("^CJ2_gY$u0", "Error Token ^", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''"Z`'"\\j9^"''', '''Illegal Escape In String: Z`'"\\j''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("142E-84", "142E-84,<EOF>", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test('''"'"'"'"0?"''', '''\'"'"'"0?,<EOF>''', 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("417.251e+66", "417.251e+66,<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''"K
'"''', '''Unclosed String: K''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("YHdFP0f_MU", "YHdFP0f_MU,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("hn134XQ", "hn134XQ,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''"
:'"4c'""''', '''Unclosed String: ''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test("bu$Jwqd2", "bu,Error Token $", 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("v5", "v5,<EOF>", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test('''"G'"9'\\c3"''', '''Illegal Escape In String: G'"9'\\c''', 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("913e-17", "913e-17,<EOF>", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("27E+33", "27E+33,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test("76", "76,<EOF>", 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("1e33", "1e33,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''## +<>d Ls0A n-xJ6-A''', '''<EOF>''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test("44vO1E07VS", "44,vO1E07VS,<EOF>", 180))

	def test_181(self):
		self.assertTrue(TestLexer.test("Ur9YNHt2", "Ur9YNHt2,<EOF>", 181))

	def test_182(self):
		self.assertTrue(TestLexer.test("2E+30", "2E+30,<EOF>", 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''"'"
'"'""''', '''Unclosed String: '"''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''"'"
'""''', '''Unclosed String: '"''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''"'"'"*'""''', '''\'"'"*'",<EOF>''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''## "]fQ+_p<dKSe''', '''<EOF>''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test("858.490", "858.490,<EOF>", 187))

	def test_188(self):
		self.assertTrue(TestLexer.test('''## I>#|d''', '''<EOF>''', 188))

	def test_189(self):
		self.assertTrue(TestLexer.test("0.868", "0.868,<EOF>", 189))

	def test_190(self):
		self.assertTrue(TestLexer.test("2.939", "2.939,<EOF>", 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("mZF", "mZF,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test("8YZG09f", "8,YZG09f,<EOF>", 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''## na^AKv#N''', '''<EOF>''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''## kiGeaw$T"i@!.gk/i2-''', '''<EOF>''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("e@gqW", "e,Error Token @", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("sp6S_", "sp6S_,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("g4BpAEUq3e", "g4BpAEUq3e,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test('''## wg''', '''<EOF>''', 198))

	def test_199(self):
		self.assertTrue(TestLexer.test('''"(\\ko/"''', '''Illegal Escape In String: (\\k''', 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("uvvQnmqFI", "uvvQnmqFI,<EOF>", 200))
