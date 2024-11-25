from lexer import lexer
from parser import parser

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def execute_statements(statements):
    for statement in statements:
        execute_statement(statement)

def execute_statement(statement):
    if statement:
        if isinstance(statement, list):
            for stmt in statement:
                execute_statement(stmt)
        else:
            print(statement)

def main():
    while True:
        try:
            s = input('severla > ')
        except EOFError:
            break
        
        if s.startswith('daer(') and s.endswith(')'):
            filename = s[5:-1].strip()
            content = read_file(filename)
            result = parser.parse(content, lexer=lexer)
            if result is not None:
                execute_statements(result)
        elif s.strip() == '':
            continue
        else:
            result = parser.parse(s, lexer=lexer)
            if result is not None:
                execute_statements(result)

if __name__ == '__main__':
    main()
