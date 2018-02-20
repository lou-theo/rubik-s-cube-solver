from random import *
from modules.affichage import *
from modules.recherche import *
from time import *


def start():
	"""Cette fonction sert à initialiser la variable globale 'compteur' qui va par la suite gérer le temps"""

	wFile("compteur","cub",0)

def melangeur(cube,can,nombre):
	"""Cette fonction sert à mélanger de manière aléatoire le cube un nombre n de fois, n étant défini par le paramètre 'nombre'"""

	for i in range(nombre):
		can.after(i*rFile("timeur","cub"),lambda:rotation(cube,can,randint(0,5),choice(["droite","gauche"])))

def rotative(cube,can,face,faceSup,norme):
	"""La fonction 'rotative' normalise les différentes fonctions qui gère les mouvements dans le cube.
	La fonction a également la notion du temps, pour cela elle s'aide de la variable globale 'compteur'"""

	compteur=rFile("compteur","cub")
	wFile("compteur","cub",compteur+1)

	if norme.upper()=="U":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationHaut(cube,can,face,faceSup,"gauche"))
	elif norme.upper()=="U'":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationHaut(cube,can,face,faceSup,"droite"))
	elif norme.upper()=="L":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationGauche(cube,can,face,faceSup,"bas"))
	elif norme.upper()=="L'":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationGauche(cube,can,face,faceSup,"haut"))
	elif norme.upper()=="F":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotation(cube,can,face,"droite"))
	elif norme.upper()=="F'":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotation(cube,can,face,"gauche"))
	elif norme.upper()=="R":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationDroite(cube,can,face,faceSup,"haut"))
	elif norme.upper()=="R'":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationDroite(cube,can,face,faceSup,"bas"))
	elif norme.upper()=="D":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationBas(cube,can,face,faceSup,"droite"))
	elif norme.upper()=="D'":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:rotationBas(cube,can,face,faceSup,"gauche"))
	elif norme.upper()=="M":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:axe(cube,can,face,faceSup,"bas"))
	elif norme.upper()=="M'":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:axe(cube,can,face,faceSup,"haut"))
	elif norme.upper()=="E":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:axe(cube,can,face,faceSup,"droite"))
	elif norme.upper()=="E'":
		can.after(rFile("compteur","cub")*rFile("timeur","cub"),lambda:axe(cube,can,face,faceSup,"gauche"))

def rotativeUser(cube,can,face,faceSup,norme):
	"""La fonction 'rotaitveUser' est identique à la fonction 'rotative', la gestion du temps en moins.
	Cela est donc pratique pour effectuer des mouvements instantanés"""

	if norme.upper()=="U":
		rotationHaut(cube,can,face,faceSup,"gauche")
	elif norme.upper()=="U'":
		rotationHaut(cube,can,face,faceSup,"droite")
	elif norme.upper()=="L":
		rotationGauche(cube,can,face,faceSup,"bas")
	elif norme.upper()=="L'":
		rotationGauche(cube,can,face,faceSup,"haut")
	elif norme.upper()=="F":
		rotation(cube,can,face,"droite")
	elif norme.upper()=="F'":
		rotation(cube,can,face,"gauche")
	elif norme.upper()=="R":
		rotationDroite(cube,can,face,faceSup,"haut")
	elif norme.upper()=="R'":
		rotationDroite(cube,can,face,faceSup,"bas")
	elif norme.upper()=="D":
		rotationBas(cube,can,face,faceSup,"droite")
	elif norme.upper()=="D'":
		rotationBas(cube,can,face,faceSup,"gauche")
	elif norme.upper()=="M":
		axe(cube,can,face,faceSup,"bas")
	elif norme.upper()=="M'":
		axe(cube,can,face,faceSup,"haut")
	elif norme.upper()=="E":
		axe(cube,can,face,faceSup,"droite")
	elif norme.upper()=="E'":
		axe(cube,can,face,faceSup,"gauche")

