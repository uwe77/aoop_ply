import ply.lex as lex
import ply.yacc as yacc

# Define lexer tokens
tokens = (
    'MISSION'
)

literals = ['=', '+', '-', '*', '(', ')'] #u can use tokens and re to do the same thing

def t_MISSION(t):
    r'\w+'
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal charater {t.value[0]}")
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left', '+', '-'),
    ('left', '*'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}

def p_statement_assign(p):
    'statement : MISSION "=" expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression'''
    if p[2] == '+':
        p[0] = f"im going to do {p[1]}, then {p[3]}"
    elif p[2] == '-':
        p[0] = f"im goint to do {p[1]} without {p[3]}"
    elif p[2] == '*':
        p[0] = f"im going to do {p[1]} and {p[3]} at the same time"

# def p_expression_uminus(p):

def p_expression_group(p):
    "expression : '('  expression ')'"
    p[0] = p[2]

def p_expression_mission(p):
    "expression : MISSION"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = ' '

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        s = input('I want to... ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)