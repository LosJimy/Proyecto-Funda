from lexer import lexer
from parser import parser

while True:
    try:
        s = input('severla > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s, lexer=lexer)
    if result is not None:
        print(result)