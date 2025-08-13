import PyPDF2
# from .commandes import *
from commandes import commandes, fichiers
import io

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
            opt = 0
            chemin = input("Entrer le chemin du document " + str(i + 1) + ": ")
            if chemin in commandes :
                commandes[chemin]()
                continue
            if chemin.lower().endswith(".pdf"):
                while True : 
                    choixM = input("Voulez vous rajouter une option pour merger ? \n y/n : ")
                    if choixM == "y" :
                        opt = option(i, chemin, merger)
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
                    break
            else :
                print("Veuillez rentrer un pdf.")

def nvPDF(merger) :
    nvTitre = input("Entre le nom du nouveau pdf : ")
    if nvTitre in commandes :
        commandes[nvTitre]()
    merger.write(f"{nvTitre}.pdf")
    merger.close()
    print("Votre pdf a été enregistré sous le nom de : " + nvTitre + ".pdf")

def option(i, chemin, merger) : 
    try : 
        pdf = open(chemin, 'rb')
        fichiers.append(pdf)
        pdf_reader = PyPDF2.PdfReader(pdf)
    except FileNotFoundError :
        return 0
    
    while True : 
        choixO = input("Souhaitez-vous : \n 1. Ajouter un certain nombre de pages \n 2. Insérer dans un autre document \n 3. Les deux\n")
        if choixO == "1" :
            choix1(merger, pdf, pdf_reader)
            return 1

        if choixO == "2" :
            opt = choix2(i, merger, pdf)
            if(opt == 0) :
                continue
            else :
                return 1

        elif choixO == "3" :
            choix3(i, merger, pdf, pdf_reader)

        else : 
            print("Veuillez choisir parmi les options.")


def choix1(merger, pdf, pdf_reader) :
    while True : 
        pPage = input("Entrez l'index de la première page à avoir : ")
        try:
            pPage = int(pPage)
            if(1 <= pPage < len(pdf_reader.pages)):
                dPage = input("Entrez l'index de la dernière page à avoir : ")
                try:
                    dPage = int(dPage)
                    if((1 <= dPage <= len(pdf_reader.pages)) and dPage != pPage):
                        merger.append(fileobj=pdf, pages=(pPage - 1, dPage))
                        return
                    else :
                        print(f"Veuillez rentrer un nombre entre {pPage} et {len(pdf_reader.pages)}.")
                except Exception as e :
                    print(f"Erreur : {e}")
            else:
                print(f"Veuillez rentrer un nombre entre 1 et {len(pdf_reader.pages) - 1}.")
        except Exception:
            print(f"Erreur : {e}")


def choix2(i, merger, pdf) :
    while True :
        if i > 0 :
            pos = input("Choisissez la page à partir de laquelle vous insérez votre pdf : ")
            try :
                pos = int(pos)
                if(1 <= pos < len(merger.pages)) :
                    merger.merge(position = pos - 1, fileobj = pdf)
                    return 1
                else :
                    print(f"Veuillez rentrer un nombre entre 1 et {len(merger.pages) - 1}")
            except Exception as e :
                print(f"Erreur : {e}")
        else : 
            print("Veuillez choisir au moins un document au préalable.")
            return 0

def choix3(i, merger, pdf, pdf_reader) :
    while True : 
        pPage = input("Entrez l'index de la première page à avoir : ")
        try:
            pPage = int(pPage)
            if(1 <= pPage < len(pdf_reader.pages)):
                dPage = input("Entrez l'index de la dernière page à avoir : ")
                try:
                    dPage = int(dPage)
                    if((1 <= dPage <= len(pdf_reader.pages)) and dPage != pPage):
                         while True :
                            if i > 0 :
                                pos = input("Choisissez la page à partir de laquelle vous insérez votre pdf : ")
                                try :
                                    pos = int(pos)
                                    if(1 <= pos < len(merger.pages)) :
                                        merger.merge(position = pos - 1, fileobj = pdf, pages=(pPage, dPage))
                                        return 1
                                    else :
                                        print(f"Veuillez rentrer un nombre entre 1 et {len(merger.pages) - 1}")
                                except Exception as e :
                                    print(f"Erreur : {e}")
                            else : 
                                print("Veuillez choisir au moins un document au préalable.")
                                return 0
                            print("Veuillez choisir au moins un document au préalable.")
                            return
                    else :
                        print(f"Veuillez rentrer un nombre entre {pPage} et {len(pdf_reader.pages)}.")
                except Exception as e :
                    print(f"Erreur : {e}")
            else:
                print(f"Veuillez rentrer un nombre entre 1 et {len(pdf_reader.pages) - 1}.")
        except Exception:
            print(f"Erreur : {e}")


if __name__ == "__main__":
    merger()