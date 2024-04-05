import sys
import os


def plus():
    filename='/data/addition.txt'
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
        try:
            with open(filename, 'r') as f:
                y = int(f.read().strip())   
        except FileNotFoundError:
            y = 0

    print(y,x)
    result = x+y
    with open(filename, 'w') as f:
        f.write(str(result))
        print(result)
    return result

if __name__ == '__main__':
    plus()
