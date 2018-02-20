from tkinter import *
from modules.mouvements import *
from modules.recherche import *
from modules.gestionnaire import *

def resoudre(cube,can):
	etape1(cube,can)
	etape2(cube,can)
	etape3(cube,can)

def coinPos(numero):
	if numero == 1:
		return [[4,6],[0,2],[1,0]]
	if numero == 2:
		return [[4,0],[3,2],[0,0]]
	if numero == 3:
		return [[4,2],[2,2],[3,0]]
	if numero == 4:
		return [[4,8],[1,2],[2,0]]
	if numero == 5:
		return [[5,0],[1,6],[0,8]]
	if numero == 6:
		return [[5,6],[0,6],[3,8]]
	if numero == 7:
		return [[5,8],[3,6],[2,8]]
	if numero == 8:
		return [[5,2],[2,6],[1,8]]

def etape1(cube,can):
	ordre = [etape1Pos(cube,coinPos(4)), etape1Pos(cube,coinPos(3)), etape1Pos(cube,coinPos(2)), etape1Pos(cube,coinPos(8)), \
	etape1Pos(cube,coinPos(7)), etape1Pos(cube,coinPos(6)), etape1Pos(cube,coinPos(5))]

	etape1Formule(cube,can,ordre[0])

	rotative(cube,can,2,4,"f'")
	etape1Formule(cube,can,ordre[1])
	rotative(cube,can,2,4,"f")

	rotative(cube,can,2,4,"r'")
	rotative(cube,can,2,4,"f'")
	etape1Formule(cube,can,ordre[2])
	rotative(cube,can,2,4,"f")
	rotative(cube,can,2,4,"r")
	
	rotative(cube,can,2,4,"f")
	etape1Formule(cube,can,ordre[3])
	rotative(cube,can,2,4,"f'")

	rotative(cube,can,2,4,"f")
	rotative(cube,can,2,4,"f")
	etape1Formule(cube,can,ordre[4])
	rotative(cube,can,2,4,"f'")
	rotative(cube,can,2,4,"f'")

	rotative(cube,can,2,4,"d'")
	rotative(cube,can,2,4,"f")
	rotative(cube,can,2,4,"f")
	etape1Formule(cube,can,ordre[5])
	rotative(cube,can,2,4,"f'")
	rotative(cube,can,2,4,"f'")
	rotative(cube,can,2,4,"d")

	rotative(cube,can,2,4,"d")
	rotative(cube,can,2,4,"f")
	etape1Formule(cube,can,ordre[6])
	rotative(cube,can,2,4,"f'")
	rotative(cube,can,2,4,"d'")

def etape1Pos(cube,coin):
	if cube[coin[0][0]][coin[0][1]] == "white" or cube[coin[0][0]][coin[0][1]] == "yellow":
		return "o"
	if cube[coin[1][0]][coin[1][1]] == "white" or cube[coin[1][0]][coin[1][1]] == "yellow":
		return "c"
	if cube[coin[2][0]][coin[2][1]] == "white" or cube[coin[2][0]][coin[2][1]] == "yellow":
		return "a"

def etape1Formule(cube,can,formule):
	if formule == "a":
		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r'")
		rotative(cube,can,5,2,"u'")

		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r'")
		rotative(cube,can,5,2,"u'")
		rotative(cube,can,5,2,"l")

		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u'")
		rotative(cube,can,5,2,"r'")

		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u'")
		rotative(cube,can,5,2,"r'")
		rotative(cube,can,5,2,"l'")

	if formule == "c":
		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u'")
		rotative(cube,can,5,2,"r'")

		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u'")
		rotative(cube,can,5,2,"r'")
		rotative(cube,can,5,2,"l")

		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r'")
		rotative(cube,can,5,2,"u'")

		rotative(cube,can,5,2,"r")
		rotative(cube,can,5,2,"u")
		rotative(cube,can,5,2,"r'")
		rotative(cube,can,5,2,"u'")
		rotative(cube,can,5,2,"l'")

