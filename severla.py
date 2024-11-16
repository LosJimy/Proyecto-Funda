from lexer import lexer
from parser import parser

statements = []

def execute_statements():
    global statements
    for statement in statements:
        if statement:
            if isinstance(statement, list):
                for stmt in statement:
                    execute_statements(stmt)
            else:
                execute_statements(statement)
    statements = []
    
def execute_statements(statement):
    if statement:
        if isinstance(statement, list):
            for stmt in statement:
                execute_statements(stmt)
        else:
            print(statement)            

while True:
    try:
        s = input('severla > ')
    except EOFError:
        break
    
    if s.strip() == "":
        execute_statements()
        continue
    
    result = parser.parse(s, lexer=lexer)
    if result is not None:
        statements.append(result)