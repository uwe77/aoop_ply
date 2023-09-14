import ply.lex as lex

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
}

tokens = ['ID'] + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_ignore = ' \t'

lexer = lex.lex()

lexer.input("wsed fw e7y98 79")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
