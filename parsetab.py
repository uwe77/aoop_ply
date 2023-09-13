
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQUALS ID NUMBER SEMICOLON\n    statements : statements statement SEMICOLON\n               | statement SEMICOLON\n    \n    statement : ID EQUALS expression\n    \n    expression : NUMBER\n    '
    
_lr_action_items = {'ID':([0,1,5,7,],[3,3,-2,-1,]),'$end':([1,5,7,],[0,-2,-1,]),'SEMICOLON':([2,4,8,9,],[5,7,-3,-4,]),'EQUALS':([3,],[6,]),'NUMBER':([6,],[9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,],[1,]),'statement':([0,1,],[2,4,]),'expression':([6,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement SEMICOLON','statements',3,'p_statements','test.py',28),
  ('statements -> statement SEMICOLON','statements',2,'p_statements','test.py',29),
  ('statement -> ID EQUALS expression','statement',3,'p_statement_assign','test.py',34),
  ('expression -> NUMBER','expression',1,'p_expression','test.py',40),
]
