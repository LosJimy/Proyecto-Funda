import ply.yacc as yacc
from lexer import tokens

variables = {}

#Definir la prioridad de los operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('nonassoc', 'LPAREN', 'RPAREN'), #prioridad parentesis
)

def p_statement_expr(p): #Espresión para mostrar el desarrollo al revés, con el resultado
    'statement : expression'
    if isinstance(p[1], dict) and 'reversed_expr' in p[1]:
        print(f"{p[1]['result']} = {p[1]['expr']}")
    else:
        print(p[1])  

def p_statement_assign(p):
    'statement : ID EQUALS expression'
    if p[1].lower() in ['end','salir']:
        print(f"Cannot assign to reserved word '{p[1]}'")
    else:
        variables[p[1]] = p[3]
        print(f"{p[1]} = {p[3]}")
    
def p_statement_print(p):
    'statement : ID LPAREN ID RPAREN'
    if p[1] == 'tnirp' and p[3] in variables:
        print(variables[p[3]])

def p_expression_paren(p): #Evaluar primero los parentesis
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    if p[1].lower() in ['end', 'salir']:
        p[0] = p[1]
    elif p[1] in variables:
        p[0] = variables[p[1]]
    else:
        print(f"Variable indefinida '{p[1]}'")
        p[0] = 0
        
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
        reversed_expr = f"{right} + {left}"
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
    string = p[1][1:-1]
    inverted = list(string[::-1])
    for i in range(len(inverted)):
        if inverted[i] == '(':
            inverted[i] =')'
        elif inverted[i] == ')':
            inverted[i] = '('
    p[0] = '"' + ''.join(inverted) + '"'
    
def p_statement_end(p): #Función para terminar el programa con "END"
    'statement : END'
    print("Ending program...")
    exit()

def p_error(p): #Salida de error
    print(f"Syntx error at '{p.value}'")

parser = yacc.yacc() 
