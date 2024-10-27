
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEDIVIDE END MINUS MULTIPLY NUMBER PLUS STRINGstatement : expressionexpression : expression PLUS expressionexpression : NUMBERexpression : expression MINUS expressionexpression : expression DIVIDE expressionexpression : expression MULTIPLY expressionexpression : STRINGstatement : END'
    
_lr_action_items = {'END':([0,],[3,]),'NUMBER':([0,6,7,8,9,],[4,4,4,4,4,]),'STRING':([0,6,7,8,9,],[5,5,5,5,5,]),'$end':([1,2,3,4,5,10,11,12,13,],[0,-1,-8,-3,-7,-2,-4,-5,-6,]),'PLUS':([2,4,5,10,11,12,13,],[6,-3,-7,-2,-4,-5,-6,]),'MINUS':([2,4,5,10,11,12,13,],[7,-3,-7,-2,-4,-5,-6,]),'DIVIDE':([2,4,5,10,11,12,13,],[8,-3,-7,8,8,-5,-6,]),'MULTIPLY':([2,4,5,10,11,12,13,],[9,-3,-7,9,9,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,6,7,8,9,],[2,10,11,12,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',15),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','parser.py',19),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',25),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',29),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','parser.py',35),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_multiply','parser.py',41),
  ('expression -> STRING','expression',1,'p_expression_string','parser.py',47),
  ('statement -> END','statement',1,'p_statement_end','parser.py',51),
]