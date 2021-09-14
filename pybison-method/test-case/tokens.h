/* Token type.  */
// #ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    T_NUM = 259,
    T_ADD = 260,
    T_SUB = 261,
    T_MUL = 262,
    T_DIV = 263,
  };
// #endif

#if ! defined YYSTYPE /*&& ! defined YYSTYPE_IS_DECLARED*/
typedef int YYSTYPE;
// # define YYSTYPE_IS_TRIVIAL 1
// # define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;