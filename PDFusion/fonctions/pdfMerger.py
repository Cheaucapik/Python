import PyPDF2
# from .commandes import *
from commandes import commandes

def merger():
    merger = PyPDF2.PdfMerger()
    nb = choixDoc()
    merge(nb, merger)
    nvPDF(merger)
    
def choixDoc():
    while True :
        nb = input("Combien de documents souhaitez vous merger ? : ")
        if nb in commandes :
            commandes[nb]()
            continue
        try:
            nb = int(nb)
            if nb > 1:
                break
            else : 
                print("Veuillez rentrer un nombre >1.")
        except ValueError:
            print("Veuillez rentrer un nombre valide.")
    return nb

def merge(nb, merger):
    for i in range(nb) : 
        while True : 
            chemin = input("Entrer le chemin du document " + str(i + 1) + ": ")
            if chemin in commandes :
                commandes[chemin]()
                continue
            if chemin.lower().endswith(".pdf"):
                while True : 
                    choixM = input("Voulez vous rajouter une option pour merger ? \n y/n : ")
                    if choixM == "y" :
                        opt = option(nb, chemin)
                        break
                    elif choixM == "n" :
                        break
                    else : 
                        print("Veuillez choisir une des options.")
                if opt == 0 :
                    try:
                        merger.append(chemin)
                        break
                    except FileNotFoundError :
                        print("Erreur : le pdf n'existe pas.")
                    except Exception as e :
                        print(f"Erreur inattendue : {e}")
            else :
                print("Veuillez rentrer un pdf.")

def nvPDF(merger) :
    nvTitre = input("Entre le nom du nouveau pdf : ")
    if nvTitre in commandes :
        commandes[nvTitre]()
    merger.write(f"{nvTitre}.pdf")
    merger.close()
    print("Votre pdf a été enregistré sous le nom de : " + nvTitre + ".pdf")

def option(nb, chemin) : 
    try : 
        pdf = open(chemin, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf)
    except FileNotFoundError :
        print("Erreur : le pdf n'existe pas.")
        return 0
     
    while True : 
        choixO = input("Souhaitez-vous : \n 1. Ajouter un certain nombre de pages \n 2. Insérer dans un autre document \n 3. Les deux\n")
        if choixO == "1" :

            while True : 
                pPage = input("Entrez l'index de la première page à avoir : ")
                try:
                    pPage = int(pPage)
                    if(1 <= pPage < len(pdf_reader.pages)):
                        dPage = input("Entrez l'index de la dernière page à avoir : ")
                        try:
                            dPage = int(dPage)
                            if(1 <= dPage <= len(pdf_reader.pages and dPage != pPage)):
                                merger.append(fileobj=pdf, pages=(pPage, dPage))
                                return 1
                            else :
                                print(f"Veuillez rentrer un nombre entre {pPage} et {len(pdf_reader.pages)}.")
                        except :
                            print("Veuillez rentrer un nombre valide.")
                    else:
                        print(f"Veuillez rentrer un nombre entre 1 et {len(pdf_reader.pages) - 1}.")
                except Exception:
                    print("Veuillez rentrer un nombre valide.")

        if choixO == "2" :
            if nb > 0 :
                pass
            else : 
                print("Veuillez choisir au moins un document au préalable.")
        elif choixO == "3" :
            if nb > 0 :
                pass
            else : 
                print("Veuillez choisir au moins un document au préalable.")
        else : 
            print("Veuillez choisir parmi les options.")




if __name__ == "__main__":
    merger()