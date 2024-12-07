import ply.yacc as yacc
from lexer import tokens

variables = {}      #Diccionario que almacena variables definidas
functions = {}      #Diccionario que almacena las funciones creadas

#Define la prioridad de los operadores para resolver ambiguedades en las expresiones
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('right', 'UMINUS'),
    ('nonassoc', 'EQUALS', 'LT', 'GT', 'LE', 'GE'),
)

#Una excepción personalizada para manejar las declaraciones de retorno en funciones.
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

#Define la estructura inicial del programa como una lista de declaraciones, ejecutandolas en orden
def p_program(p):
    'program : statement_list'
    p[0] = p[1]
    execute_statement(p[1])

#Maneja lista de declaraciones, puede ser una o varias
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

#Define if,for,while,print,
def p_statement(p):
    '''statement : assignment
                 | if_statement
                 | for_statement
                 | while_statement
                 | print_statement
                 | function_def
                 | function_call
                 | return_statement
                 | break_statement'''
    p[0] = p[1]

#Define la estructura de break
def p_break_statement(p):
    'break_statement : BREAK'
    p[0] = 'break'

#Maneja la asignación de valores a variables 
def p_assignment(p):
    'assignment : ID ASSIGN expression'
    variables[p[1]] = evaluate_expression(p[3])
    p[0] = ('assign', p[1], p[3])

#Define estructura de if,elif,else
def p_if_statement(p):
    '''if_statement : IF condition COLON statement elif_list_opt ELSE statement
                    | IF condition COLON statement elif_list_opt'''
    if len(p) == 8:
        if evaluate_expression(p[2]):
            p[0] = p[4]
        else:
            p[0] = evaluate_elif(p[5], p[7])
    elif len(p) == 6:
        if evaluate_expression(p[2]):
            p[0] = p[4]
        else:
            p[0] = evaluate_elif(p[5], None)

#Maneja las declaraciones de elif
def p_elif_list_opt(p):
    '''elif_list_opt : elif_list
                     | empty'''
    p[0] = p[1]

#Maneja las declaraciones de elif
def p_elif_list(p):
    '''elif_list : elif_list ELIF condition COLON statement
                 | ELIF condition COLON statement'''
    if len(p) == 6:
        p[0] = p[1] + [(p[3], p[5])]
    else:
        p[0] = [(p[2], p[4])]

#Define estructura bucles for
def p_for_statement(p):
    '''for_statement : FOR ID IN range statement'''
    p[0] = ('for', p[2], p[4], p[5])

#Define estructura bucles while
def p_while_statement(p):
    '''while_statement : WHILE condition statement'''
    p[0] = ('while', p[2], p[3])

#Define el rango de valores en un bucle for
def p_range(p):
    '''range : RANGE LPAREN expression COMMA expression RPAREN'''
    p[0] = list(range(evaluate_expression(p[3]), evaluate_expression(p[5])))

#Maneja las declaraciones print para imprimir expresiones
def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('print', p[3])

#Define la estructura de una función
def p_function_def(p):
    '''function_def : DEF ID LPAREN param_list RPAREN COLON statement_list'''
    functions[p[2]] = (p[4], p[7])
    p[0] = ('def', p[2], p[4], p[7])

#Define llamada de función
def p_function_call(p):
    '''function_call : ID LPAREN arg_list RPAREN'''
    p[0] = ('call', p[1], p[3])

#Maneja las declaraciones dentro de las funciones
def p_return_statement(p):
    'return_statement : RETURN expression'
    p[0] = ('return', evaluate_expression(p[2]))

