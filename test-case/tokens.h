/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    T_ID = 258,
    T_NUM = 259,
    T_ADD = 260,
    T_SUB = 261,
    T_MUL = 262,
    T_DIV = 263,
    T_LT = 264,
    T_GT = 265,
    T_LEQ = 266,
    T_GEQ = 267,
    T_EQ = 268,
    T_NEQ = 269,
    T_AND = 270,
    T_OR = 271,
    T_READ = 272,
    T_WRITE = 273,
    T_ASSIGN = 274,
    T_BEGIN = 275,
    T_END = 276,
    T_FOREACH = 277,
    T_IN = 278,
    T_REPEAT = 279,
    T_UNTIL = 280,
    T_WHILE = 281,
    T_IF = 282,
    T_THEN = 283,
    T_ELSE = 284,
    T_DECLARE = 285,
    T_INTEGER = 286,
    T_FLOAT = 287,
    T_LITERAL_STR = 288,
    T_SEMICOLON = 289, 
    T_COLON = 290, 
    T_LPAREN = 291, 
    T_RPAREN = 292, 
    T_LBRACK = 293, 
    T_RBRACK = 294, 
    T_COMMA_DELIM = 295
  };
#endif

// #if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
// typedef int YYSTYPE;
// # define YYSTYPE_IS_TRIVIAL 1
// # define YYSTYPE_IS_DECLARED 1
// #endif

typedef int YYSTYPE;

extern YYSTYPE yylval;