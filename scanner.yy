%{
#include <stdio.h>
#include <string.h>
#include <Python.h>
#define YYSTYPE void *
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) yylval = PyString_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) {(*py_input)(py_parser, buf, &result, max_size);}

#include "simple.h"
# undef yywrap
# define yywrap() 1

#undef YY_DECL
#define YY_DECL int yylex()
YY_DECL;

// Code run each time a pattern is matched.
#undef  YY_USER_ACTION  
# define YY_USER_ACTION  {}

%}

%option yylineno
%option noyywrap 

DIGIT [0-9] 
ALPHA [a-zA-Z]

%%

\/\/.*$           { yylloc.last_line++; yylloc.last_column = 0;}	
[ ]+						  { yylloc.last_column++;}	
[\t]+						  { yylloc.last_column+=2;}	
[\n]+						  {yylloc.last_line++; yylloc.last_column = 0;}	
\".+\"						{ 
                    yylloc.last_column += strlen(yytext);
                                        returntoken(T_LITERAL_STR); 
                }
";"               {
                    yylloc.last_column++;
                    returntoken(T_SEMICOLON);
                }
":="							{ 
                    yylloc.last_column += 2;
                                        returntoken(T_ASSIGN); 
                }
":"               {
                    yylloc.last_column++;
                    returntoken(T_COLON);
                }
"("               {
                    yylloc.last_column++;
                    returntoken(T_LPAREN);
                }
")"               {
                    yylloc.last_column++;
                    returntoken(T_RPAREN);
                }
"\["               {
                    yylloc.last_column++;
                    returntoken(T_LBRACK);
                }
"]"               {
                    yylloc.last_column++;
                    returntoken(T_RBRACK);
                }
", "               {
                    yylloc.last_column+=2;
                    returntoken(T_COMMA_DELIM);
                }
"\+"							  { 
                    yylloc.last_column++;
                                        returntoken(T_ADD); 
                }
"-"							  { 
                    yylloc.last_column++;
                                        returntoken(T_SUB); 
                }
"\*"							  { 
                    yylloc.last_column++;
                                        returntoken(T_MUL); 
                }
"/"							  { 
                    yylloc.last_column++;
                                        returntoken(T_DIV); 
                }
"<"							  { 
                    yylloc.last_column++;
                                        returntoken(T_LT); 
                }
">"							  { 
                    yylloc.last_column++;
                                        returntoken(T_GT); 
                }
">="							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_GEQ); 
                }
"<="							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_LEQ); 
                }
"="							  { 
                    yylloc.last_column+=1;
                                        returntoken(T_EQ); 
                }
"<>"							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_NEQ); 
                }
"and"							{ 
                    yylloc.last_column+=3;
                                        returntoken(T_AND); 
                }
"or"							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_OR); 
                }
"foreach"				  { 
                    yylloc.last_column+=7;
                                        returntoken(T_FOREACH); 
                }
"in"				      { 
                    yylloc.last_column+=2;
                                        returntoken(T_IN); 
                }
"while"				    { 
                    yylloc.last_column+=5;
                                        returntoken(T_WHILE); 
                }
"begin"					  { 
                    yylloc.last_column+=5;
                                        returntoken(T_BEGIN); 
                }
"end"				      { 
                    yylloc.last_column+=3;
                                        returntoken(T_END); 
                }
"if"				      { 
                    yylloc.last_column+=2;
                                        returntoken(T_IF); 
                }
"then"				    { 
                    yylloc.last_column+=4;
                                        returntoken(T_THEN); 
                }
"else"				    { 
                    yylloc.last_column+=4;
                                        returntoken(T_ELSE); 
                }
"write"						{ 
                    yylloc.last_column+=5;
                                        returntoken(T_WRITE); 
                }
"read"						{ 
                    yylloc.last_column+=4;
                                        returntoken(T_READ); 
                }
"int"							{ 
                    yylloc.last_column+=3;
                                        returntoken(T_INTEGER); 
                }
"float"						{ 
                    yylloc.last_column+=5;
                                        returntoken(T_FLOAT); 
                }
"repeat"				  { 
                    yylloc.last_column+=6;
                                        returntoken(T_REPEAT); 
                }
"until"				    { 
                    yylloc.last_column+=5;
                                        returntoken(T_UNTIL); 
                }
"declare"					{ 
                    yylloc.last_column+=7;
                                        returntoken(T_DECLARE); 
                }
{DIGIT}+[.]{DIGIT}+	{ 
                    yylloc.last_column += strlen(yytext);
                    returntoken(T_NUM);
                                    }
{DIGIT}+					{ 
                    yylloc.last_column += strlen(yytext);
                                        returntoken(T_NUM);
                                    }
({ALPHA}|[_])({DIGIT}|{ALPHA}|[_])*     { 
                                        yylloc.last_column += strlen(yytext);
                                                                                    returntoken(T_ID);
                                                                                }

.									{  yylloc.last_column++; returntoken(yytext[0]);}

%%

yywrap() { return(1);}