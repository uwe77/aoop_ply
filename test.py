import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NAME',
    'AGE',
    'ME',
    'YOU',
    'ACTION',
)

t_YOU = r'[y, Y]ou'
t_ME = r'[m, M]e'

def t_ACTION(t):
    r'action_[a-zA-Z]+'
    t.value = t.value[7:]
    t.type = 'ACTION'
    return t
    
def t_NAME(t):
    r'name_[a-zA-Z]+'
    t.value = t.value[5:]
    t.type = 'NAME'
    return t
    # Define a rule so we can track name

def t_AGE(t):
    r'age_\d+'
    t.value = t.value[4:]
    t.value = int(t.value)
    t.type = 'AGE'
    return t
    # Define a rule so we can track name

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # A string containing ignored characters (spaces and tabs)

t_ignore = ' \t'
# Error handling rule

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_expression_my(p):
    'expression : MY term'
    p[0] = f'my name is {p[2]}'
    
def p_expression_name(p):
    'factor : NAME'
    # p[0] = p[1]
    
def p_expression_age(p):
    'factor : AGE'
    p[0] = p[1]

def p_expression_action(p):
    'expression : expression ACTION term'
    p[0] = f'{p[1]} is {p[2]}ing {p[3]}'

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_error(p):
    print("Systax error in input!")

lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        s = input('who are u? ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
