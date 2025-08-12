import PyPDF2
import commun as c

def merger():
    merger = PyPDF2.PdfMerger()
    nb = choixDoc()
    merge(nb, merger)
    
def choixDoc():
    while True :
        nb = input("Combien de documents souhaitez vous merger ? : ")
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
            if chemin.lower().endswith(".pdf"):
                try:
                    merger.append(chemin)
                    break
                except FileNotFoundError :
                    print("Erreur : le pdf n'existe pas.")
                except Exception as e :
                    print(f"Erreur inattendue : {e}")
            else :
                print("Veuillez rentrer un pdf.")
    nvTitre = input("Entre le nom du nouveau pdf : ")
    merger.write(f"{nvTitre}.pdf")
    merger.close()
    print("Votre pdf a été enregistré sous le nom de : " + nvTitre + ".pdf")