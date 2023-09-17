
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AGE MY NAME YOURexpression : MY termfactor : NAMEfactor : AGEterm : factorexpression : term'
    
_lr_action_items = {'MY':([0,],[2,]),'NAME':([0,2,],[5,5,]),'AGE':([0,2,],[6,6,]),'$end':([1,3,4,5,6,7,],[0,-5,-4,-2,-3,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'term':([0,2,],[3,7,]),'factor':([0,2,],[4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> MY term','expression',2,'p_expression_my','test.py',43),
  ('factor -> NAME','factor',1,'p_expression_name','test.py',46),
  ('factor -> AGE','factor',1,'p_expression_age','test.py',50),
  ('term -> factor','term',1,'p_term_factor','test.py',54),
  ('expression -> term','expression',1,'p_expression_term','test.py',58),
]
