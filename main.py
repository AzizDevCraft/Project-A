import random 
import re 

with open ("C:/Users/azizb/documents/github_space/Project-A/fichier.txt", "r") as data :
    words = data.read().split ("\n")[:-1]

x = random.randint (0, len (words)-1) # Pour choisir l'indice d'un mot au hasard 
word = words [x]
print ("mot :", word)
print ("-----") # affichage du mot caché
i = 0 # compteur des tentatives possibles 

while i <= 6 :
    ch = ['-','-','-','-','-'] 
    if i == 6 : 
        print ("c'est votre dernière chance !")
    while True : 
        essai = input ("Devine le mot :").capitalize ()
        try : 
            assert len (essai) == 5 and essai.isalpha () == True 
        except AssertionError : 
            print ("tu peux entrer seulement un mot de 6 lettres seulement !")
            continue
        else : 
            break 
    for l in essai :
        if l in word : 
            a = re.search (l, word).span ()[0] 
            ch[a] = l
    word_cache = "".join (ch)
    print (word_cache)
    if word_cache == word : 
        print ("félicitation! vous avez trouvez le mot.")
        break 
    i += 1

