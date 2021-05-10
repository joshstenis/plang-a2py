#!/usr/bin/env python

"""
PyBison file automatically generated from grammar file grammar.y
You can edit this module, or import it and subclass the Parser class
"""

import sys

from bison import BisonParser, BisonNode, BisonSyntaxError

bisonFile = 'grammar.y'  # original bison file
lexFile = 'scanner.yy'    # original flex file


class ParseNode(BisonNode):
    """
    This is the base class from which all your
    parse nodes are derived.
    Add methods to this class as you need them
    """
    def __init__(self, **kw):
        BisonNode.__init__(self, **kw)

    def __str__(self):
        """Customise as needed"""
        return '<%s instance at 0x%x>' % (self.__class__.__name__, hash(self))

    def __repr__(self):
        """Customise as needed"""
        return str(self)

    def dump(self, indent=0):
        """
        Dump out human-readable, indented parse tree
        Customise as needed - here, or in the node-specific subclasses
        """
        BisonNode.dump(self, indent) # alter as needed


# ------------------------------------------------------
# Define a node class for each grammar target
# ------------------------------------------------------

class program_Node(ParseNode):
    """
    Holds a "program" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class stmt_list_Node(ParseNode):
    """
    Holds a "stmt_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class stmt_Node(ParseNode):
    """
    Holds a "stmt" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class block_Node(ParseNode):
    """
    Holds a "block" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class foreach_Node(ParseNode):
    """
    Holds a "foreach" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class while_Node(ParseNode):
    """
    Holds a "while" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class repeat_Node(ParseNode):
    """
    Holds a "repeat" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class if_stmt_Node(ParseNode):
    """
    Holds an "if_stmt" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class else_stmt_Node(ParseNode):
    """
    Holds an "else_stmt" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class assignment_Node(ParseNode):
    """
    Holds an "assignment" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class a_expr_Node(ParseNode):
    """
    Holds an "a_expr" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class a_term_Node(ParseNode):
    """
    Holds an "a_term" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class a_fact_Node(ParseNode):
    """
    Holds an "a_fact" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class varref_Node(ParseNode):
    """
    Holds a "varref" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class l_expr_Node(ParseNode):
    """
    Holds a "l_expr" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class l_term_Node(ParseNode):
    """
    Holds a "l_term" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class l_fact_Node(ParseNode):
    """
    Holds a "l_fact" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class oprel_Node(ParseNode):
    """
    Holds an "oprel" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class read_Node(ParseNode):
    """
    Holds a "read" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class write_Node(ParseNode):
    """
    Holds a "write" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class varlist_Node(ParseNode):
    """
    Holds a "varlist" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class expr_list_Node(ParseNode):
    """
    Holds an "expr_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)

