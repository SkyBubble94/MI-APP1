# coding: utf-8
from utils import *
import argparse

if __name__ == '__main__':
	# creation d un parser d argument 
	# et ajout de deux argu pour le nom des fichiers
	# et les differents filtres possibles
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", help="Nom des images à ouvrir. Peut contenir plusieurs noms à la suite pour une ouverture multiple.", nargs='*', type=str)
	parser.add_argument("-f", "--filter", help="Permet d'ajouter différents filtres à l'image entrée en argument (1 pour le décalage de 1, 2 pour le décalage de 2, 3 pour le random pixel, 4 pour le niveau de gris)" 
										, action="store", type=int)
	args = parser.parse_args()
	filtre = 0
	# si un chemin est entre alors on affiche l image correspondante
	if (args.filename):
		# si un filtre est entre alors on applique ce filtre a toutes
		# les images entrees en parametre
		if (args.filter):
			filtre = args.filter
		for file in args.filename:
			check_affiche(file, filtre)
	if (args.filter):
			filtre = args.filter
	while (1):		
		answer = input("Veuillez entrer un nom de fichier ou entrer 'exit' pour fermer le programme : ")
		if (not answer):
			pass
		elif (answer != "exit"):
			check_affiche(answer, filtre)
		else:
			break