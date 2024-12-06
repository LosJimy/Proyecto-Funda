
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTleftPLUSMINUSleftMULTIPLYDIVIDEMODULOrightUMINUSnonassocEQUALSLTGTLEGEAND ASSIGN COMMA DIVIDE ELIF ELSE EQUALS FALSE FLOAT FOR GE GT ID IF IN LE LPAREN LT MINUS MODULO MULTIPLY NOT NUMBER OR PLUS PRINT RANGE RPAREN STRING TRUE WHILEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : assignment\n                 | if_statement\n                 | for_statement\n                 | while_statement\n                 | print_statementassignment : ID ASSIGN expressionif_statement : IF condition statement elif_list_opt ELSE statement\n                    | IF condition statement elif_list_optelif_list_opt : elif_list\n                     | emptyelif_list : elif_list ELIF condition statement\n                 | ELIF condition statementfor_statement : FOR ID IN range statementwhile_statement : WHILE condition statementrange : RANGE LPAREN expression COMMA expression RPARENprint_statement : PRINT LPAREN expression RPARENcondition : expression EQUALS expression\n                 | expression LT expression\n                 | expression GT expression\n                 | expression LE expression\n                 | expression GEexpression : MINUS expression %prec UMINUSexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression MULTIPLY expression\n                  | expression DIVIDE expression\n                  | expression MODULO expression\n                  | expression OR expression\n                  | expression AND expressionexpression : NOT expressionexpression : LPAREN expression RPARENexpression : IDexpression : TRUEexpression : FALSEexpression : NUMBER\n                  | FLOATexpression : STRINGempty :'
    
