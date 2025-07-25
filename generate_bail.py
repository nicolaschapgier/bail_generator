import re
from fpdf import FPDF, XPos, YPos
from datetime import date

def genere_bail(nom_locataire, taille_m2, adresse_bien, loyer, caution, date_debut, duree):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, text="Bail de location d'habitation", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(10)

    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text=f"Date de redaction : {date.today().strftime('%d/%m/%Y')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, text="Informations sur le locataire :", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text=f"Nom du locataire : {nom_locataire}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, text="Informations sur le bien loue :", border="L,T,R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text=f"Adresse : {adresse_bien}", border="L, R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, text=f"Surface : {taille_m2} m2", border="L,B,R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, text="Conditions financieres :", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text=f"Loyer mensuel : {loyer} EUR", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, text=f"Montant du depot de garantie : {caution} EUR", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, text="Duree et dates :", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text=f"Date de debut du bail : {date_debut}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, text=f"Duree du bail : {duree} an(s)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)

    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, text="Signatures :", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text="Le bailleur : ____________________", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, text="Le locataire : ___________________", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Nettoyage du nom pour le nom de fichier
    nom_fichier = re.sub(r"\s+", "_", nom_locataire.strip().title())
    mois_annee = date.today().strftime("%m-%Y")
    pdf_name = f"{nom_fichier}_{mois_annee}.pdf"
    pdf.output(pdf_name)

if __name__ == "__main__":
    print("=== Générateur de bail de location ===")
    nom = input("Nom du locataire : ")
    taille = input("Surface du bien loue en m2 : ")
    adresse = input("Adresse du bien loue : ")
    loyer = input("Loyer mensuel (EUR) : ")
    caution = input("Montant du depot de garantie (EUR) : ")
    date_debut = input("Date de debut du bail (JJ/MM/AAAA) : ")
    duree = input("Duree du bail (en annees) : ")

    try:

        taille = float(taille)
        loyer = float(loyer)
        caution = float(caution)
        duree = int(duree)
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numeriques valides pour la surface, le loyer, la caution et la duree.")
        exit(1)

    genere_bail(nom, taille, adresse, loyer, caution, date_debut, duree)