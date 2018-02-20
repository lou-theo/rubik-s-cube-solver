from tkinter import *
from modules.affichage import *

def reboot(cube,can):
	"""Fonction servant à réinitialiser le cube, il est alors en position résolue"""

	newCube=[["green"]*9,["red"]*9,["blue"]*9,["orange"]*9,["white"]*9,["yellow"]*9]

	for face in range(6):
		for carre in range(9):
			cube[face][carre]=newCube[face][carre]

	actualise(cube,can)

def changeCouleur(cube,bouton,face,carre):
	"""Fonction associé à 'configurationCube', elle permet de changer la couleur de chaque carré"""

	fenetre = Tk()
	fenetre.title("Couleur")
	fenetre.iconbitmap("Rubik-Cube.ico")

	Button(fenetre, width=25, pady=5, bg=couleurAffiche("red"), text="Rouge", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"red")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("blue"), text="Bleu", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"blue")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("green"), text="Vert", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"green")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("white"), text="Blanc", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"white")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("orange"), text="Orange", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"orange")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("yellow"), text="Jaune", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"yellow")).pack()

def confirmeCouleur(fenetre,cube,bouton,face,carre,couleur):
	"""Fonction associé à 'changeCouleur', elle permet d'appliquer le choix et de fermer sa fenêtre."""

	bouton.config(bg=couleurAffiche(couleur))
	cube[face][carre]=couleur
	fenetre.destroy()

