import ply.yacc as yacc
from lexer import tokens

#Definir la prioridad de los operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

def p_statement_expr(p): #Espresión para mostrar el desarrollo al revés, con el resultado
    'statement : expression'
    if isinstance(p[1], dict):
        if 'reversed_expr' in p[1]:
            print(f"{p[1]['result']} = {p[1]['reversed_expr']}")
        else:
            print(f"{p[1]['result']}")
    else:
        print(p[1])  

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = {'result': p[1], 'expr': str(p[1]), 'reversed_expr': str(p[1])}

def p_expression_plus(p): #Expresión para sumar
    'expression : expression PLUS expression'
    result = p[1]['result'] + p[3]['result'] 
    expr = f"{p[1]['expr']} + {p[3]['expr']}"
    reversed_expr = f"{p[3]['result']} + {p[1]['result']}"
    p[0] = {'result': result, 'expr': expr, 'reversed_expr': reversed_expr}

  
def p_expression_minus(p): #Expresión para restar
    'expression : expression MINUS expression'
    #ARREGLAR ERROR
    result = p[1]['result'] - p[3]['result']
    expr = f"{p[1]['expr']} - {p[3]['expr']}"
    reversed_expr = f"{p[3]['result']} - {p[1]['result']}"
    p[0] = {'result': result, 'expr': expr, 'reversed_expr': reversed_expr}
    
def p_expression_divide(p): #Expresión para dividir números
    'expression : expression DIVIDE expression'
    result = p[1]['result'] / p[3]['result']
    expr = f"{p[1]['expr']} / {p[3]['expr']}"
    reversed_expr = f"{p[1]['result']} * 1/{p[3]['result']}"
    p[0] = {'result': result, 'expr': expr, 'reversed_expr': reversed_expr}

def p_expression_multiply(p): #Expresión para multiplicar
    'expression : expression MULTIPLY expression'
    result = p[1]['result'] * p[3]['result']
    expr = f"{p[1]['expr']} * {p[3]['expr']}"
    reversed_expr = f"{p[3]['result']} * {p[1]['result']}"
    p[0] = {'result': result, 'expr': expr, 'reversed_expr': reversed_expr}   
    
def p_expression_string(p): #Expresión de un String
    'expression : STRING'
    p[0] = p[0] = p[1][::-1]
    
def p_statement_end(p): #Función para terminar el programa con "END"
    'statement : END'
    print("Ending program...")
    exit()

def p_error(p): #Salida de error
    print(f"Syntx error at '{p.value}'")

parser = yacc.yacc() 
