# -----------------------------------------------------------------------------
# PLang Assignment 2 Parser
#
# Encapsulates grammar (.y) and scanner (.yy) files
# -----------------------------------------------------------------------------

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'ID', 'NUM', 'ADD', 'SUB', 'MUL', 'DIV', 
    'LT', 'GT', 'LEQ', 'GEQ', 'EQ', 'NEQ', 
    'AND', 'OR', 
    'READ', 'WRITE', 'ASSIGN', 'BEGIN', 'END', 'FOREACH', 'IN', 'REPEAT', 'UNTIL', 'WHILE', 'IF', 'THEN', 'ELSE', 'DECLARE', 
    'INTEGER', 'FLOAT', 'LITERAL_STR', 
    'SEMICOLON', 'COLON', 'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'COMMA_DELIM'
)


# ------------------------------------------
# Scanner rules defined below
# ------------------------------------------

t_ignore = ' \t\n'
t_LITERAL_STR = r'\".+\"'
t_SEMICOLON = r';'
t_ASSIGN = r':='
t_COLON = r':'
t_LPAREN = r'('
t_RPAREN =  r')'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_COMMA_DELIM = r', '
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LT = r'<'
t_GT = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_EQ = r'=='
t_NEQ = r'!='
t_AND = 'and'
t_OR = r'or'
t_FOREACH = r'foreach'
t_IN = r'in'
t_WHILE = r'while'
t_BEGIN = r'begin'
t_END = r'end'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_WRITE = r'write'
t_READ = r'read'
t_INTEGER = r'int'
t_FLOAT = r'float'
t_REPEAT = r'repeat'
t_UNTIL = r'until'
t_DECLARE = r'declare'
t_NUM = r'{DIGIT}+[.]{DIGIT}+ | {DIGIT}+'
t_ID = r'({ALPHA}|[_])({DIGIT}|{ALPHA}|[_])*'


# ------------------------------------------
# Scanner rules defined below
# ------------------------------------------