def configurationCube(cube,can,state=""):
	"""Fonction servant à l'affichage de la fenêtre permettant de rentrer une configuration personnélisée"""

	cubeConfig = Tk()
	cubeConfig.title("Configuration personnalisée")
	cubeConfig.iconbitmap("Rubik-Cube.ico")

	if state == "new":
		reboot(cube,can)


	face0 = Frame(cubeConfig, padx=5, pady=5)
	face0.grid(row=2,column=1)

	carre00 = Button(face0,bg=couleurAffiche(cube[0][0]), width=6, height=3)
	carre00.config(command=lambda:changeCouleur(cube,carre00,0,0))
	carre00.grid(row=0,column=0)

	carre01 = Button(face0,bg=couleurAffiche(cube[0][1]), width=6, height=3)
	carre01.config(command=lambda:changeCouleur(cube,carre01,0,1))
	carre01.grid(row=0,column=1)

	carre02 = Button(face0,bg=couleurAffiche(cube[0][2]), width=6, height=3)
	carre02.config(command=lambda:changeCouleur(cube,carre02,0,2))
	carre02.grid(row=0,column=2)

	carre03 = Button(face0,bg=couleurAffiche(cube[0][3]), width=6, height=3)
	carre03.config(command=lambda:changeCouleur(cube,carre03,0,3))
	carre03.grid(row=1,column=0)

	carre04 = Button(face0,bg=couleurAffiche(cube[0][4]), width=6, height=3)
	carre04.config(command=lambda:changeCouleur(cube,carre04,0,4))
	carre04.grid(row=1,column=1)

	carre05 = Button(face0,bg=couleurAffiche(cube[0][5]), width=6, height=3)
	carre05.config(command=lambda:changeCouleur(cube,carre05,0,5))
	carre05.grid(row=1,column=2)

	carre06 = Button(face0,bg=couleurAffiche(cube[0][6]), width=6, height=3)
	carre06.config(command=lambda:changeCouleur(cube,carre06,0,6))
	carre06.grid(row=2,column=0)

	carre07 = Button(face0,bg=couleurAffiche(cube[0][7]), width=6, height=3)
	carre07.config(command=lambda:changeCouleur(cube,carre07,0,7))
	carre07.grid(row=2,column=1)

	carre08 = Button(face0,bg=couleurAffiche(cube[0][8]), width=6, height=3)
	carre08.config(command=lambda:changeCouleur(cube,carre08,0,8))
	carre08.grid(row=2,column=2)


	face1 = Frame(cubeConfig, padx=5, pady=5)
	face1.grid(row=2,column=2)

	carre10 = Button(face1,bg=couleurAffiche(cube[1][0]), width=6, height=3)
	carre10.config(command=lambda:changeCouleur(cube,carre10,1,0))
	carre10.grid(row=0,column=0)	

	carre11 = Button(face1,bg=couleurAffiche(cube[1][1]), width=6, height=3)
	carre11.config(command=lambda:changeCouleur(cube,carre11,1,1))
	carre11.grid(row=0,column=1)

	carre12 = Button(face1,bg=couleurAffiche(cube[1][2]), width=6, height=3)
	carre12.config(command=lambda:changeCouleur(cube,carre12,1,2))
	carre12.grid(row=0,column=2)

	carre13 = Button(face1,bg=couleurAffiche(cube[1][3]), width=6, height=3)
	carre13.config(command=lambda:changeCouleur(cube,carre13,1,3))
	carre13.grid(row=1,column=0)

	carre14 = Button(face1,bg=couleurAffiche(cube[1][4]), width=6, height=3)
	carre14.config(command=lambda:changeCouleur(cube,carre14,1,4))
	carre14.grid(row=1,column=1)

	carre15 = Button(face1,bg=couleurAffiche(cube[1][5]), width=6, height=3)
	carre15.config(command=lambda:changeCouleur(cube,carre15,1,5))
	carre15.grid(row=1,column=2)

	carre16 = Button(face1,bg=couleurAffiche(cube[1][6]), width=6, height=3)
	carre16.config(command=lambda:changeCouleur(cube,carre16,1,6))
	carre16.grid(row=2,column=0)

	carre17 = Button(face1,bg=couleurAffiche(cube[1][7]), width=6, height=3)
	carre17.config(command=lambda:changeCouleur(cube,carre17,1,7))
	carre17.grid(row=2,column=1)

	carre18 = Button(face1,bg=couleurAffiche(cube[1][8]), width=6, height=3)
	carre18.config(command=lambda:changeCouleur(cube,carre18,1,8))
	carre18.grid(row=2,column=2)


	face2 = Frame(cubeConfig, padx=5, pady=5)
	face2.grid(row=2,column=3)

	carre20 = Button(face2,bg=couleurAffiche(cube[2][0]), width=6, height=3)
	carre20.config(command=lambda:changeCouleur(cube,carre20,2,0))
	carre20.grid(row=0,column=0)

	carre21 = Button(face2,bg=couleurAffiche(cube[2][1]), width=6, height=3)
	carre21.config(command=lambda:changeCouleur(cube,carre21,2,1))
	carre21.grid(row=0,column=1)

	carre22 = Button(face2,bg=couleurAffiche(cube[2][2]), width=6, height=3)
	carre22.config(command=lambda:changeCouleur(cube,carre22,2,2))
	carre22.grid(row=0,column=2)

	carre23 = Button(face2,bg=couleurAffiche(cube[2][3]), width=6, height=3)
	carre23.config(command=lambda:changeCouleur(cube,carre23,2,3))
	carre23.grid(row=1,column=0)

	carre24 = Button(face2,bg=couleurAffiche(cube[2][4]), width=6, height=3)
	carre24.config(command=lambda:changeCouleur(cube,carre24,2,4))
	carre24.grid(row=1,column=1)

	carre25 = Button(face2,bg=couleurAffiche(cube[2][5]), width=6, height=3)
	carre25.config(command=lambda:changeCouleur(cube,carre25,2,5))
	carre25.grid(row=1,column=2)

	carre26 = Button(face2,bg=couleurAffiche(cube[2][6]), width=6, height=3)
	carre26.config(command=lambda:changeCouleur(cube,carre26,2,6))
	carre26.grid(row=2,column=0)

	carre27 = Button(face2,bg=couleurAffiche(cube[2][7]), width=6, height=3)
	carre27.config(command=lambda:changeCouleur(cube,carre27,2,7))
	carre27.grid(row=2,column=1)

	carre28 = Button(face2,bg=couleurAffiche(cube[2][8]), width=6, height=3)
	carre28.config(command=lambda:changeCouleur(cube,carre28,2,8))
	carre28.grid(row=2,column=2)


	face3 = Frame(cubeConfig, padx=5, pady=5)
	face3.grid(row=2,column=4)

	carre30 = Button(face3,bg=couleurAffiche(cube[3][0]), width=6, height=3)
	carre30.config(command=lambda:changeCouleur(cube,carre30,3,0))
	carre30.grid(row=0,column=0)

	carre31 = Button(face3,bg=couleurAffiche(cube[3][1]), width=6, height=3)
	carre31.config(command=lambda:changeCouleur(cube,carre31,3,1))
	carre31.grid(row=0,column=1)

	carre32 = Button(face3,bg=couleurAffiche(cube[3][2]), width=6, height=3)
	carre32.config(command=lambda:changeCouleur(cube,carre32,3,2))
	carre32.grid(row=0,column=2)

	carre33 = Button(face3,bg=couleurAffiche(cube[3][3]), width=6, height=3)
	carre33.config(command=lambda:changeCouleur(cube,carre33,3,3))
	carre33.grid(row=1,column=0)

	carre34 = Button(face3,bg=couleurAffiche(cube[3][4]), width=6, height=3)
	carre34.config(command=lambda:changeCouleur(cube,carre34,3,4))
	carre34.grid(row=1,column=1)

	carre35 = Button(face3,bg=couleurAffiche(cube[3][5]), width=6, height=3)
	carre35.config(command=lambda:changeCouleur(cube,carre35,3,5))
	carre35.grid(row=1,column=2)

	carre36 = Button(face3,bg=couleurAffiche(cube[3][6]), width=6, height=3)
	carre36.config(command=lambda:changeCouleur(cube,carre36,3,6))
	carre36.grid(row=2,column=0)

	carre37 = Button(face3,bg=couleurAffiche(cube[3][7]), width=6, height=3)
	carre37.config(command=lambda:changeCouleur(cube,carre37,3,7))
	carre37.grid(row=2,column=1)

	carre38 = Button(face3,bg=couleurAffiche(cube[3][8]), width=6, height=3)
	carre38.config(command=lambda:changeCouleur(cube,carre38,3,8))
	carre38.grid(row=2,column=2)


	face4 = Frame(cubeConfig, padx=5, pady=5)
	face4.grid(row=1,column=2)

	carre40 = Button(face4,bg=couleurAffiche(cube[4][0]), width=6, height=3)
	carre40.config(command=lambda:changeCouleur(cube,carre40,4,0))
	carre40.grid(row=0,column=0)

	carre41 = Button(face4,bg=couleurAffiche(cube[4][1]), width=6, height=3)
	carre41.config(command=lambda:changeCouleur(cube,carre41,4,1))
	carre41.grid(row=0,column=1)

	carre42 = Button(face4,bg=couleurAffiche(cube[4][2]), width=6, height=3)
	carre42.config(command=lambda:changeCouleur(cube,carre42,4,2))
	carre42.grid(row=0,column=2)

	carre43 = Button(face4,bg=couleurAffiche(cube[4][3]), width=6, height=3)
	carre43.config(command=lambda:changeCouleur(cube,carre43,4,3))
	carre43.grid(row=1,column=0)

	carre44 = Button(face4,bg=couleurAffiche(cube[4][4]), width=6, height=3)
	carre44.config(command=lambda:changeCouleur(cube,carre44,4,4))
	carre44.grid(row=1,column=1)

	carre45 = Button(face4,bg=couleurAffiche(cube[4][5]), width=6, height=3)
	carre45.config(command=lambda:changeCouleur(cube,carre45,4,5))
	carre45.grid(row=1,column=2)

	carre46 = Button(face4,bg=couleurAffiche(cube[4][6]), width=6, height=3)
	carre46.config(command=lambda:changeCouleur(cube,carre46,4,6))
	carre46.grid(row=2,column=0)

	carre47 = Button(face4,bg=couleurAffiche(cube[4][7]), width=6, height=3)
	carre47.config(command=lambda:changeCouleur(cube,carre47,4,7))
	carre47.grid(row=2,column=1)

	carre48 = Button(face4,bg=couleurAffiche(cube[4][8]), width=6, height=3)
	carre48.config(command=lambda:changeCouleur(cube,carre48,4,8))
	carre48.grid(row=2,column=2)


	face5 = Frame(cubeConfig, padx=5, pady=5)
	face5.grid(row=3,column=2)

	carre50 = Button(face5,bg=couleurAffiche(cube[5][0]), width=6, height=3)
	carre50.config(command=lambda:changeCouleur(cube,carre50,5,0))
	carre50.grid(row=0,column=0)

	carre51 = Button(face5,bg=couleurAffiche(cube[5][1]), width=6, height=3)
	carre51.config(command=lambda:changeCouleur(cube,carre51,5,1))
	carre51.grid(row=0,column=1)

	carre52 = Button(face5,bg=couleurAffiche(cube[5][2]), width=6, height=3)
	carre52.config(command=lambda:changeCouleur(cube,carre52,5,2))
	carre52.grid(row=0,column=2)

	carre53 = Button(face5,bg=couleurAffiche(cube[5][3]), width=6, height=3)
	carre53.config(command=lambda:changeCouleur(cube,carre53,5,3))
	carre53.grid(row=1,column=0)

	carre54 = Button(face5,bg=couleurAffiche(cube[5][4]), width=6, height=3)
	carre54.config(command=lambda:changeCouleur(cube,carre54,5,4))
	carre54.grid(row=1,column=1)

	carre55 = Button(face5,bg=couleurAffiche(cube[5][5]), width=6, height=3)
	carre55.config(command=lambda:changeCouleur(cube,carre55,5,5))
	carre55.grid(row=1,column=2)

	carre56 = Button(face5,bg=couleurAffiche(cube[5][6]), width=6, height=3)
	carre56.config(command=lambda:changeCouleur(cube,carre56,5,6))
	carre56.grid(row=2,column=0)

	carre57 = Button(face5,bg=couleurAffiche(cube[5][7]), width=6, height=3)
	carre57.config(command=lambda:changeCouleur(cube,carre57,5,7))
	carre57.grid(row=2,column=1)

	carre58 = Button(face5,bg=couleurAffiche(cube[5][8]), width=6, height=3)
	carre58.config(command=lambda:changeCouleur(cube,carre58,5,8))
	carre58.grid(row=2,column=2)


	Button(cubeConfig,text="Ok !",command=lambda:finCubeConfig(cube,can,cubeConfig)).grid(row=4,columnspan=5)

