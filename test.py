from time import *
from tkinter import *
from random import *
from modules.affichage import *
from modules.mouvements import *
from modules.recherche import *
from modules.menu import *
from modules.gestionnaire import *
from modules.resolveur import *

def rotativeUserSafe(cube,can,face,faceSup,norme):
	if face == faceSup or faceSup == posRel(face)[4]:
		fenetre = Tk()
		fenetre.title("Erreur")
		fenetre.iconbitmap("Rubik-Cube.ico")

		Label(fenetre,text="Le mouvement est impossible !").pack()
		Button(fenetre,text="Ok",command=fenetre.destroy).pack()

	else:
		rotativeUser(cube,can,face,faceSup,norme)

def solve(cube,can):
	start()
	resoudre(cube,can)

def melange(root,cube,can,nombre):
	root.config(cursor="wait")
	melangeur(cube,can,nombre)
	root.after(nombre*rFile("timeur","cub"),lambda:root.config(cursor="arrow"))


cube=[["green"]*9,["red"]*9,["blue"]*9,["orange"]*9,["white"]*9,["yellow"]*9]

testFile("timeur","cub",1000)
testFile("nombreMelange","cub",25)
testFile("compteur","cub",0)


root=Tk()
root.title("Rubik's Solveur")
root.iconbitmap("Rubik-Cube.ico")

menuBar = Menu(root)

menuFichier = Menu(menuBar, tearoff=0)
menuFichier.add_command(label="Réinitialiser le cube",command=lambda:reboot(cube,can))
menuFichier.add_command(label="Entrer une nouvelle configuration",command=lambda:configurationCube(cube,can,"new"))
menuFichier.add_command(label="Modifier la configuration",command=lambda:configurationCube(cube,can))
menuFichier.add_separator()
menuFichier.add_command(label="Mélanger",command=lambda:melange(root,cube,can,rFile("nombreMelange","cub")))
menuFichier.add_separator()
menuFichier.add_command(label="Quitter",command=root.destroy)
menuBar.add_cascade(label="Cube",menu=menuFichier)

menuOption = Menu(menuBar, tearoff=0)
menuOption.add_command(label="Réglage du temps",command=changeTimeur)
menuOption.add_command(label="Réglage du nombre de mélange",command=changeNombreMelange)
menuBar.add_cascade(label="Option",menu=menuOption)

menuAide = Menu(menuBar, tearoff=0)
menuAide.add_command(label="Consulter la licence de l'icone",command=lambda:licence("icone"))
menuAide.add_command(label="Consulter la licence du programme",command=lambda:licence("programme"))
menuBar.add_cascade(label="Aide",menu=menuAide)

root.config(menu=menuBar)

can=Canvas(root,bg="#F0F0F0",height=550,width=710)
can.grid(row=0, column=0, rowspan=3)
actualise(cube,can)


facePrincipaleFrame = Frame(root, padx=3, pady=2, relief=RIDGE, borderwidth=1, bg="#CCCCCC")
facePrincipaleFrame.grid(row=0, column=1, padx=3, pady=2, sticky=S)
facePrincipale = StringVar(facePrincipaleFrame)
facePrincipale.set("red")
Label(facePrincipaleFrame,text="Face principale :").pack()
Radiobutton(facePrincipaleFrame, text="Rouge  ", variable=facePrincipale, value="red", bg="#CCCCCC").pack(anchor=W)
Radiobutton(facePrincipaleFrame, text="Bleu     ", variable=facePrincipale, value="blue", bg="#CCCCCC").pack(anchor=W)
Radiobutton(facePrincipaleFrame, text="Vert      ", variable=facePrincipale, value="green", bg="#CCCCCC").pack(anchor=W)
Radiobutton(facePrincipaleFrame, text="Jaune   ", variable=facePrincipale, value="yellow", bg="#CCCCCC").pack(anchor=W)
Radiobutton(facePrincipaleFrame, text="Blanc   ", variable=facePrincipale, value="white", bg="#CCCCCC").pack(anchor=W)
Radiobutton(facePrincipaleFrame, text="Orange", variable=facePrincipale, value="orange", bg="#CCCCCC").pack(anchor=W)

