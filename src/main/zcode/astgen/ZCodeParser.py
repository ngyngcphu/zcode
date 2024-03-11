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
        buf.write("\u01d4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\3\2\6\2a\n\2\r\2\16\2b\3\2\3\2\6\2g")
        buf.write("\n\2\r\2\16\2h\5\2k\n\2\6\2m\n\2\r\2\16\2n\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3w\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\u0080\n\3\5\3\u0082\n\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u008a")
        buf.write("\n\4\f\4\16\4\u008d\13\4\3\4\3\4\5\4\u0091\n\4\3\5\3\5")
        buf.write("\5\5\u0095\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u009c\n\6\3\7\3")
        buf.write("\7\3\7\5\7\u00a1\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u00ac\n\b\3\t\3\t\6\t\u00b0\n\t\r\t\16\t\u00b1")
        buf.write("\3\t\3\t\3\t\3\t\7\t\u00b8\n\t\f\t\16\t\u00bb\13\t\5\t")
        buf.write("\u00bd\n\t\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u00c5\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00d2\n")
        buf.write("\f\3\r\3\r\3\r\3\r\5\r\u00d8\n\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\7\16\u00df\n\16\f\16\16\16\u00e2\13\16\3\16\3\16\7")
        buf.write("\16\u00e6\n\16\f\16\16\16\u00e9\13\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\7\17\u00f0\n\17\f\17\16\17\u00f3\13\17\3\17\3")
        buf.write("\17\7\17\u00f7\n\17\f\17\16\17\u00fa\13\17\3\20\3\20\3")
        buf.write("\20\7\20\u00ff\n\20\f\20\16\20\u0102\13\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\7\21\u010b\n\21\f\21\16\21\u010e")
        buf.write("\13\21\3\21\3\21\7\21\u0112\n\21\f\21\16\21\u0115\13\21")
        buf.write("\3\22\3\22\5\22\u0119\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u0121\n\23\3\24\3\24\5\24\u0125\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u012c\n\25\3\26\3\26\6\26\u0130\n")
        buf.write("\26\r\26\16\26\u0131\3\26\5\26\u0135\n\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\5\27\u013f\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0166\n\37\3 \3 \3 \3 \3!\3!\3!\3!\3!")
        buf.write("\5!\u0171\n!\3\"\3\"\5\"\u0175\n\"\3#\3#\3#\3#\3#\5#\u017c")
        buf.write("\n#\3$\3$\5$\u0180\n$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u018b")
        buf.write("\n%\3&\3&\3&\3&\3&\5&\u0192\n&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\7\'\u019a\n\'\f\'\16\'\u019d\13\'\3(\3(\3(\3(\3(\3(\7")
        buf.write("(\u01a5\n(\f(\16(\u01a8\13(\3)\3)\3)\3)\3)\3)\7)\u01b0")
        buf.write("\n)\f)\16)\u01b3\13)\3*\3*\3*\5*\u01b8\n*\3+\3+\3+\5+")
        buf.write("\u01bd\n+\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01c7\n,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\5,\u01d2\n,\3,\2\5LNP-\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTV\2\b\4\2\13\r\20\20\3\2\13\r\5\2!!#\'))\3\2")
        buf.write("+,\3\2\34\35\3\2\36 \2\u01ee\2[\3\2\2\2\4\u0081\3\2\2")
        buf.write("\2\6\u0083\3\2\2\2\b\u0094\3\2\2\2\n\u009b\3\2\2\2\f\u00a0")
        buf.write("\3\2\2\2\16\u00ab\3\2\2\2\20\u00bc\3\2\2\2\22\u00be\3")
        buf.write("\2\2\2\24\u00c4\3\2\2\2\26\u00d1\3\2\2\2\30\u00d7\3\2")
        buf.write("\2\2\32\u00d9\3\2\2\2\34\u00ea\3\2\2\2\36\u00fb\3\2\2")
        buf.write("\2 \u0103\3\2\2\2\"\u0116\3\2\2\2$\u0120\3\2\2\2&\u0124")
        buf.write("\3\2\2\2(\u012b\3\2\2\2*\u012d\3\2\2\2,\u013e\3\2\2\2")
        buf.write(".\u0140\3\2\2\2\60\u0144\3\2\2\2\62\u0149\3\2\2\2\64\u014d")
        buf.write("\3\2\2\2\66\u0152\3\2\2\28\u0156\3\2\2\2:\u015b\3\2\2")
        buf.write("\2<\u0165\3\2\2\2>\u0167\3\2\2\2@\u0170\3\2\2\2B\u0174")
        buf.write("\3\2\2\2D\u017b\3\2\2\2F\u017f\3\2\2\2H\u018a\3\2\2\2")
        buf.write("J\u0191\3\2\2\2L\u0193\3\2\2\2N\u019e\3\2\2\2P\u01a9\3")
        buf.write("\2\2\2R\u01b7\3\2\2\2T\u01bc\3\2\2\2V\u01d1\3\2\2\2XZ")
        buf.write("\7\65\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\l")
        buf.write("\3\2\2\2][\3\2\2\2^`\5\4\3\2_a\7\65\2\2`_\3\2\2\2ab\3")
        buf.write("\2\2\2b`\3\2\2\2bc\3\2\2\2ck\3\2\2\2df\5\6\4\2eg\7\65")
        buf.write("\2\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2")
        buf.write("j^\3\2\2\2jd\3\2\2\2km\3\2\2\2lj\3\2\2\2mn\3\2\2\2nl\3")
        buf.write("\2\2\2no\3\2\2\2op\3\2\2\2pq\7\2\2\3q\3\3\2\2\2rs\t\2")
        buf.write("\2\2sv\7\64\2\2tu\7\"\2\2uw\5H%\2vt\3\2\2\2vw\3\2\2\2")
        buf.write("w\u0082\3\2\2\2xy\7\17\2\2yz\7\64\2\2z{\7\"\2\2{\u0082")
        buf.write("\5H%\2|\177\5:\36\2}~\7\"\2\2~\u0080\5H%\2\177}\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081r\3\2\2")
        buf.write("\2\u0081x\3\2\2\2\u0081|\3\2\2\2\u0082\5\3\2\2\2\u0083")
        buf.write("\u0084\7\21\2\2\u0084\u0085\7\64\2\2\u0085\u0086\7-\2")
        buf.write("\2\u0086\u0087\5\b\5\2\u0087\u008b\7.\2\2\u0088\u008a")
        buf.write("\7\65\2\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u0090\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008e\u0091\5\"\22\2\u008f\u0091")
        buf.write("\5*\26\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\7\3\2\2\2\u0092\u0095\5\n\6\2\u0093")
        buf.write("\u0095\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0093\3\2\2\2")
        buf.write("\u0095\t\3\2\2\2\u0096\u0097\5\f\7\2\u0097\u0098\7\61")
        buf.write("\2\2\u0098\u0099\5\n\6\2\u0099\u009c\3\2\2\2\u009a\u009c")
        buf.write("\5\f\7\2\u009b\u0096\3\2\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\13\3\2\2\2\u009d\u009e\t\3\2\2\u009e\u00a1\7\64\2\2\u009f")
        buf.write("\u00a1\5:\36\2\u00a0\u009d\3\2\2\2\u00a0\u009f\3\2\2\2")
        buf.write("\u00a1\r\3\2\2\2\u00a2\u00ac\5\4\3\2\u00a3\u00ac\5\22")
        buf.write("\n\2\u00a4\u00ac\5\26\f\2\u00a5\u00ac\5 \21\2\u00a6\u00ac")
        buf.write("\7\25\2\2\u00a7\u00ac\7\26\2\2\u00a8\u00ac\5\"\22\2\u00a9")
        buf.write("\u00ac\5$\23\2\u00aa\u00ac\5*\26\2\u00ab\u00a2\3\2\2\2")
        buf.write("\u00ab\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab\u00a5\3")
        buf.write("\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ab\u00a8")
        buf.write("\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac")
        buf.write("\17\3\2\2\2\u00ad\u00af\5\16\b\2\u00ae\u00b0\7\65\2\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4")
        buf.write("\5\20\t\2\u00b4\u00bd\3\2\2\2\u00b5\u00b9\5\16\b\2\u00b6")
        buf.write("\u00b8\7\65\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2")
        buf.write("\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bd")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00ad\3\2\2\2\u00bc")
        buf.write("\u00b5\3\2\2\2\u00bd\21\3\2\2\2\u00be\u00bf\5\24\13\2")
        buf.write("\u00bf\u00c0\7\"\2\2\u00c0\u00c1\5H%\2\u00c1\23\3\2\2")
        buf.write("\2\u00c2\u00c5\7\64\2\2\u00c3\u00c5\5F$\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\25\3\2\2\2\u00c6\u00c7")
        buf.write("\5\32\16\2\u00c7\u00c8\5\30\r\2\u00c8\u00d2\3\2\2\2\u00c9")
        buf.write("\u00ca\5\32\16\2\u00ca\u00cb\5\30\r\2\u00cb\u00cc\5\36")
        buf.write("\20\2\u00cc\u00d2\3\2\2\2\u00cd\u00ce\5\32\16\2\u00ce")
        buf.write("\u00cf\5\36\20\2\u00cf\u00d2\3\2\2\2\u00d0\u00d2\5\32")
        buf.write("\16\2\u00d1\u00c6\3\2\2\2\u00d1\u00c9\3\2\2\2\u00d1\u00cd")
        buf.write("\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\27\3\2\2\2\u00d3\u00d8")
        buf.write("\5\34\17\2\u00d4\u00d5\5\34\17\2\u00d5\u00d6\5\30\r\2")
        buf.write("\u00d6\u00d8\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d7\u00d4\3")
        buf.write("\2\2\2\u00d8\31\3\2\2\2\u00d9\u00da\7\27\2\2\u00da\u00db")
        buf.write("\7-\2\2\u00db\u00dc\5H%\2\u00dc\u00e0\7.\2\2\u00dd\u00df")
        buf.write("\7\65\2\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e3\u00e7\5\16\b\2\u00e4\u00e6")
        buf.write("\7\65\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\33\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00ea\u00eb\7\31\2\2\u00eb\u00ec\7-\2\2")
        buf.write("\u00ec\u00ed\5H%\2\u00ed\u00f1\7.\2\2\u00ee\u00f0\7\65")
        buf.write("\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f4\u00f8\5\16\b\2\u00f5\u00f7\7\65\2")
        buf.write("\2\u00f6\u00f5\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\35\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fb\u00fc\7\30\2\2\u00fc\u0100\5\16\b\2\u00fd")
        buf.write("\u00ff\7\65\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0102\3\2\2")
        buf.write("\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\37\3")
        buf.write("\2\2\2\u0102\u0100\3\2\2\2\u0103\u0104\7\22\2\2\u0104")
        buf.write("\u0105\7\64\2\2\u0105\u0106\7\23\2\2\u0106\u0107\5H%\2")
        buf.write("\u0107\u0108\7\24\2\2\u0108\u010c\5H%\2\u0109\u010b\7")
        buf.write("\65\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010f\u0113\5\16\b\2\u0110\u0112")
        buf.write("\7\65\2\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113")
        buf.write("\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114!\3\2\2\2\u0115")
        buf.write("\u0113\3\2\2\2\u0116\u0118\7\16\2\2\u0117\u0119\5H%\2")
        buf.write("\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119#\3\2\2")
        buf.write("\2\u011a\u011b\7\64\2\2\u011b\u011c\7-\2\2\u011c\u011d")
        buf.write("\5&\24\2\u011d\u011e\7.\2\2\u011e\u0121\3\2\2\2\u011f")
        buf.write("\u0121\5,\27\2\u0120\u011a\3\2\2\2\u0120\u011f\3\2\2\2")
        buf.write("\u0121%\3\2\2\2\u0122\u0125\5(\25\2\u0123\u0125\3\2\2")
        buf.write("\2\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125\'\3\2")
        buf.write("\2\2\u0126\u0127\5H%\2\u0127\u0128\7\61\2\2\u0128\u0129")
        buf.write("\5(\25\2\u0129\u012c\3\2\2\2\u012a\u012c\5H%\2\u012b\u0126")
        buf.write("\3\2\2\2\u012b\u012a\3\2\2\2\u012c)\3\2\2\2\u012d\u012f")
        buf.write("\7\32\2\2\u012e\u0130\7\65\2\2\u012f\u012e\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0134\3\2\2\2\u0133\u0135\5\20\t\2\u0134\u0133")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0137\7\33\2\2\u0137+\3\2\2\2\u0138\u013f\5.\30\2\u0139")
        buf.write("\u013f\5\60\31\2\u013a\u013f\5\62\32\2\u013b\u013f\5\64")
        buf.write("\33\2\u013c\u013f\5\66\34\2\u013d\u013f\58\35\2\u013e")
        buf.write("\u0138\3\2\2\2\u013e\u0139\3\2\2\2\u013e\u013a\3\2\2\2")
        buf.write("\u013e\u013b\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3")
        buf.write("\2\2\2\u013f-\3\2\2\2\u0140\u0141\7\3\2\2\u0141\u0142")
        buf.write("\7-\2\2\u0142\u0143\7.\2\2\u0143/\3\2\2\2\u0144\u0145")
        buf.write("\7\4\2\2\u0145\u0146\7-\2\2\u0146\u0147\5H%\2\u0147\u0148")
        buf.write("\7.\2\2\u0148\61\3\2\2\2\u0149\u014a\7\5\2\2\u014a\u014b")
        buf.write("\7-\2\2\u014b\u014c\7.\2\2\u014c\63\3\2\2\2\u014d\u014e")
        buf.write("\7\6\2\2\u014e\u014f\7-\2\2\u014f\u0150\5H%\2\u0150\u0151")
        buf.write("\7.\2\2\u0151\65\3\2\2\2\u0152\u0153\7\7\2\2\u0153\u0154")
        buf.write("\7-\2\2\u0154\u0155\7.\2\2\u0155\67\3\2\2\2\u0156\u0157")
        buf.write("\7\b\2\2\u0157\u0158\7-\2\2\u0158\u0159\5H%\2\u0159\u015a")
        buf.write("\7.\2\2\u015a9\3\2\2\2\u015b\u015c\t\3\2\2\u015c\u015d")
        buf.write("\7\64\2\2\u015d\u015e\7/\2\2\u015e\u015f\5<\37\2\u015f")
        buf.write("\u0160\7\60\2\2\u0160;\3\2\2\2\u0161\u0162\7\62\2\2\u0162")
        buf.write("\u0163\7\61\2\2\u0163\u0166\5<\37\2\u0164\u0166\7\62\2")
        buf.write("\2\u0165\u0161\3\2\2\2\u0165\u0164\3\2\2\2\u0166=\3\2")
        buf.write("\2\2\u0167\u0168\7/\2\2\u0168\u0169\5@!\2\u0169\u016a")
        buf.write("\7\60\2\2\u016a?\3\2\2\2\u016b\u016c\5B\"\2\u016c\u016d")
        buf.write("\7\61\2\2\u016d\u016e\5@!\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u0171\5B\"\2\u0170\u016b\3\2\2\2\u0170\u016f\3\2\2\2")
        buf.write("\u0171A\3\2\2\2\u0172\u0175\5> \2\u0173\u0175\5D#\2\u0174")
        buf.write("\u0172\3\2\2\2\u0174\u0173\3\2\2\2\u0175C\3\2\2\2\u0176")
        buf.write("\u0177\5H%\2\u0177\u0178\7\61\2\2\u0178\u0179\5D#\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u017c\5H%\2\u017b\u0176\3\2\2\2\u017b")
        buf.write("\u017a\3\2\2\2\u017cE\3\2\2\2\u017d\u0180\7\64\2\2\u017e")
        buf.write("\u0180\5$\23\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0182\7/\2\2\u0182\u0183\5")
        buf.write("D#\2\u0183\u0184\7\60\2\2\u0184G\3\2\2\2\u0185\u0186\5")
        buf.write("J&\2\u0186\u0187\7(\2\2\u0187\u0188\5J&\2\u0188\u018b")
        buf.write("\3\2\2\2\u0189\u018b\5J&\2\u018a\u0185\3\2\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018bI\3\2\2\2\u018c\u018d\5L\'\2\u018d\u018e")
        buf.write("\t\4\2\2\u018e\u018f\5L\'\2\u018f\u0192\3\2\2\2\u0190")
        buf.write("\u0192\5L\'\2\u0191\u018c\3\2\2\2\u0191\u0190\3\2\2\2")
        buf.write("\u0192K\3\2\2\2\u0193\u0194\b\'\1\2\u0194\u0195\5N(\2")
        buf.write("\u0195\u019b\3\2\2\2\u0196\u0197\f\4\2\2\u0197\u0198\t")
        buf.write("\5\2\2\u0198\u019a\5N(\2\u0199\u0196\3\2\2\2\u019a\u019d")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("M\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u019f\b(\1\2\u019f")
        buf.write("\u01a0\5P)\2\u01a0\u01a6\3\2\2\2\u01a1\u01a2\f\4\2\2\u01a2")
        buf.write("\u01a3\t\6\2\2\u01a3\u01a5\5P)\2\u01a4\u01a1\3\2\2\2\u01a5")
        buf.write("\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7O\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01aa\b)\1\2")
        buf.write("\u01aa\u01ab\5R*\2\u01ab\u01b1\3\2\2\2\u01ac\u01ad\f\4")
        buf.write("\2\2\u01ad\u01ae\t\7\2\2\u01ae\u01b0\5R*\2\u01af\u01ac")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2Q\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("\u01b5\7*\2\2\u01b5\u01b8\5R*\2\u01b6\u01b8\5T+\2\u01b7")
        buf.write("\u01b4\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8S\3\2\2\2\u01b9")
        buf.write("\u01ba\7\35\2\2\u01ba\u01bd\5T+\2\u01bb\u01bd\5V,\2\u01bc")
        buf.write("\u01b9\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bdU\3\2\2\2\u01be")
        buf.write("\u01d2\5> \2\u01bf\u01d2\5F$\2\u01c0\u01c1\7\64\2\2\u01c1")
        buf.write("\u01c2\7-\2\2\u01c2\u01c3\5&\24\2\u01c3\u01c4\7.\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c7\5,\27\2\u01c6\u01c0\3\2\2\2")
        buf.write("\u01c6\u01c5\3\2\2\2\u01c7\u01d2\3\2\2\2\u01c8\u01c9\7")
        buf.write("-\2\2\u01c9\u01ca\5H%\2\u01ca\u01cb\7.\2\2\u01cb\u01d2")
        buf.write("\3\2\2\2\u01cc\u01d2\7\62\2\2\u01cd\u01d2\7\t\2\2\u01ce")
        buf.write("\u01d2\7\n\2\2\u01cf\u01d2\7\63\2\2\u01d0\u01d2\7\64\2")
        buf.write("\2\u01d1\u01be\3\2\2\2\u01d1\u01bf\3\2\2\2\u01d1\u01c6")
        buf.write("\3\2\2\2\u01d1\u01c8\3\2\2\2\u01d1\u01cc\3\2\2\2\u01d1")
        buf.write("\u01cd\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d0\3\2\2\2\u01d2W\3\2\2\2\62[bhjnv\177\u0081")
        buf.write("\u008b\u0090\u0094\u009b\u00a0\u00ab\u00b1\u00b9\u00bc")
        buf.write("\u00c4\u00d1\u00d7\u00e0\u00e7\u00f1\u00f8\u0100\u010c")
        buf.write("\u0113\u0118\u0120\u0124\u012b\u0131\u0134\u013e\u0165")
        buf.write("\u0170\u0174\u017b\u017f\u018a\u0191\u019b\u01a6\u01b1")
        buf.write("\u01b7\u01bc\u01c6\u01d1")
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
    RULE_elif_stat = 11
    RULE_if_fragment = 12
    RULE_elif_fragment = 13
    RULE_else_fragment = 14
    RULE_for_stat = 15
    RULE_return_stat = 16
    RULE_func_call_stat = 17
    RULE_arglist = 18
    RULE_argprime = 19
    RULE_block_stat = 20
    RULE_io_function = 21
    RULE_read_number = 22
    RULE_write_number = 23
    RULE_read_bool = 24
    RULE_write_bool = 25
    RULE_read_string = 26
    RULE_write_string = 27
    RULE_array_type = 28
    RULE_dimension_list = 29
    RULE_array_value = 30
    RULE_array_elements = 31
    RULE_array_nested_or_expression = 32
    RULE_exprlist = 33
    RULE_index_expr = 34
    RULE_expression = 35
    RULE_expression_1 = 36
    RULE_expression_2 = 37
    RULE_expression_3 = 38
    RULE_expression_4 = 39
    RULE_expression_5 = 40
    RULE_expression_6 = 41
    RULE_expression_7 = 42

    ruleNames =  [ "program", "varDecl", "functionDecl", "paramList", "paramPrime", 
                   "formalParameter", "statement_type", "statement_list", 
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
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 86
                self.match(ZCodeParser.NEWLINE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                    self.state = 92
                    self.varDecl()
                    self.state = 94 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 93
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 96 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ZCodeParser.NEWLINE):
                            break

                    pass
                elif token in [ZCodeParser.FUNC]:
                    self.state = 98
                    self.functionDecl()
                    self.state = 100 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 99
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 102 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ZCodeParser.NEWLINE):
                            break

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 108 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC))) != 0)):
                    break

            self.state = 110
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.DYNAMIC))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 113
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 114
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 115
                    self.expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(ZCodeParser.VAR)
                self.state = 119
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 120
                self.match(ZCodeParser.ASSIGN)
                self.state = 121
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.array_type()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 123
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 124
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
        self.enterRule(localctx, 4, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ZCodeParser.FUNC)
            self.state = 130
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 131
            self.match(ZCodeParser.LB)
            self.state = 132
            self.paramList()
            self.state = 133
            self.match(ZCodeParser.RB)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 134
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.state = 140
                self.return_stat()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 141
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
        self.enterRule(localctx, 6, self.RULE_paramList)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.formalParameter()
                self.state = 149
                self.match(ZCodeParser.COMMA)
                self.state = 150
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.assign_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.if_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.for_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 164
                self.match(ZCodeParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.match(ZCodeParser.CONTINUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 166
                self.return_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 167
                self.func_call_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 168
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.statement_type()
                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 172
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 175 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 177
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.statement_type()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 180
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 185
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
        self.enterRule(localctx, 16, self.RULE_assign_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.lhs()
            self.state = 189
            self.match(ZCodeParser.ASSIGN)
            self.state = 190
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
        self.enterRule(localctx, 20, self.RULE_if_stat)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.if_fragment()
                self.state = 197
                self.elif_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.if_fragment()
                self.state = 200
                self.elif_stat()
                self.state = 201
                self.else_fragment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.if_fragment()
                self.state = 204
                self.else_fragment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
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
        self.enterRule(localctx, 22, self.RULE_elif_stat)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.elif_fragment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.elif_fragment()
                self.state = 211
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
        self.enterRule(localctx, 24, self.RULE_if_fragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ZCodeParser.IF)
            self.state = 216
            self.match(ZCodeParser.LB)
            self.state = 217
            self.expression()
            self.state = 218
            self.match(ZCodeParser.RB)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 219
                self.match(ZCodeParser.NEWLINE)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.statement_type()
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 226
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_elif_fragment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(ZCodeParser.ELIF)
            self.state = 233
            self.match(ZCodeParser.LB)
            self.state = 234
            self.expression()
            self.state = 235
            self.match(ZCodeParser.RB)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 236
                self.match(ZCodeParser.NEWLINE)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self.statement_type()
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 243
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_else_fragment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ZCodeParser.ELSE)
            self.state = 250
            self.statement_type()
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 251
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_for_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ZCodeParser.FOR)
            self.state = 258
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 259
            self.match(ZCodeParser.UNTIL)
            self.state = 260
            self.expression()
            self.state = 261
            self.match(ZCodeParser.BY)
            self.state = 262
            self.expression()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 263
                self.match(ZCodeParser.NEWLINE)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
            self.statement_type()
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 270
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_return_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.RETURN)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.SUB_OF) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 277
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
        self.enterRule(localctx, 34, self.RULE_func_call_stat)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 281
                self.match(ZCodeParser.LB)
                self.state = 282
                self.arglist()
                self.state = 283
                self.match(ZCodeParser.RB)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
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
        self.enterRule(localctx, 36, self.RULE_arglist)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB_OF, ZCodeParser.NOT_OP, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
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
        self.enterRule(localctx, 38, self.RULE_argprime)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expression()
                self.state = 293
                self.match(ZCodeParser.COMMA)
                self.state = 294
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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
        self.enterRule(localctx, 40, self.RULE_block_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.BEGIN)
            self.state = 301 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 300
                self.match(ZCodeParser.NEWLINE)
                self.state = 303 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 305
                self.statement_list()


            self.state = 308
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
        self.enterRule(localctx, 42, self.RULE_io_function)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.read_number()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.write_number()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.read_bool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.write_bool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.read_string()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 315
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
        self.enterRule(localctx, 44, self.RULE_read_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(ZCodeParser.T__0)
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
        self.enterRule(localctx, 46, self.RULE_write_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(ZCodeParser.T__1)
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
        self.enterRule(localctx, 48, self.RULE_read_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ZCodeParser.T__2)
            self.state = 328
            self.match(ZCodeParser.LB)
            self.state = 329
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
        self.enterRule(localctx, 50, self.RULE_write_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.T__3)
            self.state = 332
            self.match(ZCodeParser.LB)
            self.state = 333
            self.expression()
            self.state = 334
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
        self.enterRule(localctx, 52, self.RULE_read_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ZCodeParser.T__4)
            self.state = 337
            self.match(ZCodeParser.LB)
            self.state = 338
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
        self.enterRule(localctx, 54, self.RULE_write_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(ZCodeParser.T__5)
            self.state = 341
            self.match(ZCodeParser.LB)
            self.state = 342
            self.expression()
            self.state = 343
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
        self.enterRule(localctx, 56, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 346
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 347
            self.match(ZCodeParser.LS)
            self.state = 348
            self.dimension_list()
            self.state = 349
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
        self.enterRule(localctx, 58, self.RULE_dimension_list)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 352
                self.match(ZCodeParser.COMMA)
                self.state = 353
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
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
        self.enterRule(localctx, 60, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZCodeParser.LS)
            self.state = 358
            self.array_elements()
            self.state = 359
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
        self.enterRule(localctx, 62, self.RULE_array_elements)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.array_nested_or_expression()
                self.state = 362
                self.match(ZCodeParser.COMMA)
                self.state = 363
                self.array_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
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
        self.enterRule(localctx, 64, self.RULE_array_nested_or_expression)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
        self.enterRule(localctx, 66, self.RULE_exprlist)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.expression()
                self.state = 373
                self.match(ZCodeParser.COMMA)
                self.state = 374
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
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
        self.enterRule(localctx, 68, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 379
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 380
                self.func_call_stat()
                pass


            self.state = 383
            self.match(ZCodeParser.LS)
            self.state = 384
            self.exprlist()
            self.state = 385
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
        self.enterRule(localctx, 70, self.RULE_expression)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.expression_1()
                self.state = 388
                self.match(ZCodeParser.CONCAT_OP)
                self.state = 389
                self.expression_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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
        self.enterRule(localctx, 72, self.RULE_expression_1)
        self._la = 0 # Token type
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.expression_2(0)
                self.state = 395
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_OP) | (1 << ZCodeParser.NOT_EQUAL_OP) | (1 << ZCodeParser.LESS_THAN_OP) | (1 << ZCodeParser.LESS_EQUAL_OP) | (1 << ZCodeParser.GREATER_THAN_OP) | (1 << ZCodeParser.GREATER_EQUAL_OP) | (1 << ZCodeParser.STRING_COMPARE_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 396
                self.expression_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expression_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 404
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 405
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 406
                    self.expression_3(0) 
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OF or _la==ZCodeParser.SUB_OF):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 417
                    self.expression_4(0) 
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OF) | (1 << ZCodeParser.DIV_OF) | (1 << ZCodeParser.MOD_OF))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 428
                    self.expression_5() 
                self.state = 433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_expression_5)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(ZCodeParser.NOT_OP)
                self.state = 435
                self.expression_5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB_OF, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
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
        self.enterRule(localctx, 82, self.RULE_expression_6)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(ZCodeParser.SUB_OF)
                self.state = 440
                self.expression_6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
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
        self.enterRule(localctx, 84, self.RULE_expression_7)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.index_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.IDENTIFIER]:
                    self.state = 446
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 447
                    self.match(ZCodeParser.LB)
                    self.state = 448
                    self.arglist()
                    self.state = 449
                    self.match(ZCodeParser.RB)
                    pass
                elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                    self.state = 451
                    self.io_function()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 454
                self.match(ZCodeParser.LB)
                self.state = 455
                self.expression()
                self.state = 456
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 458
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 459
                self.match(ZCodeParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 460
                self.match(ZCodeParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 461
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 462
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
        self._predicates[37] = self.expression_2_sempred
        self._predicates[38] = self.expression_3_sempred
        self._predicates[39] = self.expression_4_sempred
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
         




