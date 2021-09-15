# coding: utf-8
def parsing(file_name):
	'''
	Fonction qui permet de parser le fichier specifie en entree
	Renvoie un dictionnaire contenant :
	le format ppm du fichier ('format'),
	la hauteur de l'image ('height'),
	la largeur de l'image ('width'),
	la valeur max d'un pixel ('max') et
	un tableau de tuple contenant chaque pixel ('pixels').
	'''
	dict = {}
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
	for line in data:
		comp = list(map(int, line.split()))
		t = [tuple(comp[j:j+3]) for j in range(0, len(comp), 3)]
		for el in t:
			dict['pixels'].append(el)

	return (dict)


def hexa(n):
	'''
	Fonction qui renvoie une chaine de caractere
	representant l'entier n, entre en parametre,
	dans la base hexadecimal bb
	Précondition : 0 < n <= 255
	'''
	base = "0123456789abcdef"
	return (base[n // 16] + base[n % 16])


def hex_conversion(tuple, max):
	'''
	Fonction qui renvoie la valeur en hexadecimal
	du tuple de couleur entree en parametre en prenant
	en compte la valeur max d une couleur
	'''
	res = "#"
	for el in tuple:
		# ajout de la valeur en hexadecimale a la string total
		# en tenant compte de la valeur max possible
		if (el == 0):
			res += '00'
		else:
			res += hexa(el + (255 - max))
	return (res)


if __name__ == '__main__':

	print(parsing("F16.512.ppm"))
