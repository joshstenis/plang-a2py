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

    bisonEngineLibName = 'parser-engine'

    tokens = ['T_ID', 'T_NUM', 'T_ADD', 'T_SUB', 'T_MUL', 'T_DIV', 'T_LT', 'T_GT', 'T_LEQ', 'T_GEQ', 'T_EQ', 'T_NEQ', 'T_AND', 'T_OR', 'T_READ', 'T_WRITE', 'T_ASSIGN', 'T_BEGIN', 'T_END', 'T_FOREACH', 'T_IN', 'T_REPEAT', 'T_UNTIL', 'T_WHILE', 'T_IF', 'T_THEN', 'T_ELSE', 'T_DECLARE', 'T_INTEGER', 'T_FLOAT', 'T_LITERAL_STR', 'T_SEMICOLON', 'T_COLON', 'T_LPAREN', 'T_RPAREN', 'T_LBRACK', 'T_RBRACK', 'T_COMMA_DELIM', 'T_QUIT']
    precedences = (('left', ('T_SUB', 'T_ADD')),
        ('left', ('T_MUL', 'T_DIV')),
    )

    def read(self, nbytes):
        return input('I EXIST: ') + '\n'

    start = 'program'

    def on_program(self, target, option, names, items):
        """
        program : stmt_list T_SEMICOLON
        """
        if 'error' in option:
            raise BisonSyntaxError
        else:
            return program_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)

    def on_stmt_list(self, target, option, names, items):
        """
        stmt_list : stmt_list T_SEMICOLON stmt
            | stmt
        """
        if 'error' in option:
            raise BisonSyntaxError('ERROR')
        else:
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
        if 'error' in option:
            raise BisonSyntaxError
        else:
            return stmt_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)

    def on_block(self, target, option, names, items):
        """
        block : T_BEGIN stmt_list T_END
        """
        if 'error' in option:
            raise BisonSyntaxError
        else:
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
        if 'error' in option:
            raise BisonSyntaxError
        else:
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
        if 'error' in option:
            raise BisonSyntaxError('ERROR')
        else:
            return while_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)

    def on_repeat(self, target, option, names, items):
        """
        repeat : T_REPEAT stmt_list T_UNTIL l_expr
        """
        if 'error' in option:
            raise BisonSyntaxError
        else:
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
        if 'error' in option:
            raise BisonSyntaxError
        else:
            return if_stmt_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)

    def on_else_stmt(self, target, option, names, items):
        """
        else_stmt : 
            | T_ELSE stmt
        """
        try:
            node = else_stmt_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_assignment(self, target, option, names, items):
        """
        assignment : varref T_ASSIGN l_expr
        """
        try:
            node = assignment_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_a_expr(self, target, option, names, items):
        """
        a_expr : a_expr T_ADD a_term 
            | a_expr T_SUB a_term
            | a_term
        """
        try:
            node = a_expr_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_a_term(self, target, option, names, items):
        """
        a_term : a_term T_MUL a_fact
            | a_term T_DIV a_fact
            | a_fact
        """
        try:
            node = a_term_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_a_fact(self, target, option, names, items):
        """
        a_fact : varref
            | T_NUM
            | T_LITERAL_STR
            | T_SUB a_fact
            | T_LPAREN a_expr T_RPAREN
        """
        try:
            node = a_fact_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_varref(self, target, option, names, items):
        """
        varref : T_ID 
            | varref T_LBRACK a_expr T_RBRACK
        """
        try:
            node = varref_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_l_expr(self, target, option, names, items):
        """
        l_expr : l_expr T_AND l_term
            | l_term
        """
        try:
            node = l_expr_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_l_term(self, target, option, names, items):
        """
        l_term : l_term T_OR l_fact
            | l_fact
        """
        try:
            node = l_term_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_l_fact(self, target, option, names, items):
        """
        l_fact : l_fact oprel a_expr
            | a_expr
            | T_LPAREN l_expr T_RPAREN
        """
        try:
            node = l_fact_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_oprel(self, target, option, names, items):
        """
        oprel : T_LT
            | T_GT
            | T_LEQ
            | T_GEQ
            | T_EQ
            | T_NEQ
        """
        try:
            node = oprel_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_read(self, target, option, names, items):
        """
        read : T_READ varlist
        """
        try:
            node = read_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_write(self, target, option, names, items):
        """
        write : T_WRITE expr_list
        """
        try:
            node = write_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_varlist(self, target, option, names, items):
        """
        varlist : varref
            | varref T_COMMA_DELIM varlist
        """
        try:
            node = varlist_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError

    def on_expr_list(self, target, option, names, items):
        """
        expr_list : a_expr
            | expr_list T_COMMA_DELIM a_expr
        """
        try:
            node = expr_list_Node(target=target, 
                                option=option, 
                                names=names, 
                                items=items)
            return node
        except:
            raise BisonSyntaxError
    
    lexscript = r"""
%{
#include <stdio.h>
#include <string.h>
#include <Python.h>
#define YYSTYPE void *
#include "simple.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) yylval = PyUnicode_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) {(*py_input)(py_parser, buf, &result, max_size);}

%}

DIGIT [0-9] 
ALPHA [a-zA-Z]

%%

"quit-parser"       { returntoken(T_QUIT); }

\/\/.*$           { yylloc.last_line++; yylloc.last_column = 0;}	
[ ]+						  { yylloc.last_column++;}	
[\t]+						  { yylloc.last_column+=2;}	
[\n]+						  {yylloc.last_line++; yylloc.last_column = 0;}	
\".+\"						{ 
                    yylloc.last_column += strlen(yytext);
                                        returntoken(T_LITERAL_STR); 
                }
";"               {
                    yylloc.last_column++;
                    returntoken(T_SEMICOLON);
                }
":="							{ 
                    yylloc.last_column += 2;
                                        returntoken(T_ASSIGN); 
                }
":"               {
                    yylloc.last_column++;
                    returntoken(T_COLON);
                }
"("               {
                    yylloc.last_column++;
                    returntoken(T_LPAREN);
                }
")"               {
                    yylloc.last_column++;
                    returntoken(T_RPAREN);
                }
"\["               {
                    yylloc.last_column++;
                    returntoken(T_LBRACK);
                }
"]"               {
                    yylloc.last_column++;
                    returntoken(T_RBRACK);
                }
", "               {
                    yylloc.last_column+=2;
                    returntoken(T_COMMA_DELIM);
                }
"\+"							  { 
                    yylloc.last_column++;
                                        returntoken(T_ADD); 
                }
"-"							  { 
                    yylloc.last_column++;
                                        returntoken(T_SUB); 
                }
"\*"							  { 
                    yylloc.last_column++;
                                        returntoken(T_MUL); 
                }
"/"							  { 
                    yylloc.last_column++;
                                        returntoken(T_DIV); 
                }
"<"							  { 
                    yylloc.last_column++;
                                        returntoken(T_LT); 
                }
">"							  { 
                    yylloc.last_column++;
                                        returntoken(T_GT); 
                }
">="							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_GEQ); 
                }
"<="							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_LEQ); 
                }
"="							  { 
                    yylloc.last_column+=1;
                                        returntoken(T_EQ); 
                }
"<>"							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_NEQ); 
                }
"and"							{ 
                    yylloc.last_column+=3;
                                        returntoken(T_AND); 
                }
"or"							{ 
                    yylloc.last_column+=2;
                                        returntoken(T_OR); 
                }
"foreach"				  { 
                    yylloc.last_column+=7;
                                        returntoken(T_FOREACH); 
                }
"in"				      { 
                    yylloc.last_column+=2;
                                        returntoken(T_IN); 
                }
"while"				    { 
                    yylloc.last_column+=5;
                                        returntoken(T_WHILE); 
                }
"begin"					  { 
                    yylloc.last_column+=5;
                                        returntoken(T_BEGIN); 
                }
"end"				      { 
                    yylloc.last_column+=3;
                                        returntoken(T_END); 
                }
"if"				      { 
                    yylloc.last_column+=2;
                                        returntoken(T_IF); 
                }
"then"				    { 
                    yylloc.last_column+=4;
                                        returntoken(T_THEN); 
                }
"else"				    { 
                    yylloc.last_column+=4;
                                        returntoken(T_ELSE); 
                }
"write"						{ 
                    yylloc.last_column+=5;
                                        returntoken(T_WRITE); 
                }
"read"						{ 
                    yylloc.last_column+=4;
                                        returntoken(T_READ); 
                }
"int"							{ 
                    yylloc.last_column+=3;
                                        returntoken(T_INTEGER); 
                }
"float"						{ 
                    yylloc.last_column+=5;
                                        returntoken(T_FLOAT); 
                }
"repeat"				  { 
                    yylloc.last_column+=6;
                                        returntoken(T_REPEAT); 
                }
"until"				    { 
                    yylloc.last_column+=5;
                                        returntoken(T_UNTIL); 
                }
"declare"					{ 
                    yylloc.last_column+=7;
                                        returntoken(T_DECLARE); 
                }
{DIGIT}+[.]{DIGIT}+	{ 
                    yylloc.last_column += strlen(yytext);
                    returntoken(T_NUM);
                                    }
{DIGIT}+					{ 
                    yylloc.last_column += strlen(yytext);
                                        returntoken(T_NUM);
                                    }
({ALPHA}|[_])({DIGIT}|{ALPHA}|[_])*     { 
                                        yylloc.last_column += strlen(yytext);
                                                                                    returntoken(T_ID);
                                                                                }
.									{  yylloc.last_column++; returntoken(yytext[0]);}

%%

yywrap() { return(1);}
    """

if __name__ == "__main__":
    p = Parser(verbose=0)
    p.run(debug=1)             # file='inputs/expr1_pass.smp'
    sys.exit()