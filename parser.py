#!/usr/bin/env python

import sys
from bison import BisonParser, BisonNode, BisonSyntaxError

bisonFile = 'grammar.y'  # original bison file
lexFile = 'scanner.yy'    # original flex file


class Parser(BisonParser):

    defaultNodeClass = BisonNode

    bisonEngineLibName = 'simple'
    tokens = ['T_ID', 'T_NUM', 'T_ADD', 'T_SUB', 'T_MUL', 'T_DIV', 'T_LT', 'T_GT', 'T_LEQ', 'T_GEQ', 'T_EQ', 'T_NEQ', 'T_AND', 'T_OR', 'T_READ', 'T_WRITE', 'T_ASSIGN', 'T_BEGIN', 'T_END', 'T_FOREACH', 'T_IN', 'T_REPEAT', 'T_UNTIL', 'T_WHILE', 'T_IF', 'T_THEN', 'T_ELSE', 'T_DECLARE', 'T_INTEGER', 'T_FLOAT', 'T_LITERAL_STR', 'T_SEMICOLON', 'T_COLON', 'T_LPAREN', 'T_RPAREN', 'T_LBRACK', 'T_RBRACK', 'T_COMMA_DELIM']

    precedences = (
        )

    start = 'program'

    def on_program(self, target, option, names, items):
        """
        program: stmt_list T_SEMICOLON
        """
        return

    def on_stmt_list(self, target, option, names, items):
        """
        stmt_list: stmt_list T_SEMICOLON stmt
            | stmt
        """

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

    def on_block(self, target, option, names, items):
        """
        block : T_BEGIN stmt_list T_END
        """

    def on_foreach(self, target, option, names, items):
        """
        foreach : T_FOREACH T_ID
            T_IN
            T_LPAREN a_fact T_COLON a_fact T_RPAREN 
            stmt
        """

    def on_while(self, target, option, names, items):
        """
        while : T_WHILE l_expr
            T_BEGIN
            stmt_list
            T_END
        """

    def on_repeat(self, target, option, names, items):
        """
        repeat : T_REPEAT stmt_list T_UNTIL l_expr
        """

    def on_if_stmt(self, target, option, names, items):
        """
        if_stmt : T_IF l_expr
            T_THEN stmt_list
            T_ELSE else_stmt
        """

    def on_else_stmt(self, target, option, names, items):
        """
        else_stmt : 
            | T_ELSE stmt
        """

    def on_assignment(self, target, option, names, items):
        """
        assignment : varref T_ASSIGN l_expr
        """

    def on_a_expr(self, target, option, names, items):
        """
        a_expr : a_expr T_ADD a_term 
            | a_expr T_SUB a_term
            | a_term
        """

    def on_a_term(self, target, option, names, items):
        """
        a_term : a_term T_MUL a_fact
            | a_term T_DIV a_fact
            | a_fact
        """

    def on_a_fact(self, target, option, names, items):
        """
        a_fact : varref
            | T_NUM
            | T_LITERAL_STR
            | T_SUB a_fact
            | T_LPAREN a_expr T_RPAREN
        """

    def on_varref(self, target, option, names, items):
        """
        varref : T_ID 
            | varref T_LBRACK a_expr T_RBRACK
        """

    def on_l_expr(self, target, option, names, items):
        """
        l_expr : l_expr T_AND l_term
            | l_term
        """

    def on_l_term(self, target, option, names, items):
        """
        l_term : l_term T_OR l_fact
            | l_fact
        """

    def on_l_fact(self, target, option, names, items):
        """
        l_fact : l_fact oprel a_expr
            | a_expr
            | T_LPAREN l_expr T_RPAREN
        """

    def on_oprel(self, target, option, names, items):
        """
        oprel : T_LT
            | T_GT
            | T_LEQ
            | T_GEQ
            | T_EQ
            | T_NEQ
        """

    def on_read(self, target, option, names, items):
        """
        read : T_READ varlist
        """

    def on_write(self, target, option, names, items):
        """
        write: T_WRITE expr_list
        """

    def on_varlist(self, target, option, names, items):
        """
        varlist : varref
            | varref T_COMMA_DELIM varlist
        """

    def on_expr_list(self, target, option, names, items):
        """
        expr_list : a_expr
            | expr_list T_COMMA_DELIM a_expr
        """