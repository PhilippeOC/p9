# Projet 9 : Développez une application Web en utilisant Django.
## Application permettant à une communauté d'utilisateurs de consulter, de publier ou de solliciter une critique de livres ou d'articles à la demande.


# Installation
1. Créer un dossier pour le projet

2. Dans ce dossier, créer un environnement virtuel avec la commande:
- sous Windows: `python -m venv <environment_name>`  
- sous Linux: `python3 -m venv <environment_name>`

3. Activer cet environnement avec la commande:
- sous Windows: `<environment_name>\Scripts\Activate.ps1`
- sous Linux: `source <environment_name>/bin/activate`

4. Télecharger (puis décompresser) l'application depuis le repository github

5. Installer la liste des paquets Python nécessaires dans cet environnement avec la commande:
- sous Windows: `pip install -r requirements.txt`
- sous Linux: `pip3 install -r requirements.txt`  


# Exécution
1. Pour lancer le programme, dans le dossier `LITReview` (contenant `manage.py`), taper la commande: 
- sous Windows: `python manage.py runserver`
- sous Linux: `python3 manage.py runserver`

2. Ouvrir le lien http://127.0.0.1:8000/ dans un navigateur

# Administration du site
1. Créer un super utilisateur en remplissant les champs demandés avec la commande:
- sous Windows: `python manage.py createsuperuser`
- sous Linux: `python3 manage.py createsuperuser`

2. Ouvrir le lien http://127.0.0.1:8000/admin/ dans un navigateur pour vous connecter à l'interface d'administration.

