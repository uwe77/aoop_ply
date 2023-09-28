import ply.lex as lex
import ply.yacc as yacc
import pytest
# Define Token types
tokens = ( 'NAME',
           'ADD', 
           'TEAM', 
           'SEMICOLON',
            )
# Define ADD's token, or (t_ADD = r'\+')
def t_ADD(t):
    r'\+'
    t.type = 'ADD'
    # print(f'Token ADD detact:{t.value}')
    return t

# Define SEMICOLON's token, (t_SEMICOLON = r';')
def t_SEMICOLON(t):
    r';'
    t.type = 'SEMICOLON'
    # print(f'Token SEMICOLON detact:{t.value}')
    return t

# Define a rule so we can track Team
def t_TEAM(t):
    r'\w+:'
    t.value = t.value[:-1]
    t.type = 'TEAM'
    # print(f'Token team detact:{t.value}')
    return t

# Define a rule so we can track name
def t_NAME(t):
    r'[a-zA-Z]+'
    t.type = 'NAME'
    # print(f'Token name detact:{t.value}')
    return t

# A string containing ignored characters (spaces and tabs)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#===========Parser's rule====================== 

def p_expr_add(p):
    'expr : expr ADD term'
#p[0]^  p[1]^ p[2]^ p[3]^
    p[0] = f'{p[1]}, {p[3]}'
    # print(f'Parser_add_{p[1]},{p[2]},{p[3]} = {p[0]}')

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]
    # print(f'Parser_expr_term_{p[1]} = {p[0]}')

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
    # print(f'Parser_term_factor_{p[1]} = {p[0]}')

def p_factor_name(p):
    'factor : NAME'
    p[0] = p[1]
    # print(f'Parser_name_{p[1]} = {p[0]}')

def p_factor_expr(p):
    'factor : TEAM expr SEMICOLON'
    p[0] = f'{p[1]}:( {p[2]} )'
    # print(f'Parser_TEAM_SEMI{p[1]},{p[2]} = {p[0]}')

def p_error(p):
    print("Systax error in input!")
    
def setup_lexer_parser():
    l = lex.lex()
    p = yacc.yacc()
    return l,p

def test_lexer():
    lexer_instance, _ = setup_lexer_parser()
    lexer_instance.input('TeamA: John;\n TeamB: Alice + Bob;')
    tokens = []
    for token in lexer_instance:
        tokens.append(token.type)
    assert tokens == ['TEAM', 'NAME', 'SEMICOLON', 'TEAM', 'NAME', 'ADD', 'NAME', 'SEMICOLON']

def test_parser():
    _, parser_instance = setup_lexer_parser()
    input_string = 'arg: welly+ pual + mike+ julie +uwe+wenyuh+pheobe+leo+CJ+Zchi;'
    result = parser_instance.parse(input_string)
    expected_result = 'arg:( welly, pual, mike, julie, uwe, wenyuh, pheobe, leo, CJ, Zchi )'
    assert result == expected_result

if __name__ == '__main__':
    pytest.main()
    lexer, parser = setup_lexer_parser()
    while True:
        try:
            s = input('TeamUP: ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(f'Team & Members: {result}')