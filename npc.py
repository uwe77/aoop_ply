import ply.lex as lex
import ply.yacc as yacc

# Define lexer tokens
tokens = (
    "MISSION",
    ';',
)

t_SEMICOLON = r';'

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

def p_statements(p):
    '''
    statements : statements statement SEMICOLON
               | statement SEMICOLON
    '''

def p_statement_assign(p):
    '''
    statement : MISSION
    '''
    print(f"I want to do {p[1]} = {p[3]}")

# def p_expression(p):
#     '''
#     expression : NUMBER
#     '''

parser = yacc.yacc()

while True:
    try:
        s = input('I want to... ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)