/* 2114417 */

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: ((varDecl | functionDecl) NEWLINE*)+ EOF;

varDecl: (NUMBER | BOOL | STRING | DYNAMIC) IDENTIFIER (
		ASSIGN expr
	)?
	| VAR IDENTIFIER ASSIGN expr
	| array_type (ASSIGN array_value)?;

functionDecl:
	FUNC IDENTIFIER LB paramList RB NEWLINE* statement_list?;

paramList: paramPrime |;
paramPrime: formalParameter COMMA paramPrime | formalParameter;
formalParameter: (NUMBER | BOOL | STRING) IDENTIFIER
	| array_type;

statement_type:
	varDecl
	| assign_stat
	| if_stat
	| for_stat
	| BREAK
	| CONTINUE
	| return_stat
	| func_call_stat
	| block_stat;

statement_list:
	statement_type NEWLINE+ statement_list
	| statement_type NEWLINE*;

assign_stat: lhs ASSIGN expr;
lhs: IDENTIFIER | index_expr;

if_stat: if_fragment elif_fragment*? else_fragment?;
if_fragment: IF LB expr RB NEWLINE* statement_list;
elif_fragment: ELIF LB expr RB NEWLINE* statement_list;
else_fragment: ELSE statement_list;

for_stat:
	FOR IDENTIFIER UNTIL expr BY expr NEWLINE* statement_list?;

return_stat: RETURN expr?;

func_call_stat: (IDENTIFIER LB arglist RB) | io_function;
arglist: argprime |;
argprime: expr COMMA argprime | expr;

block_stat: BEGIN NEWLINE+ statement_list? END;

io_function:
	read_number
	| write_number
	| read_bool
	| write_bool
	| read_string
	| write_string;

read_number: 'readNumber' LB RB;
write_number: 'writeNumber' LB expr RB;
read_bool: 'readBool' LB RB;
write_bool: 'writeBool' LB expr RB;
read_string: 'readString' LB RB;
write_string: 'writeString' LB expr RB;

array_type: (NUMBER | STRING | BOOL) IDENTIFIER LS dimension_list RS;
dimension_list: NUMBERLIT COMMA dimension_list | NUMBERLIT;

array_value: LS array_elements RS;
array_elements:
	array_nested_or_expression COMMA array_elements
	| array_nested_or_expression;
array_nested_or_expression: array_value | exprlist;

exprlist: expr COMMA exprlist | expr;
index_expr: (IDENTIFIER | func_call_stat) LS exprlist RS;

expr:
	LB expr RB
	| index_expr
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
	| array_value
	| func_call_stat
	| NUMBERLIT
	| TRUE
	| FALSE
	| STRINGLIT
	| IDENTIFIER;

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
fragment INT: [0-9]+;
fragment EXP: [eE] [+\-]? INT;

STRINGLIT: '"' CHAR_LIT*? '"' {self.text = self.text[1:-1]};
fragment CHAR_LIT: (ESC | ~[\\\n"]);
fragment ESC: '\\' [bfrnt'\\] | '\'"';

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

NEWLINE: '\r'? '\n';

COMMENT: '##' .*? ('\r'? '\n')+ -> skip;

WS: [ \t\b\f\r]+ -> skip;

UNCLOSE_STRING:
	'"' CHAR_LIT*? UNTERMINATED {
			unclosed_part = self.text[1:-1] if self.text[-1] == '\n' else self.text[1:]
			raise UncloseString(unclosed_part)
		};
fragment UNTERMINATED: NEWLINE | EOF;

ILLEGAL_ESCAPE:
	'"' CHAR_LIT*? ('\\' ~[bfrnt'\\]) {IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};