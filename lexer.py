import ply.lex as lex

tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'END',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_STRING = r'\".*?\"'
t_ignore = ' \t'
t_END = r'END'

def t_NUMBER(t): #Función de el token Number
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t): #Función que se activa cada vez  que el lexer encuentra una nueva linea en el código fuente
    r'\n+'
    t.lexer.lineno += len(t.value) #Incrementa contador de lineas cada vez que se encuentra una nueva línea

def t_error(t): #Funcion para detectar error e imprimir donde está el error
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    
lexer = lex.lex()