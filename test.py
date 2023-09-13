import ply.yacc as yacc
from ply.lex import lex

# 定义词法分析器（lexer）
tokens = (
    'ID',       # 标识符（变量名）
    'EQUALS',   # 赋值符号（=）
    'NUMBER',   # 数字
    'SEMICOLON',# 分号（;）
)

# 正则表达式规则
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUALS = r'='
t_NUMBER = r'\d+'
t_SEMICOLON = r';'

t_ignore = ' \t'

# 错误处理
def t_error(t):
    print(f"不合法的字符 '{t.value[0]}'")
    t.lexer.skip(1)

# 构建解析器（parser）
def p_statements(p):
    '''
    statements : statements statement SEMICOLON
               | statement SEMICOLON
    '''

def p_statement_assign(p):
    '''
    statement : ID EQUALS expression
    '''
    print(f"赋值语句：{p[1]} = {p[3]}")

def p_expression(p):
    '''
    expression : NUMBER
    '''

# 错误处理
def p_error(p):
    print("语法错误")

# 创建 lexer 和 parser
lexer = lex()
parser = yacc.yacc()

# 测试输入
input_text = """
x = 10;
y = x + 5;
"""

parser.parse(input_text)