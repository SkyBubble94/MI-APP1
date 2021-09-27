from time import sleep
import sys
from termcolor import colored, cprint
from random import randint

def stoa(name):
    with open(name, 'r') as ppm:
        data = ppm.read()
    data = data.split("\n")
    return (data)

string = [stoa("p/s.txt"), stoa("p/a.txt"), stoa("p/l.txt")]
c = -1
for i in range(len(string[0])-1):
    c +=1
    for j in range(len(string)):
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta", "white"]
        print(colored(string[j][i], colors[c]), end = "")
        
        sys.stdout.flush()
    sleep(0.05)
    print('\r')




