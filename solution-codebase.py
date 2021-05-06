import io, re, sys
from enum import Enum

class Token(Enum):
    K_FOREACH = 200
    K_PRINT = 201
    K_WHILE = 202
    K_REPEAT = 203
    K_UNTIL = 204
    K_BEGIN = 205
    K_END = 206
    K_DECLARE = 209
    K_IF = 210
    K_THEN = 211
    K_MAIN = 212
    K_INTEGER = 213
    K_FLOAT = 214
    OP_ASSIGN = 220
    OP_ADD = 221
    OP_SUB = 222
    OP_MUL = 223
    OP_DIV = 224
    OP_LT = 225
    OP_GT = 226
    OP_LEQ = 227
    OP_GEQ = 228
    OP_EQ  = 229
    # OP_DIFF is ~=
    OP_DIFF = 230
    # OP_PLUSPLUS is ++
    OP_PLUSPLUS = 231
    # OP_ADDINC is +=
    OP_ADDINC = 232
    CAR_A = 400
    CAR_B = 401
    CAR_C = 402
    CAR_AB = 403
    # literals
    T_ID = 240
    L_INTEGER = 241
    L_FLOAT = 242
    T_EOF = 280

class Lexer(object):
    def __init__(self):
        self.yytext = None
        self.curr = None
        self.l_float = re.compile('\d+\.\d+')
        self.comment = re.compile('\/\/.*$')
        self.eof = re.compile('<<EOF>>')

    def rules(self):
        if self.comment.match(self.curr):
            pass
        elif self.curr.isspace():
            pass
        elif self.curr == "\n":
            pass

        elif self.l_float.match(self.curr):
            return Token.L_FLOAT.value
        elif self.curr == "=":
            return Token.OP_ASSIGN.value
        elif self.curr == "+":
            return Token.OP_ADD.value
        elif self.curr == "-":
            return Token.OP_SUB.value
        elif self.curr == "*":
            return Token.OP_MUL.value
        elif self.curr == "/":
            return Token.OP_DIV.value
        elif self.curr == ";":
            return ";"
        elif self.curr == "<":
            return Token.OP_LT.value
        elif self.curr == ">":
            return Token.OP_GT.value
        elif self.curr == "<=":
            return Token.OP_LEQ.value
        elif self.curr == ">=":
            return Token.OP_GEQ.value
        elif self.curr == "==":
            return Token.OP_EQ.value
        elif self.curr == "~=":
            return Token.OP_DIFF.value
        elif self.curr == "++":
            return Token.OP_PLUSPLUS.value
        elif self.curr == "+=":
            return Token.OP_ADDINC.value
        elif self.curr == "main":
            return Token.K_MAIN.value
        elif self.curr == "integer":
            return Token.K_INTEGER.value
        elif self.curr == "float":
            return Token.K_FLOAT.value
        elif self.curr == "foreach":
            return Token.K_FOREACH.value
        elif self.curr == "begin":
            return Token.K_BEGIN.value
        elif self.curr == "end":
            return Token.K_END.value
        elif self.curr == "repeat":
            return Token.K_REPEAT.value
        elif self.curr == "until":
            return Token.K_UNTIL.value
        elif self.curr == "then":
            return Token.K_THEN.value
        elif self.curr == "while":
            return Token.K_WHILE.value
        elif self.curr == "declare":
            return Token.K_DECLARE.value
        elif self.curr == "if":
            return Token.K_IF.value
        elif self.curr == "print":
            return Token.K_PRINT.value
        elif self.curr.isdigit():
            return Token.L_INTEGER.value
        elif self.curr[0] == "@" and self.curr[1].isalpha():
            return Token.T_ID.value
        elif self.eof.match(self.curr):
            return Token.T_EOF.value
        else:
            return self.curr

    def loadWord(self, yyin):
        self.yytext = yyin.split(" ")
        tok = []
        for i in self.yytext:
            self.curr = i
            tok.append(self.rules())
        return tok

class Parser(self, stream):
    def __init__(self):
        self.stream = stream

    def parse(self):
        # grammar rules defined here

        # output PASS or FAIL based on grammar

def main():
    # create parser object

    # loop input seekage

if __name__ == "__main__":
    main()