from time import sleep
import sys
from termcolor import colored
import argparse




def stoa(name):
    with open(name, 'r') as ppm:
        data = ppm.read()
    data = data.split("\n")
    return (data)

def str_m(str, fonts = "big"):
    res = []
    for l in str:
        res.append(stoa(f"fonts/{fonts}/{ord(l)}.txt"))
    return (res)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("str", help="blabla", type=str, action="store")
    parser.add_argument("-f", "--fonts", help="blabla", type=str, action="store")
    parser.add_argument("-r", "--rainbow", help="blabla", action="store_true")
    args = parser.parse_args()
    string = str_m(args.str, args.fonts)
    c = -1
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta", "grey","white"]
    for i in range(len(string[0])-1):
        c += 1
        for j in range(len(string)):
            if (args.rainbow):         
                print(colored(string[j][i], colors[c]), end="")
            else:
                print(string[j][i], end="")
            #sys.stdout.flush()
        sleep(0.1)
        print('\r')
