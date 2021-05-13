
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND ASSIGN BEGIN COLON COMMA_DELIM DIV ELSE END EQ FOREACH GEQ GT ID IF IN LBRACK LEQ LITERAL_STR LPAREN LT MUL NEQ NUM OR RBRACK READ REPEAT RPAREN SEMICOLON SUB THEN UNTIL WHILE WRITEprogram : stmt_list SEMICOLONstmt_list : stmt_list SEMICOLON stmt \n        | stmtstmt : assignment \n        | read \n        | write \n        | while \n        | repeat \n        | block \n        | foreach \n        | if_stmtblock : BEGIN stmt_list ENDforeach : FOREACH ID IN LPAREN a_fact COLON a_fact RPAREN stmtwhile : WHILE l_expr blockrepeat : REPEAT stmt_list UNTIL l_exprif_stmt : IF l_expr THEN stmt_list ELSE else_stmtelse_stmt : \n        | ELSE stmtassignment : varref ASSIGN l_expra_expr : a_expr ADD a_term\n        | a_expr SUB a_term\n        | a_terma_term : a_term MUL a_fact\n        | a_term DIV a_fact\n        | a_facta_fact : varref \n        | NUM \n        | LITERAL_STR \n        | SUB a_fact \n        | LPAREN a_expr RPARENvarref : ID \n        | varref LBRACK a_expr RBRACKl_expr : l_expr AND l_term\n        | l_terml_term : l_term OR l_fact\n        | l_factl_fact : l_fact oprel a_expr\n        | a_expr\n        | LPAREN l_expr RPARENoprel : LT\n        | GT\n        | LEQ\n        | GEQ\n        | EQ\n        | NEQread : READ varlistwrite : WRITE expr_listvarlist : varref\n        | varref COMMA_DELIM varlistexpr_list : a_expr\n        | expr_list COMMA_DELIM a_expr'
    