class Parser(BisonParser):
    """
    bison Parser class generated automatically by bison2py from the
    grammar file "grammar.y" and lex file "scanner.yy"

    You may (and probably should) edit the methods in this class.
    You can freely edit the rules (in the method docstrings), the
    tokens list, the start symbol, and the precedences.

    Each time this class is instantiated, a hashing technique in the
    base class detects if you have altered any of the rules. If any
    changes are detected, a new dynamic lib for the parser engine
    will be generated automatically.
    """

    bisonCmd = ['bison', '-d', '-v', '-t']
    bisonFile = 'tmp.y'
    bisonCFile = 'tmp.tab.c'
    bisonHFIle = 'tmp.tab.h'

    flexCmd = ['flex', '-o']
    flexFile = 'tmp.yy'
    flexCFile = 'lex.yy.c'

    cflags_pre = ['-fPIC']
    cflags_post = ['-O3', '-g']

    file = None
    keepfiles = 0

    bisonEngineLibName = 'parser2-engine'

    tokens = ['T_ID', 'T_NUM', 'T_ADD', 'T_SUB', 'T_MUL', 'T_DIV', 'T_LT', 'T_GT', 'T_LEQ', 'T_GEQ', 'T_EQ', 'T_NEQ', 'T_AND', 'T_OR', 'T_READ', 'T_WRITE', 'T_ASSIGN', 'T_BEGIN', 'T_END', 'T_FOREACH', 'T_IN', 'T_REPEAT', 'T_UNTIL', 'T_WHILE', 'T_IF', 'T_THEN', 'T_ELSE', 'T_DECLARE', 'T_INTEGER', 'T_FLOAT', 'T_LITERAL_STR', 'T_SEMICOLON', 'T_COLON', 'T_LPAREN', 'T_RPAREN', 'T_LBRACK', 'T_RBRACK', 'T_COMMA_DELIM']
    precedences = ()

    # -------------------------------------
    # Override default read method
    # -------------------------------------
    def read(self, nbytes):
        try:
            return input() + '\n'
        except:
            return ''

    start = 'program'

    def on_program(self, target, option, names, items):
        """
        program : stmt_list T_SEMICOLON
        """
        return program_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_stmt_list(self, target, option, names, items):
        """
        stmt_list : stmt_list T_SEMICOLON stmt
            | stmt
        """
        return stmt_list_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_stmt(self, target, option, names, items):
        """
        stmt : assignment
            | read 
            | write
            | while
            | repeat
            | block
            | foreach
            | if_stmt
        """
        return stmt_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_block(self, target, option, names, items):
        """
        block : T_BEGIN stmt_list T_END
        """
        return block_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_foreach(self, target, option, names, items):
        """
        foreach : T_FOREACH T_ID
            T_IN
            T_LPAREN a_fact T_COLON a_fact T_RPAREN 
            stmt
        """
        return foreach_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_while(self, target, option, names, items):
        """
        while : T_WHILE l_expr
            T_BEGIN
            stmt_list
            T_END
        """
        return while_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_repeat(self, target, option, names, items):
        """
        repeat : T_REPEAT stmt_list T_UNTIL l_expr
        """
        return repeat_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_if_stmt(self, target, option, names, items):
        """
        if_stmt : T_IF l_expr
            T_THEN stmt_list
            T_ELSE else_stmt
        """
        return if_stmt_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_else_stmt(self, target, option, names, items):
        """
        else_stmt : 
            | T_ELSE stmt
        """
        return else_stmt_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_assignment(self, target, option, names, items):
        """
        assignment : varref T_ASSIGN l_expr
        """
        return assignment_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_a_expr(self, target, option, names, items):
        """
        a_expr : a_expr T_ADD a_term 
            | a_expr T_SUB a_term
            | a_term
        """
        return a_expr_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_a_term(self, target, option, names, items):
        """
        a_term : a_term T_MUL a_fact
            | a_term T_DIV a_fact
            | a_fact
        """
        return a_term_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_a_fact(self, target, option, names, items):
        """
        a_fact : varref
            | T_NUM
            | T_LITERAL_STR
            | T_SUB a_fact
            | T_LPAREN a_expr T_RPAREN
        """
        return a_fact_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_varref(self, target, option, names, items):
        """
        varref : T_ID 
            | varref T_LBRACK a_expr T_RBRACK
        """
        return varref_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_l_expr(self, target, option, names, items):
        """
        l_expr : l_expr T_AND l_term
            | l_term
        """
        return l_expr_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_l_term(self, target, option, names, items):
        """
        l_term : l_term T_OR l_fact
            | l_fact
        """
        return l_term_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_l_fact(self, target, option, names, items):
        """
        l_fact : l_fact oprel a_expr
            | a_expr
            | T_LPAREN l_expr T_RPAREN
        """
        return l_fact_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_oprel(self, target, option, names, items):
        """
        oprel : T_LT
            | T_GT
            | T_LEQ
            | T_GEQ
            | T_EQ
            | T_NEQ
        """
        return oprel_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_read(self, target, option, names, items):
        """
        read : T_READ varlist
        """
        return read_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_write(self, target, option, names, items):
        """
        write : T_WRITE expr_list
        """
        return write_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_varlist(self, target, option, names, items):
        """
        varlist : varref
            | varref T_COMMA_DELIM varlist
        """
        return varlist_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    def on_expr_list(self, target, option, names, items):
        """
        expr_list : a_expr
            | expr_list T_COMMA_DELIM a_expr
        """
        return expr_list_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    lexscript = lexFile

if __name__ == "__main__":
    p = Parser()
    p.run()