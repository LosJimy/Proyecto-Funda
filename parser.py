import ply.yacc as yacc
from lexer import tokens

variables = {}

# Definir la prioridad de los operadores
precedence = (
    ('left', 'EQEQ', 'NE'),  # prioridad == !=
    ('left', 'LT', 'LE', 'GT', 'GE'),  # prioridad < > <= >=
    ('left', 'PLUS', 'MINUS'),  # prioridad suma y resta
    ('left', 'MULTIPLY', 'DIVIDE'),  # prioridad multiplicación y división
    ('nonassoc', 'LPAREN', 'RPAREN'),  # prioridad paréntesis
)

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_expr(p):
    'statement : expression'
    if isinstance(p[1], dict) and 'reversed_expr' in p[1]:
        print(f"{p[1]['result']} = {p[1]['expr']}")
    else:
        print(p[1])
    p[0] = p[1]

def p_statement_assign(p):
    'statement : ID EQUALS expression'
    if p[1].lower() in ['end', 'salir']:
        print(f"Cannot assign to reserved word '{p[1]}'")
    else:
        variables[p[1]] = p[3]
    p[0] = None

def p_statement_print(p):
    '''statement : ID LPAREN STRING RPAREN
                 | ID LPAREN ID RPAREN'''
    if p[1] == 'tnirp':
        if p[3].startswith('"') and p[3].endswith('"'):
            print(p[3][1:-1])
        elif p[3].startswith("'") and p[3].endswith("'"):
            print(p[3][1:-1])
        elif p[3] in variables:
            print(variables[p[3]])
    p[0] = None

def p_statement_if(p):
    'statement : IF expression LBRACE statement_list RBRACE'
    condition_met = evaluate_condition(p[2])
    print(f"ecaluando condición if: {p[2]} - Met: {condition_met}")
    if condition_met:
        print(f"Ejecutando bloque if: {p[2]}")
        for stmt in p[4]:
            execute_statement(stmt)
    else:
        print("La condición del if no se cumplió.")
    p[0] = None

def p_statement_if_else(p):
    'statement : IF expression LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'
    condition_met = evaluate_condition(p[2])
    print(f"Evaluando condición if-else: {p[2]} - Met: {condition_met}")
    if condition_met:
        print(f"Ejecutando bloque if: {p[2]}")
        for stmt in p[4]:
            execute_statement(stmt)
    else:
        print(f"Ejecutando bloque else: {p[2]}")
        for stmt in p[8]:
            execute_statement(stmt)
    p[0] = None

def p_statement_end(p):
    'statement : END'
    print("Ending program...")
    exit()

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    if p[1] in variables:
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
                  | expression DIVIDE expression
                  | expression EQEQ expression
                  | expression NE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression'''

    left = p[1] if isinstance(p[1], (int, float)) else p[1]['result']
    right = p[3] if isinstance(p[3], (int, float)) else p[3]['result']

    if p[2] == '+':
        result = left + right
    elif p[2] == '-':
        result = left - right
    elif p[2] == '*':
        result = left * right
    elif p[2] == '/':
        result = left / right
    elif p[2] == '==':
        result = left == right
    elif p[2] == '!=':
        result = left != right
    elif p[2] == '<':
        result = left < right
    elif p[2] == '>':
        result = left > right
    elif p[2] == '<=':
        result = left <= right
    elif p[2] == '>=':
        result = left >= right

    p[0] = {'result': result, 'expr': f"{left} {p[2]} {right}", 'reversed_expr': f"{right} {p[2]} {left}"}
    print(f"Evaluación de binop: {p[0]}")

def p_expression_string(p):
    '''expression : STRING'''
    string = p[1][1:-1]
    inverted = list(string[::-1])
    for i in range(len(inverted)):
        if inverted[i] == '(':
            inverted[i] = ')'
        elif inverted[i] == ')':
            inverted[i] = '('
    normal_string = ''.join(string)
    reversed_string = ''.join(inverted)
    p[0] = f'"{reversed_string}" | "{normal_string}"'

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

def evaluate_condition(condition):
    if isinstance(condition, dict):
        print(f"Evaluando dict condición: {condition}")
        return condition['result']
    print(f"Evaluando condición directa: {condition}")
    return bool(condition)

# Esta es la función completa, con todos los ajustes.
parser = yacc.yacc()

def execute_statement(statement):
    if statement:
        if isinstance(statement, list):
            for stmt in statement:
                execute_statement(stmt)
        else:
            print(statement)