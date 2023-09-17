import ply.lex as lex
import ply.yacc as yacc
# import re
class NPC:
    # NPC's name, age, gender
    # def __init__(self) -> None:
    #     self._name_match = r'[a-zA-Z]+'
    #     self.reserved = {
    #     'my name is' : 'my_name_is',
    #     }
        
    ### building token=============================================

    tokens = (
        #declear your tokens type
        'NAME',
        'AGE',
        'MY',
        'YOUR',
    )
    # define your tokens
    t_YOUR = r'[y, Y]our'

    t_MY = r'[m, M]y'

    def t_NAME(self, t):
        r'name_is_[a-zA-Z]+'
        t.value = t.value[8:]
        t.type = 'NAME'
        return t
        # Define a rule so we can track name
    
    def t_AGE(self, t):
        r'age_is_\d+'
        t.value = t.value[7:]
        t.value = int(t.value)
        t.type = 'AGE'
        return t
        # Define a rule so we can track name

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        # A string containing ignored characters (spaces and tabs)

    t_ignore = ' \t'
    # Error handling rule

    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        # Build the lexer
    ###============================================================
    
    ###building parser=============================================
    def p_expression_my(p):
        'expression : MY term'
        p[0] = f'my name is {p[2]}'
    def p_expression_name(p):
        'factor : NAME'
        # p[0] = p[1]
        
    def p_expression_age(p):
        'factor : AGE'
        p[0] = p[1]

    def p_term_factor(p):
        'term : factor'
        p[0] = p[1]

    def p_expression_term(p):
        'expression : term'
        p[0] = p[1]

    def p_error(p):
        print("Systax error in input!")
    ###============================================================
    def build_lexer(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        # self.parser = yacc.yacc(module=self, **kwargs)
        # Test it output

    def build_parser(self):
        self.parser = yacc.yacc()

    def test_token(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
    
    # def test_parser(self, **kwargs):

n = NPC()
n.build_lexer()
n.build_parser()
n.test_token("my name_is_uwe and my age_is_22")