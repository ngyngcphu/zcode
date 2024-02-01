/* 2114417 */

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (varDecl statement* | functionDecl)+ EOF;

varDecl: (NUMBER | BOOL | STRING | DYNAMIC) IDENTIFIER (
		ASSIGN expr
	)? NEWLINE+
	| VAR IDENTIFIER ASSIGN expr NEWLINE+
	| array_type (ASSIGN array_value)? NEWLINE+;

functionDecl:
	FUNC IDENTIFIER LB paramList RB NEWLINE* (
		returnStat
		| blockStat
	);
paramList: paramPrime |;
paramPrime: formalParameter COMMA paramPrime | formalParameter;
formalParameter: (NUMBER | BOOL | STRING) IDENTIFIER
	| array_type;

statement: varDecl;

array_type: (NUMBER | STRING | BOOL) IDENTIFIER LS dimension_list RS;
dimension_list:
	INTLIT_NON_ZERO COMMA dimension_list
	| INTLIT_NON_ZERO;

array_value: LS array_elements RS;
array_elements:
	array_nested_or_expression COMMA array_elements
	| array_nested_or_expression;
array_nested_or_expression: array_value | exprlist;

exprlist: expr COMMA exprlist | expr;

expr:
	LB expr RB
	| (IDENTIFIER | func_call) LS exprlist RS
	| <assoc = right> SUB_OF expr
	| <assoc = right> NOT_OP expr
	| expr (MUL_OF | DIV_OF | MOD_OF) expr
	| expr (ADD_OF | SUB_OF) expr
	| expr (AND_OP | OR_OP) expr
	| expr (
		EQUAL_OP
		| STRING_COMPARE_OP
		| NOT_EQUAL_OP
		| LESS_THAN_OP
		| GREATER_THAN_OP
		| LESS_EQUAL_OP
		| GREATER_EQUAL_OP
	) expr
	| expr CONCAT_OP expr
	| NUMBERLIT
	| TRUE
	| FALSE
	| STRINGLIT
	| array_value
	| IDENTIFIER;

func_call: IDENTIFIER LB arglist RB;
arglist: argprime |;
argprime: expr COMMA argprime | expr;

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

ADD_OF: '+';
SUB_OF: '-';
MUL_OF: '*';
DIV_OF: '/';
MOD_OF: '%';
EQUAL_OP: '=';
ASSIGN: '<-';
NOT_EQUAL_OP: '!=';
LESS_THAN_OP: '<';
LESS_EQUAL_OP: '<=';
GREATER_THAN_OP: '>';
GREATER_EQUAL_OP: '>=';
CONCAT_OP: '...';
STRING_COMPARE_OP: '==';
NOT_OP: 'not';
AND_OP: 'and';
OR_OP: 'or';

LB: '(';
RB: ')';
LS: '[';
RS: ']';
COMMA: ',';

NUMBERLIT: INT EXP? | INT '.' [0-9]* EXP?;
fragment INT: '0' | [1-9][0-9]*;
fragment INTLIT_NON_ZERO: [1-9][0-9]*;
fragment EXP: [eE] [+\-]? [0-9]+;

STRINGLIT: '"' CHAR_LIT*? '"' {self.text = self.text[1:-1]};
fragment CHAR_LIT: (ESC | ~[\\'"]);
fragment ESC: '\\' [bfrnt'\\] | '\'"';

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

NEWLINE: '\r'? '\n';

COMMENT: '##' .*? ('\r'? '\n')+ -> skip;

WS: [ \t\b\f\r]+ -> skip;

UNCLOSE_STRING:
	'"' CHAR_LIT*? UNTERMINATED {raise UncloseString(self.text[1:])};
fragment UNTERMINATED: '\r'? '\n' | EOF;

ILLEGAL_ESCAPE:
	'"' CHAR_LIT*? ('\\' ~[bfrnt'\\]) {IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};