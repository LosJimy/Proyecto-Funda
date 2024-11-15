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
    p[0] = p[1]

def p_expression_neg(p):
    'expression : MINUS expression %prec MINUS'
    p[0] = -p[2]
        
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    
    left = p[1] if isinstance(p[1], (int, float)) else p[1]['result']
    right = p[3] if isinstance(p[3], (int, float)) else p[3]['result']   

    if p[2] == '+':
        result = left + right
        expr = f"{left} + {right}"
        reversed_expr = f"{left} + {right}"
    elif p[2] == '-':
        result = left - right
        expr = f"{left} - {right}"
        reversed_expr = f"-{right} + {left}"
    elif p[2] == '*':
        result = left * right
        expr = f"{left} * {right}"
        reversed_expr = f"{right} * {left}"
    elif p[2] == '/':
        result = left / right
        expr = f"{left} / {right}"
        reversed_expr = f"{left} * 1/{right}"
            
    p[0] = {'result': result, 'expr': expr, 'reversed_expr': reversed_expr}
    
def p_expression_string(p): #Expresión de un String
    'expression : STRING'
    p[0] = p[1][::-1]
    
def p_statement_end(p): #Función para terminar el programa con "END"
    'statement : END'
    print("Ending program...")
    exit()

def p_error(p): #Salida de error
    print(f"Syntx error at '{p.value}'")

parser = yacc.yacc() 