_lr_action_items = {'ID':([0,2,3,4,5,6,7,8,10,11,12,14,15,16,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,78,79,81,],[9,9,-3,-4,-5,-6,-7,-8,21,27,21,-2,21,9,21,21,21,-35,-36,-37,-38,-39,-40,9,21,-9,-41,21,21,21,21,-24,21,21,21,21,21,21,21,-25,-33,-17,-11,-12,-13,21,-20,-21,-22,-23,-26,-27,-28,-29,-30,-31,-32,-34,9,-19,9,21,9,-16,21,-10,9,-15,-14,21,-18,]),'IF':([0,2,3,4,5,6,7,8,14,16,21,22,23,24,25,26,28,30,31,36,44,45,48,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,71,72,74,75,76,78,81,],[10,10,-3,-4,-5,-6,-7,-8,-2,10,-35,-36,-37,-38,-39,-40,10,-9,-41,-24,-25,-33,-17,-11,-12,-13,-20,-21,-22,-23,-26,-27,-28,-29,-30,-31,-32,-34,10,-19,10,10,-16,-10,10,-15,-14,-18,]),'FOR':([0,2,3,4,5,6,7,8,14,16,21,22,23,24,25,26,28,30,31,36,44,45,48,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,71,72,74,75,76,78,81,],[11,11,-3,-4,-5,-6,-7,-8,-2,11,-35,-36,-37,-38,-39,-40,11,-9,-41,-24,-25,-33,-17,-11,-12,-13,-20,-21,-22,-23,-26,-27,-28,-29,-30,-31,-32,-34,11,-19,11,11,-16,-10,11,-15,-14,-18,]),'WHILE':([0,2,3,4,5,6,7,8,14,16,21,22,23,24,25,26,28,30,31,36,44,45,48,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,71,72,74,75,76,78,81,],[12,12,-3,-4,-5,-6,-7,-8,-2,12,-35,-36,-37,-38,-39,-40,12,-9,-41,-24,-25,-33,-17,-11,-12,-13,-20,-21,-22,-23,-26,-27,-28,-29,-30,-31,-32,-34,12,-19,12,12,-16,-10,12,-15,-14,-18,]),'PRINT':([0,2,3,4,5,6,7,8,14,16,21,22,23,24,25,26,28,30,31,36,44,45,48,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,71,72,74,75,76,78,81,],[13,13,-3,-4,-5,-6,-7,-8,-2,13,-35,-36,-37,-38,-39,-40,13,-9,-41,-24,-25,-33,-17,-11,-12,-13,-20,-21,-22,-23,-26,-27,-28,-29,-30,-31,-32,-34,13,-19,13,13,-16,-10,13,-15,-14,-18,]),'$end':([1,2,3,4,5,6,7,8,14,21,22,23,24,25,26,30,31,44,45,48,50,51,52,58,59,60,61,62,63,64,65,68,72,74,76,78,],[0,-1,-3,-4,-5,-6,-7,-8,-2,-35,-36,-37,-38,-39,-40,-9,-41,-25,-33,-17,-11,-12,-13,-26,-27,-28,-29,-30,-31,-32,-34,-19,-16,-10,-15,-14,]),'ELIF':([4,5,6,7,8,21,22,23,24,25,26,30,31,44,45,48,50,51,52,58,59,60,61,62,63,64,65,68,72,74,76,78,],[-4,-5,-6,-7,-8,-35,-36,-37,-38,-39,-40,-9,53,-25,-33,-17,-11,70,-13,-26,-27,-28,-29,-30,-31,-32,-34,-19,-16,-10,-15,-14,]),'ELSE':([4,5,6,7,8,21,22,23,24,25,26,30,31,44,45,48,50,51,52,58,59,60,61,62,63,64,65,68,72,74,76,78,],[-4,-5,-6,-7,-8,-35,-36,-37,-38,-39,-40,-9,-41,-25,-33,-17,69,-12,-13,-26,-27,-28,-29,-30,-31,-32,-34,-19,-16,-10,-15,-14,]),'ASSIGN':([9,],[15,]),'MINUS':([10,12,15,17,18,19,20,21,22,23,24,25,26,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,49,53,54,55,56,57,58,59,60,61,62,63,64,65,70,73,77,79,80,],[18,18,18,38,18,18,18,-35,-36,-37,-38,-39,-40,18,38,18,18,18,18,18,18,18,18,18,18,18,-25,38,38,38,18,38,38,38,38,-26,-27,-28,-29,-30,38,38,-34,18,18,38,18,38,]),'NOT':([10,12,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,70,73,79,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'LPAREN':([10,12,13,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,67,70,73,79,],[20,20,29,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,73,20,20,20,]),'TRUE':([10,12,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,70,73,79,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'FALSE':([10,12,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,70,73,79,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'NUMBER':([10,12,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,70,73,79,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'FLOAT':([10,12,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,70,73,79,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'STRING':([10,12,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,70,73,79,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'EQUALS':([17,21,22,23,24,25,26,44,45,58,59,60,61,62,63,64,65,],[32,-35,-36,-37,-38,-39,-40,-25,-33,-26,-27,-28,-29,-30,-31,-32,-34,]),'LT':([17,21,22,23,24,25,26,44,45,58,59,60,61,62,63,64,65,],[33,-35,-36,-37,-38,-39,-40,-25,-33,-26,-27,-28,-29,-30,-31,-32,-34,]),'GT':([17,21,22,23,24,25,26,44,45,58,59,60,61,62,63,64,65,],[34,-35,-36,-37,-38,-39,-40,-25,-33,-26,-27,-28,-29,-30,-31,-32,-34,]),'LE':([17,21,22,23,24,25,26,44,45,58,59,60,61,62,63,64,65,],[35,-35,-36,-37,-38,-39,-40,-25,-33,-26,-27,-28,-29,-30,-31,-32,-34,]),'GE':([17,21,22,23,24,25,26,44,45,58,59,60,61,62,63,64,65,],[36,-35,-36,-37,-38,-39,-40,-25,-33,-26,-27,-28,-29,-30,-31,-32,-34,]),'PLUS':([17,21,22,23,24,25,26,30,44,45,46,49,54,55,56,57,58,59,60,61,62,63,64,65,77,80,],[37,-35,-36,-37,-38,-39,-40,37,-25,37,37,37,37,37,37,37,-26,-27,-28,-29,-30,37,37,-34,37,37,]),'MULTIPLY':([17,21,22,23,24,25,26,30,44,45,46,49,54,55,56,57,58,59,60,61,62,63,64,65,77,80,],[39,-35,-36,-37,-38,-39,-40,39,-25,39,39,39,39,39,39,39,39,39,-28,-29,-30,39,39,-34,39,39,]),'DIVIDE':([17,21,22,23,24,25,26,30,44,45,46,49,54,55,56,57,58,59,60,61,62,63,64,65,77,80,],[40,-35,-36,-37,-38,-39,-40,40,-25,40,40,40,40,40,40,40,40,40,-28,-29,-30,40,40,-34,40,40,]),'MODULO':([17,21,22,23,24,25,26,30,44,45,46,49,54,55,56,57,58,59,60,61,62,63,64,65,77,80,],[41,-35,-36,-37,-38,-39,-40,41,-25,41,41,41,41,41,41,41,41,41,-28,-29,-30,41,41,-34,41,41,]),'OR':([17,21,22,23,24,25,26,30,44,45,46,49,54,55,56,57,58,59,60,61,62,63,64,65,77,80,],[42,-35,-36,-37,-38,-39,-40,42,-25,-33,42,42,42,42,42,42,-26,-27,-28,-29,-30,-31,-32,-34,42,42,]),'AND':([17,21,22,23,24,25,26,30,44,45,46,49,54,55,56,57,58,59,60,61,62,63,64,65,77,80,],[43,-35,-36,-37,-38,-39,-40,43,-25,-33,43,43,43,43,43,43,-26,-27,-28,-29,-30,43,-32,-34,43,43,]),'RPAREN':([21,22,23,24,25,26,44,45,46,49,58,59,60,61,62,63,64,65,80,],[-35,-36,-37,-38,-39,-40,-25,-33,65,68,-26,-27,-28,-29,-30,-31,-32,-34,81,]),'COMMA':([21,22,23,24,25,26,44,45,58,59,60,61,62,63,64,65,77,],[-35,-36,-37,-38,-39,-40,-25,-33,-26,-27,-28,-29,-30,-31,-32,-34,79,]),'IN':([27,],[47,]),'RANGE':([47,],[67,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,16,28,66,69,71,75,],[3,14,31,48,72,74,76,78,]),'assignment':([0,2,16,28,66,69,71,75,],[4,4,4,4,4,4,4,4,]),'if_statement':([0,2,16,28,66,69,71,75,],[5,5,5,5,5,5,5,5,]),'for_statement':([0,2,16,28,66,69,71,75,],[6,6,6,6,6,6,6,6,]),'while_statement':([0,2,16,28,66,69,71,75,],[7,7,7,7,7,7,7,7,]),'print_statement':([0,2,16,28,66,69,71,75,],[8,8,8,8,8,8,8,8,]),'condition':([10,12,53,70,],[16,28,71,75,]),'expression':([10,12,15,18,19,20,29,32,33,34,35,37,38,39,40,41,42,43,53,70,73,79,],[17,17,30,44,45,46,49,54,55,56,57,58,59,60,61,62,63,64,17,17,77,80,]),'elif_list_opt':([31,],[50,]),'elif_list':([31,],[51,]),'empty':([31,],[52,]),'range':([47,],[66,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',17),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',22),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',23),
  ('statement -> assignment','statement',1,'p_statement','parser.py',30),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',31),
  ('statement -> for_statement','statement',1,'p_statement','parser.py',32),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',33),
  ('statement -> print_statement','statement',1,'p_statement','parser.py',34),
  ('assignment -> ID ASSIGN expression','assignment',3,'p_assignment','parser.py',38),
  ('if_statement -> IF condition statement elif_list_opt ELSE statement','if_statement',6,'p_if_statement','parser.py',43),
  ('if_statement -> IF condition statement elif_list_opt','if_statement',4,'p_if_statement','parser.py',44),
  ('elif_list_opt -> elif_list','elif_list_opt',1,'p_elif_list_opt','parser.py',57),
  ('elif_list_opt -> empty','elif_list_opt',1,'p_elif_list_opt','parser.py',58),
  ('elif_list -> elif_list ELIF condition statement','elif_list',4,'p_elif_list','parser.py',62),
  ('elif_list -> ELIF condition statement','elif_list',3,'p_elif_list','parser.py',63),
  ('for_statement -> FOR ID IN range statement','for_statement',5,'p_for_statement','parser.py',70),
  ('while_statement -> WHILE condition statement','while_statement',3,'p_while_statement','parser.py',74),
  ('range -> RANGE LPAREN expression COMMA expression RPAREN','range',6,'p_range','parser.py',78),
  ('print_statement -> PRINT LPAREN expression RPAREN','print_statement',4,'p_print_statement','parser.py',82),
  ('condition -> expression EQUALS expression','condition',3,'p_condition','parser.py',151),
  ('condition -> expression LT expression','condition',3,'p_condition','parser.py',152),
  ('condition -> expression GT expression','condition',3,'p_condition','parser.py',153),
  ('condition -> expression LE expression','condition',3,'p_condition','parser.py',154),
  ('condition -> expression GE','condition',2,'p_condition','parser.py',155),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',170),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',174),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',175),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binop','parser.py',176),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',177),
  ('expression -> expression MODULO expression','expression',3,'p_expression_binop','parser.py',178),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','parser.py',179),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','parser.py',180),
  ('expression -> NOT expression','expression',2,'p_expression_not','parser.py',184),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',188),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',192),
  ('expression -> TRUE','expression',1,'p_expression_true','parser.py',196),
  ('expression -> FALSE','expression',1,'p_expression_false','parser.py',200),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',204),
  ('expression -> FLOAT','expression',1,'p_expression_number','parser.py',205),
  ('expression -> STRING','expression',1,'p_expression_string','parser.py',209),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',213),
]
