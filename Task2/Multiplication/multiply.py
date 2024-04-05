import sys


def multiply():
    if len(sys.argv) > 2:
        x = int(sys.argv[1])
        y = int(sys.argv[2])   
    else:
        x = int(sys.argv[1])
        y = int(input())
    
    print(x * y) 


if __name__ == '__main__':
    multiply()
