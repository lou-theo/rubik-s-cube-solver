from tkinter import *
import os
import pickle

def rFile(nom,extension):
	"""Fonction servant à lire un fichier en fonction de son nom et extension"""

	with open("fichiers/"+str(nom)+"."+str(extension),"rb") as fichier:
		if extension == "txt":
			contenu = fichier.read()
		else:
			depickler = pickle.Unpickler(fichier)
			contenu = depickler.load()
	return contenu

def wFile(nom,extension,contenu):
	"""Fonction servant à écrire un fichier en fonction de son nom et extension"""

	with open("fichiers/"+str(nom)+"."+str(extension),"wb") as fichier:
		if extension == "txt":
			fichier.write(contenu)
		else:
			pickler = pickle.Pickler(fichier)
			pickler.dump(contenu)

def testFile(nom,extension,valeur):
	"""Fonction servant à vérifier l'existence d'un fichier, si ce dernier n'existe pas, il est créé."""
	
	try:
		os.mkdir("fichiers")
	except:
		pass

	try:
		with open("fichiers/"+str(nom)+"."+str(extension),"rb") as fichier:
			depickler = pickle.Unpickler(fichier)
			depickler.load()
	except:
		with open("fichiers/"+str(nom)+"."+str(extension),"wb") as fichier:
			pickler = pickle.Pickler(fichier)
			pickler.dump(valeur)