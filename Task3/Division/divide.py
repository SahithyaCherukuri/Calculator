import sys


def divide():
    filename='/data/divide.txt'
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
        try:
            with open(filename, 'r') as f:
                y = int(f.read().strip())   
        except FileNotFoundError:
            y = 100

    print(y,x)
    result = y//x
    with open(filename, 'w') as f:
        f.write(str(result))
        print(result)


if __name__ == '__main__':
    divide()
