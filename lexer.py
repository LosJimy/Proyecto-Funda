import ply.lex as lex

tokens = (
    'NUMBER', 'FLOAT', 'STRING', 'PLUS', 'MINUS', 'DIVIDE', 'MULTIPLY',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'EQUALS', 'EQEQ', 'NE', 'LT', 'GT',
    'LE', 'GE', 'ID', 'IF', 'ELSE', 'END',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALS = r'='
t_EQEQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_STRING = r'(\".*?\"|\'.*?\')'
t_ignore = ' \t'

def t_IF(t):
    r'fi|if'
    t.type = 'IF'
    return t

def t_ELSE(t):
    r'esle|else'
    t.type = 'ELSE'
    return t

def t_END(t):
    r'END|End|end|SALIR|Salir|salir'
    t.type = 'END'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-z_0-9]*'
    t.type = 'ID'
    return t

def t_FLOAT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
