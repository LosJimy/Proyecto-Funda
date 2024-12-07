import ply.lex as lex

#Creación de Tokens
tokens = (
    'ID', 'STRING', 'FLOAT', 'NUMBER',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO',
    'PLUSEQUALS', 'MINUSEQUALS',
    'ASSIGN', 'LPAREN', 'RPAREN', 'COMMA', 'COLON',
    'IF', 'ELSE', 'ELIF', 'FOR', 'IN', 'RANGE', 'WHILE',
    'EQUALS', 'LT', 'GT', 'LE', 'GE',
    'TRUE', 'FALSE', 'PRINT', 'OR', 'AND', 'NOT',
    'DEF', 'RETURN', 'BREAK'
)

#Definición de Tokens
t_PLUSEQUALS = r'\+='
t_MINUSEQUALS = r'-='
t_BREAK = r'break'
t_COLON = r':'
t_DEF = r'def'
t_RETURN = r'return'
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
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_ignore = ' \t'

#Definición Funciones de Tokens
def t_COMMENT(t):
    r'\#.*'
    pass

def t_IF(t):
    r'fi'
    return t

def t_ELSE(t):
    r'esle'
    return t

def t_ELIF(t):
    r'file'
    return t

def t_FOR(t):
    r'rof'
    return t

def t_IN(t):
    r'ni'
    return t

def t_RANGE(t):
    r'egnar'
    return t

def t_WHILE(t):
    r'elihw'
    return t

def t_PRINT(t):
    r'tnirp'
    return t

def t_TRUE(t):
    r'eurt'
    return t

def t_FALSE(t):
    r'eslaf'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_STRING(t):
    r'(<<.*?>>|<.*?>|\".*?\"|\'.*?\')'
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
