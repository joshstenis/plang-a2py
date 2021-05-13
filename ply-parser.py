# -----------------------------------------------------------------------------
# Programming Assignment #2 Parser
#
# Author: Josh Stenis
# -----------------------------------------------------------------------------

tokens = (
    'COMMENT', 'LITERAL_STR', 'SEMICOLON', 'ASSIGN', 'COLON', 'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'COMMA', 
    'ADD', 'SUB', 'MUL', 'DIV', 
    'LT', 'GT', 'LEQ', 'GEQ', 'EQ', 'NEQ', 
    'FOREACH', 'REPEAT', 'WHILE', 'BEGIN', 'UNTIL', 'WRITE', 'THEN', 'ELSE', 'READ', 'END', 'AND', 'OR', 'IF', 'IN', 
    'ID', 'NUM', 'EOF'
)

# Skips commmented lines
def t_COMMENT(t):
    r'\/\/.*$'
    t.lexer.lineno += 1
    t.lexer.skip(len(t.value))

def t_LITERAL_STR(t):
    r'\".+\"'
    return t
def t_SEMICOLON(t):
    r';'
    return t
def t_ASSIGN(t):
    r':='
    return t
def t_COLON(t):
    r':'
    return t
def t_LPAREN(t):
    r'\('
    return t
def t_RPAREN(t):
    r'\)'
    return t
def t_LBRACK(t):
    r'\['
    return t
def t_RBRACK(t):
    r']'
    return t
def t_COMMA(t):
    r','
    return t
def t_ADD(t):
    r'\+'
    return t
def t_SUB(t):
    r'-'
    return t
def t_MUL(t):
    r'\*'
    return t
def t_DIV(t):
    r'/'
    return t
def t_LEQ(t):
    r'<='
    return t
def t_GEQ(t):
    r'>='
    return t
def t_LT(t):
    r'<'
    return t
def t_GT(t):
    r'>'
    return t
def t_EQ(t):
    r'=='
    return t
def t_NEQ(t):
    r'!='
    return t
def t_FOREACH(t):
    r'foreach'
    return t
def t_REPEAT(t):
    r'repeat'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_BEGIN(t):
    r'begin'
    return t
def t_UNTIL(t):
    r'until'
    return t
def t_WRITE(t):
    r'write'
    return t
def t_THEN(t):
    r'then'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_READ(t):
    r'read'
    return t
def t_END(t):
    r'end'
    return t
def t_AND(t):
    r'and'
    return t
def t_OR(t):
    r'or'
    return t
def t_IF(t):
    r'if'
    return t
def t_IN(t):
    r'in'
    return t
def t_NUM(t):
    r'\d+\.\d+|\d+'
    return t
def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

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
    ('left', ('MUL', 'DIV'))
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
              | NUM 
              | varref
              | LITERAL_STR 
              | LPAREN a_expr RPAREN'''

def p_a_op(p):
    '''a_op : ADD 
            | SUB 
            | MUL 
            | DIV'''

def p_varref(p):
    '''varref : varref LBRACK a_expr RBRACK 
              | ID'''

def p_l_expr(p):
    '''l_expr : LPAREN l_expr RPAREN 
              | l_expr l_op l_expr
              | l_expr oprel l_expr
              | a_expr'''

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
    if p == None:
        print('End of file reached.')
    else:
        print('Parsing error: ({0}, \'{1}\') at line {2}'.format(p.type, p.value, p.lexer.lineno))

import ply.yacc as yacc
parser = yacc.yacc()


# ------------------------------------------
# Code executed here
# ------------------------------------------

prgm = open('inputs/{}.smp'.format(input('File: ')), 'r').read()
parser.parse(prgm, lexer=lexer)