def rotation(cube,can,face,sens):
	"""Fonction gérant la rotation d'une face.
	Correspond au mouvement F si sens = droite / F' si sens = gauche"""

	if sens=="droite":
		cube[face][0], cube[face][1], cube[face][2], cube[face][5], cube[face][8], cube[face][7], cube[face][6], cube[face][3] \
		= cube[face][6], cube[face][3], cube[face][0], cube[face][1], cube[face][2], cube[face][5], cube[face][8], cube[face][7]

		pos=posRel(face)

		cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]], \
		cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], \
		cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]], \
		cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]] \
		= cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]], \
		cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]], \
		cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], \
		cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]]

	elif sens=="gauche":
		cube[face][0], cube[face][1], cube[face][2], cube[face][5], cube[face][8], cube[face][7], cube[face][6], cube[face][3] \
		= cube[face][2],cube[face][5],cube[face][8],cube[face][7],cube[face][6],cube[face][3],cube[face][0],cube[face][1]

		pos=posRel(face)

		cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]], \
		cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], \
		cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]], \
		cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]] \
		= cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], \
		cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]], \
		cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]], \
		cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]]

	actualise(cube,can)

def rotationHaut(cube,can,face,faceSup,sens):
	"""Fonction se basant sur la fonction 'rotation' afin de permettre un autre mouvement.
	Correspond au mouvement U si sens = gauche / U' si sens = droite"""

	if sens=="gauche":
		rotation(cube,can,faceSup,"droite")
	elif sens=="droite":
		rotation(cube,can,faceSup,"gauche")

def rotationBas(cube,can,face,faceSup,sens):
	"""Fonction se basant sur la fonction 'rotation' afin de permettre un autre mouvement.
	Correspond au mouvement D si sens = droite / D' si sens = gauche"""

	faceBas=posRel(faceSup)[4]
	rotation(cube,can,faceBas,sens)

def rotationDroite(cube,can,face,faceSup,sens):
	"""Fonction se basant sur la fonction 'rotation' afin de permettre un autre mouvement.
	Correspond au mouvement R si sens = haut / R' si sens = bas"""

	pos=posRel(face)
	for i in range(4):
		if pos[i][0]==faceSup:
			supChiffre=i
	faceDroite=posRel(face)[boussole(supChiffre+1)][0]

	if sens=="haut":
		rotation(cube,can,faceDroite,"droite")
	elif sens=="bas":
		rotation(cube,can,faceDroite,"gauche")

def rotationGauche(cube,can,face,faceSup,sens):
	"""Fonction se basant sur la fonction 'rotation' afin de permettre un autre mouvement.
	Correspond au mouvement L si sens = bas / L' si sens = haut"""
	
	pos=posRel(face)
	for i in range(4):
		if pos[i][0]==faceSup:
			supChiffre=i
	faceDroite=posRel(face)[boussole(supChiffre-1)][0]
	
	if sens=="haut":
		rotation(cube,can,faceDroite,"gauche")
	elif sens=="bas":
		rotation(cube,can,faceDroite,"droite")

