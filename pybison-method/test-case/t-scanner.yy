%{
#include <stdio.h>
#include <string.h>
#include <Python.h>
#define YYSTYPE void *
#include "tokens.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) yylval = PyUnicode_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) {(*py_input)(py_parser, buf, &result, max_size);}
%}

DIGIT [0-9]

%%

\/\/.*$
[ ]+
[\t]+
[\n]+
"\+"				{ returntoken(T_ADD); }
"-"					{ returntoken(T_SUB); }
"\*"				{ returntoken(T_MUL); }
"/"					{ returntoken(T_DIV); }
{DIGIT}+[.]{DIGIT}+	                            { returntoken(T_NUM); }
{DIGIT}+					                    { returntoken(T_NUM); }
.

%%

yywrap() { return(1);}