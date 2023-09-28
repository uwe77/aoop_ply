import ply.lex as lex
import ply.yacc as yacc
tokens = ( 'NAME',
           'ADD', 
           'TEAM', 
           'SEMICOLON',
            )

t_ADD = r'\+'

t_SEMICOLON = r';'
def t_NAME(t):
    r'[a-zA-Z]+'
    t.type = 'NAME'
    return t
# Define a rule so we can track name
def t_TEAM(t):
    r'\w+'
    t.value = t.value[:-1]
    t.type = 'TEAM'
    return t
# define a rule so we can track group
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    

def p_term_add(p):
    'term : term ADD factor'
    p[0] = f'{p[1]},\n{p[3]}'

def p_factor_name(p):
    'factor : NAME'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_expr_term(p):
    'expression : TEAM term SEMICOLON'
    p[0] = f'{p[1]}:( {p[2]} )'
    
def p_error(p):
    print("Systax error in input!")
        
if __name__ == '__main__':
    lexer = lex.lex()
    parser = yacc.yacc()
    while True:
        try:
            s = input('input ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(f'result: {result}')