
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '4B452841F02C4CFA8154E4C84B279E7A'
    
_lr_action_items = {'PLUS':([2,3,4,5,6,11,12,13,14,15,],[-3,-7,10,-6,10,-8,-5,-4,-2,-1,]),'RPAREN':([2,3,5,6,11,12,13,14,15,],[-3,-7,-6,11,-8,-5,-4,-2,-1,]),'TIMES':([2,3,5,11,12,13,14,15,],[8,-7,-6,-8,-5,-4,8,8,]),'MINUS':([2,3,4,5,6,11,12,13,14,15,],[-3,-7,9,-6,9,-8,-5,-4,-2,-1,]),'NUM':([0,1,7,8,9,10,],[3,3,3,3,3,3,]),'$end':([2,3,4,5,11,12,13,14,15,],[-3,-7,0,-6,-8,-5,-4,-2,-1,]),'DIVIDE':([2,3,5,11,12,13,14,15,],[7,-7,-6,-8,-5,-4,7,7,]),'LPAREN':([0,1,7,8,9,10,],[1,1,1,1,1,1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,1,],[4,6,]),'factor':([0,1,7,8,9,10,],[5,5,12,13,5,5,]),'term':([0,1,9,10,],[2,2,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr PLUS term','expr',3,'p_expr','sec19_str_parser.py',135),
  ('expr -> expr MINUS term','expr',3,'p_expr','sec19_str_parser.py',136),
  ('expr -> term','expr',1,'p_expr_term','sec19_str_parser.py',146),
  ('term -> term TIMES factor','term',3,'p_term','sec19_str_parser.py',153),
  ('term -> term DIVIDE factor','term',3,'p_term','sec19_str_parser.py',154),
  ('term -> factor','term',1,'p_term_factor','sec19_str_parser.py',164),
  ('factor -> NUM','factor',1,'p_factor','sec19_str_parser.py',171),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_group','sec19_str_parser.py',178),
]