def coinCouleur(coul1,coul2,coul3):
	if coul1 in ["white","red","green"] and coul2 in ["white","red","green"]  and coul3 in ["white","red","green"]:
		return 1
	if coul1 in ["white","orange","green"] and coul2 in ["white","orange","green"]  and coul3 in ["white","orange","green"]:
		return 2
	if coul1 in ["white","orange","blue"] and coul2 in ["white","orange","blue"]  and coul3 in ["white","orange","blue"]:
		return 3
	if coul1 in ["white","red","blue"] and coul2 in ["white","red","blue"]  and coul3 in ["white","red","blue"]:
		return 4
	if coul1 in ["yellow","red","green"] and coul2 in ["yellow","red","green"]  and coul3 in ["yellow","red","green"]:
		return 5
	if coul1 in ["yellow","orange","green"] and coul2 in ["yellow","orange","green"]  and coul3 in ["yellow","orange","green"]:
		return 6
	if coul1 in ["yellow","orange","blue"] and coul2 in ["yellow","orange","blue"]  and coul3 in ["yellow","orange","blue"]:
		return 7
	if coul1 in ["yellow","red","blue"] and coul2 in ["yellow","red","blue"]  and coul3 in ["yellow","red","blue"]:
		return 8

def etape2(cube,can):
	ordre=[coinCouleur(cube[coinPos(2)[0][0]][coinPos(2)[0][1]], cube[coinPos(2)[1][0]][coinPos(2)[1][1]], \
	 cube[coinPos(2)[2][0]][coinPos(2)[2][1]])]

	while ordre[-1] != 2:
		ordre += [coinCouleur(cube[coinPos(ordre[-1])[0][0]][coinPos(ordre[-1])[0][1]], \
		 cube[coinPos(ordre[-1])[1][0]][coinPos(ordre[-1])[1][1]], cube[coinPos(ordre[-1])[2][0]][coinPos(ordre[-1])[2][1]])]

	ordre.remove(2)

	complet=[1,3,4,5,6,7,8]

	for i in ordre:
		if i in complet:
				complet.remove(i)

	complet = etape2Verif(cube,complet)

	while complet != []:
		debut=complet[0]
		ordre+=[coinCouleur(cube[coinPos(debut)[0][0]][coinPos(debut)[0][1]], cube[coinPos(debut)[1][0]][coinPos(debut)[1][1]], \
		 cube[coinPos(debut)[2][0]][coinPos(debut)[2][1]])]

		premier = [coinCouleur(cube[coinPos(debut)[0][0]][coinPos(debut)[0][1]], cube[coinPos(debut)[1][0]][coinPos(debut)[1][1]], \
		 cube[coinPos(debut)[2][0]][coinPos(debut)[2][1]])]

		while ordre[-1] != debut:
			ordre += [coinCouleur(cube[coinPos(ordre[-1])[0][0]][coinPos(ordre[-1])[0][1]], \
			 cube[coinPos(ordre[-1])[1][0]][coinPos(ordre[-1])[1][1]], cube[coinPos(ordre[-1])[2][0]][coinPos(ordre[-1])[2][1]])]
		ordre+=premier

		for i in ordre:
			if i in complet:
				complet.remove(i)

	if len(ordre)%2 != 0:
		ordre+=[3]

	for formule in ordre:
		etape2Formule(cube,can,formule)

