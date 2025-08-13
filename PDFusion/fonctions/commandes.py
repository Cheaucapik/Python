import os

def aide():
    print("\n", "*" * 20, "Commandes utiles à utiliser à n'importe quel moment", "*" * 20, "\n")
    print("exit : quitter l'application")
    print("annuler : annuler l'action")
    print("defaut -e : sélectionne un dossier par défaut pour sélectionner des fichiers")
    print("defaut -s : sélectionne un dossier par défaut dans lequel enregistrer les fichiers")
    print("aide : lister les commandes d'aide\n")

def q() :
    for f in fichiers :
        f.close()
    exit()

def annuler() :
    pass

def defE() :
    while True :
        cheminDef = input("Veuillez rentrer le chemin du répertoire : ")
        if os.path.exists(cheminDef) :
            ecrireCheminE(cheminDef)
            break

def defS() :
    while True :
        cheminDef = input("Veuillez rentrer le chemin du répertoire : ")
        if os.path.exists(cheminDef) :
            ecrireCheminS(cheminDef)
            break
        else :
            choix = input("Fichier inexistant, voulez-vous le créer ? \n y/n : ")
            if choix == "y" :
                nvFichier = input("Veuillez entrer le chemin du nouveau répertoire : ")
                os.mkdir(nvFichier)
                ecrireCheminS(nvFichier)
                break
            elif choix != "n" :
                print("Veuillez choisir parmi les options.")

def lireCheminE() :
    with open("chemin.txt", "r") as f :
        lignes = f.readlines()

        if not lignes :
            return  ""
        premiere_ligne = lignes[0].strip()

        return str(premiere_ligne)

def ecrireCheminE(nvChemin) :
    with open("chemin.txt", "r") as f :
        lignes = f.readlines()
        if not lignes:
            lignes = []
        
        if lignes:
            lignes[0] = f"{nvChemin}\n"
        else:
            lignes.append(f"{nvChemin}\n")


    with open("chemin.txt", "w") as f :
        f.writelines(lignes)


def lireCheminS() :
    with open("chemin.txt", "r") as f:
        lignes = f.readlines()

        if len(lignes) < 2 :
            return ""
        
        deuxieme_ligne = lignes[1].strip()

        return str(deuxieme_ligne)
    
def ecrireCheminS(nvChemin) :
    with open("chemin.txt", "r") as f :
        lignes = f.readlines()

        while len(lignes) < 2:
            lignes.append("\n")
        
        lignes[1] = f"{nvChemin}"

    with open("chemin.txt", "w") as f :
        f.writelines(lignes)


if __name__ == "__main__" :
    print(lireCheminE())
    print(lireCheminS())

fichiers = []

commandes = {
    "aide" : aide,
    "exit" : q, 
    "annuler" : annuler,
    "defaut -e" : defE,
    "defaut -s" : defS
}