import random


#Initialisation du score.
user_vect=0
pc_vect=0
egal=0

#Comment jeuer.
print("                                        ________Jeu Pierre, Feuille, Ciseaux________\n")
print("                                               ----Pour Pierre select  (p).----")
print("                                               ----Pour Feuille select (f).----")
print("                                               ----Pour Ciseaux select (c).----")
print("                                            ----Pour Nouvelle Partie select(n).----\n")

#Avior le nom d'utilisateur.
nom=str(input("                                Veuiller saisire votre nom d'utilisateur: "))

#Affechage du score initial.
print("------------------------------------------------------   score   ------------------------------------------------------")

#La boucle de programme.
while True:
    orde=random.randrange(1,4)
    print("                                       [",nom,":",user_vect,"]   [ égalités:",egal,"]   [ Pc:",pc_vect,"]\n")


    t=str(input("Selectionner votre coup: Pour Pierre select :(p), Pour Feuille select :(f), Pour Ciseaux select :(c), \nPour Nouvelle Partie select(n). \nPour Quitter select :(q).\n"))
    if t=="n":
        user_vect=0
        pc_vect=0
        egal=0
    else:
        print("")


    if t=="q":
        break

    elif t!="p" and t!="f" and t!="c":
        continue

    if orde==1:
        if t=='p':
            print("Pierre vs Pierre")
            egal=egal+1

        elif t=='f':
            print("Pierre vs Feuille")
            user_vect=user_vect+1

        elif t=='c':
            print("Pierre vs Ciseaux")
            pc_vect=pc_vect+1

    elif orde==2:
        if t=='p':
            print("Feuille vs Pierre")
            pc_vect=pc_vect+1

        elif t=='f':
            print("Feuille vs Feuille")
            egal=egal+1

        elif t=='c':
            print("Feuille vs Ciseaux")
            user_vect=user_vect+1

    elif orde==3:
        if t=='p':
            print("Ciseaux vs Pierre")
            user_vect=user_vect+1

        elif t=='f':
            print("Ciseaux vs Feuille")
            pc_vect=pc_vect+1

        elif t=='c':
            print("Ciseaux vs Ciseaux")
            egal=egal+1