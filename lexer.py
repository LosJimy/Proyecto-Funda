import ply.lex as lex

tokens = (
    'ID',
    'STRING',
    'FLOAT',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'IF',
    'ELSE',
    'ELIF',
    'FOR',
    'IN',
    'RANGE',
    'WHILE',
    'EQUALS',
    'LT',
    'GT',
    'LE',
    'GE',
    'TRUE',
    'FALSE',
    'PRINT',
    'OR',    # Token para operador lógico OR (||)
    'AND',   # Token para operador lógico AND (&&)
    'NOT',   # Token para operador lógico NOT (!)
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_EQUALS = r'=='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_OR = r'\|\|'   # Expresión regular para operador OR
t_AND = r'&&'    # Expresión regular para operador AND
t_NOT = r'!'     # Expresión regular para operador NOT
t_ignore = ' \t'

def t_COMMENT(t):
    r'\#.*'
    pass  # Ignorar los comentarios

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELIF(t):
    r'elif'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_RANGE(t):
    r'range'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la posición {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()
