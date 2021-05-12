%language "c"
%skeleton "glr.c" 
%require "3.0.2"
%verbose
%defines 
%locations

// %code
// {
// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>

// extern void yyerror (char const *);
// extern int yylex ();
// extern char * yytext;
// }

%token T_NUM
%token T_ADD
%token T_SUB
%token T_MUL
%token T_DIV

%%

program : a_expr ;

a_expr : a_expr T_ADD a_term 
    | a_expr T_SUB a_term
    | a_term
     ; 

a_term : a_term T_MUL a_fact
    | a_term T_DIV a_fact
    | a_fact
     ; 

a_fact : T_NUM ;

%%

//void yyerror (YYLTYPE * loc, char const * msg)
// void yyerror (char const * msg)
// {
//   #ifndef PL_GRADER
//   printf ("Found error: %s (line %d, column %d)\n",
//     yytext, yylloc.last_line, yylloc.last_column);
//   #endif
// }