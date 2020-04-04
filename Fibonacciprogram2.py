import argparse

def Fibonacci(a):
    x, b = 0, 1
    for i in range(a):
        x, b = b, x+b
    return x
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="the input for the program should be a positive integer.", type=int)
    args = parser.parse_args()
    result = Fibonacci(args.output)
    print ("The Fibonacci sequence upto "+str(args.output)+"is"+str(result))
if __name__ == '__main__':
    main()