def etape2Verif(cube,complet):
	if coinCouleur(cube[coinPos(1)[0][0]][coinPos(1)[0][1]], cube[coinPos(1)[1][0]][coinPos(1)[1][1]], \
	 cube[coinPos(1)[2][0]][coinPos(1)[2][1]])==1:
		complet.remove(1)
	if coinCouleur(cube[coinPos(3)[0][0]][coinPos(3)[0][1]], cube[coinPos(3)[1][0]][coinPos(3)[1][1]], \
	 cube[coinPos(3)[2][0]][coinPos(3)[2][1]])==3:
		complet.remove(3)
	if coinCouleur(cube[coinPos(4)[0][0]][coinPos(4)[0][1]], cube[coinPos(4)[1][0]][coinPos(4)[1][1]], \
	 cube[coinPos(4)[2][0]][coinPos(4)[2][1]])==4:
		complet.remove(4)
	if coinCouleur(cube[coinPos(5)[0][0]][coinPos(5)[0][1]], cube[coinPos(5)[1][0]][coinPos(5)[1][1]], \
	 cube[coinPos(5)[2][0]][coinPos(5)[2][1]])==5:
		complet.remove(5)
	if coinCouleur(cube[coinPos(6)[0][0]][coinPos(6)[0][1]], cube[coinPos(6)[1][0]][coinPos(6)[1][1]], \
	 cube[coinPos(6)[2][0]][coinPos(6)[2][1]])==6:
		complet.remove(6)
	if coinCouleur(cube[coinPos(7)[0][0]][coinPos(7)[0][1]], cube[coinPos(7)[1][0]][coinPos(7)[1][1]], \
	 cube[coinPos(7)[2][0]][coinPos(7)[2][1]])==7:
		complet.remove(7)
	if coinCouleur(cube[coinPos(8)[0][0]][coinPos(8)[0][1]], cube[coinPos(8)[1][0]][coinPos(8)[1][1]], \
	 cube[coinPos(8)[2][0]][coinPos(8)[2][1]])==8:
		complet.remove(8)
	return complet

def etape2DatFormule(cube,can):
	rotative(cube,can,2,4,"l")
	rotative(cube,can,2,4,"u'")
	rotative(cube,can,2,4,"r'")
	rotative(cube,can,2,4,"u")

	rotative(cube,can,2,4,"l'")
	rotative(cube,can,2,4,"u")
	rotative(cube,can,2,4,"u")
	rotative(cube,can,2,4,"r")
	rotative(cube,can,2,4,"u'")

	rotative(cube,can,2,4,"r'")
	rotative(cube,can,2,4,"u")
	rotative(cube,can,2,4,"u")
	rotative(cube,can,2,4,"r")

def etape2Formule(cube,can,formule):
	if formule == 1:
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		etape2DatFormule(cube,can)
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")

	if formule == 3:
		etape2DatFormule(cube,can)

	if formule == 4:
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		etape2DatFormule(cube,can)
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")

	if formule == 5:
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		etape2DatFormule(cube,can)
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"d'")

	if formule == 6:
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		etape2DatFormule(cube,can)
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"d'")

	if formule == 7:
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		etape2DatFormule(cube,can)
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"d")

	if formule == 8:
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")
		etape2DatFormule(cube,can)
		rotative(cube,can,2,4,"f'")
		rotative(cube,can,2,4,"f'")

def arretePos(lettre):
	if lettre == "a":
		return [[4,3],[0,1]]
	if lettre == "b":
		return [[0,1],[4,3]]
	if lettre == "c":
		return [[4,1],[3,1]]
	if lettre == "d":
		return [[3,1],[4,1]]
	if lettre == "e":
		return [[4,5],[2,1]]
	if lettre == "f":
		return [[2,1],[4,5]]
	if lettre == "g":
		return [[4,7],[1,1]]
	if lettre == "h":
		return [[1,1],[4,7]]
	if lettre == "i":
		return [[1,3],[0,5]]
	if lettre == "j":
		return [[0,5],[1,3]]
	if lettre == "k":
		return [[0,3],[3,5]]
	if lettre == "l":
		return [[3,5],[0,3]]
	if lettre == "m":
		return [[3,3],[2,5]]
	if lettre == "n":
		return [[2,5],[3,3]]
	if lettre == "o":
		return [[2,3],[1,5]]
	if lettre == "p":
		return [[1,5],[2,3]]
	if lettre == "q":
		return [[0,7],[5,3]]
	if lettre == "r":
		return [[5,3],[0,7]]
	if lettre == "s":
		return [[3,7],[5,7]]
	if lettre == "t":
		return [[5,7],[3,7]]
	if lettre == "u":
		return [[2,7],[5,5]]
	if lettre == "v":
		return [[5,5],[2,7]]
	if lettre == "w":
		return [[1,7],[5,1]]
	if lettre == "x":
		return [[5,1],[1,7]]

