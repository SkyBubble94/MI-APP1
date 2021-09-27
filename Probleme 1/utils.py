# coding: utf-8
from random import randint
from fltk import *
from test import *

def i_filter(pixel, filtre):
	'''
	Application de filtres sur le pixel entre 
	Renvoie le pixel modifie
	'''
	if (pixel != [255, 255, 255]):
	    if (filtre == 1):
	    	# decalage de 1 vers la droite des composantes RGB (RGB -> BRG)
	        pixel[0], pixel[1], pixel[2] = pixel[1], pixel[2], pixel[0]
	    elif (filtre == 2):
	    	# decalage de 2 vers la droite des composantes RGB (RGB -> GBR)
	        pixel[0], pixel[1], pixel[2] = pixel[2], pixel[0], pixel[1]
	    elif (filtre == 3):
	    	# filtre random pixel
	    	maxi = max(pixel[0], pixel[1], pixel[2])
	    	pixel[pixel.index(maxi)] = randint(0, 205)
	    elif (filtre == 4):	    	
	    	# filtre niveau de gris
	    	v = (pixel[0] + pixel[1] + pixel[2]) // 3
	    	pixel[0], pixel[1], pixel[2] = v, v, v	    	
	return (pixel)


def affiche_image(file_name, filtre):
	'''
	Affiche l image file_name avec d eventuels filtres
	file_name doit etre une chaine de caractere
	filtre doit etre un entier
	'''
	# recuperation des donnees du fichier
	data = parsing(file_name)

	# definition de la taille de l image a afficher
	size = ((data['width'], data['height']))
	if (filtre != 0):
		for i in range(0, len(data['pixels']) - 1):
			data['pixels'][i] = i_filter(data['pixels'][i], filtre)

	# creation de la fenetre de la taille de l image
	cree_fenetre(size[1], size[0])
	pixel = 0
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			# affichage du pixel avec la couleur correspondante
			point(j, i, hex_conversion((data['pixels'][pixel]), data['max']))
			pixel += 1

	attend_ev()
	ferme_fenetre()


def slice_3(data, dict):
	'''
	Slice les lignes de data afin d'obtenir une 
	liste contenant les composantes
	RGB de chaque pixel
	(Les composantes doivent etre separees par des espace)
	data doit etre une chaine de caractere
	Renvoie le dictionnaire modifie
	'''
	for line in data:
		comp = list(map(int, line.split()))
		t = [list(comp[j:j+3]) for j in range(0, len(comp), 3)]
		dict['pixels'] += t
	return (dict)


def slice_1(data, dict):
	'''
	Slice les lignes de data afin d'obtenir une 
	liste contenant les composantes
	RGB de chaque pixel
	(Les composantes doivent etre separees par des retour a la ligne)
	data doit etre une chaine de caractere
	Renvoie le dictionnaire modifie
	'''
	for l in range(0, len(data), 3):
		dict['pixels'].append(list((int(data[l]), int(data[l + 1]), int(data[l + 2]))))


def parsing(file_name):
	'''
	Parse le fichier de nom file_name en entree
	file_name doit etre une chaine de caractere
	Renvoie un dictionnaire contenant :
	le format ppm du fichier ('format'),
	la hauteur de l'image ('height'),
	la largeur de l'image ('width'),
	la valeur max d'un pixel ('max') et
	une liste de liste contenant chaque pixel ('pixels').
	'''
	dict = {}
	try:
		with open(file_name, 'r') as ppm:
			data = ppm.read()
		# separation des donnees ligne par ligne
		# et tri des commentaires
		data = data.split('\n')
		for l in range(len(data)):
			if '#' in data[l]:
				data[l] = data[l][:data[l].index('#')]
	                        
		data = list(filter(None, data))

		dict['format'] = data.pop(0)

		# definition de la taille (hauteur et largeur)
		size = data.pop(0).split()
		dict['height'], dict['width'] = int(size[0]), int(size[1])

		# definition de la valeur max d un pixel
		dict['max'] = int(data.pop(0))

		# definition d un tableau qui stockera tous les tuples pour chaque pixel de l image
		dict['pixels'] = []
		if (len(data[0].split()) % 3 == 0):
			slice_3(data, dict)
		else:
			slice_1(data, dict)
		return (dict)
	# Si l ouverture est impossible 
	# le programme s arrete 
	except OSError:
		raise SystemExit(f"Impossible d'ouvir le fichier : {file_name}")	


def hexa(n):
	'''
	Renvoie une chaine de caractere
	representant l'entier n, entre en parametre,
	dans la base hexadecimal
	Précondition : 0 <= n <= 255
	'''
	base = "0123456789abcdef"
	return (base[n // 16] + base[n % 16])


def hex_conversion(pixel, max):
	'''
	Renvoie la valeur en hexadecimal
	du pixel entree en parametre en prenant
	en compte la valeur max d une couleur
	pixel doit etre une liste de 3 entiers
	max doit etre un entier
	'''
	res = "#"
	for el in pixel:
		# ajout de la valeur en hexadecimale a la string totale
		# en tenant compte de la valeur max possible
		if (el == 0):
			res += '00'
		else:
			res += hexa(el + (255 - max))
	return (res)


def check_affiche(file_name, filtre=0):
	'''
	Verifie si le fichier passe	en parametre est 
	dans l'extension ".ppm" et l affiche si c est
	le cas
	'''
	if (file_name[-4:] == ".ppm"):
		affiche_image(file_name, filtre)
	else:
		raise SystemExit("Format du fichier invalide")
