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
    r'[a-zA-Z]+:'
    t.value = t.value[:-1]
    t.type = 'TEAM' return t
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
    

def p_expression_add(p):
    'expression : expression ADD term'
    
def p_expression_semicolon(p):
    'expression : expression SEMICOLON term'

def p_factor_name(p):
    'factor : NAME'
    
def p_factor_team(p):
    'factor : TEAM'
    
def p_error(p):
    print("Systax error in input!")
        
if __name__ == '__main__':
    lexer = lex.lex()
    parser = yacc.yacc()
    while True:
        try:
            s = input('input: ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)