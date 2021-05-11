#!/usr/bin/env python

"""
PyBison file automatically generated from grammar file t-grammar.y
You can edit this module, or import it and subclass the Parser class
"""

import sys

from bison import BisonParser, BisonNode, BisonSyntaxError

bisonFile = 't-grammar.y'  # original bison file
lexFile = 't-scanner.yy'    # original flex file


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

class Parser(BisonParser):
    """
    bison Parser class generated automatically by bison2py from the
    grammar file "t-grammar.y" and lex file "t-scanner.yy"

    You may (and probably should) edit the methods in this class.
    You can freely edit the rules (in the method docstrings), the
    tokens list, the start symbol, and the precedences.

    Each time this class is instantiated, a hashing technique in the
    base class detects if you have altered any of the rules. If any
    changes are detected, a new dynamic lib for the parser engine
    will be generated automatically.
    """

    # --------------------------------------------
    # basename of binary parser engine dynamic lib
    # --------------------------------------------
    bisonEngineLibName = 'testParser'

    # ----------------------------------------------------------------
    # lexer tokens - these must match those in your lex script (below)
    # ----------------------------------------------------------------
    tokens = ['T_NUM', 'T_ADD', 'T_SUB', 'T_MUL', 'T_DIV']

    # ------------------------------
    # precedences
    # ------------------------------
    precedences = (
        )

    start = 'program'

    def on_program(self, target, option, names, items):
        """
        program : a_expr
        """
        return program_Node(target=target, 
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
        a_fact : T_NUM
        """
        return a_fact_Node(target=target, 
                            option=option, 
                            names=names, 
                            items=items)

    lexscript= r"""
%{
#include <stdio.h>
#include <string.h>
#include <Python.h>
#define YYSTYPE void *
#include "tokens.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) yylval = PyUnicode_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) {(*py_input)(py_parser, buf, &result, max_size);}
%}

DIGIT [0-9]

%%

[ \t\n]+
"\+"				{ returntoken(T_ADD); }
"-"					{ returntoken(T_SUB); }
"\*"				{ returntoken(T_MUL); }
"/"					{ returntoken(T_DIV); }
{DIGIT}+[.]{DIGIT}+	                            { returntoken(T_NUM); }
{DIGIT}+					                    { returntoken(T_NUM); }
.

%%

yywrap() { return(1);}
    """

if __name__ == '__main__':
    Parser(verbose=1).run(file='test-inputs.smp', debug=1)