def axe(cube,can,face,faceSup,sens):
	"""Focntion gérant la rotation des axes du cube
	Correspond au mouvement M si sens = bas / M' si sens = haut
							E si sens = droite / E' si sens = gauche"""

	sensGlobal=[]
	pos=posRel(face)
	for i in range(4):
		if pos[i][0]==faceSup:
			sensChiffre=i

	sens=int(deReconnaissanceDirection(sens))
	sensGlobal=reconnaissanceDirection(sensChiffre+sens)

	if sensGlobal=="haut":
		cube[face][1], cube[face][4], cube[face][7], \
		cube[posRel(face)[2][0]][posRel(face)[2][2]], cube[posRel(face)[2][0]][4], cube[posRel(face)[2][0]][arreteOppose(posRel(face)[2][2])], \
		cube[posRel(face)[4]][7], cube[posRel(face)[4]][4], cube[posRel(face)[4]][1], \
		cube[posRel(face)[0][0]][arreteOppose(posRel(face)[0][2])], cube[posRel(face)[0][0]][4], cube[posRel(face)[0][0]][posRel(face)[0][2]] \
		= cube[posRel(face)[2][0]][posRel(face)[2][2]], cube[posRel(face)[2][0]][4], cube[posRel(face)[2][0]][arreteOppose(posRel(face)[2][2])], \
		cube[posRel(face)[4]][7], cube[posRel(face)[4]][4], cube[posRel(face)[4]][1], \
		cube[posRel(face)[0][0]][arreteOppose(posRel(face)[0][2])], cube[posRel(face)[0][0]][4], cube[posRel(face)[0][0]][posRel(face)[0][2]], \
		cube[face][1], cube[face][4], cube[face][7]

	elif sensGlobal=="droite":
		cube[face][3], cube[face][4], cube[face][5], \
		cube[posRel(face)[1][0]][posRel(face)[1][2]], cube[posRel(face)[1][0]][4], cube[posRel(face)[1][0]][arreteOppose(posRel(face)[1][2])], \
		cube[posRel(face)[4]][3], cube[posRel(face)[4]][4], cube[posRel(face)[4]][5], \
		cube[posRel(face)[3][0]][arreteOppose(posRel(face)[3][2])], cube[posRel(face)[3][0]][4], cube[posRel(face)[3][0]][posRel(face)[3][2]] \
		= cube[posRel(face)[3][0]][arreteOppose(posRel(face)[3][2])], cube[posRel(face)[3][0]][4], cube[posRel(face)[3][0]][posRel(face)[3][2]], \
		cube[face][3], cube[face][4], cube[face][5], \
		cube[posRel(face)[1][0]][posRel(face)[1][2]], cube[posRel(face)[1][0]][4], cube[posRel(face)[1][0]][arreteOppose(posRel(face)[1][2])], \
		cube[posRel(face)[4]][3], cube[posRel(face)[4]][4], cube[posRel(face)[4]][5]
	
	elif sensGlobal=="gauche":
		cube[face][3], cube[face][4], cube[face][5], \
		cube[posRel(face)[1][0]][posRel(face)[1][2]], cube[posRel(face)[1][0]][4], cube[posRel(face)[1][0]][arreteOppose(posRel(face)[1][2])], \
		cube[posRel(face)[4]][3], cube[posRel(face)[4]][4], cube[posRel(face)[4]][5], \
		cube[posRel(face)[3][0]][arreteOppose(posRel(face)[3][2])], cube[posRel(face)[3][0]][4], cube[posRel(face)[3][0]][posRel(face)[3][2]] \
		= cube[posRel(face)[1][0]][posRel(face)[1][2]], cube[posRel(face)[1][0]][4], cube[posRel(face)[1][0]][arreteOppose(posRel(face)[1][2])], \
		cube[posRel(face)[4]][3], cube[posRel(face)[4]][4], cube[posRel(face)[4]][5], \
		cube[posRel(face)[3][0]][arreteOppose(posRel(face)[3][2])], cube[posRel(face)[3][0]][4], cube[posRel(face)[3][0]][posRel(face)[3][2]], \
		cube[face][3], cube[face][4], cube[face][5]
	
	elif sensGlobal=="bas":
		cube[face][1], cube[face][4], cube[face][7], \
		cube[posRel(face)[2][0]][posRel(face)[2][2]], cube[posRel(face)[2][0]][4], cube[posRel(face)[2][0]][arreteOppose(posRel(face)[2][2])], \
		cube[posRel(face)[4]][7], cube[posRel(face)[4]][4], cube[posRel(face)[4]][1], \
		cube[posRel(face)[0][0]][arreteOppose(posRel(face)[0][2])], cube[posRel(face)[0][0]][4], cube[posRel(face)[0][0]][posRel(face)[0][2]] \
		= cube[posRel(face)[0][0]][arreteOppose(posRel(face)[0][2])], cube[posRel(face)[0][0]][4], cube[posRel(face)[0][0]][posRel(face)[0][2]], \
		cube[face][1], cube[face][4], cube[face][7], \
		cube[posRel(face)[2][0]][posRel(face)[2][2]], cube[posRel(face)[2][0]][4], cube[posRel(face)[2][0]][arreteOppose(posRel(face)[2][2])], \
		cube[posRel(face)[4]][7], cube[posRel(face)[4]][4], cube[posRel(face)[4]][1]

	actualise(cube,can)