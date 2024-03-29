/* 2114417 */

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: NEWLINE* (decl NEWLINE+)+ EOF;

decl: varDecl | functionDecl;

varDecl: (NUMBER | BOOL | STRING | DYNAMIC) IDENTIFIER (
		ASSIGN expression
	)?
	| VAR IDENTIFIER ASSIGN expression
	| (NUMBER | STRING | BOOL) IDENTIFIER LS dimension_list RS (
		ASSIGN expression
	)?;

functionDecl:
	FUNC IDENTIFIER LB paramList RB NEWLINE* (
		return_stat
		| block_stat
	)?;

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

assign_stat: lhs ASSIGN expression;
lhs: IDENTIFIER | index_expr;

if_stat:
	if_fragment elif_stat
	| if_fragment elif_stat else_fragment
	| if_fragment else_fragment
	| if_fragment;
elif_stat: elif_fragment | elif_fragment elif_stat;

if_fragment:
	IF LB expression RB NEWLINE* statement_type NEWLINE*;
elif_fragment:
	ELIF LB expression RB NEWLINE* statement_type NEWLINE*;
else_fragment: ELSE statement_type NEWLINE*;

for_stat:
	FOR IDENTIFIER UNTIL expression BY expression NEWLINE* statement_type NEWLINE*;

return_stat: RETURN expression?;

func_call_stat: (IDENTIFIER LB arglist RB) | io_function;
arglist: argprime |;
argprime: expression COMMA argprime | expression;

block_stat: BEGIN NEWLINE+ statement_list? END;

io_function:
	read_number
	| write_number
	| read_bool
	| write_bool
	| read_string
	| write_string;

read_number: 'readNumber' LB RB;
write_number: 'writeNumber' LB expression RB;
read_bool: 'readBool' LB RB;
write_bool: 'writeBool' LB expression RB;
read_string: 'readString' LB RB;
write_string: 'writeString' LB expression RB;

array_type: (NUMBER | STRING | BOOL) IDENTIFIER LS dimension_list RS;
dimension_list: NUMBERLIT COMMA dimension_list | NUMBERLIT;

array_value: LS array_elements RS;
array_elements:
	array_nested_or_expression COMMA array_elements
	| array_nested_or_expression;
array_nested_or_expression: array_value | exprlist;

exprlist: expression COMMA exprlist | expression;
index_expr: (IDENTIFIER | func_call_stat) LS exprlist RS;

expression: expression_1 CONCAT_OP expression_1 | expression_1;
expression_1:
	expression_2 (
		EQUAL_OP
		| STRING_COMPARE_OP
		| NOT_EQUAL_OP
		| LESS_THAN_OP
		| GREATER_THAN_OP
		| LESS_EQUAL_OP
		| GREATER_EQUAL_OP
	) expression_2
	| expression_2;
expression_2:
	expression_2 (AND_OP | OR_OP) expression_3
	| expression_3;
expression_3:
	expression_3 (ADD_OF | SUB_OF) expression_4
	| expression_4;
expression_4:
	expression_4 (MUL_OF | DIV_OF | MOD_OF) expression_5
	| expression_5;
expression_5: NOT_OP expression_5 | expression_6;
expression_6: SUB_OF expression_6 | expression_7;
expression_7:
	array_value
	| index_expr
	| (IDENTIFIER LB arglist RB | io_function)
	| LB expression RB
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

COMMENT: '##' ~[\n]* -> skip;

WS: [ \t\b\f\r]+ -> skip;

UNCLOSE_STRING:
	'"' CHAR_LIT*? UNTERMINATED {
			unclosed_part = self.text[1:-1] if self.text[-1] == '\n' else self.text[1:]
			raise UncloseString(unclosed_part)
		};
fragment UNTERMINATED: NEWLINE | EOF;

ILLEGAL_ESCAPE:
	'"' CHAR_LIT*? ('\\' ~[bfrnt'\\]) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};