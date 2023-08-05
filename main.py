import random 
import re 

with open ("C:/Users/azizb/documents/github_space/Project-A/fichier.txt", "r") as data :
    words = data.read().split ("\n")[:-1]

x = random.randint (0, len (words)-1) # Pour choisir l'indice d'un mot au hasard 
word = words [x]
print ("mot :", word)
word_cache = "-----"
print (word_cache) # affichage du mot caché
i = 0 # compteur des tentatives possibles 

while i <= 6 : 
    if i == 6 : 
        print ("c'est votre dernière chance !")
    while True : 
        essai = input ("Devine le mot :")
        try : 
            assert len (essai) == 5 and essai.isalpha () == True 
        except AssertionError : 
            print ("tu peux entrer seulement un mot de 6 lettres seulement !")
            continue
        else : 
            break 
    for l in essai : 
        a = re.search (l, word).span () # erreur dans cette ligne 

    i += 1

