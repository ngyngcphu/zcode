import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test("ni$", "ni,Error Token $", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("Ov^Po6", "Ov,Error Token ^", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''## g(2@?0N#Q6i@S- ''', '''<EOF>''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''## a#%X(q3!~1X}`Q:J)NMh''', '''<EOF>''', 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''"\\g5'"'"'""''', '''Illegal Escape In String: \\g''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test("96.282E-41", "96.282E-41,<EOF>", 106))

	def test_107(self):
		self.assertTrue(TestLexer.test('''## ^QDt''', '''<EOF>''', 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("ekhJK1zN5", "ekhJK1zN5,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test("9.548", "9.548,<EOF>", 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''## {Y.''', '''<EOF>''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test("Ao39PsBcLP", "Ao39PsBcLP,<EOF>", 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("@ZadA", "Error Token @", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("82e-53", "82e-53,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("1pg", "1,pg,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("0.595E-18", "0.595E-18,<EOF>", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''## V>x<iP9#''', '''<EOF>''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''"a~ ''', '''Unclosed String: a~ ''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''## <d,$''', '''<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test("W", "W,<EOF>", 120))

	def test_121(self):
		self.assertTrue(TestLexer.test("2.660e13", "2.660e13,<EOF>", 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("UvH^VY", "UvH,Error Token ^", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("^R^wn", "Error Token ^", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("A&dd^j_K", "A,Error Token &", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test('''## %,MZW22s>Zhb#''', '''<EOF>''', 126))

	def test_127(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 127))

	def test_128(self):
		self.assertTrue(TestLexer.test("4zY6lk2y_", "4,zY6lk2y_,<EOF>", 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''## O~pmhN9B''', '''<EOF>''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''"l'""''', '''l'",<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''";'"\\hWz"''', '''Illegal Escape In String: ;'"\\h''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 133))

	def test_134(self):
		self.assertTrue(TestLexer.test("45.098e+41", "45.098e+41,<EOF>", 134))

	def test_135(self):
		self.assertTrue(TestLexer.test('''"M~'"y'""''', '''M~'"y'",<EOF>''', 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''## F@W*sx._^huh}n>t:''', '''<EOF>''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("62", "62,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''"\\dh'"@'"]"''', '''Illegal Escape In String: \\d''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("8.951", "8.951,<EOF>", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("BW", "BW,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## {XT;t3+Y*!''', '''<EOF>''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test("370.972", "370.972,<EOF>", 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''## t.''', '''<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("69E-37", "69E-37,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("510.834E+52", "510.834E+52,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test('''## X!jfM$.>SXqxMG?npU)m''', '''<EOF>''', 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''"\\eD'"R"''', '''Illegal Escape In String: \\e''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''"/\\m
8'""''', '''Illegal Escape In String: /\\m''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''## +00n#$UBU7*c}j;C]''', '''<EOF>''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''## t&<:a5#pN''', '''<EOF>''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test('''"yB'" ''', '''Unclosed String: yB'" ''', 152))

	def test_153(self):
		self.assertTrue(TestLexer.test('''## umMw#TPb i[L/l.P!1A''', '''<EOF>''', 153))

	def test_154(self):
		self.assertTrue(TestLexer.test('''## j:w54G~?IxbJLMpYl''', '''<EOF>''', 154))

	def test_155(self):
		self.assertTrue(TestLexer.test("fFMpBNSe", "fFMpBNSe,<EOF>", 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("2E+63", "2E+63,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("9.457", "9.457,<EOF>", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''"!"''', '''!,<EOF>''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test('''## {$&`FCL''', '''<EOF>''', 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## ;Hev''', '''<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test('''## :Lz7!2!&p0`5J9ZMQN''', '''<EOF>''', 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''## ~&=gj7''', '''<EOF>''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 163))

	def test_164(self):
		self.assertTrue(TestLexer.test("94.795", "94.795,<EOF>", 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("#tT^QahTP", "Error Token #", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("uXw_f5Gjn5", "uXw_f5Gjn5,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test('''"\\z'"'"'"'""''', '''Illegal Escape In String: \\z''', 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''## HGV.''', '''<EOF>''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test('''"9'"w\\e'"l"''', '''Illegal Escape In String: 9'"w\\e''', 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("E0hoHCsD7Q", "E0hoHCsD7Q,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''## /^)''', '''<EOF>''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test('''## bGq->N-.-;1W.[''', '''<EOF>''', 173))

	def test_174(self):
		self.assertTrue(TestLexer.test('''"'"'"Z'"F"''', '''\'"'"Z'"F,<EOF>''', 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("26e-13", "26e-13,<EOF>", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("3Pr", "3,Pr,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test('''## P:EyXjbISB6VE''', '''<EOF>''', 178))

	def test_179(self):
		self.assertTrue(TestLexer.test("zi", "zi,<EOF>", 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''".'"  ''', '''Unclosed String: .'"  ''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''## A0ii2Ss''', '''<EOF>''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''## kG+"f+S[<e''', '''<EOF>''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''"B\\h'"'"'""''', '''Illegal Escape In String: B\\h''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("84.254e-25", "84.254e-25,<EOF>", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("zw4AHYBy", "zw4AHYBy,<EOF>", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''"'"'"'"wm ''', '''Unclosed String: '"'"'"wm ''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("578.965", "578.965,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''"
'"'""''', '''Unclosed String: ''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''"1'""''', '''1'",<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("ALTmtnMfw", "ALTmtnMfw,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''## n"AhHmH9n~igL&>''', '''<EOF>''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test("88e+74", "88e+74,<EOF>", 193))

	def test_194(self):
		self.assertTrue(TestLexer.test("pFM^dnEOVJ", "pFM,Error Token ^", 194))

	def test_195(self):
		self.assertTrue(TestLexer.test('''"\\ie3'"''', '''Illegal Escape In String: \\i''', 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("TxyqOPK", "TxyqOPK,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("7.454E17", "7.454E17,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("aLL", "aLL,<EOF>", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("8.157E-14", "8.157E-14,<EOF>", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("17", "17,<EOF>", 200))
