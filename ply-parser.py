# -----------------------------------------------------------------------------
# Programming Assignment #2 Parser
#
# Author: Josh Stenis
# -----------------------------------------------------------------------------

tokens = (
    'COMMENT', 
    'ID', 'NUM', 'ADD', 'SUB', 'MUL', 'DIV', 
    'LT', 'GT', 'LEQ', 'GEQ', 'EQ', 'NEQ', 
    'AND', 'OR', 
    'READ', 'WRITE', 'ASSIGN', 'BEGIN', 'END', 'FOREACH', 'IN', 'REPEAT', 'UNTIL', 'WHILE', 'IF', 'THEN', 'ELSE', 'LITERAL_STR', 
    'SEMICOLON', 'COLON', 'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'COMMA'
)

# Skips commmented lines
def t_COMMENT(t):
    r'\/\/.*$'
    t.lexer.lineno += 1
    t.lexer.skip(len(t.value))

t_LITERAL_STR = r'\".+\"'
t_SEMICOLON = r';'
t_ASSIGN = r':='
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN =  r'\)'
t_LBRACK = r'\['
t_RBRACK = r']'
t_COMMA = r','
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LEQ = r'<='
t_GEQ = r'>='
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NEQ = r'!='
t_FOREACH = r'foreach'
t_REPEAT = r'repeat'
t_WHILE = r'while'
t_BEGIN = r'begin'
t_UNTIL = r'until'
t_WRITE = r'write'
t_THEN = r'then'
t_ELSE = r'else'
t_READ = r'read'
t_END = r'end'
t_AND = r'and'
t_OR = r'or'
t_IF = r'if'
t_IN = r'in'
t_NUM = r'\d+\.\d+|\d+'
t_ID = r'[a-zA-Z_]\w*'

t_ignore = ' \t'

# Skips newline characters and updates t.lexer.lineno
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print('Illegal character: ({0}, {1})'.format(t.type, t.value))

import ply.lex as lex
lexer = lex.lex()


# ------------------------------------------
# Grammar rules defined below
# ------------------------------------------

precedences = [
    ('left', 'OR'), 
    ('left', 'AND'), 
    ('left', ('SUB', 'ADD')),
    ('left', ('MUL', 'DIV')),
]

def p_program(p):
    '''program : stmt_list SEMICOLON'''

def p_stmt_list(p):
    '''stmt_list : stmt_list SEMICOLON stmt 
                 | stmt'''

def p_stmt(p):
    '''stmt : assignment 
            | read 
            | write 
            | while 
            | repeat 
            | block 
            | foreach 
            | if_stmt'''

def p_assignment(p):
    '''assignment : varref ASSIGN l_expr'''

def p_read(p):
    '''read : READ varlist'''

def p_write(p):
    '''write : WRITE expr_list'''

def p_while(p):
    '''while : WHILE l_expr block'''

def p_repeat(p):
    '''repeat : REPEAT stmt_list UNTIL l_expr'''

def p_block(p):
    '''block : BEGIN stmt_list END'''

def p_foreach(p):
    '''foreach : FOREACH ID IN LPAREN a_expr COLON a_expr RPAREN stmt'''

def p_if_stmt(p):
    '''if_stmt : IF l_expr THEN stmt_list ELSE else_stmt'''

def p_else_stmt(p):
    '''else_stmt : ELSE stmt
                 | '''

def p_a_expr(p):
    '''a_expr : a_expr a_op a_expr
              | SUB a_expr 
              | varref
              | NUM 
              | LITERAL_STR 
              | LPAREN a_expr RPAREN'''

def p_a_op(p):
    '''a_op : ADD 
            | SUB 
            | MUL 
            | DIV'''

def p_varref(p):
    '''varref : ID 
              | varref LBRACK a_expr RBRACK'''

def p_l_expr(p):
    '''l_expr : l_expr l_op l_expr
              | l_expr oprel a_expr
              | a_expr
              | LPAREN l_expr RPAREN'''

def p_l_op(p):
    '''l_op : OR 
            | AND'''

def p_oprel(p):
    '''oprel : LT
             | GT
             | LEQ
             | GEQ
             | EQ
             | NEQ'''

def p_varlist(p):
    '''varlist : varlist COMMA varlist
               | varref'''

def p_expr_list(p):
    '''expr_list : a_expr
                 | expr_list COMMA a_expr'''

def p_error(p):
    print('Parsing error: ({0}, \'{1}\') at line {2}'.format(p.type, p.value, p.lexer.lineno))

import ply.yacc as yacc
parser = yacc.yacc(method='LALR')


# ------------------------------------------
# Code executed here
# ------------------------------------------

prgm = open('inputs/{}.smp'.format(input('File: ')), 'r').read()
parser.parse(prgm, lexer=lexer)