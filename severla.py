from lexer import lexer
from parser import parser

def main():
    with open('codigo.txt', 'r') as f:
        data = f.read()
    lexer.input(data)
    parser.parse(data)

if __name__ == '__main__':
    main()
