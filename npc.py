import ply.lex as lex
import ply.yacc as yacc

# Define lexer tokens
tokens = (
    'KEY',
    'EQUALS',
    'VALUE',
    'NEWLINE',
)

# Lexer rules
t_EQUALS = r'='
t_ignore = ' \t'

def t_KEY(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'KEY'
    return t

def t_VALUE(t):
    r'[^=\n]+'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# # Parser rules
def p_config(p):
    '''
    config : config key_value
           | key_value
    '''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_key_value(p):
    'key_value : KEY EQUALS VALUE NEWLINE'
    p[0] = (p[1], p[3])

def p_error(p):
    print(f"Syntax error at line {p.lineno}: {p.value}")


parser = yacc.yacc()

# # Sample configuration text
config_text = """
name = John
age = 30
email = john@example.com
"""

# # Parse the configuration
config = parser.parse(config_text)

# Print the parsed configuration
try:
    for key, value in config:
        print(f"{key}: {value}")
except:
    print("error")