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
        buf.write("\u01d6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\3\2\6\2c\n\2\r\2\16\2d\6\2g")
        buf.write("\n\2\r\2\16\2h\3\2\3\2\3\3\3\3\5\3o\n\3\3\4\3\4\3\4\3")
        buf.write("\4\5\4u\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u0082\n\4\5\4\u0084\n\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\7\5\u008c\n\5\f\5\16\5\u008f\13\5\3\5\3\5\5\5\u0093\n")
        buf.write("\5\3\6\3\6\5\6\u0097\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u009e")
        buf.write("\n\7\3\b\3\b\3\b\5\b\u00a3\n\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u00ae\n\t\3\n\3\n\6\n\u00b2\n\n\r\n\16")
        buf.write("\n\u00b3\3\n\3\n\3\n\3\n\7\n\u00ba\n\n\f\n\16\n\u00bd")
        buf.write("\13\n\5\n\u00bf\n\n\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00c7")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00d4")
        buf.write("\n\r\3\16\3\16\3\16\3\16\5\16\u00da\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00e1\n\17\f\17\16\17\u00e4\13\17\3\17")
        buf.write("\3\17\7\17\u00e8\n\17\f\17\16\17\u00eb\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\7\20\u00f2\n\20\f\20\16\20\u00f5\13\20")
        buf.write("\3\20\3\20\7\20\u00f9\n\20\f\20\16\20\u00fc\13\20\3\21")
        buf.write("\3\21\3\21\7\21\u0101\n\21\f\21\16\21\u0104\13\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u010d\n\22\f\22\16")
        buf.write("\22\u0110\13\22\3\22\3\22\7\22\u0114\n\22\f\22\16\22\u0117")
        buf.write("\13\22\3\23\3\23\5\23\u011b\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\5\24\u0123\n\24\3\25\3\25\5\25\u0127\n\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u012e\n\26\3\27\3\27\6\27\u0132")
        buf.write("\n\27\r\27\16\27\u0133\3\27\5\27\u0137\n\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0141\n\30\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \5 \u0168\n \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u0173\n\"\3#\3#\5#\u0177\n#\3$\3$\3$\3$\3$\5$\u017e")
        buf.write("\n$\3%\3%\5%\u0182\n%\3%\3%\3%\3%\3&\3&\3&\3&\3&\5&\u018d")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0194\n\'\3(\3(\3(\3(\3(\3")
        buf.write("(\7(\u019c\n(\f(\16(\u019f\13(\3)\3)\3)\3)\3)\3)\7)\u01a7")
        buf.write("\n)\f)\16)\u01aa\13)\3*\3*\3*\3*\3*\3*\7*\u01b2\n*\f*")
        buf.write("\16*\u01b5\13*\3+\3+\3+\5+\u01ba\n+\3,\3,\3,\5,\u01bf")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01c9\n-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\5-\u01d4\n-\3-\2\5NPR.\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVX\2\b\4\2\13\r\20\20\3\2\13\r\5\2!!#\'))\3\2+,\3")
        buf.write("\2\34\35\3\2\36 \2\u01ee\2]\3\2\2\2\4n\3\2\2\2\6\u0083")
        buf.write("\3\2\2\2\b\u0085\3\2\2\2\n\u0096\3\2\2\2\f\u009d\3\2\2")
        buf.write("\2\16\u00a2\3\2\2\2\20\u00ad\3\2\2\2\22\u00be\3\2\2\2")
        buf.write("\24\u00c0\3\2\2\2\26\u00c6\3\2\2\2\30\u00d3\3\2\2\2\32")
        buf.write("\u00d9\3\2\2\2\34\u00db\3\2\2\2\36\u00ec\3\2\2\2 \u00fd")
        buf.write("\3\2\2\2\"\u0105\3\2\2\2$\u0118\3\2\2\2&\u0122\3\2\2\2")
        buf.write("(\u0126\3\2\2\2*\u012d\3\2\2\2,\u012f\3\2\2\2.\u0140\3")
        buf.write("\2\2\2\60\u0142\3\2\2\2\62\u0146\3\2\2\2\64\u014b\3\2")
        buf.write("\2\2\66\u014f\3\2\2\28\u0154\3\2\2\2:\u0158\3\2\2\2<\u015d")
        buf.write("\3\2\2\2>\u0167\3\2\2\2@\u0169\3\2\2\2B\u0172\3\2\2\2")
        buf.write("D\u0176\3\2\2\2F\u017d\3\2\2\2H\u0181\3\2\2\2J\u018c\3")
        buf.write("\2\2\2L\u0193\3\2\2\2N\u0195\3\2\2\2P\u01a0\3\2\2\2R\u01ab")
        buf.write("\3\2\2\2T\u01b9\3\2\2\2V\u01be\3\2\2\2X\u01d3\3\2\2\2")
        buf.write("Z\\\7\65\2\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2")
        buf.write("^f\3\2\2\2_]\3\2\2\2`b\5\4\3\2ac\7\65\2\2ba\3\2\2\2cd")
        buf.write("\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2\2\2f`\3\2\2\2gh\3\2")
        buf.write("\2\2hf\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\7\2\2\3k\3\3\2\2")
        buf.write("\2lo\5\6\4\2mo\5\b\5\2nl\3\2\2\2nm\3\2\2\2o\5\3\2\2\2")
        buf.write("pq\t\2\2\2qt\7\64\2\2rs\7\"\2\2su\5J&\2tr\3\2\2\2tu\3")
        buf.write("\2\2\2u\u0084\3\2\2\2vw\7\17\2\2wx\7\64\2\2xy\7\"\2\2")
        buf.write("y\u0084\5J&\2z{\t\3\2\2{|\7\64\2\2|}\7/\2\2}~\5> \2~\u0081")
        buf.write("\7\60\2\2\177\u0080\7\"\2\2\u0080\u0082\5J&\2\u0081\177")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083")
        buf.write("p\3\2\2\2\u0083v\3\2\2\2\u0083z\3\2\2\2\u0084\7\3\2\2")
        buf.write("\2\u0085\u0086\7\21\2\2\u0086\u0087\7\64\2\2\u0087\u0088")
        buf.write("\7-\2\2\u0088\u0089\5\n\6\2\u0089\u008d\7.\2\2\u008a\u008c")
        buf.write("\7\65\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0092\3\2\2\2")
        buf.write("\u008f\u008d\3\2\2\2\u0090\u0093\5$\23\2\u0091\u0093\5")
        buf.write(",\27\2\u0092\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\t\3\2\2\2\u0094\u0097\5\f\7\2\u0095\u0097")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\13\3\2\2\2\u0098\u0099\5\16\b\2\u0099\u009a\7\61\2\2")
        buf.write("\u009a\u009b\5\f\7\2\u009b\u009e\3\2\2\2\u009c\u009e\5")
        buf.write("\16\b\2\u009d\u0098\3\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\r\3\2\2\2\u009f\u00a0\t\3\2\2\u00a0\u00a3\7\64\2\2\u00a1")
        buf.write("\u00a3\5<\37\2\u00a2\u009f\3\2\2\2\u00a2\u00a1\3\2\2\2")
        buf.write("\u00a3\17\3\2\2\2\u00a4\u00ae\5\6\4\2\u00a5\u00ae\5\24")
        buf.write("\13\2\u00a6\u00ae\5\30\r\2\u00a7\u00ae\5\"\22\2\u00a8")
        buf.write("\u00ae\7\25\2\2\u00a9\u00ae\7\26\2\2\u00aa\u00ae\5$\23")
        buf.write("\2\u00ab\u00ae\5&\24\2\u00ac\u00ae\5,\27\2\u00ad\u00a4")
        buf.write("\3\2\2\2\u00ad\u00a5\3\2\2\2\u00ad\u00a6\3\2\2\2\u00ad")
        buf.write("\u00a7\3\2\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2")
        buf.write("\u00ad\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3")
        buf.write("\2\2\2\u00ae\21\3\2\2\2\u00af\u00b1\5\20\t\2\u00b0\u00b2")
        buf.write("\7\65\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b6\5\22\n\2\u00b6\u00bf\3\2\2\2\u00b7\u00bb")
        buf.write("\5\20\t\2\u00b8\u00ba\7\65\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00af\3")
        buf.write("\2\2\2\u00be\u00b7\3\2\2\2\u00bf\23\3\2\2\2\u00c0\u00c1")
        buf.write("\5\26\f\2\u00c1\u00c2\7\"\2\2\u00c2\u00c3\5J&\2\u00c3")
        buf.write("\25\3\2\2\2\u00c4\u00c7\7\64\2\2\u00c5\u00c7\5H%\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\27\3\2\2\2\u00c8")
        buf.write("\u00c9\5\34\17\2\u00c9\u00ca\5\32\16\2\u00ca\u00d4\3\2")
        buf.write("\2\2\u00cb\u00cc\5\34\17\2\u00cc\u00cd\5\32\16\2\u00cd")
        buf.write("\u00ce\5 \21\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0\5\34\17")
        buf.write("\2\u00d0\u00d1\5 \21\2\u00d1\u00d4\3\2\2\2\u00d2\u00d4")
        buf.write("\5\34\17\2\u00d3\u00c8\3\2\2\2\u00d3\u00cb\3\2\2\2\u00d3")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\31\3\2\2\2\u00d5")
        buf.write("\u00da\5\36\20\2\u00d6\u00d7\5\36\20\2\u00d7\u00d8\5\32")
        buf.write("\16\2\u00d8\u00da\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9\u00d6")
        buf.write("\3\2\2\2\u00da\33\3\2\2\2\u00db\u00dc\7\27\2\2\u00dc\u00dd")
        buf.write("\7-\2\2\u00dd\u00de\5J&\2\u00de\u00e2\7.\2\2\u00df\u00e1")
        buf.write("\7\65\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e5\u00e9\5\20\t\2\u00e6\u00e8")
        buf.write("\7\65\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\35\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ed\7\31\2\2\u00ed\u00ee\7-\2\2")
        buf.write("\u00ee\u00ef\5J&\2\u00ef\u00f3\7.\2\2\u00f0\u00f2\7\65")
        buf.write("\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00fa\5\20\t\2\u00f7\u00f9\7\65\2")
        buf.write("\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\37\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fe\7\30\2\2\u00fe\u0102\5\20\t\2\u00ff")
        buf.write("\u0101\7\65\2\2\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2")
        buf.write("\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103!\3\2")
        buf.write("\2\2\u0104\u0102\3\2\2\2\u0105\u0106\7\22\2\2\u0106\u0107")
        buf.write("\7\64\2\2\u0107\u0108\7\23\2\2\u0108\u0109\5J&\2\u0109")
        buf.write("\u010a\7\24\2\2\u010a\u010e\5J&\2\u010b\u010d\7\65\2\2")
        buf.write("\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0111\u0115\5\20\t\2\u0112\u0114\7\65\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116#\3\2\2\2\u0117\u0115\3\2\2")
        buf.write("\2\u0118\u011a\7\16\2\2\u0119\u011b\5J&\2\u011a\u0119")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b%\3\2\2\2\u011c\u011d")
        buf.write("\7\64\2\2\u011d\u011e\7-\2\2\u011e\u011f\5(\25\2\u011f")
        buf.write("\u0120\7.\2\2\u0120\u0123\3\2\2\2\u0121\u0123\5.\30\2")
        buf.write("\u0122\u011c\3\2\2\2\u0122\u0121\3\2\2\2\u0123\'\3\2\2")
        buf.write("\2\u0124\u0127\5*\26\2\u0125\u0127\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0125\3\2\2\2\u0127)\3\2\2\2\u0128\u0129")
        buf.write("\5J&\2\u0129\u012a\7\61\2\2\u012a\u012b\5*\26\2\u012b")
        buf.write("\u012e\3\2\2\2\u012c\u012e\5J&\2\u012d\u0128\3\2\2\2\u012d")
        buf.write("\u012c\3\2\2\2\u012e+\3\2\2\2\u012f\u0131\7\32\2\2\u0130")
        buf.write("\u0132\7\65\2\2\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2")
        buf.write("\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0136")
        buf.write("\3\2\2\2\u0135\u0137\5\22\n\2\u0136\u0135\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\7\33\2")
        buf.write("\2\u0139-\3\2\2\2\u013a\u0141\5\60\31\2\u013b\u0141\5")
        buf.write("\62\32\2\u013c\u0141\5\64\33\2\u013d\u0141\5\66\34\2\u013e")
        buf.write("\u0141\58\35\2\u013f\u0141\5:\36\2\u0140\u013a\3\2\2\2")
        buf.write("\u0140\u013b\3\2\2\2\u0140\u013c\3\2\2\2\u0140\u013d\3")
        buf.write("\2\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141/")
        buf.write("\3\2\2\2\u0142\u0143\7\3\2\2\u0143\u0144\7-\2\2\u0144")
        buf.write("\u0145\7.\2\2\u0145\61\3\2\2\2\u0146\u0147\7\4\2\2\u0147")
        buf.write("\u0148\7-\2\2\u0148\u0149\5J&\2\u0149\u014a\7.\2\2\u014a")
        buf.write("\63\3\2\2\2\u014b\u014c\7\5\2\2\u014c\u014d\7-\2\2\u014d")
        buf.write("\u014e\7.\2\2\u014e\65\3\2\2\2\u014f\u0150\7\6\2\2\u0150")
        buf.write("\u0151\7-\2\2\u0151\u0152\5J&\2\u0152\u0153\7.\2\2\u0153")
        buf.write("\67\3\2\2\2\u0154\u0155\7\7\2\2\u0155\u0156\7-\2\2\u0156")
        buf.write("\u0157\7.\2\2\u01579\3\2\2\2\u0158\u0159\7\b\2\2\u0159")
        buf.write("\u015a\7-\2\2\u015a\u015b\5J&\2\u015b\u015c\7.\2\2\u015c")
        buf.write(";\3\2\2\2\u015d\u015e\t\3\2\2\u015e\u015f\7\64\2\2\u015f")
        buf.write("\u0160\7/\2\2\u0160\u0161\5> \2\u0161\u0162\7\60\2\2\u0162")
        buf.write("=\3\2\2\2\u0163\u0164\7\62\2\2\u0164\u0165\7\61\2\2\u0165")
        buf.write("\u0168\5> \2\u0166\u0168\7\62\2\2\u0167\u0163\3\2\2\2")
        buf.write("\u0167\u0166\3\2\2\2\u0168?\3\2\2\2\u0169\u016a\7/\2\2")
        buf.write("\u016a\u016b\5B\"\2\u016b\u016c\7\60\2\2\u016cA\3\2\2")
        buf.write("\2\u016d\u016e\5D#\2\u016e\u016f\7\61\2\2\u016f\u0170")
        buf.write("\5B\"\2\u0170\u0173\3\2\2\2\u0171\u0173\5D#\2\u0172\u016d")
        buf.write("\3\2\2\2\u0172\u0171\3\2\2\2\u0173C\3\2\2\2\u0174\u0177")
        buf.write("\5@!\2\u0175\u0177\5F$\2\u0176\u0174\3\2\2\2\u0176\u0175")
        buf.write("\3\2\2\2\u0177E\3\2\2\2\u0178\u0179\5J&\2\u0179\u017a")
        buf.write("\7\61\2\2\u017a\u017b\5F$\2\u017b\u017e\3\2\2\2\u017c")
        buf.write("\u017e\5J&\2\u017d\u0178\3\2\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("G\3\2\2\2\u017f\u0182\7\64\2\2\u0180\u0182\5&\24\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0184\7/\2\2\u0184\u0185\5F$\2\u0185\u0186\7\60")
        buf.write("\2\2\u0186I\3\2\2\2\u0187\u0188\5L\'\2\u0188\u0189\7(")
        buf.write("\2\2\u0189\u018a\5L\'\2\u018a\u018d\3\2\2\2\u018b\u018d")
        buf.write("\5L\'\2\u018c\u0187\3\2\2\2\u018c\u018b\3\2\2\2\u018d")
        buf.write("K\3\2\2\2\u018e\u018f\5N(\2\u018f\u0190\t\4\2\2\u0190")
        buf.write("\u0191\5N(\2\u0191\u0194\3\2\2\2\u0192\u0194\5N(\2\u0193")
        buf.write("\u018e\3\2\2\2\u0193\u0192\3\2\2\2\u0194M\3\2\2\2\u0195")
        buf.write("\u0196\b(\1\2\u0196\u0197\5P)\2\u0197\u019d\3\2\2\2\u0198")
        buf.write("\u0199\f\4\2\2\u0199\u019a\t\5\2\2\u019a\u019c\5P)\2\u019b")
        buf.write("\u0198\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019eO\3\2\2\2\u019f\u019d\3\2\2")
        buf.write("\2\u01a0\u01a1\b)\1\2\u01a1\u01a2\5R*\2\u01a2\u01a8\3")
        buf.write("\2\2\2\u01a3\u01a4\f\4\2\2\u01a4\u01a5\t\6\2\2\u01a5\u01a7")
        buf.write("\5R*\2\u01a6\u01a3\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9Q\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01ac\b*\1\2\u01ac\u01ad\5T+\2\u01ad\u01b3")
        buf.write("\3\2\2\2\u01ae\u01af\f\4\2\2\u01af\u01b0\t\7\2\2\u01b0")
        buf.write("\u01b2\5T+\2\u01b1\u01ae\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4S\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b7\7*\2\2\u01b7\u01ba\5T+\2\u01b8")
        buf.write("\u01ba\5V,\2\u01b9\u01b6\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("U\3\2\2\2\u01bb\u01bc\7\35\2\2\u01bc\u01bf\5V,\2\u01bd")
        buf.write("\u01bf\5X-\2\u01be\u01bb\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("W\3\2\2\2\u01c0\u01d4\5@!\2\u01c1\u01d4\5H%\2\u01c2\u01c3")
        buf.write("\7\64\2\2\u01c3\u01c4\7-\2\2\u01c4\u01c5\5(\25\2\u01c5")
        buf.write("\u01c6\7.\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c9\5.\30\2")
        buf.write("\u01c8\u01c2\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01d4\3")
        buf.write("\2\2\2\u01ca\u01cb\7-\2\2\u01cb\u01cc\5J&\2\u01cc\u01cd")
        buf.write("\7.\2\2\u01cd\u01d4\3\2\2\2\u01ce\u01d4\7\62\2\2\u01cf")
        buf.write("\u01d4\7\t\2\2\u01d0\u01d4\7\n\2\2\u01d1\u01d4\7\63\2")
        buf.write("\2\u01d2\u01d4\7\64\2\2\u01d3\u01c0\3\2\2\2\u01d3\u01c1")
        buf.write("\3\2\2\2\u01d3\u01c8\3\2\2\2\u01d3\u01ca\3\2\2\2\u01d3")
        buf.write("\u01ce\3\2\2\2\u01d3\u01cf\3\2\2\2\u01d3\u01d0\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4Y\3\2\2")
        buf.write("\2\61]dhnt\u0081\u0083\u008d\u0092\u0096\u009d\u00a2\u00ad")
        buf.write("\u00b3\u00bb\u00be\u00c6\u00d3\u00d9\u00e2\u00e9\u00f3")
        buf.write("\u00fa\u0102\u010e\u0115\u011a\u0122\u0126\u012d\u0133")
        buf.write("\u0136\u0140\u0167\u0172\u0176\u017d\u0181\u018c\u0193")
        buf.write("\u019d\u01a8\u01b3\u01b9\u01be\u01c8\u01d3")
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
    RULE_decl = 1
    RULE_varDecl = 2
    RULE_functionDecl = 3
    RULE_paramList = 4
    RULE_paramPrime = 5
    RULE_formalParameter = 6
    RULE_statement_type = 7
    RULE_statement_list = 8
    RULE_assign_stat = 9
    RULE_lhs = 10
    RULE_if_stat = 11
    RULE_elif_stat = 12
    RULE_if_fragment = 13
    RULE_elif_fragment = 14
    RULE_else_fragment = 15
    RULE_for_stat = 16
    RULE_return_stat = 17
    RULE_func_call_stat = 18
    RULE_arglist = 19
    RULE_argprime = 20
    RULE_block_stat = 21
    RULE_io_function = 22
    RULE_read_number = 23
    RULE_write_number = 24
    RULE_read_bool = 25
    RULE_write_bool = 26
    RULE_read_string = 27
    RULE_write_string = 28
    RULE_array_type = 29
    RULE_dimension_list = 30
    RULE_array_value = 31
    RULE_array_elements = 32
    RULE_array_nested_or_expression = 33
    RULE_exprlist = 34
    RULE_index_expr = 35
    RULE_expression = 36
    RULE_expression_1 = 37
    RULE_expression_2 = 38
    RULE_expression_3 = 39
    RULE_expression_4 = 40
    RULE_expression_5 = 41
    RULE_expression_6 = 42
    RULE_expression_7 = 43

    ruleNames =  [ "program", "decl", "varDecl", "functionDecl", "paramList", 
                   "paramPrime", "formalParameter", "statement_type", "statement_list", 
                   "assign_stat", "lhs", "if_stat", "elif_stat", "if_fragment", 
                   "elif_fragment", "else_fragment", "for_stat", "return_stat", 
                   "func_call_stat", "arglist", "argprime", "block_stat", 
                   "io_function", "read_number", "write_number", "read_bool", 
                   "write_bool", "read_string", "write_string", "array_type", 
                   "dimension_list", "array_value", "array_elements", "array_nested_or_expression", 
                   "exprlist", "index_expr", "expression", "expression_1", 
                   "expression_2", "expression_3", "expression_4", "expression_5", 
                   "expression_6", "expression_7" ]

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

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclContext,i)


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
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 88
                self.match(ZCodeParser.NEWLINE)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.decl()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 95
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 98 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC))) != 0)):
                    break

            self.state = 104
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.varDecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.functionDecl()
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

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dimension_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ZCodeParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.DYNAMIC))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 111
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 112
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 113
                    self.expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(ZCodeParser.VAR)
                self.state = 117
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 118
                self.match(ZCodeParser.ASSIGN)
                self.state = 119
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 121
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 122
                self.match(ZCodeParser.LS)
                self.state = 123
                self.dimension_list()
                self.state = 124
                self.match(ZCodeParser.RS)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 125
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 126
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
        self.enterRule(localctx, 6, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ZCodeParser.FUNC)
            self.state = 132
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 133
            self.match(ZCodeParser.LB)
            self.state = 134
            self.paramList()
            self.state = 135
            self.match(ZCodeParser.RB)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 136
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 142
                self.return_stat()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 143
                self.block_stat()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
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
        self.enterRule(localctx, 8, self.RULE_paramList)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
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
        self.enterRule(localctx, 10, self.RULE_paramPrime)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.formalParameter()
                self.state = 151
                self.match(ZCodeParser.COMMA)
                self.state = 152
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
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
        self.enterRule(localctx, 12, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
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
        self.enterRule(localctx, 14, self.RULE_statement_type)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.assign_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.if_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.for_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(ZCodeParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.match(ZCodeParser.CONTINUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 168
                self.return_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 169
                self.func_call_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 170
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
        self.enterRule(localctx, 16, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.statement_type()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 174
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 177 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 179
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.statement_type()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 182
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
        self.enterRule(localctx, 18, self.RULE_assign_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.lhs()
            self.state = 191
            self.match(ZCodeParser.ASSIGN)
            self.state = 192
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
        self.enterRule(localctx, 20, self.RULE_lhs)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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


        def elif_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statContext,0)


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
        self.enterRule(localctx, 22, self.RULE_if_stat)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.if_fragment()
                self.state = 199
                self.elif_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.if_fragment()
                self.state = 202
                self.elif_stat()
                self.state = 203
                self.else_fragment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.if_fragment()
                self.state = 206
                self.else_fragment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.if_fragment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_fragment(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_fragmentContext,0)


        def elif_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stat" ):
                return visitor.visitElif_stat(self)
            else:
                return visitor.visitChildren(self)




    def elif_stat(self):

        localctx = ZCodeParser.Elif_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elif_stat)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.elif_fragment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.elif_fragment()
                self.state = 213
                self.elif_stat()
                pass


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

        def statement_type(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_typeContext,0)


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
        self.enterRule(localctx, 26, self.RULE_if_fragment)
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
            self.statement_type()
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 228
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def statement_type(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_typeContext,0)


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
        self.enterRule(localctx, 28, self.RULE_elif_fragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(ZCodeParser.ELIF)
            self.state = 235
            self.match(ZCodeParser.LB)
            self.state = 236
            self.expression()
            self.state = 237
            self.match(ZCodeParser.RB)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 238
                self.match(ZCodeParser.NEWLINE)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
            self.statement_type()
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 245
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def statement_type(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_typeContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_else_fragment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_fragment" ):
                return visitor.visitElse_fragment(self)
            else:
                return visitor.visitChildren(self)




    def else_fragment(self):

        localctx = ZCodeParser.Else_fragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_else_fragment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ZCodeParser.ELSE)
            self.state = 252
            self.statement_type()
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 253
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def statement_type(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_typeContext,0)


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
        self.enterRule(localctx, 32, self.RULE_for_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ZCodeParser.FOR)
            self.state = 260
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 261
            self.match(ZCodeParser.UNTIL)
            self.state = 262
            self.expression()
            self.state = 263
            self.match(ZCodeParser.BY)
            self.state = 264
            self.expression()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 265
                self.match(ZCodeParser.NEWLINE)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self.statement_type()
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 272
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_return_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.RETURN)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.SUB_OF) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 279
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
        self.enterRule(localctx, 36, self.RULE_func_call_stat)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 283
                self.match(ZCodeParser.LB)
                self.state = 284
                self.arglist()
                self.state = 285
                self.match(ZCodeParser.RB)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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
        self.enterRule(localctx, 38, self.RULE_arglist)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB_OF, ZCodeParser.NOT_OP, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
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
        self.enterRule(localctx, 40, self.RULE_argprime)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.expression()
                self.state = 295
                self.match(ZCodeParser.COMMA)
                self.state = 296
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
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
        self.enterRule(localctx, 42, self.RULE_block_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(ZCodeParser.BEGIN)
            self.state = 303 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 302
                self.match(ZCodeParser.NEWLINE)
                self.state = 305 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 307
                self.statement_list()


            self.state = 310
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
        self.enterRule(localctx, 44, self.RULE_io_function)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.read_number()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.write_number()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.read_bool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.write_bool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.read_string()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
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
        self.enterRule(localctx, 46, self.RULE_read_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ZCodeParser.T__0)
            self.state = 321
            self.match(ZCodeParser.LB)
            self.state = 322
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
        self.enterRule(localctx, 48, self.RULE_write_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.T__1)
            self.state = 325
            self.match(ZCodeParser.LB)
            self.state = 326
            self.expression()
            self.state = 327
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
        self.enterRule(localctx, 50, self.RULE_read_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.T__2)
            self.state = 330
            self.match(ZCodeParser.LB)
            self.state = 331
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
        self.enterRule(localctx, 52, self.RULE_write_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ZCodeParser.T__3)
            self.state = 334
            self.match(ZCodeParser.LB)
            self.state = 335
            self.expression()
            self.state = 336
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
        self.enterRule(localctx, 54, self.RULE_read_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.T__4)
            self.state = 339
            self.match(ZCodeParser.LB)
            self.state = 340
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
        self.enterRule(localctx, 56, self.RULE_write_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.T__5)
            self.state = 343
            self.match(ZCodeParser.LB)
            self.state = 344
            self.expression()
            self.state = 345
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
        self.enterRule(localctx, 58, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 348
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 349
            self.match(ZCodeParser.LS)
            self.state = 350
            self.dimension_list()
            self.state = 351
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
        self.enterRule(localctx, 60, self.RULE_dimension_list)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 354
                self.match(ZCodeParser.COMMA)
                self.state = 355
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
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
        self.enterRule(localctx, 62, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(ZCodeParser.LS)
            self.state = 360
            self.array_elements()
            self.state = 361
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
        self.enterRule(localctx, 64, self.RULE_array_elements)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.array_nested_or_expression()
                self.state = 364
                self.match(ZCodeParser.COMMA)
                self.state = 365
                self.array_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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
        self.enterRule(localctx, 66, self.RULE_array_nested_or_expression)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
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
        self.enterRule(localctx, 68, self.RULE_exprlist)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.expression()
                self.state = 375
                self.match(ZCodeParser.COMMA)
                self.state = 376
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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
        self.enterRule(localctx, 70, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 381
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 382
                self.func_call_stat()
                pass


            self.state = 385
            self.match(ZCodeParser.LS)
            self.state = 386
            self.exprlist()
            self.state = 387
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
        self.enterRule(localctx, 72, self.RULE_expression)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.expression_1()
                self.state = 390
                self.match(ZCodeParser.CONCAT_OP)
                self.state = 391
                self.expression_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
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
        self.enterRule(localctx, 74, self.RULE_expression_1)
        self._la = 0 # Token type
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.expression_2(0)
                self.state = 397
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_OP) | (1 << ZCodeParser.NOT_EQUAL_OP) | (1 << ZCodeParser.LESS_THAN_OP) | (1 << ZCodeParser.LESS_EQUAL_OP) | (1 << ZCodeParser.GREATER_THAN_OP) | (1 << ZCodeParser.GREATER_EQUAL_OP) | (1 << ZCodeParser.STRING_COMPARE_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 398
                self.expression_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 411
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 408
                    self.expression_3(0) 
                self.state = 413
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 417
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 418
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OF or _la==ZCodeParser.SUB_OF):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 419
                    self.expression_4(0) 
                self.state = 424
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 428
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 429
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OF) | (1 << ZCodeParser.DIV_OF) | (1 << ZCodeParser.MOD_OF))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 430
                    self.expression_5() 
                self.state = 435
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
        self.enterRule(localctx, 82, self.RULE_expression_5)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ZCodeParser.NOT_OP)
                self.state = 437
                self.expression_5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB_OF, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
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
        self.enterRule(localctx, 84, self.RULE_expression_6)
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(ZCodeParser.SUB_OF)
                self.state = 442
                self.expression_6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
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


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_7" ):
                return visitor.visitExpression_7(self)
            else:
                return visitor.visitChildren(self)




    def expression_7(self):

        localctx = ZCodeParser.Expression_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression_7)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.index_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.IDENTIFIER]:
                    self.state = 448
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 449
                    self.match(ZCodeParser.LB)
                    self.state = 450
                    self.arglist()
                    self.state = 451
                    self.match(ZCodeParser.RB)
                    pass
                elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                    self.state = 453
                    self.io_function()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 456
                self.match(ZCodeParser.LB)
                self.state = 457
                self.expression()
                self.state = 458
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 460
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 461
                self.match(ZCodeParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 462
                self.match(ZCodeParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 463
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 464
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
        self._predicates[38] = self.expression_2_sempred
        self._predicates[39] = self.expression_3_sempred
        self._predicates[40] = self.expression_4_sempred
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
         




