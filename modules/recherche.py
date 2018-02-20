def posRel(face):
	"""Fonction renvoyant la position des faces autour de 'face' puis des indices -> [[face, indice1,indice2,indice3],...]
	La position de ces dernières est renvoyée selon le modèle Haut / Droite / Bas / Gauche / Dernière
	Les indices se lisent dans le sens de la lecture"""

	if face==0:
		return [[4,0,3,6],[1,0,3,6],[5,6,3,0],[3,2,5,8],2]
	elif face==1:
		return [[4,6,7,8],[2,0,3,6],[5,0,1,2],[0,2,5,8],3]
	elif face==2:
		return [[4,8,5,2],[3,0,3,6],[5,2,5,8],[1,2,5,8],0]
	elif face==3:
		return [[4,2,1,0],[0,0,3,6],[5,8,7,6],[2,2,5,8],1]
	elif face==4:
		return [[3,2,1,0],[2,2,1,0],[1,0,1,2],[0,0,1,2],5]
	elif face==5:
		return [[1,6,7,8],[2,6,7,8],[3,8,7,6],[0,8,7,6],4]

def boussole(sensChiffre):
	"""Fonction servant à conserver les chiffres entre 0 et 3 afin que ces derniers suivent le modèle
	d'une boussole."""

	if sensChiffre<0:
		while sensChiffre<0:
			sensChiffre+=4
	elif sensChiffre>3:
		while sensChiffre>3:
			sensChiffre-=4
	return sensChiffre

def reconnaissanceDirection(sensChiffre):
	"""On donne un chiffre et la fonction renvoit la direction associé selon le modèle d'une boussole"""

	sensChiffre=boussole(sensChiffre)
	if sensChiffre==0:
		return "haut"
	elif sensChiffre==1:
		return "droite"
	elif sensChiffre==2:
		return "bas"
	elif sensChiffre==3:
		return "gauche"

def deReconnaissanceDirection(sens):
	"""On donne une direction et la fonction renvoit le chiffre associé selon le modèle d'une boussole"""

	if sens=="haut":
		return 0
	elif sens=="droite":
		return 1
	elif sens=="bas":
		return 2
	elif sens=="gauche":
		return 3

def arreteOppose(indice):
	"""On donne l'indice d'une arrête, l'indice opposé nous est renvoyé"""

	if indice==1:
		return 7
	elif indice==5:
		return 3
	elif indice==7:
		return 1
	elif indice==3:
		return 5

def findCoin(cube,can,coul,coul2,coul3):
	"""Fonction servant à obtenir la position d'un coin selon les couleurs de ce dernier"""

	for face in range(6):
		if coul == cube[face][0]:
			possible=[ cube[posRel(face)[0][0]][posRel(face)[0][1]], cube[posRel(face)[3][0]][posRel(face)[3][1]] ]
			if coul2 in possible and coul3 in possible:
				return [face,0]

		if coul == cube[face][2]:
			possible=[cube[posRel(face)[0][0]][posRel(face)[0][3]], cube[posRel(face)[1][0]][posRel(face)[1][1]]]
			if coul2 in possible and coul3 in possible:
				return [face,2]

		if coul == cube[face][8]:
			possible=[cube[posRel(face)[2][0]][posRel(face)[2][3]], cube[posRel(face)[1][0]][posRel(face)[1][3]]]
			if coul2 in possible and coul3 in possible:
				return [face,8]

		if coul == cube[face][6]:
			possible=[cube[posRel(face)[2][0]][posRel(face)[2][1]], cube[posRel(face)[3][0]][posRel(face)[3][3]]]
			if coul2 in possible and coul3 in possible:
				return [face,6]

def findArrete(cube,can,coul,coul2):
	"""Fonction servant à obtenir la position d'une arrête selon les couleurs de cette dernière"""

	for face in range(6):
		if coul == cube[face][1] and coul2 == cube[posRel(face)[0][0]] [posRel(face)[0][2]]:
			return [face,1]

		if coul == cube[face][5] and coul2 == cube[posRel(face)[1][0]][posRel(face)[1][2]]:
			return [face,5]

		if coul == cube[face][7] and coul2 == cube[posRel(face)[2][0]][posRel(face)[2][2]]:
			return [face,7]

		if coul == cube[face][3] and coul2 == cube[posRel(face)[3][0]][posRel(face)[3][2]]:
			return [face,3]

def findFace(cube,can,coul):
	"""Fonction servant à obtenir la position d'une face, qui est alors associé à la couleur d'un carré central"""

	for face in range(6):
		if coul == cube[face][4]:
			return face