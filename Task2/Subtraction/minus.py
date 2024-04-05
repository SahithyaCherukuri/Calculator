import sys


def minus():
    if len(sys.argv) > 2:
        x = int(sys.argv[1])
        y = int(sys.argv[2])   
    else:
        y = int(sys.argv[1])
        x = int(input())
    
    print(x - y) 



if __name__ == '__main__':
    minus()