def arreteCouleur(coul1,coul2):
	if coul1 == "white" and coul2 == "green":
		return "a"
	if coul1 == "green" and coul2 == "white":
		return "b"
	if coul1 == "white" and coul2 == "orange":
		return "c"
	if coul1 == "orange" and coul2 == "white":
		return "d"
	if coul1 == "white" and coul2 == "blue":
		return "e"
	if coul1 == "blue" and coul2 == "white":
		return "f"
	if coul1 == "white" and coul2 == "red":
		return "g"
	if coul1 == "red" and coul2 == "white":
		return "h"
	if coul1 == "red" and coul2 == "green":
		return "i"
	if coul1 == "green" and coul2 == "red":
		return "j"
	if coul1 == "green" and coul2 == "orange":
		return "k"
	if coul1 == "orange" and coul2 == "green":
		return "l"
	if coul1 == "orange" and coul2 == "blue":
		return "m"
	if coul1 == "blue" and coul2 == "orange":
		return "n"
	if coul1 == "blue" and coul2 == "red":
		return "o"
	if coul1 == "red" and coul2 == "blue":
		return "p"
	if coul1 == "green" and coul2 == "yellow":
		return "q"
	if coul1 == "yellow" and coul2 == "green":
		return "r"
	if coul1 == "orange" and coul2 == "yellow":
		return "s"
	if coul1 == "yellow" and coul2 == "orange":
		return "t"
	if coul1 == "blue" and coul2 == "yellow":
		return "u"
	if coul1 == "yellow" and coul2 == "blue":
		return "v"
	if coul1 == "red" and coul2 == "yellow":
		return "w"
	if coul1 == "yellow" and coul2 == "red":
		return "x"

