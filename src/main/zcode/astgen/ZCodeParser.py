# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u01bb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\7\2X\n\2\f\2\16")
        buf.write("\2[\13\2\3\2\3\2\6\2_\n\2\r\2\16\2`\3\2\5\2d\n\2\6\2f")
        buf.write("\n\2\r\2\16\2g\3\2\3\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3y\n\3\5\3{\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\7\4\u0083\n\4\f\4\16\4\u0086\13\4\3\4\3\4\5")
        buf.write("\4\u008a\n\4\3\4\6\4\u008d\n\4\r\4\16\4\u008e\3\4\3\4")
        buf.write("\6\4\u0093\n\4\r\4\16\4\u0094\3\4\6\4\u0098\n\4\r\4\16")
        buf.write("\4\u0099\5\4\u009c\n\4\3\5\3\5\5\5\u00a0\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6\u00a7\n\6\3\7\3\7\3\7\5\7\u00ac\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b7\n\b\3\t\3\t")
        buf.write("\6\t\u00bb\n\t\r\t\16\t\u00bc\3\t\3\t\3\t\3\t\7\t\u00c3")
        buf.write("\n\t\f\t\16\t\u00c6\13\t\5\t\u00c8\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\5\13\u00d0\n\13\3\f\3\f\7\f\u00d4\n\f\f\f\16")
        buf.write("\f\u00d7\13\f\3\f\5\f\u00da\n\f\3\r\3\r\3\r\3\r\3\r\7")
        buf.write("\r\u00e1\n\r\f\r\16\r\u00e4\13\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\7\16\u00ed\n\16\f\16\16\16\u00f0\13\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\7\20\u00fe\n\20\f\20\16\20\u0101\13\20\3\20\3\20\3\21")
        buf.write("\3\21\5\21\u0107\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u010f\n\22\3\23\3\23\5\23\u0113\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u011a\n\24\3\25\3\25\6\25\u011e\n\25\r")
        buf.write("\25\16\25\u011f\3\25\5\25\u0123\n\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u012d\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u0154\n\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3 \5 \u015f\n \3!\3!\5!\u0163\n!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u016a\n\"\3#\3#\5#\u016e\n#\3#\3#\3#\3#\3$\3$\3$")
        buf.write("\3$\3$\5$\u0179\n$\3%\3%\3%\3%\3%\5%\u0180\n%\3&\3&\3")
        buf.write("&\3&\3&\3&\7&\u0188\n&\f&\16&\u018b\13&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\7\'\u0193\n\'\f\'\16\'\u0196\13\'\3(\3(\3(")
        buf.write("\3(\3(\3(\7(\u019e\n(\f(\16(\u01a1\13(\3)\3)\3)\5)\u01a6")
        buf.write("\n)\3*\3*\3*\5*\u01ab\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\5+\u01b9\n+\3+\3\u00d5\5JLN,\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRT\2\b\4\2\13\r\20\20\3\2\13\r\5\2!!#\'))\3\2+,\3\2")
        buf.write("\34\35\3\2\36 \2\u01d2\2Y\3\2\2\2\4z\3\2\2\2\6|\3\2\2")
        buf.write("\2\b\u009f\3\2\2\2\n\u00a6\3\2\2\2\f\u00ab\3\2\2\2\16")
        buf.write("\u00b6\3\2\2\2\20\u00c7\3\2\2\2\22\u00c9\3\2\2\2\24\u00cf")
        buf.write("\3\2\2\2\26\u00d1\3\2\2\2\30\u00db\3\2\2\2\32\u00e7\3")
        buf.write("\2\2\2\34\u00f3\3\2\2\2\36\u00f6\3\2\2\2 \u0104\3\2\2")
        buf.write("\2\"\u010e\3\2\2\2$\u0112\3\2\2\2&\u0119\3\2\2\2(\u011b")
        buf.write("\3\2\2\2*\u012c\3\2\2\2,\u012e\3\2\2\2.\u0132\3\2\2\2")
        buf.write("\60\u0137\3\2\2\2\62\u013b\3\2\2\2\64\u0140\3\2\2\2\66")
        buf.write("\u0144\3\2\2\28\u0149\3\2\2\2:\u0153\3\2\2\2<\u0155\3")
        buf.write("\2\2\2>\u015e\3\2\2\2@\u0162\3\2\2\2B\u0169\3\2\2\2D\u016d")
        buf.write("\3\2\2\2F\u0178\3\2\2\2H\u017f\3\2\2\2J\u0181\3\2\2\2")
        buf.write("L\u018c\3\2\2\2N\u0197\3\2\2\2P\u01a5\3\2\2\2R\u01aa\3")
        buf.write("\2\2\2T\u01b8\3\2\2\2VX\7\65\2\2WV\3\2\2\2X[\3\2\2\2Y")
        buf.write("W\3\2\2\2YZ\3\2\2\2Ze\3\2\2\2[Y\3\2\2\2\\^\5\4\3\2]_\7")
        buf.write("\65\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ad\3\2")
        buf.write("\2\2bd\5\6\4\2c\\\3\2\2\2cb\3\2\2\2df\3\2\2\2ec\3\2\2")
        buf.write("\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\2\2\3j")
        buf.write("\3\3\2\2\2kl\t\2\2\2lo\7\64\2\2mn\7\"\2\2np\5F$\2om\3")
        buf.write("\2\2\2op\3\2\2\2p{\3\2\2\2qr\7\17\2\2rs\7\64\2\2st\7\"")
        buf.write("\2\2t{\5F$\2ux\58\35\2vw\7\"\2\2wy\5F$\2xv\3\2\2\2xy\3")
        buf.write("\2\2\2y{\3\2\2\2zk\3\2\2\2zq\3\2\2\2zu\3\2\2\2{\5\3\2")
        buf.write("\2\2|}\7\21\2\2}~\7\64\2\2~\177\7-\2\2\177\u0080\5\b\5")
        buf.write("\2\u0080\u0084\7.\2\2\u0081\u0083\7\65\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0089\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0087\u008a\5 \21\2\u0088\u008a\5(\25\2\u0089\u0087\3")
        buf.write("\2\2\2\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u009b")
        buf.write("\3\2\2\2\u008b\u008d\7\65\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0092\5\20\t\2\u0091\u0093")
        buf.write("\7\65\2\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u009c\3\2\2\2")
        buf.write("\u0096\u0098\7\65\2\2\u0097\u0096\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009c\3\2\2\2\u009b\u008c\3\2\2\2\u009b\u0097\3\2\2\2")
        buf.write("\u009c\7\3\2\2\2\u009d\u00a0\5\n\6\2\u009e\u00a0\3\2\2")
        buf.write("\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\t\3\2")
        buf.write("\2\2\u00a1\u00a2\5\f\7\2\u00a2\u00a3\7\61\2\2\u00a3\u00a4")
        buf.write("\5\n\6\2\u00a4\u00a7\3\2\2\2\u00a5\u00a7\5\f\7\2\u00a6")
        buf.write("\u00a1\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\13\3\2\2\2\u00a8")
        buf.write("\u00a9\t\3\2\2\u00a9\u00ac\7\64\2\2\u00aa\u00ac\58\35")
        buf.write("\2\u00ab\u00a8\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\r\3\2")
        buf.write("\2\2\u00ad\u00b7\5\4\3\2\u00ae\u00b7\5\22\n\2\u00af\u00b7")
        buf.write("\5\26\f\2\u00b0\u00b7\5\36\20\2\u00b1\u00b7\7\25\2\2\u00b2")
        buf.write("\u00b7\7\26\2\2\u00b3\u00b7\5 \21\2\u00b4\u00b7\5\"\22")
        buf.write("\2\u00b5\u00b7\5(\25\2\u00b6\u00ad\3\2\2\2\u00b6\u00ae")
        buf.write("\3\2\2\2\u00b6\u00af\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6")
        buf.write("\u00b1\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b3\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\17\3\2")
        buf.write("\2\2\u00b8\u00ba\5\16\b\2\u00b9\u00bb\7\65\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\5\20\t")
        buf.write("\2\u00bf\u00c8\3\2\2\2\u00c0\u00c4\5\16\b\2\u00c1\u00c3")
        buf.write("\7\65\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c8\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c7\u00b8\3\2\2\2\u00c7\u00c0\3")
        buf.write("\2\2\2\u00c8\21\3\2\2\2\u00c9\u00ca\5\24\13\2\u00ca\u00cb")
        buf.write("\7\"\2\2\u00cb\u00cc\5F$\2\u00cc\23\3\2\2\2\u00cd\u00d0")
        buf.write("\7\64\2\2\u00ce\u00d0\5D#\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\25\3\2\2\2\u00d1\u00d5\5\30\r\2\u00d2")
        buf.write("\u00d4\5\32\16\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2")
        buf.write("\2\u00d5\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d9")
        buf.write("\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00da\5\34\17\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\27\3\2\2\2\u00db")
        buf.write("\u00dc\7\27\2\2\u00dc\u00dd\7-\2\2\u00dd\u00de\5F$\2\u00de")
        buf.write("\u00e2\7.\2\2\u00df\u00e1\7\65\2\2\u00e0\u00df\3\2\2\2")
        buf.write("\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6")
        buf.write("\5\20\t\2\u00e6\31\3\2\2\2\u00e7\u00e8\7\31\2\2\u00e8")
        buf.write("\u00e9\7-\2\2\u00e9\u00ea\5F$\2\u00ea\u00ee\7.\2\2\u00eb")
        buf.write("\u00ed\7\65\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\5\20\t\2\u00f2")
        buf.write("\33\3\2\2\2\u00f3\u00f4\7\30\2\2\u00f4\u00f5\5\20\t\2")
        buf.write("\u00f5\35\3\2\2\2\u00f6\u00f7\7\22\2\2\u00f7\u00f8\7\64")
        buf.write("\2\2\u00f8\u00f9\7\23\2\2\u00f9\u00fa\5F$\2\u00fa\u00fb")
        buf.write("\7\24\2\2\u00fb\u00ff\5F$\2\u00fc\u00fe\7\65\2\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3")
        buf.write("\2\2\2\u0102\u0103\5\20\t\2\u0103\37\3\2\2\2\u0104\u0106")
        buf.write("\7\16\2\2\u0105\u0107\5F$\2\u0106\u0105\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107!\3\2\2\2\u0108\u0109\7\64\2\2\u0109")
        buf.write("\u010a\7-\2\2\u010a\u010b\5$\23\2\u010b\u010c\7.\2\2\u010c")
        buf.write("\u010f\3\2\2\2\u010d\u010f\5*\26\2\u010e\u0108\3\2\2\2")
        buf.write("\u010e\u010d\3\2\2\2\u010f#\3\2\2\2\u0110\u0113\5&\24")
        buf.write("\2\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111")
        buf.write("\3\2\2\2\u0113%\3\2\2\2\u0114\u0115\5F$\2\u0115\u0116")
        buf.write("\7\61\2\2\u0116\u0117\5&\24\2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u011a\5F$\2\u0119\u0114\3\2\2\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("\'\3\2\2\2\u011b\u011d\7\32\2\2\u011c\u011e\7\65\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u0123\5")
        buf.write("\20\t\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\u0125\7\33\2\2\u0125)\3\2\2\2\u0126")
        buf.write("\u012d\5,\27\2\u0127\u012d\5.\30\2\u0128\u012d\5\60\31")
        buf.write("\2\u0129\u012d\5\62\32\2\u012a\u012d\5\64\33\2\u012b\u012d")
        buf.write("\5\66\34\2\u012c\u0126\3\2\2\2\u012c\u0127\3\2\2\2\u012c")
        buf.write("\u0128\3\2\2\2\u012c\u0129\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012b\3\2\2\2\u012d+\3\2\2\2\u012e\u012f\7\3\2")
        buf.write("\2\u012f\u0130\7-\2\2\u0130\u0131\7.\2\2\u0131-\3\2\2")
        buf.write("\2\u0132\u0133\7\4\2\2\u0133\u0134\7-\2\2\u0134\u0135")
        buf.write("\5F$\2\u0135\u0136\7.\2\2\u0136/\3\2\2\2\u0137\u0138\7")
        buf.write("\5\2\2\u0138\u0139\7-\2\2\u0139\u013a\7.\2\2\u013a\61")
        buf.write("\3\2\2\2\u013b\u013c\7\6\2\2\u013c\u013d\7-\2\2\u013d")
        buf.write("\u013e\5F$\2\u013e\u013f\7.\2\2\u013f\63\3\2\2\2\u0140")
        buf.write("\u0141\7\7\2\2\u0141\u0142\7-\2\2\u0142\u0143\7.\2\2\u0143")
        buf.write("\65\3\2\2\2\u0144\u0145\7\b\2\2\u0145\u0146\7-\2\2\u0146")
        buf.write("\u0147\5F$\2\u0147\u0148\7.\2\2\u0148\67\3\2\2\2\u0149")
        buf.write("\u014a\t\3\2\2\u014a\u014b\7\64\2\2\u014b\u014c\7/\2\2")
        buf.write("\u014c\u014d\5:\36\2\u014d\u014e\7\60\2\2\u014e9\3\2\2")
        buf.write("\2\u014f\u0150\7\62\2\2\u0150\u0151\7\61\2\2\u0151\u0154")
        buf.write("\5:\36\2\u0152\u0154\7\62\2\2\u0153\u014f\3\2\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154;\3\2\2\2\u0155\u0156\7/\2\2\u0156")
        buf.write("\u0157\5> \2\u0157\u0158\7\60\2\2\u0158=\3\2\2\2\u0159")
        buf.write("\u015a\5@!\2\u015a\u015b\7\61\2\2\u015b\u015c\5> \2\u015c")
        buf.write("\u015f\3\2\2\2\u015d\u015f\5@!\2\u015e\u0159\3\2\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f?\3\2\2\2\u0160\u0163\5<\37\2\u0161")
        buf.write("\u0163\5B\"\2\u0162\u0160\3\2\2\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163A\3\2\2\2\u0164\u0165\5F$\2\u0165\u0166\7\61\2\2")
        buf.write("\u0166\u0167\5B\"\2\u0167\u016a\3\2\2\2\u0168\u016a\5")
        buf.write("F$\2\u0169\u0164\3\2\2\2\u0169\u0168\3\2\2\2\u016aC\3")
        buf.write("\2\2\2\u016b\u016e\7\64\2\2\u016c\u016e\5\"\22\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0170\7/\2\2\u0170\u0171\5B\"\2\u0171\u0172\7\60")
        buf.write("\2\2\u0172E\3\2\2\2\u0173\u0174\5H%\2\u0174\u0175\7(\2")
        buf.write("\2\u0175\u0176\5H%\2\u0176\u0179\3\2\2\2\u0177\u0179\5")
        buf.write("H%\2\u0178\u0173\3\2\2\2\u0178\u0177\3\2\2\2\u0179G\3")
        buf.write("\2\2\2\u017a\u017b\5J&\2\u017b\u017c\t\4\2\2\u017c\u017d")
        buf.write("\5J&\2\u017d\u0180\3\2\2\2\u017e\u0180\5J&\2\u017f\u017a")
        buf.write("\3\2\2\2\u017f\u017e\3\2\2\2\u0180I\3\2\2\2\u0181\u0182")
        buf.write("\b&\1\2\u0182\u0183\5L\'\2\u0183\u0189\3\2\2\2\u0184\u0185")
        buf.write("\f\4\2\2\u0185\u0186\t\5\2\2\u0186\u0188\5L\'\2\u0187")
        buf.write("\u0184\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018aK\3\2\2\2\u018b\u0189\3\2\2")
        buf.write("\2\u018c\u018d\b\'\1\2\u018d\u018e\5N(\2\u018e\u0194\3")
        buf.write("\2\2\2\u018f\u0190\f\4\2\2\u0190\u0191\t\6\2\2\u0191\u0193")
        buf.write("\5N(\2\u0192\u018f\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195M\3\2\2\2\u0196\u0194")
        buf.write("\3\2\2\2\u0197\u0198\b(\1\2\u0198\u0199\5P)\2\u0199\u019f")
        buf.write("\3\2\2\2\u019a\u019b\f\4\2\2\u019b\u019c\t\7\2\2\u019c")
        buf.write("\u019e\5P)\2\u019d\u019a\3\2\2\2\u019e\u01a1\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0O\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a2\u01a3\7*\2\2\u01a3\u01a6\5P)\2\u01a4")
        buf.write("\u01a6\5R*\2\u01a5\u01a2\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("Q\3\2\2\2\u01a7\u01a8\7\35\2\2\u01a8\u01ab\5R*\2\u01a9")
        buf.write("\u01ab\5T+\2\u01aa\u01a7\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("S\3\2\2\2\u01ac\u01b9\5<\37\2\u01ad\u01b9\5D#\2\u01ae")
        buf.write("\u01b9\5\"\22\2\u01af\u01b0\7-\2\2\u01b0\u01b1\5F$\2\u01b1")
        buf.write("\u01b2\7.\2\2\u01b2\u01b9\3\2\2\2\u01b3\u01b9\7\62\2\2")
        buf.write("\u01b4\u01b9\7\t\2\2\u01b5\u01b9\7\n\2\2\u01b6\u01b9\7")
        buf.write("\63\2\2\u01b7\u01b9\7\64\2\2\u01b8\u01ac\3\2\2\2\u01b8")
        buf.write("\u01ad\3\2\2\2\u01b8\u01ae\3\2\2\2\u01b8\u01af\3\2\2\2")
        buf.write("\u01b8\u01b3\3\2\2\2\u01b8\u01b4\3\2\2\2\u01b8\u01b5\3")
        buf.write("\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9U")
        buf.write("\3\2\2\2\60Y`cgoxz\u0084\u0089\u008e\u0094\u0099\u009b")
        buf.write("\u009f\u00a6\u00ab\u00b6\u00bc\u00c4\u00c7\u00cf\u00d5")
        buf.write("\u00d9\u00e2\u00ee\u00ff\u0106\u010e\u0112\u0119\u011f")
        buf.write("\u0122\u012c\u0153\u015e\u0162\u0169\u016d\u0178\u017f")
        buf.write("\u0189\u0194\u019f\u01a5\u01aa\u01b8")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'writeBool'", "'readString'", "'writeString'", "'true'", 
                     "'false'", "'number'", "'bool'", "'string'", "'return'", 
                     "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'...'", "'=='", "'not'", "'and'", "'or'", 
                     "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TRUE", "FALSE", 
                      "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "ADD_OF", "SUB_OF", 
                      "MUL_OF", "DIV_OF", "MOD_OF", "EQUAL_OP", "ASSIGN", 
                      "NOT_EQUAL_OP", "LESS_THAN_OP", "LESS_EQUAL_OP", "GREATER_THAN_OP", 
                      "GREATER_EQUAL_OP", "CONCAT_OP", "STRING_COMPARE_OP", 
                      "NOT_OP", "AND_OP", "OR_OP", "LB", "RB", "LS", "RS", 
                      "COMMA", "NUMBERLIT", "STRINGLIT", "IDENTIFIER", "NEWLINE", 
                      "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_varDecl = 1
    RULE_functionDecl = 2
    RULE_paramList = 3
    RULE_paramPrime = 4
    RULE_formalParameter = 5
    RULE_statement_type = 6
    RULE_statement_list = 7
    RULE_assign_stat = 8
    RULE_lhs = 9
    RULE_if_stat = 10
    RULE_if_fragment = 11
    RULE_elif_fragment = 12
    RULE_else_fragment = 13
    RULE_for_stat = 14
    RULE_return_stat = 15
    RULE_func_call_stat = 16
    RULE_arglist = 17
    RULE_argprime = 18
    RULE_block_stat = 19
    RULE_io_function = 20
    RULE_read_number = 21
    RULE_write_number = 22
    RULE_read_bool = 23
    RULE_write_bool = 24
    RULE_read_string = 25
    RULE_write_string = 26
    RULE_array_type = 27
    RULE_dimension_list = 28
    RULE_array_value = 29
    RULE_array_elements = 30
    RULE_array_nested_or_expression = 31
    RULE_exprlist = 32
    RULE_index_expr = 33
    RULE_expression = 34
    RULE_expression_1 = 35
    RULE_expression_2 = 36
    RULE_expression_3 = 37
    RULE_expression_4 = 38
    RULE_expression_5 = 39
    RULE_expression_6 = 40
    RULE_expression_7 = 41

    ruleNames =  [ "program", "varDecl", "functionDecl", "paramList", "paramPrime", 
                   "formalParameter", "statement_type", "statement_list", 
                   "assign_stat", "lhs", "if_stat", "if_fragment", "elif_fragment", 
                   "else_fragment", "for_stat", "return_stat", "func_call_stat", 
                   "arglist", "argprime", "block_stat", "io_function", "read_number", 
                   "write_number", "read_bool", "write_bool", "read_string", 
                   "write_string", "array_type", "dimension_list", "array_value", 
                   "array_elements", "array_nested_or_expression", "exprlist", 
                   "index_expr", "expression", "expression_1", "expression_2", 
                   "expression_3", "expression_4", "expression_5", "expression_6", 
                   "expression_7" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    TRUE=7
    FALSE=8
    NUMBER=9
    BOOL=10
    STRING=11
    RETURN=12
    VAR=13
    DYNAMIC=14
    FUNC=15
    FOR=16
    UNTIL=17
    BY=18
    BREAK=19
    CONTINUE=20
    IF=21
    ELSE=22
    ELIF=23
    BEGIN=24
    END=25
    ADD_OF=26
    SUB_OF=27
    MUL_OF=28
    DIV_OF=29
    MOD_OF=30
    EQUAL_OP=31
    ASSIGN=32
    NOT_EQUAL_OP=33
    LESS_THAN_OP=34
    LESS_EQUAL_OP=35
    GREATER_THAN_OP=36
    GREATER_EQUAL_OP=37
    CONCAT_OP=38
    STRING_COMPARE_OP=39
    NOT_OP=40
    AND_OP=41
    OR_OP=42
    LB=43
    RB=44
    LS=45
    RS=46
    COMMA=47
    NUMBERLIT=48
    STRINGLIT=49
    IDENTIFIER=50
    NEWLINE=51
    COMMENT=52
    WS=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    ERROR_CHAR=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.VarDeclContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 84
                self.match(ZCodeParser.NEWLINE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                    self.state = 90
                    self.varDecl()
                    self.state = 92 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 91
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 94 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ZCodeParser.NEWLINE):
                            break

                    pass
                elif token in [ZCodeParser.FUNC]:
                    self.state = 96
                    self.functionDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC))) != 0)):
                    break

            self.state = 103
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ZCodeParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.DYNAMIC))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 107
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 108
                    self.expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(ZCodeParser.VAR)
                self.state = 112
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 113
                self.match(ZCodeParser.ASSIGN)
                self.state = 114
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.array_type()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 116
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 117
                    self.expression()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamListContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def return_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statContext,0)


        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = ZCodeParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ZCodeParser.FUNC)
            self.state = 123
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 124
            self.match(ZCodeParser.LB)
            self.state = 125
            self.paramList()
            self.state = 126
            self.match(ZCodeParser.RB)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 127
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 133
                self.return_stat()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 134
                self.block_stat()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                pass
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 138 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 137
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 140 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 142
                self.statement_list()
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 143
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 146 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass

            elif la_ == 2:
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 148
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 151 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = ZCodeParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.paramPrime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self):
            return self.getTypedRuleContext(ZCodeParser.FormalParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamPrime" ):
                return visitor.visitParamPrime(self)
            else:
                return visitor.visitChildren(self)




    def paramPrime(self):

        localctx = ZCodeParser.ParamPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramPrime)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.formalParameter()
                self.state = 160
                self.match(ZCodeParser.COMMA)
                self.state = 161
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.formalParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_formalParameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameter" ):
                return visitor.visitFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def formalParameter(self):

        localctx = ZCodeParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 167
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclContext,0)


        def assign_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_statContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(ZCodeParser.If_statContext,0)


        def for_stat(self):
            return self.getTypedRuleContext(ZCodeParser.For_statContext,0)


        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def return_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statContext,0)


        def func_call_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_statContext,0)


        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_type" ):
                return visitor.visitStatement_type(self)
            else:
                return visitor.visitChildren(self)




    def statement_type(self):

        localctx = ZCodeParser.Statement_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement_type)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.assign_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.if_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.for_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.match(ZCodeParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.match(ZCodeParser.CONTINUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 177
                self.return_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 178
                self.func_call_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 179
                self.block_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_type(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_typeContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.statement_type()
                self.state = 184 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 183
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 186 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 188
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.statement_type()
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 191
                        self.match(ZCodeParser.NEWLINE) 
                    self.state = 196
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stat" ):
                return visitor.visitAssign_stat(self)
            else:
                return visitor.visitChildren(self)




    def assign_stat(self):

        localctx = ZCodeParser.Assign_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.lhs()
            self.state = 200
            self.match(ZCodeParser.ASSIGN)
            self.state = 201
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lhs)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.index_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_fragment(self):
            return self.getTypedRuleContext(ZCodeParser.If_fragmentContext,0)


        def elif_fragment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_fragmentContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_fragmentContext,i)


        def else_fragment(self):
            return self.getTypedRuleContext(ZCodeParser.Else_fragmentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stat" ):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




    def if_stat(self):

        localctx = ZCodeParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.if_fragment()
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 208
                    self.elif_fragment() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 214
                self.else_fragment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_fragmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_fragment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_fragment" ):
                return visitor.visitIf_fragment(self)
            else:
                return visitor.visitChildren(self)




    def if_fragment(self):

        localctx = ZCodeParser.If_fragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_fragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.IF)
            self.state = 218
            self.match(ZCodeParser.LB)
            self.state = 219
            self.expression()
            self.state = 220
            self.match(ZCodeParser.RB)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 221
                self.match(ZCodeParser.NEWLINE)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_fragmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_fragment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_fragment" ):
                return visitor.visitElif_fragment(self)
            else:
                return visitor.visitChildren(self)




    def elif_fragment(self):

        localctx = ZCodeParser.Elif_fragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elif_fragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ZCodeParser.ELIF)
            self.state = 230
            self.match(ZCodeParser.LB)
            self.state = 231
            self.expression()
            self.state = 232
            self.match(ZCodeParser.RB)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 233
                self.match(ZCodeParser.NEWLINE)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_fragmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_fragment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_fragment" ):
                return visitor.visitElse_fragment(self)
            else:
                return visitor.visitChildren(self)




    def else_fragment(self):

        localctx = ZCodeParser.Else_fragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_else_fragment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.ELSE)
            self.state = 242
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stat" ):
                return visitor.visitFor_stat(self)
            else:
                return visitor.visitChildren(self)




    def for_stat(self):

        localctx = ZCodeParser.For_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ZCodeParser.FOR)
            self.state = 245
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 246
            self.match(ZCodeParser.UNTIL)
            self.state = 247
            self.expression()
            self.state = 248
            self.match(ZCodeParser.BY)
            self.state = 249
            self.expression()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 250
                self.match(ZCodeParser.NEWLINE)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stat" ):
                return visitor.visitReturn_stat(self)
            else:
                return visitor.visitChildren(self)




    def return_stat(self):

        localctx = ZCodeParser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_return_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.RETURN)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.SUB_OF) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 259
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def arglist(self):
            return self.getTypedRuleContext(ZCodeParser.ArglistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def io_function(self):
            return self.getTypedRuleContext(ZCodeParser.Io_functionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stat" ):
                return visitor.visitFunc_call_stat(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stat(self):

        localctx = ZCodeParser.Func_call_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_call_stat)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 263
                self.match(ZCodeParser.LB)
                self.state = 264
                self.arglist()
                self.state = 265
                self.match(ZCodeParser.RB)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.io_function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = ZCodeParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arglist)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB_OF, ZCodeParser.NOT_OP, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.argprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgprime" ):
                return visitor.visitArgprime(self)
            else:
                return visitor.visitChildren(self)




    def argprime(self):

        localctx = ZCodeParser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_argprime)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.expression()
                self.state = 275
                self.match(ZCodeParser.COMMA)
                self.state = 276
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stat" ):
                return visitor.visitBlock_stat(self)
            else:
                return visitor.visitChildren(self)




    def block_stat(self):

        localctx = ZCodeParser.Block_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.BEGIN)
            self.state = 283 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 282
                self.match(ZCodeParser.NEWLINE)
                self.state = 285 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 287
                self.statement_list()


            self.state = 290
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def read_number(self):
            return self.getTypedRuleContext(ZCodeParser.Read_numberContext,0)


        def write_number(self):
            return self.getTypedRuleContext(ZCodeParser.Write_numberContext,0)


        def read_bool(self):
            return self.getTypedRuleContext(ZCodeParser.Read_boolContext,0)


        def write_bool(self):
            return self.getTypedRuleContext(ZCodeParser.Write_boolContext,0)


        def read_string(self):
            return self.getTypedRuleContext(ZCodeParser.Read_stringContext,0)


        def write_string(self):
            return self.getTypedRuleContext(ZCodeParser.Write_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_io_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_function" ):
                return visitor.visitIo_function(self)
            else:
                return visitor.visitChildren(self)




    def io_function(self):

        localctx = ZCodeParser.Io_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_io_function)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.read_number()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.write_number()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.read_bool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.write_bool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 296
                self.read_string()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 297
                self.write_string()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_read_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_number" ):
                return visitor.visitRead_number(self)
            else:
                return visitor.visitChildren(self)




    def read_number(self):

        localctx = ZCodeParser.Read_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_read_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.T__0)
            self.state = 301
            self.match(ZCodeParser.LB)
            self.state = 302
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_write_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_number" ):
                return visitor.visitWrite_number(self)
            else:
                return visitor.visitChildren(self)




    def write_number(self):

        localctx = ZCodeParser.Write_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_write_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ZCodeParser.T__1)
            self.state = 305
            self.match(ZCodeParser.LB)
            self.state = 306
            self.expression()
            self.state = 307
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_read_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_bool" ):
                return visitor.visitRead_bool(self)
            else:
                return visitor.visitChildren(self)




    def read_bool(self):

        localctx = ZCodeParser.Read_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_read_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(ZCodeParser.T__2)
            self.state = 310
            self.match(ZCodeParser.LB)
            self.state = 311
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_write_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_bool" ):
                return visitor.visitWrite_bool(self)
            else:
                return visitor.visitChildren(self)




    def write_bool(self):

        localctx = ZCodeParser.Write_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_write_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(ZCodeParser.T__3)
            self.state = 314
            self.match(ZCodeParser.LB)
            self.state = 315
            self.expression()
            self.state = 316
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_read_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_string" ):
                return visitor.visitRead_string(self)
            else:
                return visitor.visitChildren(self)




    def read_string(self):

        localctx = ZCodeParser.Read_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_read_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(ZCodeParser.T__4)
            self.state = 319
            self.match(ZCodeParser.LB)
            self.state = 320
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_write_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_string" ):
                return visitor.visitWrite_string(self)
            else:
                return visitor.visitChildren(self)




    def write_string(self):

        localctx = ZCodeParser.Write_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_write_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(ZCodeParser.T__5)
            self.state = 323
            self.match(ZCodeParser.LB)
            self.state = 324
            self.expression()
            self.state = 325
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dimension_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = ZCodeParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 328
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 329
            self.match(ZCodeParser.LS)
            self.state = 330
            self.dimension_list()
            self.state = 331
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dimension_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list" ):
                return visitor.visitDimension_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list(self):

        localctx = ZCodeParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_dimension_list)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 334
                self.match(ZCodeParser.COMMA)
                self.state = 335
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(ZCodeParser.NUMBERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def array_elements(self):
            return self.getTypedRuleContext(ZCodeParser.Array_elementsContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(ZCodeParser.LS)
            self.state = 340
            self.array_elements()
            self.state = 341
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_nested_or_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Array_nested_or_expressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_elements(self):
            return self.getTypedRuleContext(ZCodeParser.Array_elementsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elements" ):
                return visitor.visitArray_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_elements(self):

        localctx = ZCodeParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_elements)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.array_nested_or_expression()
                self.state = 344
                self.match(ZCodeParser.COMMA)
                self.state = 345
                self.array_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.array_nested_or_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_nested_or_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_nested_or_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_nested_or_expression" ):
                return visitor.visitArray_nested_or_expression(self)
            else:
                return visitor.visitChildren(self)




    def array_nested_or_expression(self):

        localctx = ZCodeParser.Array_nested_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_nested_or_expression)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.exprlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exprlist)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.expression()
                self.state = 355
                self.match(ZCodeParser.COMMA)
                self.state = 356
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_call_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 361
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 362
                self.func_call_stat()
                pass


            self.state = 365
            self.match(ZCodeParser.LS)
            self.state = 366
            self.exprlist()
            self.state = 367
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression_1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression_1Context,i)


        def CONCAT_OP(self):
            return self.getToken(ZCodeParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.expression_1()
                self.state = 370
                self.match(ZCodeParser.CONCAT_OP)
                self.state = 371
                self.expression_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.expression_1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression_2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression_2Context,i)


        def EQUAL_OP(self):
            return self.getToken(ZCodeParser.EQUAL_OP, 0)

        def STRING_COMPARE_OP(self):
            return self.getToken(ZCodeParser.STRING_COMPARE_OP, 0)

        def NOT_EQUAL_OP(self):
            return self.getToken(ZCodeParser.NOT_EQUAL_OP, 0)

        def LESS_THAN_OP(self):
            return self.getToken(ZCodeParser.LESS_THAN_OP, 0)

        def GREATER_THAN_OP(self):
            return self.getToken(ZCodeParser.GREATER_THAN_OP, 0)

        def LESS_EQUAL_OP(self):
            return self.getToken(ZCodeParser.LESS_EQUAL_OP, 0)

        def GREATER_EQUAL_OP(self):
            return self.getToken(ZCodeParser.GREATER_EQUAL_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_1" ):
                return visitor.visitExpression_1(self)
            else:
                return visitor.visitChildren(self)




    def expression_1(self):

        localctx = ZCodeParser.Expression_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression_1)
        self._la = 0 # Token type
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.expression_2(0)
                self.state = 377
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_OP) | (1 << ZCodeParser.NOT_EQUAL_OP) | (1 << ZCodeParser.LESS_THAN_OP) | (1 << ZCodeParser.LESS_EQUAL_OP) | (1 << ZCodeParser.GREATER_THAN_OP) | (1 << ZCodeParser.GREATER_EQUAL_OP) | (1 << ZCodeParser.STRING_COMPARE_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 378
                self.expression_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.expression_2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_3Context,0)


        def expression_2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_2Context,0)


        def AND_OP(self):
            return self.getToken(ZCodeParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(ZCodeParser.OR_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_2" ):
                return visitor.visitExpression_2(self)
            else:
                return visitor.visitChildren(self)



    def expression_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expression_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 386
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 387
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 388
                    self.expression_3(0) 
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_4Context,0)


        def expression_3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_3Context,0)


        def ADD_OF(self):
            return self.getToken(ZCodeParser.ADD_OF, 0)

        def SUB_OF(self):
            return self.getToken(ZCodeParser.SUB_OF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_3" ):
                return visitor.visitExpression_3(self)
            else:
                return visitor.visitChildren(self)



    def expression_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 397
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 398
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OF or _la==ZCodeParser.SUB_OF):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 399
                    self.expression_4(0) 
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_5Context,0)


        def expression_4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_4Context,0)


        def MUL_OF(self):
            return self.getToken(ZCodeParser.MUL_OF, 0)

        def DIV_OF(self):
            return self.getToken(ZCodeParser.DIV_OF, 0)

        def MOD_OF(self):
            return self.getToken(ZCodeParser.MOD_OF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_4" ):
                return visitor.visitExpression_4(self)
            else:
                return visitor.visitChildren(self)



    def expression_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 408
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 409
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OF) | (1 << ZCodeParser.DIV_OF) | (1 << ZCodeParser.MOD_OF))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 410
                    self.expression_5() 
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(ZCodeParser.NOT_OP, 0)

        def expression_5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_5Context,0)


        def expression_6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_5" ):
                return visitor.visitExpression_5(self)
            else:
                return visitor.visitChildren(self)




    def expression_5(self):

        localctx = ZCodeParser.Expression_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expression_5)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(ZCodeParser.NOT_OP)
                self.state = 417
                self.expression_5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB_OF, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.expression_6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OF(self):
            return self.getToken(ZCodeParser.SUB_OF, 0)

        def expression_6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_6Context,0)


        def expression_7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_6" ):
                return visitor.visitExpression_6(self)
            else:
                return visitor.visitChildren(self)




    def expression_6(self):

        localctx = ZCodeParser.Expression_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expression_6)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(ZCodeParser.SUB_OF)
                self.state = 422
                self.expression_6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.expression_7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def func_call_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_statContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_7" ):
                return visitor.visitExpression_7(self)
            else:
                return visitor.visitChildren(self)




    def expression_7(self):

        localctx = ZCodeParser.Expression_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expression_7)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.index_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
                self.func_call_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 429
                self.match(ZCodeParser.LB)
                self.state = 430
                self.expression()
                self.state = 431
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 433
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 434
                self.match(ZCodeParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 435
                self.match(ZCodeParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 436
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 437
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.expression_2_sempred
        self._predicates[37] = self.expression_3_sempred
        self._predicates[38] = self.expression_4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_2_sempred(self, localctx:Expression_2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_3_sempred(self, localctx:Expression_3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression_4_sempred(self, localctx:Expression_4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




