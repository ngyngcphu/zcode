import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test('''## ,l)y82''', '''Error Token #''', 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("60.954", "60.954,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''## l0("`JM''', '''Error Token #''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''## *?``,=ZY''', '''Error Token #''', 104))

	# def test_105(self):
	# 	self.assertTrue(TestLexer.test('''"\\g'"n'""''', '''"\\g,Error Token '''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test("120e+90", "120e+90,<EOF>", 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("0.025", "0.025,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("23", "23,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''## kRSo"s9x''', '''Error Token #''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''"'"#'"'""''', '''\'"#'"'",<EOF>''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''## 3q#K91dAMP''', '''Error Token #''', 111))

	# def test_112(self):
	# 	self.assertTrue(TestLexer.test('''"'"ph'"\\j'""''', '''"'"ph'"\\j,Error Token '''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test('''"'"/"''', '''\'"/,<EOF>''', 113))

	def test_114(self):
		self.assertTrue(TestLexer.test('''"q
M'"b'""''', '''q
M'"b'",<EOF>''', 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("72.178", "72.178,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test('''## T8{a>kwBI;2<''', '''Error Token #''', 116))

	def test_117(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 117))

	def test_118(self):
		self.assertTrue(TestLexer.test("2Cy", "2,Cy,<EOF>", 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''"='" ''', '''Unclosed String: ='" ''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''## 8~/Nw$4aa7cqP''', '''Error Token #''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("561E-30", "561E-30,<EOF>", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("gcKFz", "gcKFz,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("87", "87,<EOF>", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("945e+92", "945e+92,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("6e+57", "6e+57,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test('''## 3!#y)/z9p{de5`0]35''', '''Error Token #''', 127))

	def test_128(self):
		self.assertTrue(TestLexer.test("53E00", "53E00,<EOF>", 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("1.097e+81", "1.097e+81,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''## ^2}NGyd{0f[?3M;E''', '''Error Token #''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test("1e-73", "1e-73,<EOF>", 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("21.370e+38", "21.370e+38,<EOF>", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''## n$+QN3q.E''', '''Error Token #''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("7.256", "7.256,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''"'"ph '""''', '''\'"ph '",<EOF>''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("T2K96u5u", "T2K96u5u,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''## )k]&*]xb''', '''Error Token #''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("w0Nnnsll", "w0Nnnsll,<EOF>", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("b5262", "b5262,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''"
;"''', '''
;,<EOF>''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test("jvLk", "jvLk,<EOF>", 142))

	# def test_143(self):
	# 	self.assertTrue(TestLexer.test('''"\\j'"E'"JJ"''', '''"\\j,Error Token '''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test("e1", "e1,<EOF>", 144))

	def test_145(self):
		self.assertTrue(TestLexer.test('''"X<~'", ''', '''Unclosed String: X<~'", ''', 145))

	def test_146(self):
		self.assertTrue(TestLexer.test('''## #(6WJou~$DjruK`fj''', '''Error Token #''', 146))

	# def test_147(self):
	# 	self.assertTrue(TestLexer.test('''"\\j'""''', '''"\\j,Error Token '''', 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''## .Y->nsUb{5Z}L''', '''Error Token #''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test("P8kYR^aZ", "P8kYR,Error Token ^", 149))

	def test_150(self):
		self.assertTrue(TestLexer.test("251.139", "251.139,<EOF>", 150))

	def test_151(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("eCQ", "eCQ,<EOF>", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("44", "44,<EOF>", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test('''## y4odMu@''', '''Error Token #''', 154))

	# def test_155(self):
	# 	self.assertTrue(TestLexer.test('''"N/\\d'""''', '''"N/\\d,Error Token '''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''## oOjXzG}3''', '''Error Token #''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''## 6_".Au2#d2Q2_''', '''Error Token #''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("cNU", "cNU,<EOF>", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 159))

	def test_160(self):
		self.assertTrue(TestLexer.test("663.057", "663.057,<EOF>", 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("jJ4", "jJ4,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test("$ZJK&nNWC1", "Error Token $", 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("&", "Error Token &", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test("G4137ms3", "G4137ms3,<EOF>", 164))

	def test_165(self):
		self.assertTrue(TestLexer.test('''## 43j])0''', '''Error Token #''', 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("SQkff", "SQkff,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("5.561", "5.561,<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test("yGuZlo", "yGuZlo,<EOF>", 168))

	def test_169(self):
		self.assertTrue(TestLexer.test('''## mn)B%o0 BNb^.n''', '''Error Token #''', 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("GPpd", "GPpd,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test("S^P", "S,Error Token ^", 171))

	def test_172(self):
		self.assertTrue(TestLexer.test("X2pqGF", "X2pqGF,<EOF>", 172))

# 	def test_173(self):
# 		self.assertTrue(TestLexer.test('''"'"
# \\j'""''', '''"'"
# \\j,Error Token '''', 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("f", "f,<EOF>", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''## !xz.hO.oFDuO''', '''Error Token #''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("6.058E00", "6.058E00,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("Xv9", "Xv9,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''"o'"A ''', '''Unclosed String: o'"A ''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test("ymG", "ymG,<EOF>", 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''## 0-S+D ~;WA&U%t|sU$''', '''Error Token #''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''"'"n'"P"''', '''\'"n'"P,<EOF>''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''## 6j>OOLB7s>TL>c_VsR''', '''Error Token #''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("f9fO$&7", "f9fO,Error Token $", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''## k_icdHd0p<I51z[B0TX?''', '''Error Token #''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test("233.450", "233.450,<EOF>", 187))

	# def test_188(self):
	# 	self.assertTrue(TestLexer.test('''"\\l'"["''', '''"\\l,Error Token '''', 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''"O'"'"N ''', '''Unclosed String: O'"'"N ''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test("mmiD7b", "mmiD7b,<EOF>", 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("44", "44,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test("2E+63", "2E+63,<EOF>", 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''## 0{tW|jxb%h_>b(Z''', '''Error Token #''', 193))

	# def test_194(self):
	# 	self.assertTrue(TestLexer.test('''"\\i'""''', '''"\\i,Error Token '''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test('''"'"'" "''', '''\'"'" ,<EOF>''', 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("pve6u", "pve6u,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("966.281E04", "966.281E04,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test('''"\\pp"''', '''"\\p,p,Unclosed String: ''', 198))
