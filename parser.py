import ply.yacc as yacc
from lexer import tokens

#Definir la prioridad de los operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

def p_statement_expr(p): #Espresión para mostrar el desarrollo al revés, con el resultado
    'statement : expression'
    print(f"{p[1]['expr']} = {p[1]['result']}")

def p_expression_number(p): #Expresión de un numero?
    'expression : NUMBER'
    p[0] = {'result': p[1], 'expr': str(p[1])}

def p_expression_plus(p): #Expresión para sumar
    'expression : expression PLUS expression'
    #CAMBIO LUEGO BORRAR HACER QUE SEA
    #3+4=7
    #7=4+3
    result = p[1]['result'] + p[3]['result'] 
    expr = f"{p[1]['expr']} + {p[3]['expr']}"
    p[0] = {'result': result, 'expr': expr}

  
def p_expression_minus(p): #Expresión para restar
    'expression : expression MINUS expression'
    #CAMBIO LUEGO BORRAR HACER QUE SEA
    #4-3=1
    #1 = -3 + 4
    result = p[1]['result'] - p[3]['result']
    expr = f"{p[1]['expr']} - {p[3]['expr']}"
    p[0] = {'result': result, 'expr': expr}
    
def p_expression_divide(p): #Expresión para dividir números
    'expression : expression DIVIDE expression'
    #CAMBIO LUEGO BORRAR HACER QUE SEA
    #25/5 = 5
    #5 = 25 * 1/5
    result = p[1]['result'] / p[3]['result']
    expr = f"{p[1]['expr']} / {p[3]['expr']}"
    p[0] = {'result': result, 'expr': expr}

def p_expression_multiply(p): #Expresión para multiplicar
    #CAMBIO LUEGO BORRAR HACER QUE SEA
    #3*4=12
    #12=4*3
    'expression : expression MULTIPLY expression'
    result = p[1]['result'] * p[3]['result']
    expr = f"{p[1]['expr']} * {p[3]['expr']}"
    p[0] = {'result': result, 'expr': expr}   
    
def p_expression_string(p): #Expresión de un String
    'expression : STRING'
    p[0] = {'result': p[1][::-1], 'expr': p[1][::-1]}    
    
def p_statement_end(p): #Función para terminar el programa con "END"
    'statement : END'
    print("Ending program...")
    exit()

def p_error(p): #Salida de error
    print(f"Syntx error at '{p.value}'")

parser = yacc.yacc() 