def etape3(cube,can):

	ordre=[arreteCouleur(cube[arretePos("c")[0][0]][arretePos("c")[0][1]], cube[arretePos("c")[1][0]][arretePos("c")[1][1]])]

	while ordre[-1] not in ("c","d"):
		ordre += [arreteCouleur(cube[arretePos(ordre[-1])[0][0]][arretePos(ordre[-1])[0][1]], \
			cube[arretePos(ordre[-1])[1][0]][arretePos(ordre[-1])[1][1]])]

	if "c" in ordre:
		ordre.remove("c")
	if "d" in ordre:
		ordre.remove("d")

	complet=["a","b","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]

	for i in ordre:
		if i in complet:
			complet.remove(i)
		if binome(i) in complet:
			complet.remove(binome(i))

	complet = etape3Verif(cube,complet)

	while complet != []:
		debut=complet[0]
		ordre += [arreteCouleur(cube[arretePos(debut)[0][0]][arretePos(debut)[0][1]], \
			cube[arretePos(debut)[1][0]][arretePos(debut)[1][1]])]

		premier = [arreteCouleur(cube[arretePos(debut)[0][0]][arretePos(debut)[0][1]], \
			cube[arretePos(debut)[1][0]][arretePos(debut)[1][1]])]

		while ordre[-1] not in(debut,binome(debut)):
			ordre += [arreteCouleur(cube[arretePos(ordre[-1])[0][0]][arretePos(ordre[-1])[0][1]], \
			cube[arretePos(ordre[-1])[1][0]][arretePos(ordre[-1])[1][1]])]
		if 	ordre[-1] == debut:
			ordre += premier
		elif ordre[-1] == binome(debut):
			ordre += [binome(premier[0])]

		for i in ordre:
			if i in complet:
				complet.remove(i)
			if binome(i) in complet:
				complet.remove(binome(i))

	for formule in ordre:
		etape3Formule(cube,can,formule)

def etape3Verif(cube,complet):
	if arreteCouleur(cube[arretePos("a")[0][0]][arretePos("a")[0][1]], cube[arretePos("a")[1][0]][arretePos("a")[1][1]])=="a":
		complet.remove("a")
	if arreteCouleur(cube[arretePos("b")[0][0]][arretePos("b")[0][1]], cube[arretePos("b")[1][0]][arretePos("b")[1][1]])=="b":
		complet.remove("b")
	if arreteCouleur(cube[arretePos("e")[0][0]][arretePos("e")[0][1]], cube[arretePos("e")[1][0]][arretePos("e")[1][1]])=="e":
		complet.remove("e")
	if arreteCouleur(cube[arretePos("f")[0][0]][arretePos("f")[0][1]], cube[arretePos("f")[1][0]][arretePos("f")[1][1]])=="f":
		complet.remove("f")
	if arreteCouleur(cube[arretePos("g")[0][0]][arretePos("g")[0][1]], cube[arretePos("g")[1][0]][arretePos("g")[1][1]])=="g":
		complet.remove("g")
	if arreteCouleur(cube[arretePos("h")[0][0]][arretePos("h")[0][1]], cube[arretePos("h")[1][0]][arretePos("h")[1][1]])=="h":
		complet.remove("h")
	if arreteCouleur(cube[arretePos("i")[0][0]][arretePos("i")[0][1]], cube[arretePos("i")[1][0]][arretePos("i")[1][1]])=="i":
		complet.remove("i")
	if arreteCouleur(cube[arretePos("j")[0][0]][arretePos("j")[0][1]], cube[arretePos("j")[1][0]][arretePos("j")[1][1]])=="j":
		complet.remove("j")
	if arreteCouleur(cube[arretePos("k")[0][0]][arretePos("k")[0][1]], cube[arretePos("k")[1][0]][arretePos("k")[1][1]])=="k":
		complet.remove("k")
	if arreteCouleur(cube[arretePos("l")[0][0]][arretePos("l")[0][1]], cube[arretePos("l")[1][0]][arretePos("l")[1][1]])=="l":
		complet.remove("l")
	if arreteCouleur(cube[arretePos("m")[0][0]][arretePos("m")[0][1]], cube[arretePos("m")[1][0]][arretePos("m")[1][1]])=="m":
		complet.remove("m")
	if arreteCouleur(cube[arretePos("n")[0][0]][arretePos("n")[0][1]], cube[arretePos("n")[1][0]][arretePos("n")[1][1]])=="n":
		complet.remove("n")
	if arreteCouleur(cube[arretePos("o")[0][0]][arretePos("o")[0][1]], cube[arretePos("o")[1][0]][arretePos("o")[1][1]])=="o":
		complet.remove("o")
	if arreteCouleur(cube[arretePos("p")[0][0]][arretePos("p")[0][1]], cube[arretePos("p")[1][0]][arretePos("p")[1][1]])=="p":
		complet.remove("p")
	if arreteCouleur(cube[arretePos("q")[0][0]][arretePos("q")[0][1]], cube[arretePos("q")[1][0]][arretePos("q")[1][1]])=="q":
		complet.remove("q")
	if arreteCouleur(cube[arretePos("r")[0][0]][arretePos("r")[0][1]], cube[arretePos("r")[1][0]][arretePos("r")[1][1]])=="r":
		complet.remove("r")
	if arreteCouleur(cube[arretePos("s")[0][0]][arretePos("s")[0][1]], cube[arretePos("s")[1][0]][arretePos("s")[1][1]])=="s":
		complet.remove("s")
	if arreteCouleur(cube[arretePos("t")[0][0]][arretePos("t")[0][1]], cube[arretePos("t")[1][0]][arretePos("t")[1][1]])=="t":
		complet.remove("t")
	if arreteCouleur(cube[arretePos("u")[0][0]][arretePos("u")[0][1]], cube[arretePos("u")[1][0]][arretePos("u")[1][1]])=="u":
		complet.remove("u")
	if arreteCouleur(cube[arretePos("v")[0][0]][arretePos("v")[0][1]], cube[arretePos("v")[1][0]][arretePos("v")[1][1]])=="v":
		complet.remove("v")
	if arreteCouleur(cube[arretePos("w")[0][0]][arretePos("w")[0][1]], cube[arretePos("w")[1][0]][arretePos("w")[1][1]])=="w":
		complet.remove("w")
	if arreteCouleur(cube[arretePos("x")[0][0]][arretePos("x")[0][1]], cube[arretePos("x")[1][0]][arretePos("x")[1][1]])=="x":
		complet.remove("x")

	return complet

def etape3DatFormule(cube,can):
	rotative(cube,can,2,4,"r")
	rotative(cube,can,2,4,"u")
	rotative(cube,can,2,4,"r'")
	rotative(cube,can,2,4,"u'")
	rotative(cube,can,2,4,"r'")

	rotative(cube,can,2,4,"f")
	rotative(cube,can,2,4,"r")
	rotative(cube,can,2,4,"r")
	rotative(cube,can,2,4,"u'")
	rotative(cube,can,2,4,"r'")
	rotative(cube,can,2,4,"u'")

	rotative(cube,can,2,4,"r")
	rotative(cube,can,2,4,"u")
	rotative(cube,can,2,4,"r'")
	rotative(cube,can,2,4,"f'")

def etape3Formule(cube,can,formule):
	if formule == "a": 
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"m")
		rotative(cube,can,2,4,"m")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"m'")
		rotative(cube,can,2,4,"m'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")

	if formule == "b":
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"m'")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"m")
		rotative(cube,can,2,4,"l")

	if formule == "e":
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"m'")
		rotative(cube,can,2,4,"m'")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"m")
		rotative(cube,can,2,4,"m")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")

	if formule == "f":
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"m")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"m'")
		rotative(cube,can,2,4,"l'")

	if formule == "g":
		etape3DatFormule(cube,can)

	if formule == "h":
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"m'")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"m")
		rotative(cube,can,2,4,"l")

	if formule == "i":
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"d'")

	if formule == "j":
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")

	if formule == "k":
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"d'")

	if formule == "l":
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"d'")

	if formule == "m":
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"d")

	if formule == "n":
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"d")

	if formule == "o":
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")

	if formule == "p":
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"d")

	if formule == "q":
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d'")

	if formule == "r":
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d'")

	if formule == "s":
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"d'")

	if formule == "t":
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"d'")

	if formule == "u":
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"d")

	if formule == "v":
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"d")

	if formule == "w":
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"d'")
		rotative(cube,can,2,4,"e'")
		rotative(cube,can,2,4,"l")
		etape3DatFormule(cube,can) # check
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"e")
		rotative(cube,can,2,4,"d")
		rotative(cube,can,2,4,"l")

	if formule == "x":
		rotative(cube,can,2,4,"l'")
		rotative(cube,can,2,4,"l'")
		etape3DatFormule(cube,can)
		rotative(cube,can,2,4,"l")
		rotative(cube,can,2,4,"l")

def binome(lettre):
	if lettre=="a":
		return "b"
	if lettre=="b":
		return "a"
	if lettre=="c":
		return "d"
	if lettre=="d":
		return "c"
	if lettre=="e":
		return "f"
	if lettre=="f":
		return "e"
	if lettre=="g":
		return "h"
	if lettre=="h":
		return "g"
	if lettre=="i":
		return "j"
	if lettre=="j":
		return "i"
	if lettre=="k":
		return "l"
	if lettre=="l":
		return "k"
	if lettre=="m":
		return "n"
	if lettre=="n":
		return "m"
	if lettre=="o":
		return "p"
	if lettre=="p":
		return "o"
	if lettre=="q":
		return "r"		
	if lettre=="r":
		return "q"
	if lettre=="s":
		return "t"		
	if lettre=="t":
		return "s"
	if lettre=="u":
		return "v"
	if lettre=="v":
		return "u"
	if lettre=="w":
		return "x"
	if lettre=="x":
		return "w"