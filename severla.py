from lexer import lexer
from parser import parser

statements = []

def execute_statements():
    global statements
    for statement in statements:
        if statement:
            if isinstance(statement, list):
                for stmt in statement:
                    execute_statement(stmt)
            else:
                execute_statement(statement)
    statements = []

def execute_statement(statement):
    if statement:
        if isinstance(statement, list):
            for stmt in statement:
                execute_statement(stmt)
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