#Maneja las listas de parámetros y argumentos en funciones
def p_param_list(p):
    '''param_list : param_list COMMA ID
                  | ID
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

#Maneja las listas de parámetros y argumentos en funciones
def p_arg_list(p):
    '''arg_list : arg_list COMMA expression
                | expression
                | empty'''
    if len(p) == 4:
        p[0] = p[1] + [evaluate_expression(p[3])]
    elif len(p) == 2:
        p[0] = [evaluate_expression(p[1])]
    else:
        p[0] = []

#Evalua las condiciones en las declaraciones elif
def evaluate_elif(elifs, else_stmt):
    for cond, stmt in elifs:
        if evaluate_expression(cond):
            return stmt
    return else_stmt

#Ejecuta una lista de declaraciones
def execute_statement(stmts):
    if isinstance(stmts, list):
        for stmt in stmts:
            execute_single_statement(stmt)
    else:
        execute_single_statement(stmts)

#Ejecuta una declaración individual, incuyendo asignaciones, bucles, funciones y retornos
def execute_single_statement(stmt):
    if isinstance(stmt, tuple):
        if stmt[0] == 'print':
            value = evaluate_expression(stmt[1])
            if isinstance(value, str):
                # Imprimir la cadena original y la cadena invertida
                print(f"{value} | {value[::-1]}")
            else:
                print(value)
        elif stmt[0] == 'for':
            execute_for_statement(stmt)
        elif stmt[0] == 'while':
            execute_while_statement(stmt)
        elif stmt[0] == 'assign':
            variables[stmt[1]] = evaluate_expression(stmt[2])
        elif stmt[0] == 'def':
            functions[stmt[1]] = (stmt[2], stmt[3])
        elif stmt[0] == 'call':
            result = execute_function_call(stmt)
            if result is not None:
                variables['result'] = result
        elif stmt[0] == 'return':
            raise ReturnException(evaluate_expression(stmt[1]))
    elif stmt == 'break':
        raise BreakException()

class BreakException(Exception):
    pass

#Ejecuta bucle for
def execute_for_statement(stmt):
    variable, iter_range, body = stmt[1], stmt[2], stmt[3]
    for value in iter_range:
        variables[variable] = value
        execute_statement(body)

#Ejecuta bucle while
def execute_while_statement(stmt):
    condition, body = stmt[1], stmt[2]
    while evaluate_expression(condition):
        execute_statement(body)

#Ejecuta una llamada a función
def execute_function_call(stmt):
    func_name, args = stmt[1], stmt[2]  # stmt[1]: nombre de la función, stmt[2]: argumentos
    if func_name not in functions:
        raise ValueError(f"Función '{func_name}' no definida")
    
    # Recuperar parámetros y cuerpo de la función
    params, body = functions[func_name]
    
    # Crear un entorno local para las variables de la función
    local_vars = variables.copy()  # Copia las variables globales (entorno actual)

    # Asignar valores a los parámetros en el entorno local
    for param, arg in zip(params, args):
        local_vars[param] = evaluate_expression(arg)  # Evalúa los argumentos

    # Ejecutar el cuerpo de la función
    try:
        execute_statement(body)  # Ejecuta el cuerpo de la función
    except ReturnException as ret:
        return ret.value  # Devuelve el valor si hay un return

    # Restaurar las variables globales después de la ejecución
    variables.update(local_vars)

    # Si no hay un return explícito, devuelve None
    return None

#Evalúa expresiones aritméticas, logicas y de variables
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

#Define las condiciones para las declaraciones if, elif y else
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

#Maneja la negación en expresiones
def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -evaluate_expression(p[2])

#Define operaciones binarias 
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression OR expression
                  | expression AND expression'''
    p[0] = (p[2], evaluate_expression(p[1]), evaluate_expression(p[3]))

#Maneja negación logica
def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('!', p[2])

#Maneja las expresiones entre paréntesis
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

#Maneja identificadores de variables
def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

#Maneja el valor booleano TRUE
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

#Maneja el valor booleano FALSE
def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

#Maneja números
def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = p[1]

#Maneja cadenas de texto
def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

#Define regla vacía
def p_empty(p):
    'empty :'
    p[0] = []

#Maneja los errores de sintaxis en el parser
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()

