import ply.lex as lex
# import re
class NPC:
    # NPC's name, age, gender
    def __init__(self) -> None:
        self._name_match = r'[a-zA-Z]+'
        self.reserved = {
        'my name is' : 'my_name_is',
        }
        
    
    tokens = (
        'NAME',
        'AGE',
        'MY',
        'YOU',
        'ID',
        'my_name_is'
    )
    
    t_YOU = r'you'

    t_MY = r'[m, M]y'

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    def t_NAME(self, t):
        # self.name = r'\w+'
        # t.value = self.name
        r'name_is_[a-zA-Z]+;'
        t.value = t.value[8:-1]
        t.type = 'NAME'
        return t
        # Define a rule so we can track name
    
    def t_AGE(self, t):
        # self.age = r'\d+'
        # r'my age is ' + self.age
        # t.value = self.age
        r'age_is_\d+;'
        t.value = t.value[7:-1]
        t.type = 'AGE'
        return t
        # Define a rule so we can track name

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        # A string containing ignored characters (spaces and tabs)

    # t_ignore = ' \t'
    # Error handling rule

    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        # Build the lexer

    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        # Test it output
    
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

n = NPC()
n.build()
n.test("my name is uwe  and my age_is_22;")