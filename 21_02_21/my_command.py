import sys

def f(sting):
    print(sting)


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print(arg)