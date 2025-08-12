import pdfDiviser as d
import pdfMerger as m

print("Bienvenue sur PDFusion ! \n")

while True : 
    choix = input("Choisissez une option : \n 1. Merger \n 2. Diviser \n")
    if choix == "1" : 
        m.merger()
    elif choix == "2" :
        d.diviser()
    else :
        print("Veuillez choisir parmi les options.")