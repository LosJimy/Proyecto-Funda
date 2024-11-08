import ply.yacc as yacc
from lexer import tokens

#Definir la prioridad de los operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

def p_statement_expr(p): #Espresión para mostrar el desarrollo al revés, con el resultado
    'statement : expression'
    if isinstance(p[1], dict) and 'reversed_expr' in p[1]:
        print(f"{p[1]['result']} = {p[1]['reversed_expr']}")
    else:
        print(p[1])  

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    inverted_number = str(p[1])[::-1] # invertir número
    if isinstance(p[1], float):
        p[0] = float(inverted_number)
    else:
        if inverted_number.endswith('-'):
            inverted_number = '-' + inverted_number[:-1]
        p[0] = int(inverted_number)

def p_expression_neg(p):
    'expression : MINUS expression %prec MINUS'
    p[0] = -p[2]
        
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        result = p[1] + p[3]
        expr = f"{p[1]} + {p[3]}"
        reversed_expr = f"{p[3]} + {p[1]}"
    elif p[2] == '-':
        result = p[1] + p[3]
        expr = f"{p[1]} - {p[3]}"
        reversed_expr = f"-{p[3]} + {p[1]}"
    elif p[2] == '*':
        result = p[1] * p[3]
        expr = f"{p[1]} * {p[3]}"
        reversed_expr = f"{p[3]} * {p[1]}"
    elif p[2] == '/':
        result = p[1] / p[3]
        expr = f"{p[1]} / {p[3]}"
        reversed_expr = f"{p[1]} * 1/{p[3]}"
            
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
