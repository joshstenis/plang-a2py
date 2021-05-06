import ply.lex as lex

tokens = (
    'LITERAL_STR',
    'ASSIGN',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'LT',
    'GT',
    'GEQ',
    'LEQ',
    'EQ',
    'NEQ',
    'AND',
    'OR',
    'FOREACH',
    'IN',
    'WHILE',
    'BEGIN',
    'END',
    'IF',
    'THEN',
    'ELSE',
    'WRITE',
    'READ',
    'INTEGER',
    'FLOAT',
    'REPEAT',
    'UNTIL',
    'DECLARE',
    'NUM',
    'ID'
)

t_LITERAL_STR = r'\".+\"'
t_ASSIGN = r':='
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LT = r'<'
t_GT = r'>'
t_GEQ = r'>='
t_LEQ = r'<='
t_EQ = r'=='
t_NEQ = r'!='
t_AND = r'and'
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
t_NUM = r'\d+\.\d+ | \d+'
t_ID = r'(^\W\d_|_)(\d|^\W\d_|[_])*'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\/\/'

def t_err(t):
    t.lexer.skip(1)

lexer = lex.lex()