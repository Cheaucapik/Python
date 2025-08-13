import PyPDF2
#from .commandes import *
from commandes import commandes, fichiers, lireCheminE, lireCheminS
import os

def diviser() :
    pdf_reader, pdf_writer = debut()
    choixPages(pdf_reader, pdf_writer)
    
def debut() :
    while True :
        print("chemin actuel : ", lireCheminE())
        pdf = input("Entrer un document pdf : ")
        if pdf in commandes :
            commandes[pdf]()
            continue
        if pdf.lower().endswith('.pdf'):
            try:
                path = os.path.join(lireCheminE(), f"{pdf}")
                pdf_file = open(path, 'rb')
                fichiers.append(pdf_file)
                break
            except FileNotFoundError :
                print("Erreur : le pdf n'existe pas.")
            except Exception as e :
                print(f"Erreur inattendue : {e}")
        else :
            print("Veuillez rentrer un pdf.")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()
    return pdf_reader, pdf_writer

def choixPages(pdf_reader, pdf_writer) :
    while True : 
        choix = input("Combien de pages souhaitez vous extraire ? ")
        if choix in commandes :
            commandes[choix]()
            continue
        try:
            choix = int(choix)
            if(choix > 0):
                break
            else:
                print("Veuillez rentrer un nombre positif.")
        except Exception as e:
            print(f"Erreur : {e}")

    pages = []
    print('Dans l\'ordre insérer les pages')
    print("Entrez les pages que vous souhaitez avoir :")
    for i in range(choix):
        while True : 
            numPage = input()
            if numPage in commandes :
                commandes[numPage]()
                continue
            try:
                numPage = int(numPage)
                if(1 <= numPage <= len(pdf_reader.pages)):
                    pages.append(numPage)
                    break
                else:
                    print(f"Veuillez rentrer un nombre entre 1 et {len(pdf_reader.pages)}.")
            except Exception as e:
                print(f"Erreur : {e}")
        print("Sélection : ", pages)

        page = pdf_reader.pages[numPage - 1]
        pdf_writer.add_page(page)
    nvPDF(pdf_writer)


def nvPDF(pdf_writer) :
    nvTitre = input("Entre le nom du nouveau pdf : ")
    if nvTitre in commandes :
        commandes[nvTitre]()
    fichier_sortie = os.path.join(lireCheminS(), f"{nvTitre}.pdf")
    if os.path.exists(fichier_sortie) :
        replace = input("Le fichier existe déjà voulez-vous le remplacer ? \n y/n : ")
        if replace == "n" : 
            pdf_writer.close()
    try : 
        pdf_writer.write(fichier_sortie)
        pdf_writer.close()
        print("Votre pdf a été enregistré sous le nom de : " + nvTitre + ".pdf")
        try :
            os.startfile(lireCheminS())
        except Exception:
            print("Impossible d'ouvrir le dossier.")
    except :
        print("Votre fichier n'a pas été enregistré.")

if __name__ == "__main__":
    diviser()