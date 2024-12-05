import ply.yacc as yacc
from lexer import tokens

variables = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('nonassoc', 'EQUALS', 'LT', 'GT', 'LE', 'GE'),
)

def p_program(p):
    'program : statement_list'
    p[0] = p[1]
    execute_statement(p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment
                 | if_statement
                 | print_statement'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID ASSIGN expression'
    variables[p[1]] = p[3]
    p[0] = ('assign', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF condition statement ELSE statement
                    | IF condition statement'''
    if len(p) == 6:
        if p[2]:
            p[0] = p[3]
        else:
            p[0] = p[5]
    else:
        if p[2]:
            p[0] = p[3]
        else:
            p[0] = None

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('print', p[3])

def execute_statement(stmts):
    if isinstance(stmts, list):
        for stmt in stmts:
            if isinstance(stmt, tuple) and stmt[0] == 'print':
                print(stmt[1])
    elif isinstance(stmts, tuple) and stmts[0] == 'print':
        print(stmts[1])

def p_condition(p):
    '''condition : expression EQUALS expression
                 | expression LT expression
                 | expression GT expression
                 | expression LE expression
                 | expression GE expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_id(p):
    'expression : ID'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f"Variable '{p[1]}' no definida")
        p[0] = 0

def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
