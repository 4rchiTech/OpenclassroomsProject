dernière modification le 11/05/2022 à 18h30

############ READ ME ################################################################

Script de scrapping du site http://books.toscrape.com/

*** fonctions ***
- enregistrement des logs pour debug dans fichier dédié
- lecture du menu catégories pour création de l'architecture documentaire
- création d'un fichier csv par catégorie et extraction des livres par catégorie
- extraction des informations de chaque livre de la catégorie visée au sein du fichier csv visé
- extraction de l'image de couverture de chaque livre et enregistrement au sein d'un dossier unique images

*** Prérequis ***

- Python 3.9 ou supérieur
- un dossier nommé "images" dans le même dossier que le script main.py
- un dossier nommé "data" dans le même dossier que le script main.py

##################################################

Etapes d'utilisation :

1. Créer un environnement virtuel via le terminal :

python -m venv chemin_du_dossier_projet

ex : ex python -m venv C:\Users\solut\Desktop\env_test

------

2. Activer l'environnement virtuel via le terminal :

a) se déplacer dans le fichier "Scripts" créé dans le dossier de l'environnement_virtuel via la commande cd chemin_du_dossier_scripts
b) puis saisir : activate.bat

------

3. Installer les dépendances du script via le terminal : 

pip install -r requirements

------

4. Lancer le script via le terminal : 

a) via la commande cd se déplacer dans le dossier qui comprend le fichier main.py
b) puis saisir : python main.py

------

5. Si vous souhaitez quitter l'environnement virtuel  :

a) Se déplacer dans le fichier "Scripts" créé dans le dossier de l'environnement_virtuel via la commande cd chemin_du_dossier_scripts
b) Puis saisir : deactivate.bat
When you are done with the virtual environment, you have to unlog from it by calling

#####################################################################################