faceSupFrame = Frame(root, padx=3, pady=2, relief=RIDGE, borderwidth=1, bg="#CCCCCC")
faceSupFrame.grid(row=0, column=2, padx=3, pady=2, sticky=S)
faceSup = StringVar(faceSupFrame)
faceSup.set("white")
Label(faceSupFrame,text="Face supérieure :").pack()
Radiobutton(faceSupFrame, text="Rouge  ", variable=faceSup, value="red", bg="#CCCCCC").pack(anchor=W)
Radiobutton(faceSupFrame, text="Bleu     ", variable=faceSup, value="blue", bg="#CCCCCC").pack(anchor=W)
Radiobutton(faceSupFrame, text="Vert      ", variable=faceSup, value="green", bg="#CCCCCC").pack(anchor=W)
Radiobutton(faceSupFrame, text="Jaune   ", variable=faceSup, value="yellow", bg="#CCCCCC").pack(anchor=W)
Radiobutton(faceSupFrame, text="Blanc   ", variable=faceSup, value="white", bg="#CCCCCC").pack(anchor=W)
Radiobutton(faceSupFrame, text="Orange", variable=faceSup, value="orange", bg="#CCCCCC").pack(anchor=W)

boutonFrame = Frame(root, height=200)
boutonFrame.grid(row=1, column=1, columnspan=2)

Button(boutonFrame, text="F", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "F") , bg="#CCCCCC" ,padx=12).grid(row=1, column=1, sticky=E, padx=1, pady=1)
Button(boutonFrame, text="F'", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "F'") , bg="#CCCCCC" ,padx=12).grid(row=1, column=2, sticky=W, padx=1, pady=1)

Button(boutonFrame, text="U", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "U") , bg="#CCCCCC" ,padx=11).grid(row=2, column=1, sticky=E, padx=1, pady=1)
Button(boutonFrame, text="U'", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "U'") , bg="#CCCCCC" ,padx=11).grid(row=2, column=2, sticky=W, padx=1, pady=1)

Button(boutonFrame, text="R", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "R") , bg="#CCCCCC" ,padx=11).grid(row=3, column=1, sticky=E, padx=1, pady=1)
Button(boutonFrame, text="R'", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "R'") , bg="#CCCCCC" ,padx=11).grid(row=3, column=2, sticky=W, padx=1, pady=1)

Button(boutonFrame, text="D", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "D") , bg="#CCCCCC" ,padx=11).grid(row=4, column=1, sticky=E, padx=1, pady=1)
Button(boutonFrame, text="D'", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "D'") , bg="#CCCCCC" ,padx=11).grid(row=4, column=2, sticky=W, padx=1, pady=1)

Button(boutonFrame, text="L", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "L") , bg="#CCCCCC" ,padx=12).grid(row=5, column=1, sticky=E, padx=1, pady=1)
Button(boutonFrame, text="L'", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "L'") , bg="#CCCCCC" ,padx=12).grid(row=5, column=2, sticky=W, padx=1, pady=1)

Button(boutonFrame, text="M", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "M") , bg="#CCCCCC" ,padx=10).grid(row=6, column=1, sticky=E, padx=1, pady=1)
Button(boutonFrame, text="M'", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "M'") , bg="#CCCCCC" ,padx=10).grid(row=6, column=2, sticky=W, padx=1, pady=1)

Button(boutonFrame, text="E", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "E") , bg="#CCCCCC" ,padx=12).grid(row=7, column=1, sticky=E, padx=1, pady=1)
Button(boutonFrame, text="E'", command=lambda:rotativeUserSafe(cube, can, findFace(cube,can,facePrincipale.get()), \
	findFace(cube,can,faceSup.get()), "E'") , bg="#CCCCCC" ,padx=12).grid(row=7, column=2, sticky=W, padx=1, pady=1)

Button(root, text="Résoudre !", command=lambda:solve(cube,can)).grid(row=2, column=1, columnspan=2)
