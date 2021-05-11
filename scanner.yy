%{
#include <stdio.h>
#include <string.h>
#include <Python.h>
#define YYSTYPE void *
#include "simple.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) yylval = PyUnicode_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) {(*py_input)(py_parser, buf, &result, max_size);}
%}

DIGIT [0-9] 
ALPHA [a-zA-Z]

%%

\/\/.*$
[ ]+
[\t]+
[\n]+
\".+\"						{ returntoken(T_LITERAL_STR); }
";"               { returntoken(T_SEMICOLON); }
":="							{ returntoken(T_ASSIGN); }
":"               { returntoken(T_COLON); }
"("               { returntoken(T_LPAREN); }
")"               { returntoken(T_RPAREN); }
"\["               { returntoken(T_LBRACK); }
"]"               { returntoken(T_RBRACK); }
", "               { returntoken(T_COMMA_DELIM); }
"\+"				{ returntoken(T_ADD); }
"-"					{ returntoken(T_SUB); }
"\*"				{ returntoken(T_MUL); }
"/"					{ returntoken(T_DIV); }
"<"				    { returntoken(T_LT); }
">"					{ returntoken(T_GT); }
">="				{ returntoken(T_GEQ); }
"<="			    { returntoken(T_LEQ); }
"="					{ returntoken(T_EQ); }
"<>"			    { returntoken(T_NEQ); }
"and"				{ returntoken(T_AND); }
"or"				{ returntoken(T_OR); }
"foreach"			{ returntoken(T_FOREACH); }
"in"				{ returntoken(T_IN); }
"while"				{ returntoken(T_WHILE); }
"begin"		        { returntoken(T_BEGIN); }
"end"				{ returntoken(T_END); }
"if"				{ returntoken(T_IF); }
"then"				{ returntoken(T_THEN); }
"else"				{ returntoken(T_ELSE); }
"write"			    { returntoken(T_WRITE); }
"read"		        { returntoken(T_READ); }
"int"				{ returntoken(T_INTEGER); }
"float"			    { returntoken(T_FLOAT); }
"repeat"		    { returntoken(T_REPEAT); }
"until"				{ returntoken(T_UNTIL); }
"declare"			{ returntoken(T_DECLARE); }
{DIGIT}+[.]{DIGIT}+	                            { returntoken(T_NUM); }
{DIGIT}+					                    { returntoken(T_NUM);}
({ALPHA}|[_])({DIGIT}|{ALPHA}|[_])*             { returntoken(T_ID); }
.

%%

yywrap() { return(1);}