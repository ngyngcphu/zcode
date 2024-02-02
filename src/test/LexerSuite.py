import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test('''## A3l{mTLWTO[&''', '''Error Token #''', 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("UUp4PzBW^", "UUp4PzBW,Error Token ^", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("yd_X", "yd_X,<EOF>", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''"\\kR%"''', '''"\\k,R,%,Unclosed String: ''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''"
'"'"'" ''', '''Unclosed String: 
''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 107))

	def test_108(self):
		self.assertTrue(TestLexer.test('''## F3A''', '''Error Token #''', 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"'"^RD"''', '''\'"^RD,<EOF>''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''## ]I&*!c''', '''Error Token #''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''## _MRG-%@,}0vrbL"D''', '''Error Token #''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test("vqJOOdYk", "vqJOOdYk,<EOF>", 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("MldfF", "MldfF,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("1N", "1,N,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("8Rzls7g", "8,Rzls7g,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("#wKuPh", "Error Token #", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test("771e-96", "771e-96,<EOF>", 117))

	def test_118(self):
		self.assertTrue(TestLexer.test("Ynro", "Ynro,<EOF>", 118))

	def test_119(self):
		self.assertTrue(TestLexer.test("797E+28", "797E+28,<EOF>", 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''"\\w'"'""''', '''"\\w,Error Token '''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test("77", "77,<EOF>", 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("Mt", "Mt,<EOF>", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("9bO8n", "9,bO8n,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("kqYJP@", "kqYJP,Error Token @", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("UGA", "UGA,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("Vkni7Y", "Vkni7Y,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''"'"'" "''', '''\'"'" ,<EOF>''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("3.345e-58", "3.345e-58,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("rkf", "rkf,<EOF>", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test("K@Z40", "K,Error Token @", 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("$", "Error Token $", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''"|'"0v ''', '''Unclosed String: |'"0v ''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''## 9t$@]pMn73"''', '''Error Token #''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("48E+84", "48E+84,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''## x<Nl%h''', '''Error Token #''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("29E-52", "29E-52,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test("9e+35", "9e+35,<EOF>", 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("1&4HI", "1,Error Token &", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("p_vXM3TN4k", "p_vXM3TN4k,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## @b#H/fdlA-[(ty89JN''', '''Error Token #''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''"hj*G"''', '''hj*G,<EOF>''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''## 6S5&]GOCQZ''', '''Error Token #''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("#L@EmY3k", "Error Token #", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test('''## &ZORE61''', '''Error Token #''', 146))

	def test_147(self):
		self.assertTrue(TestLexer.test('''## *VKi ''', '''Error Token #''', 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("g2fdt69K$0", "g2fdt69K,Error Token $", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test("705", "705,<EOF>", 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''## <VS;GxZwWrwQx''', '''Error Token #''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''"@'"q"''', '''@'"q,<EOF>''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("0.554", "0.554,<EOF>", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''## [dR kJ[fv-[mr''', '''Error Token #''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''## C''', '''Error Token #''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''"'"dl'""''', '''\'"dl'",<EOF>''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''"\\k'"#"''', '''"\\k,Error Token '''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("Uy", "Uy,<EOF>", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## jbmc`4%*8{YlT!i$-gaU''', '''Error Token #''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("SCIhd1JC3k", "SCIhd1JC3k,<EOF>", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test("40.064", "40.064,<EOF>", 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("l@Y", "l,Error Token @", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test('''## $q]TN)J>OO.''', '''Error Token #''', 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("b", "b,<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test("340.084", "340.084,<EOF>", 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("f", "f,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("651.783E-66", "651.783E-66,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''"iya'""''', '''iya'",<EOF>''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test("Ox", "Ox,<EOF>", 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("wr^@Wk&W", "wr,Error Token ^", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test('''"'"?"''', '''\'"?,<EOF>''', 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''"
H"''', '''
H,<EOF>''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("Ez", "Ez,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test("Ro8", "Ro8,<EOF>", 177))

	def test_178(self):
		self.assertTrue(TestLexer.test('''## DwJ^0tNNFfPx[J|_aY''', '''Error Token #''', 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''## G~YfN9,2-E4b5/BKVNb''', '''Error Token #''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''"?P'": ''', '''Unclosed String: ?P'": ''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''"\\wT'"'"b"''', '''"\\w,T,Error Token '''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''"'"r\\v'"'"'""''', '''"'"r\\v,Error Token '''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''## t?c>WgQ[qG''', '''Error Token #''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''"\\a'"Q"''', '''"\\a,Error Token '''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("72.773", "72.773,<EOF>", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''"jt'" ''', '''Unclosed String: jt'" ''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test('''"e'"'"\\z'""''', '''"e'"'"\\z,Error Token '''', 188))

	def test_189(self):
		self.assertTrue(TestLexer.test("45.089e+43", "45.089e+43,<EOF>", 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''## !:>M.1=''', '''Error Token #''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test("9.635E+73", "9.635E+73,<EOF>", 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''"!'""''', '''!'",<EOF>''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("TKEPFUmc", "TKEPFUmc,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test('''"
e,'""''', '''
e,'",<EOF>''', 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("A@x&Rbl73", "A,Error Token @", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test('''## ^MYmZ''', '''Error Token #''', 198))

	def test_199(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 200))
