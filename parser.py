import ply.yacc as yacc
from lexer import tokens

def p_expression_plus(p): #Expresión para sumar
    'expression : expression "+" expression'
    p[0] = p[1] + p[3]

def p_expression_number(p): #Expresión de un numero?
    'expression : NUMBER'
    p[0] = int(str(p[1])[::-1])
    
def p_expression_string(p): #Expresión de un String
    'expression : STRING'
    p[0] = p[1][::-1]
    
def p_error(p): #Salida de error
    print(f"Syntx error at '{p.value}'")

parser = yacc.yacc() 
