# Générateur de bail de location PDF

Ce projet permet de générer automatiquement un bail de location au format PDF en ligne de commande, à partir de quelques informations saisies.

## Prérequis

- Python 3.8 ou supérieur installé sur votre machine
> Si Python n'est pas installé 
[Téléchargez l’installateur Windows (python-3.8.x-amd64.exe)](https://www.python.org/downloads/release/python-380/)

## Installation et utilisation

1. **Cloner ou copier le dossier du projet**  
   Téléchargez ou clonez ce dépôt sur votre ordinateur.
    ```sh
    git clone https://github.com/nicolaschapgier/bail_generator.git
    ```

2. **Se déplacer dans le dossier du projet**  
   ```sh
   cd pdf_bail
   ```

3. **Créer un environnement virtuel**  
   ```sh
   python -m venv venv
   ```

4. **Activer l’environnement virtuel**  
   ```sh
   venv\Scripts\activate
   ```

5. **Installer les dépendances**  
   ```sh
   pip install -r requirements.txt
   ```

6. **Lancer le script**  
   ```sh
   python generate_bail.py
   ```

7. **Répondre aux questions**  
   Saisissez les informations demandées dans le terminal.  
   Un fichier PDF sera généré dans le dossier courant, nommé selon le locataire et le mois.

## Bonnes pratiques

- **Ne pas versionner le dossier `venv`** : il est ignoré grâce au fichier `.gitignore`.
- **Pour toute nouvelle installation** : il suffit de répéter les étapes ci-dessus.

## Librairie utilisée pour la génération de pdf
[fpdf.org](https://www.fpdf.org/)

---

*Projet Python pour automatiser la génération de baux de location