def finCubeConfig(cube,can,fen):
	"""Fonction associé à 'configurationCube', elle permet de fermer sa fenêtre"""

	fen.destroy()
	actualise(cube,can)

def licence(nom):
	"""Fonction gérant l'affichage des licences"""

	fenetre = Tk()
	fenetre.title("Licence")
	fenetre.iconbitmap("Rubik-Cube.ico")

	if nom == "icone":
		Label(fenetre,text=rFile("licenceIcone","txt")).pack()

	elif nom == "programme":
		Label(fenetre,text=rFile("licenceProgramme","txt")).pack()

	Button(fenetre,text="Ok",command=fenetre.destroy).pack()

def changeTimeur():
	"""Fonction servant à afficher la fenêtre permettant de régler le timeur"""

	fenetre = Tk()
	fenetre.title("Réglage")
	fenetre.iconbitmap("Rubik-Cube.ico")

	Label(fenetre,text="Réglez le temps entre chaque coup en millisecondes :").pack()
	newTimeur = StringVar(fenetre)
	newTimeur.set(rFile("timeur","cub"))
	spin = Spinbox(fenetre, justify="center", from_=0, to=10000, increment=50, textvariable=newTimeur)
	spin.pack()

	Button(fenetre, text="Ok", command=lambda:finChangeTimeur(fenetre, newTimeur.get())).pack()

def finChangeTimeur(fenetre,newTimeur):
	"""Fonction associé à la fonction 'changeTimeur', elle permet de fermer la fenêtre."""
	
	wFile("timeur","cub",int(newTimeur))
	fenetre.destroy()

def changeNombreMelange():
	"""Fonction servant à afficher la fenêtre permettant de régler le nombre de mélange"""
	
	fenetre = Tk()
	fenetre.title("Réglage")
	fenetre.iconbitmap("Rubik-Cube.ico")

	Label(fenetre,text="Réglez le nombre de coups pour mélanger :").pack()
	newNombreMelange = StringVar(fenetre)
	newNombreMelange.set(rFile("nombreMelange","cub"))
	spin = Spinbox(fenetre, justify="center", from_=0, to=500, increment=1, textvariable=newNombreMelange)
	spin.pack()

	Button(fenetre, text="Ok", command=lambda:finChangeNombreMelange(fenetre, newNombreMelange.get())).pack()

def finChangeNombreMelange(fenetre,newNombreMelange):
	"""Fonction associé à la fonction 'changeNombreMelange', elle permet de fermer la fenêtre."""
	
	wFile("nombreMelange","cub",int(newNombreMelange))
	fenetre.destroy()