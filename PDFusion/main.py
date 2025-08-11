import pdfDiviser as D
import pdfMerger as M

print("Bienvenue sur PDFusion ! \n")

choix = input("Choisissez une option : \n 1. Merger \n 2. Diviser")
if choix == "1" : 
    M.merger()
elif choix == "2" :
    D.diviser()
else :
    print("Veuillez choisir parmi les options.")