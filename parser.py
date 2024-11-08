import ply.yacc as yacc
from lexer import tokens

#Definir la prioridad de los operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

def p_statement_expr(p): #Espresión para mostrar el desarrollo al revés, con el resultado
    'statement : expression'
    if isinstance(p[1], dict) and 'terms' in p[1]:
        reversed_expr = ' + '.join(reversed(p[1]['terms']))
        print(f"{p[1]['value']} = {reversed_expr}")
    else:
        print(p[1])

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = {'value': p[1], 'terms': [str(p[1])]}

def p_expression_neg(p):
    'expression : MINUS expression %prec MINUS'
    p[2]['value'] = -p[2]['value']
    p[0] = p[2]
        
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    
    left = p[1]['value']
    right = p[3]['value']

    if p[2] == '+':
        result = left + right
    elif p[2] == '-':
        result = left - right
    elif p[2] == '*':
        result = left * right
    elif p[2] == '/':
        result = left / right
            
    terms = p[1]['terms'] + p[3]['terms']
    p[0] = {'value': result, 'terms': terms}
    
def p_expression_string(p): #Expresión de un String
    'expression : STRING'
    p[0] = {'value': p[1][::-1], 'terms': [p[1][::-1]]}
    
def p_statement_end(p): #Función para terminar el programa con "END"
    'statement : END'
    print("Ending program...")
    exit()

def p_error(p): #Salida de error
    print(f"Syntx error at '{p.value}'")

parser = yacc.yacc() 
