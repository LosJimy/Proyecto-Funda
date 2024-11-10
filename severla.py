from lexer import lexer
from parser import parser

while True:
    try:
        s = input('severla > ') #Try de correr el programa, sino que tipee error
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s, lexer=lexer)
    if result is not None:
        print(result)