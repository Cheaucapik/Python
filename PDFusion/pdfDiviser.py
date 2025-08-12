import PyPDF2
import commun as c

def diviser() :
    pdf_reader, pdf_writer = debut()
    choixPages(pdf_reader, pdf_writer)
    
def debut() :
    while True :
        pdf = input("Entrer un document pdf : ")
        if pdf.lower().endswith('.pdf'):
            try:
                pdf_file = open(pdf, 'rb')
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
        try:
            choix = int(choix)
            if(choix > 0):
                break
            else:
                print("Veuillez rentrer un nombre positif.")
        except Exception:
            print("Veuillez rentrer un nombre valide.")

    pages = []
    print('Dans l\'ordre insérer les pages')
    print("Entrez les pages que vous souhaitez avoir :")
    for i in range (choix):
        while True : 
            numPage = input()
            try:
                numPage = int(numPage)
                if(1 <= numPage <= len(pdf_reader.pages)):
                    pages.append(numPage)
                    break
                else:
                    print(f"Veuillez rentrer un nombre entre 1 et {len(pdf_reader.pages)}.")
            except Exception:
                print("Veuillez rentrer un nombre valide.")
        print("Sélection : ", pages)

        page = pdf_reader.pages[numPage - 1]
        pdf_writer.add_page(page)

    nvNom = input("Entrer un nom de pdf : ")
    pdf_writer.write(f"{nvNom}.pdf")