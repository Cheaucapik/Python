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
            chemin = input("Entrer le chemin du document " + str(i + 1) + ": ")
            if chemin in commandes :
                commandes[chemin]()
                continue
            if chemin.lower().endswith(".pdf"):
                verifPDF(chemin, i, merger)
                break
            else :
                print("Veuillez rentrer un pdf.")

def verifPDF(chemin, i, merger) : 
    try : 
        pdf = open(chemin, 'rb')
        fichiers.append(pdf)
        pdf_reader = PyPDF2.PdfReader(pdf)
        option_merge(i, chemin, merger, pdf_reader, pdf)
    except FileNotFoundError :
        print("Erreur : Le fichier n'existe pas, ou n'a pas été trouvé.")
        return 0

def option_merge(i, chemin, merger, pdf_reader, pdf) :
    opt = 0
    while True : 
        choixM = input("Voulez vous rajouter une option pour merger ? \n y/n : ")
        if choixM == "y" :
            opt = option(i, merger, pdf_reader, pdf)
            break
        elif choixM == "n" :
            break
        else : 
            print("Veuillez choisir une des options.")  

    if opt == 0 : 
        merger.append(chemin)



def option(i, merger, pdf_reader, pdf) : 
    
    while True : 
        choixO = input("Souhaitez-vous : \n 1. Ajouter un certain nombre de pages \n 2. Insérer dans un autre document \n 3. Les deux\n")
        if choixO == "1" :
            pPage, dPage =choixPages(pdf_reader)
            merger.append(fileobj = pdf, pages = (pPage, dPage))
            return 1

        if choixO == "2" and i > 0 :
            pos = choixPos(merger)
            merger.merge(position = pos - 1, fileobj = pdf)
            return 1

        elif choixO == "3" and i > 0 :
            pPage, dPage, pos = choixBoth(merger, pdf_reader)
            merger.merge(position = pos - 1, fileobj = pdf, pages=(pPage, dPage))
            return 1

        elif choixO in ("2", "3") :
            print("Veuillez choisir au moins un document au préalable. \n")
            continue

        else : 
            print("Veuillez choisir parmi les options. \n")


def choixPages(pdf_reader) : 
    while True : 
        pPage = input("Entrez l'index de la première page à avoir : ")
        try:
            pPage = int(pPage)
            if(1 <= pPage < len(pdf_reader.pages)):
                dPage = input("Entrez l'index de la dernière page à avoir : ")
                try:
                    dPage = int(dPage)
                    if((1 <= dPage <= len(pdf_reader.pages)) and dPage != pPage):
                        return pPage - 1, dPage
                    else :
                        print(f"Veuillez rentrer un nombre entre {pPage} et {len(pdf_reader.pages)}.")
                except Exception as e :
                    print(f"Erreur : {e}")
            else:
                print(f"Veuillez rentrer un nombre entre 1 et {len(pdf_reader.pages) - 1}.")
        except Exception:
            print(f"Erreur : {e}")


def choixPos(merger) :
    while True :
        pos = input("Choisissez la page à partir de laquelle vous insérez votre pdf : ")
        try :
            pos = int(pos)
            if(1 <= pos < len(merger.pages)) :
                return pos
            else :
                print(f"Veuillez rentrer un nombre entre 1 et {len(merger.pages) - 1}")
        except Exception as e :
            print(f"Erreur : {e}")


def choixBoth(merger, pdf_reader) :
    pPage, dPage = choixPages(pdf_reader)
    pos = choixPos(merger)
    return pPage, dPage, pos


def nvPDF(merger) :
    nvTitre = input("Entre le nom du nouveau pdf : ")
    if nvTitre in commandes :
        commandes[nvTitre]()
    merger.write(f"{nvTitre}.pdf")
    merger.close()
    print("Votre pdf a été enregistré sous le nom de : " + nvTitre + ".pdf")

if __name__ == "__main__":
    merger()