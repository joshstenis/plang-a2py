# -----------------------------------------------------------------------------
# PLang Assignment 2 Parser
#
# Encapsulates grammar (.y) and scanner (.yy) files
# -----------------------------------------------------------------------------


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
t_SEMICOLON = ';'
t_ASSIGN = ':='
t_COLON = ':'
t_LPAREN = r'\('
t_RPAREN =  r'\)'
t_LBRACK = r'\['
t_RBRACK = ']'
t_COMMA_DELIM = ', '
t_ADD = r'\+'
t_SUB = '-'
t_MUL = r'\*'
t_DIV = '/'
t_LT = '<'
t_GT = '>'
t_LEQ = '<='
t_GEQ = '>='
t_EQ = '=='
t_NEQ = '!='
t_AND = 'and'
t_OR = 'or'
t_FOREACH = 'foreach'
t_IN = 'in'
t_WHILE = 'while'
t_BEGIN = 'begin'
t_END = 'end'
t_IF = 'if'
t_THEN = 'then'
t_ELSE = 'else'
t_WRITE = 'write'
t_READ = 'read'
t_REPEAT = 'repeat'
t_UNTIL = 'until'
t_NUM = r'[0-9]+[.][0-9]+ | [0-9]+'
t_ID = r'([a-zA-Z] | [_])([0-9]] | [a-zA-Z] | [_])*'

def t_error(t):
    # print('Invalid character: {}'.format(t.value[0]))
    # t.lexer.skip(1)
    pass

import ply.lex as lex
lexer = lex.lex()


# ------------------------------------------
# Grammar rules defined below
# ------------------------------------------

def p_program(t):
    '''
    program : stmt_list SEMICOLON
    '''

def p_stmt_list(t):
    '''
    stmt_list : stmt_list SEMICOLON stmt
        | stmt
    '''

def p_stmt(t):
    '''
    stmt : assignment
        | read 
        | write
        | while
        | repeat
        | block
        | foreach
        | if_stmt
    '''

def p_block(t):
    '''
    block : BEGIN stmt_list END
    '''

def p_foreach(t):
    '''
    foreach : FOREACH ID IN LPAREN a_fact COLON a_fact RPAREN stmt
    '''

def p_while(t):
    '''
    while : WHILE l_expr block
    '''

def p_repeat(t):
    '''
    repeat : REPEAT stmt_list UNTIL l_expr
    '''

def p_if_stmt(t):
    '''
    if_stmt : IF l_expr THEN stmt_list ELSE else_stmt
    '''

def p_else_stmt(t):
    '''
    else_stmt : 
        | ELSE stmt
    '''

def p_assignment(t):
    '''
    assignment : varref ASSIGN l_expr
    '''

def p_a_expr(t):
    '''
    a_expr : a_expr ADD a_term
        | a_expr SUB a_term
        | a_term
    '''

def p_a_term(t):
    '''
    a_term : a_term MUL a_fact
        | a_term DIV a_fact
        | a_fact
    '''

def p_a_fact(t):
    '''
    a_fact : varref
        | NUM
        | LITERAL_STR
        | SUB a_fact
        | LPAREN a_expr RPAREN
    '''

def p_varref(t):
    '''
    varref : ID
        | varref LBRACK a_expr RBRACK
    '''

def p_l_expr(t):
    '''
    l_expr : l_expr AND l_term
        | l_term
    '''

def p_l_term(t):
    '''
    l_term : l_term OR l_fact
        | l_fact
    '''

def p_l_fact(t):
    '''
    l_fact : l_fact oprel a_expr
        | a_expr
        | LPAREN l_expr RPAREN
    '''

def p_oprel(t):
    '''
    oprel : LT
        | GT
        | LEQ
        | GEQ
        | EQ
        | NEQ
    '''

def p_read(t):
    '''
    read : READ varlist
    '''

def p_write(t):
    '''
    write : WRITE expr_list
    '''

def p_varlist(t):
    '''
    varlist : varref
        | varref COMMA_DELIM varlist
    '''

def p_expr_list(t):
    '''
    expr_list : a_expr
        | expr_list COMMA_DELIM a_expr
    '''

def p_error(t):
    print('Syntax error at {}\n'.format(t))               # at {}'.format(t.value)

import ply.yacc as yacc
parser = yacc.yacc()


# ------------------------------------------
# Code executed here
# ------------------------------------------

prgm = open('inputs/{}.smp'.format(input('File: ')), 'r').read()
parser.parse(prgm)