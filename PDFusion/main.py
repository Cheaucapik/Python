import fonctions.pdfDiviser as d
import fonctions.pdfMerger as m
from fonctions.commandes import *

def main() : 
    print("*\n" * 80)
    print("Bienvenue sur PDFusion ! \n".center(80))
    print("*\n" * 80)

    print("Tapez \"aide\" à tout moment pour afficher toutes les commandes disponibles \n")

    while True : 
        choix = input("Choisissez une option : \n 1. Merger \n 2. Diviser \n")
        if choix == "1" : 
            m.merger()
        elif choix == "2" :
            d.diviser()
        elif choix in commandes :
            commandes[choix]()
        else :
            print("Veuillez choisir parmi les options.")

if __name__ == "__main__" :
    main()