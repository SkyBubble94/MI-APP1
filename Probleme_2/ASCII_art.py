import argparse
from termcolor import colored
from math import *


def split_file(name):
    '''
    Split le fichier 'name' avec les retours
    a la ligne
    Renvoie un tableau
    '''
    with open(name, 'r') as file:
        data = file.read()
    data = data.split("\n")
    for line in range(len(data) - 1):
        data[line] = data[line][1:]
    return (data)


def create_ascii_str(str, dico, font="big"):
    '''
    Cree une chaine de caractere en ascii art

    Chaque lettre est representee sous forme de tableau
    contenant les caraceteres necessaires a son affichage
    en ascii art
    str et font doivent etre des chaines de caractere
    dico est un dictionnaire de memoisation

    Renvoie une liste de liste
    '''
    with open(f"fonts/{font}/61.txt", 'r') as file:
        size = file.readlines()
    size = len(size)
    res = []
    for lettre in str:
        if (lettre in dico.keys()):
            res.append(dico[lettre])
        else:
            if (ord(lettre) == 32):
                temp = []
                for _ in range(size + 1):
                    temp.append(" "*(size//2))
                lettre_ascii = temp
            elif (ord(lettre) < 32 or ord(lettre) > 127):
                lettre_ascii = split_file(f"fonts/{font}/{ord('#')}.txt")
            else:
                lettre_ascii = split_file(f"fonts/{font}/{ord(lettre)}.txt")
            res.append(lettre_ascii)
            dico[lettre] = lettre_ascii
    return (res)


def print_str(string, args, number):
    '''
    Affiche la chaine de caractere en ASCII art

    string doit etre une liste de liste de caractere
    args doit etre les arguments parse par argparse
    number doit etre un entier
    '''
    size = len(string[0][0])
    space = [" "*(size)]*(len(string[0]))
    if (number > len(string)):
        number = len(string)
    c = 0
    for i in range(0, len(string[0]) - 1):
        for j in range(number):
            if ((string[j] != space or j != number)):
                if (string[j] != space or j > 0 ):
                    if (args.colors == "rainbow"):
                        print(colored(string[j][i], COLORS[c]), end="")
                    else:
                        print(colored(string[j][i], args.colors), end="")
        c += 1
        if (string[j] != space and (i <= len(string[0]) or j != 0)):
            print("\r")
    print("\r")

def main():
    '''
    Fonction principale
    '''
    memo = dict()
    fonts = ["big", "standard", "small", "mini"]
    global COLORS
    COLORS = ["red", "yellow", "green", "cyan", "blue", "magenta", "grey", "white"]

    parser = argparse.ArgumentParser(description="Programme qui permet d'écrire une chaine de caractere en ascii art")
    parser.add_argument("text", help="message à afficher", type=str, action="store")
    parser.add_argument("-f", "--font", help="permet de choisir la police utilisée", type=str, action="store", choices=fonts)
    parser.add_argument("-c", "--colors", help="permet de selectionner la couleur ", type=str, action="store", choices=["red", "yellow", "green", "cyan", "blue", "magenta", "grey", "white", "rainbow"])
    parser.add_argument("-n", "--number", help="permet de spécifier un nombre de lettre maximal à afficher par ligne", type=int, action="store")

    args = parser.parse_args()

    if (args.text):
        if (args.font in fonts):
            string = create_ascii_str(args.text, memo, args.font)
        else:
            string = create_ascii_str(args.text,memo)

        number = len(string)
        length = len(memo[args.text[0]][0])

        if (args.number and args.number < len(string) and args.number > 0):
            number = args.number

        if ((len(string) == number)):
            print_str(string, args, number)

        else:
            for a in range(ceil((len(string) / number))):
                print_str(string[a*number:], args, number)


if __name__ == "__main__":
    main()
