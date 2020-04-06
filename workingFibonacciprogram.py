#!/usr/bin/python3

import argparse
import os.path



def Fibonacci(a, path):
    if os.path.isfile(path):
        raise ValueError("This file already exsists")
    try:
        file = open(path, "w")

        x, b = 0, 1
        file.write("\n" + str(x))
        for i in range(a):
            x, b = b, x + b
            file.write("\n" + str(x))

        return x


        print("Written to file \"" + path + "\"")
        file.close()
    except IOError:
        print("Error writing to file")

def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-n", help="the input for the program should be a positive integer.", type=int)
    parser.add_argument('-n', metavar='size', type=str, nargs="+", help="Sequence number in fibonacci sequence")
    parser.add_argument('-f', metavar='Filename', type=str, nargs="+", help="this argument is for writing a file")
    args = parser.parse_args()
    args.n[0] = int(args.n[0])


    path = args.f[0]
    result =  Fibonacci(args.n[0], path)
 # result = Fibonacci(args.n[0])
    print ("The Fibonacci sequence upto "+str(args.n[0])+" is "+str(result))

if __name__ == '__main__':
    main()



