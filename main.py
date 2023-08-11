import random 
<<<<<<< HEAD
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
=======

with open ("fichier.txt", "r") as data :
    words = data.read().split ("\n")[:-1]

alpha = set () #liste des lettres à ne pas utiliser 

x = random.randint (0, len (words)-1) # Pour choisir l'indice d'un mot au hasard 
word = words [x].lower ()
print ("-----") # affichage du mot caché
i = 0 # compteur des tentatives possibles 

while i <= 6 :
    ch = ['-','-','-','-','-'] 
>>>>>>> 5368b4b1c2b11859e3c6cd16faa51de74e5544ac
    if i == 6 : 
        print ("c'est votre dernière chance !")
    while True : 
        essai = input ("Devine le mot :")
        try : 
            assert len (essai) == 5 and essai.isalpha () == True 
        except AssertionError : 
            print ("tu peux entrer seulement un mot de 6 lettres seulement !")
            continue
<<<<<<< HEAD
        else : 
            break 
<<<<<<< HEAD
    for l in essai : 
        a = re.search (l, word).span ()

=======
=======
        break 
>>>>>>> while_adj
    for pos, item in enumerate (essai) :
        if item in word : 
            ch [pos] = item
        else : 
            alpha.add (item)

    word_cache = "".join (ch)
    print (word_cache)
    if word_cache == word : 
        print ("félicitation! vous avez trouvez le mot.")
        break 
    print ("lettre à ne pas utiliser :",alpha)
>>>>>>> 5368b4b1c2b11859e3c6cd16faa51de74e5544ac
    i += 1

