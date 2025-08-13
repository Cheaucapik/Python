def aide():
    print("*" * 20, "Commandes utiles à utiliser à n'importe quel moment", "*" * 20, "\n")
    print("exit : quitter l'application")
    print("retour : aller en arrière")
    print("avance : revenir en avant")
    print("annuler : annuler l'action")
    print("aide : lister les commandes d'aide\n")

def q() :
    for f in fichiers :
        f.close()
    exit()

def retour() :
    pass

def avance() :
    pass

def annuler() :
    pass

fichiers = []

commandes = {
    "aide" : aide,
    "exit" : q, 
    "retour" : retour,
    "avance" : avance,
    "annuler" : annuler
}