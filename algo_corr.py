with open ("C:/Users/azizb/Documents/github_space/Project-A/fichier.txt", "r") as data : 
    lines = data.read()
    liste = list (set (lines.split ("\n")))
    print (liste)
with open ("C:/Users/azizb/Documents/github_space/Project-A/fichier.txt", "w") as data : 
    for i in liste : 
        if len (i) == 5 : 
            data.write ("{}{}".format(i, "\n"))
