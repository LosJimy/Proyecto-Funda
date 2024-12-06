import ply.yacc as yacc
from lexer import tokens

variables = {}

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
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
                 | for_statement
                 | while_statement
                 | print_statement'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID ASSIGN expression'
    variables[p[1]] = evaluate_expression(p[3])
    p[0] = ('assign', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF condition statement elif_list_opt ELSE statement
                    | IF condition statement elif_list_opt'''
    if len(p) == 7:
        if evaluate_expression(p[2]):
            p[0] = p[3]
        else:
            p[0] = evaluate_elif(p[4], p[6])
    elif len(p) == 6:
        if evaluate_expression(p[2]):
            p[0] = p[3]
        else:
            p[0] = evaluate_elif(p[4], None)

def p_elif_list_opt(p):
    '''elif_list_opt : elif_list
                     | empty'''
    p[0] = p[1]

def p_elif_list(p):
    '''elif_list : elif_list ELIF condition statement
                 | ELIF condition statement'''
    if len(p) == 5:
        p[0] = p[1] + [(p[3], p[4])]
    else:
        p[0] = [(p[2], p[3])]

def p_for_statement(p):
    '''for_statement : FOR ID IN range statement'''
    p[0] = ('for', p[2], p[4], p[5])

def p_while_statement(p):
    '''while_statement : WHILE condition statement'''
    p[0] = ('while', p[2], p[3])

def p_range(p):
    '''range : RANGE LPAREN expression COMMA expression RPAREN'''
    p[0] = list(range(evaluate_expression(p[3]), evaluate_expression(p[5])))

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('print', p[3])

def evaluate_elif(elifs, else_stmt):
    for cond, stmt in elifs:
        if evaluate_expression(cond):
            return stmt
    return else_stmt

def execute_statement(stmts):
    if isinstance(stmts, list):
        for stmt in stmts:
            execute_single_statement(stmt)
    else:
        execute_single_statement(stmts)

def execute_single_statement(stmt):
    if isinstance(stmt, tuple):
        if stmt[0] == 'print':
            print(evaluate_expression(stmt[1]))
        elif stmt[0] == 'for':
            execute_for_statement(stmt)
        elif stmt[0] == 'while':
            execute_while_statement(stmt)
        elif stmt[0] == 'assign':
            variables[stmt[1]] = evaluate_expression(stmt[2])

def execute_for_statement(stmt):
    variable, iter_range, body = stmt[1], stmt[2], stmt[3]
    for value in iter_range:
        variables[variable] = value
        execute_statement(body)

def execute_while_statement(stmt):
    condition, body = stmt[1], stmt[2]
    while evaluate_expression(condition):
        execute_statement(body)

def evaluate_expression(expr):
    if isinstance(expr, (int, float, str, bool)):
        return expr
    elif isinstance(expr, tuple):
        if expr[0] == 'id':
            value = variables.get(expr[1], None)
            if value is None:
                raise ValueError(f"Variable '{expr[1]}' no definida")
            return value
        elif expr[0] in ('+', '-', '*', '/', '%'):
            left = evaluate_expression(expr[1])
            right = evaluate_expression(expr[2])
            if expr[0] == '+':
                return left + right
            elif expr[0] == '-':
                return left - right
            elif expr[0] == '*':
                return left * right
            elif expr[0] == '/':
                return left / right
            elif expr[0] == '%':
                return left % right
        elif expr[0] == '!':
            return not evaluate_expression(expr[1])
        elif expr[0] == '||':
            return evaluate_expression(expr[1]) or evaluate_expression(expr[2])
        elif expr[0] == '&&':
            return evaluate_expression(expr[1]) and evaluate_expression(expr[2])
    return expr

def p_condition(p):
    '''condition : expression EQUALS expression
                 | expression LT expression
                 | expression GT expression
                 | expression LE expression
                 | expression GE'''
    left = evaluate_expression(p[1])
    right = evaluate_expression(p[3])
    if p[2] == '==':
        p[0] = left == right
    elif p[2] == '<':
        p[0] = left < right
    elif p[2] == '>':
        p[0] = left > right
    elif p[2] == '<=':
        p[0] = left <= right
    elif p[2] == '>=':
        p[0] = left >= right

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -evaluate_expression(p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression OR expression
                  | expression AND expression'''  # Añadidos OR y AND
    p[0] = (p[2], evaluate_expression(p[1]), evaluate_expression(p[3]))

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('!', p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

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

def p_empty(p):
    'empty :'
    p[0] = []

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