_lr_action_items = {'READ':([0,16,17,21,68,71,90,94,],[13,13,13,13,13,13,13,13,]),'WRITE':([0,16,17,21,68,71,90,94,],[14,14,14,14,14,14,14,14,]),'WHILE':([0,16,17,21,68,71,90,94,],[15,15,15,15,15,15,15,15,]),'REPEAT':([0,16,17,21,68,71,90,94,],[16,16,16,16,16,16,16,16,]),'BEGIN':([0,16,17,19,21,28,30,31,32,33,35,36,37,38,53,68,71,72,75,76,77,78,79,80,81,82,83,90,94,],[17,17,17,-31,17,-22,-25,-26,-27,-28,17,-34,-36,-38,-29,17,17,-32,-20,-21,-23,-24,-30,-33,-35,-37,-39,17,17,]),'FOREACH':([0,16,17,21,68,71,90,94,],[18,18,18,18,18,18,18,18,]),'IF':([0,16,17,21,68,71,90,94,],[20,20,20,20,20,20,20,20,]),'ID':([0,13,14,15,16,17,18,20,21,22,23,29,34,39,47,48,49,50,51,52,56,57,58,59,60,61,62,63,64,67,68,71,85,89,90,94,],[19,19,19,19,19,19,42,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-40,-41,-42,-43,-44,-45,19,19,19,19,19,19,19,]),'$end':([1,21,],[0,-1,]),'SEMICOLON':([2,3,4,5,6,7,8,9,10,11,19,24,25,26,27,28,30,31,32,33,36,37,38,40,41,44,45,53,55,69,72,73,74,75,76,77,78,79,80,81,82,83,84,86,88,91,93,95,],[21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-31,-46,-48,-47,-50,-22,-25,-26,-27,-28,-34,-36,-38,68,68,-2,-19,-29,-14,-12,-32,-49,-51,-20,-21,-23,-24,-30,-33,-35,-37,-39,-15,68,-17,-16,-18,-13,]),'UNTIL':([3,4,5,6,7,8,9,10,11,19,24,25,26,27,28,30,31,32,33,36,37,38,40,44,45,53,55,69,72,73,74,75,76,77,78,79,80,81,82,83,84,88,91,93,95,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-31,-46,-48,-47,-50,-22,-25,-26,-27,-28,-34,-36,-38,67,-2,-19,-29,-14,-12,-32,-49,-51,-20,-21,-23,-24,-30,-33,-35,-37,-39,-15,-17,-16,-18,-13,]),'END':([3,4,5,6,7,8,9,10,11,19,24,25,26,27,28,30,31,32,33,36,37,38,41,44,45,53,55,69,72,73,74,75,76,77,78,79,80,81,82,83,84,88,91,93,95,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-31,-46,-48,-47,-50,-22,-25,-26,-27,-28,-34,-36,-38,69,-2,-19,-29,-14,-12,-32,-49,-51,-20,-21,-23,-24,-30,-33,-35,-37,-39,-15,-17,-16,-18,-13,]),'ELSE':([3,4,5,6,7,8,9,10,11,19,24,25,26,27,28,30,31,32,33,36,37,38,44,45,53,55,69,72,73,74,75,76,77,78,79,80,81,82,83,84,86,88,91,93,95,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-31,-46,-48,-47,-50,-22,-25,-26,-27,-28,-34,-36,-38,-2,-19,-29,-14,-12,-32,-49,-51,-20,-21,-23,-24,-30,-33,-35,-37,-39,-15,88,90,-16,-18,-13,]),'ASSIGN':([12,19,72,],[22,-31,-32,]),'LBRACK':([12,19,25,31,72,],[23,-31,23,23,-32,]),'NUM':([14,15,20,22,23,29,34,39,48,49,50,51,52,56,57,58,59,60,61,62,63,64,67,85,89,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-40,-41,-42,-43,-44,-45,32,32,32,]),'LITERAL_STR':([14,15,20,22,23,29,34,39,48,49,50,51,52,56,57,58,59,60,61,62,63,64,67,85,89,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-40,-41,-42,-43,-44,-45,33,33,33,]),'SUB':([14,15,19,20,22,23,27,28,29,30,31,32,33,34,38,39,46,48,49,50,51,52,53,54,56,57,58,59,60,61,62,63,64,66,67,72,74,75,76,77,78,79,82,85,89,],[29,29,-31,29,29,29,50,-22,29,-25,-26,-27,-28,29,50,29,50,29,29,29,29,29,-29,50,29,29,29,-40,-41,-42,-43,-44,-45,50,29,-32,50,-20,-21,-23,-24,-30,50,29,29,]),'LPAREN':([14,15,20,22,23,29,34,39,48,49,50,51,52,56,57,58,59,60,61,62,63,64,67,70,85,89,],[34,39,39,39,34,34,34,39,34,34,34,34,34,39,39,34,-40,-41,-42,-43,-44,-45,39,85,34,34,]),'COMMA_DELIM':([19,25,26,27,28,30,31,32,33,53,72,74,75,76,77,78,79,],[-31,47,48,-50,-22,-25,-26,-27,-28,-29,-32,-51,-20,-21,-23,-24,-30,]),'MUL':([19,28,30,31,32,33,53,72,75,76,77,78,79,],[-31,51,-25,-26,-27,-28,-29,-32,51,51,-23,-24,-30,]),'DIV':([19,28,30,31,32,33,53,72,75,76,77,78,79,],[-31,52,-25,-26,-27,-28,-29,-32,52,52,-23,-24,-30,]),'ADD':([19,27,28,30,31,32,33,38,46,53,54,66,72,74,75,76,77,78,79,82,],[-31,49,-22,-25,-26,-27,-28,49,49,-29,49,49,-32,49,-20,-21,-23,-24,-30,49,]),'LT':([19,28,30,31,32,33,37,38,53,66,72,75,76,77,78,79,81,82,83,],[-31,-22,-25,-26,-27,-28,59,-38,-29,-38,-32,-20,-21,-23,-24,-30,59,-37,-39,]),'GT':([19,28,30,31,32,33,37,38,53,66,72,75,76,77,78,79,81,82,83,],[-31,-22,-25,-26,-27,-28,60,-38,-29,-38,-32,-20,-21,-23,-24,-30,60,-37,-39,]),'LEQ':([19,28,30,31,32,33,37,38,53,66,72,75,76,77,78,79,81,82,83,],[-31,-22,-25,-26,-27,-28,61,-38,-29,-38,-32,-20,-21,-23,-24,-30,61,-37,-39,]),'GEQ':([19,28,30,31,32,33,37,38,53,66,72,75,76,77,78,79,81,82,83,],[-31,-22,-25,-26,-27,-28,62,-38,-29,-38,-32,-20,-21,-23,-24,-30,62,-37,-39,]),'EQ':([19,28,30,31,32,33,37,38,53,66,72,75,76,77,78,79,81,82,83,],[-31,-22,-25,-26,-27,-28,63,-38,-29,-38,-32,-20,-21,-23,-24,-30,63,-37,-39,]),'NEQ':([19,28,30,31,32,33,37,38,53,66,72,75,76,77,78,79,81,82,83,],[-31,-22,-25,-26,-27,-28,64,-38,-29,-38,-32,-20,-21,-23,-24,-30,64,-37,-39,]),'OR':([19,28,30,31,32,33,36,37,38,53,66,72,75,76,77,78,79,80,81,82,83,],[-31,-22,-25,-26,-27,-28,57,-36,-38,-29,-38,-32,-20,-21,-23,-24,-30,57,-35,-37,-39,]),'AND':([19,28,30,31,32,33,35,36,37,38,43,45,53,65,66,72,75,76,77,78,79,80,81,82,83,84,],[-31,-22,-25,-26,-27,-28,56,-34,-36,-38,56,56,-29,56,-38,-32,-20,-21,-23,-24,-30,-33,-35,-37,-39,56,]),'THEN':([19,28,30,31,32,33,36,37,38,43,53,72,75,76,77,78,79,80,81,82,83,],[-31,-22,-25,-26,-27,-28,-34,-36,-38,71,-29,-32,-20,-21,-23,-24,-30,-33,-35,-37,-39,]),'RBRACK':([19,28,30,31,32,33,46,53,72,75,76,77,78,79,],[-31,-22,-25,-26,-27,-28,72,-29,-32,-20,-21,-23,-24,-30,]),'RPAREN':([19,28,30,31,32,33,36,37,38,53,54,65,66,72,75,76,77,78,79,80,81,82,83,92,],[-31,-22,-25,-26,-27,-28,-34,-36,-38,-29,79,83,79,-32,-20,-21,-23,-24,-30,-33,-35,-37,-39,94,]),'COLON':([19,31,32,33,53,72,79,87,],[-31,-26,-27,-28,-29,-32,-30,89,]),'IN':([42,],[70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,16,17,71,],[2,40,41,86,]),'stmt':([0,16,17,21,68,71,90,94,],[3,3,3,44,44,3,93,95,]),'assignment':([0,16,17,21,68,71,90,94,],[4,4,4,4,4,4,4,4,]),'read':([0,16,17,21,68,71,90,94,],[5,5,5,5,5,5,5,5,]),'write':([0,16,17,21,68,71,90,94,],[6,6,6,6,6,6,6,6,]),'while':([0,16,17,21,68,71,90,94,],[7,7,7,7,7,7,7,7,]),'repeat':([0,16,17,21,68,71,90,94,],[8,8,8,8,8,8,8,8,]),'block':([0,16,17,21,35,68,71,90,94,],[9,9,9,9,55,9,9,9,9,]),'foreach':([0,16,17,21,68,71,90,94,],[10,10,10,10,10,10,10,10,]),'if_stmt':([0,16,17,21,68,71,90,94,],[11,11,11,11,11,11,11,11,]),'varref':([0,13,14,15,16,17,20,21,22,23,29,34,39,47,48,49,50,51,52,56,57,58,67,68,71,85,89,90,94,],[12,25,31,31,12,12,31,12,31,31,31,31,31,25,31,31,31,31,31,31,31,31,31,12,12,31,31,12,12,]),'varlist':([13,47,],[24,73,]),'expr_list':([14,],[26,]),'a_expr':([14,15,20,22,23,34,39,48,56,57,58,67,],[27,38,38,38,46,54,66,74,38,38,82,38,]),'a_term':([14,15,20,22,23,34,39,48,49,50,56,57,58,67,],[28,28,28,28,28,28,28,28,75,76,28,28,28,28,]),'a_fact':([14,15,20,22,23,29,34,39,48,49,50,51,52,56,57,58,67,85,89,],[30,30,30,30,30,53,30,30,30,30,30,77,78,30,30,30,30,87,92,]),'l_expr':([15,20,22,39,67,],[35,43,45,65,84,]),'l_term':([15,20,22,39,56,67,],[36,36,36,36,80,36,]),'l_fact':([15,20,22,39,56,57,67,],[37,37,37,37,37,81,37,]),'oprel':([37,81,],[58,58,]),'else_stmt':([88,],[91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list SEMICOLON','program',2,'p_program','ply-parser.py',72),
  ('stmt_list -> stmt_list SEMICOLON stmt','stmt_list',3,'p_stmt_list','ply-parser.py',75),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','ply-parser.py',76),
  ('stmt -> assignment','stmt',1,'p_stmt','ply-parser.py',79),
  ('stmt -> read','stmt',1,'p_stmt','ply-parser.py',80),
  ('stmt -> write','stmt',1,'p_stmt','ply-parser.py',81),
  ('stmt -> while','stmt',1,'p_stmt','ply-parser.py',82),
  ('stmt -> repeat','stmt',1,'p_stmt','ply-parser.py',83),
  ('stmt -> block','stmt',1,'p_stmt','ply-parser.py',84),
  ('stmt -> foreach','stmt',1,'p_stmt','ply-parser.py',85),
  ('stmt -> if_stmt','stmt',1,'p_stmt','ply-parser.py',86),
  ('block -> BEGIN stmt_list END','block',3,'p_block','ply-parser.py',89),
  ('foreach -> FOREACH ID IN LPAREN a_fact COLON a_fact RPAREN stmt','foreach',9,'p_foreach','ply-parser.py',92),
  ('while -> WHILE l_expr block','while',3,'p_while','ply-parser.py',95),
  ('repeat -> REPEAT stmt_list UNTIL l_expr','repeat',4,'p_repeat','ply-parser.py',98),
  ('if_stmt -> IF l_expr THEN stmt_list ELSE else_stmt','if_stmt',6,'p_if_stmt','ply-parser.py',101),
  ('else_stmt -> <empty>','else_stmt',0,'p_else_stmt','ply-parser.py',104),
  ('else_stmt -> ELSE stmt','else_stmt',2,'p_else_stmt','ply-parser.py',105),
  ('assignment -> varref ASSIGN l_expr','assignment',3,'p_assignment','ply-parser.py',108),
  ('a_expr -> a_expr ADD a_term','a_expr',3,'p_a_expr','ply-parser.py',111),
  ('a_expr -> a_expr SUB a_term','a_expr',3,'p_a_expr','ply-parser.py',112),
  ('a_expr -> a_term','a_expr',1,'p_a_expr','ply-parser.py',113),
  ('a_term -> a_term MUL a_fact','a_term',3,'p_a_term','ply-parser.py',116),
  ('a_term -> a_term DIV a_fact','a_term',3,'p_a_term','ply-parser.py',117),
  ('a_term -> a_fact','a_term',1,'p_a_term','ply-parser.py',118),
  ('a_fact -> varref','a_fact',1,'p_a_fact','ply-parser.py',121),
  ('a_fact -> NUM','a_fact',1,'p_a_fact','ply-parser.py',122),
  ('a_fact -> LITERAL_STR','a_fact',1,'p_a_fact','ply-parser.py',123),
  ('a_fact -> SUB a_fact','a_fact',2,'p_a_fact','ply-parser.py',124),
  ('a_fact -> LPAREN a_expr RPAREN','a_fact',3,'p_a_fact','ply-parser.py',125),
  ('varref -> ID','varref',1,'p_varref','ply-parser.py',128),
  ('varref -> varref LBRACK a_expr RBRACK','varref',4,'p_varref','ply-parser.py',129),
  ('l_expr -> l_expr AND l_term','l_expr',3,'p_l_expr','ply-parser.py',132),
  ('l_expr -> l_term','l_expr',1,'p_l_expr','ply-parser.py',133),
  ('l_term -> l_term OR l_fact','l_term',3,'p_l_term','ply-parser.py',136),
  ('l_term -> l_fact','l_term',1,'p_l_term','ply-parser.py',137),
  ('l_fact -> l_fact oprel a_expr','l_fact',3,'p_l_fact','ply-parser.py',140),
  ('l_fact -> a_expr','l_fact',1,'p_l_fact','ply-parser.py',141),
  ('l_fact -> LPAREN l_expr RPAREN','l_fact',3,'p_l_fact','ply-parser.py',142),
  ('oprel -> LT','oprel',1,'p_oprel','ply-parser.py',145),
  ('oprel -> GT','oprel',1,'p_oprel','ply-parser.py',146),
  ('oprel -> LEQ','oprel',1,'p_oprel','ply-parser.py',147),
  ('oprel -> GEQ','oprel',1,'p_oprel','ply-parser.py',148),
  ('oprel -> EQ','oprel',1,'p_oprel','ply-parser.py',149),
  ('oprel -> NEQ','oprel',1,'p_oprel','ply-parser.py',150),
  ('read -> READ varlist','read',2,'p_read','ply-parser.py',153),
  ('write -> WRITE expr_list','write',2,'p_write','ply-parser.py',156),
  ('varlist -> varref','varlist',1,'p_varlist','ply-parser.py',159),
  ('varlist -> varref COMMA_DELIM varlist','varlist',3,'p_varlist','ply-parser.py',160),
  ('expr_list -> a_expr','expr_list',1,'p_expr_list','ply-parser.py',163),
  ('expr_list -> expr_list COMMA_DELIM a_expr','expr_list',3,'p_expr_list','ply-parser.py',164),
]
