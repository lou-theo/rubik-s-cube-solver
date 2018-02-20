from tkinter import *
from modules.gestionnaire import *

def couleurAffiche(couleur):
	"""Fonction permettant de modifier les couleurs et les rendre plus proche du Rubik's Cube"""

	if couleur == "red":
		return "#CC0000"
	elif couleur == "green":
		return "#006600"
	elif couleur == "blue":
		return "#0000CC"
	elif couleur == "orange":
		return "#FF4500"
	elif couleur == "yellow":
		return "#FFD500"
	elif couleur == "white":
		return "#FFFFFF"

def actualise(cube,can):
	"""Fonction gérant le canevas"""
	
	for i in range(3): # la hauteur
		for j in range(3): # la longueur
			can.create_rectangle(20+180+50*j,20+20+50*i,20+230+50*j,20+70+50*i,width=2,fill=couleurAffiche(cube[4][3*i+j]))

	for z in range(4):
		for i in range(3):
			for j in range(3):
				can.create_rectangle(20+20+160*z+50*j,20+180+50*i,20+70+160*z+50*j,20+230+50*i,width=2,fill=couleurAffiche(cube[z][3*i+j]))


	for i in range(3):
		for j in range(3):
			can.create_rectangle(20+180+50*j,20+340+50*i,20+230+50*j,20+390+50*i,width=2,fill=couleurAffiche(cube[5][3*i+j]))

	can.create_rectangle(20+170,20+10,20+180,20+500,width=0,fill="black")
	can.create_rectangle(20+330,20+10,20+340,20+500,width=0,fill="black")
	can.create_rectangle(20+10,20+170,20+20,20+340,width=0,fill="black")
	can.create_rectangle(20+490,20+170,20+500,20+340,width=0,fill="black")
	can.create_rectangle(20+650,20+170,20+660,20+340,width=0,fill="black")
	can.create_rectangle(20+10,20+170,20+660,20+180,width=0,fill="black")
	can.create_rectangle(20+10,20+330,20+660,20+340,width=0,fill="black")
	can.create_rectangle(20+170,20+10,20+330,20+20,width=0,fill="black")
	can.create_rectangle(20+170,20+490,20+330,20+500,width=0,fill="black")

	can.create_rectangle(70,177,160,190,width=1,fill=couleurAffiche(cube[4][4]))
	can.create_rectangle(70,360,160,373,width=1,fill=couleurAffiche(cube[5][4]))
	can.create_rectangle(390,177,480,190,width=1,fill=couleurAffiche(cube[4][4]))
	can.create_rectangle(390,360,480,373,width=1,fill=couleurAffiche(cube[5][4]))
	can.create_rectangle(550,177,640,190,width=1,fill=couleurAffiche(cube[4][4]))
	can.create_rectangle(550,360,640,373,width=1,fill=couleurAffiche(cube[5][4]))
	can.create_rectangle(230,17,320,30,width=1,fill=couleurAffiche(cube[3][4]))
	can.create_rectangle(230,520,320,533,width=1,fill=couleurAffiche(cube[3][4]))
	can.create_rectangle(17,230,30,320,width=1,fill=couleurAffiche(cube[3][4]))
	can.create_rectangle(693,230,680,320,width=1,fill=couleurAffiche(cube[0][4]))
	can.create_rectangle(177,70,190,160,width=1,fill=couleurAffiche(cube[0][4]))
	can.create_rectangle(360,70,373,160,width=1,fill=couleurAffiche(cube[2][4]))
	can.create_rectangle(177,390,190,480,width=1,fill=couleurAffiche(cube[0][4]))
	can.create_rectangle(360,390,373,480,width=1,fill=couleurAffiche(cube[2][4]))