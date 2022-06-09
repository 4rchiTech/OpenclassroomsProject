from datetime import datetime
import time
from tinydb import TinyDB, Query


##################################################################################

db = TinyDB("db.json")
print(db.all())


nombre_choix_menu = 6

liste_tournois = []
liste_joueurs = []

##################################################################################


class Joueur:
    def __init__(
        self,
        id_joueur,
        nom,
        prenom,
        date_naissance,
        sexe,
        classement,
        historique_tournois,
        nb_points,
    ):
        self.id_joueur = id_joueur
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.historique_tournois = historique_tournois
        self.nb_points = nb_points


class Tournoi:
    def __init__(
        self,
        numero_tournoi,
        nom,
        statut,
        nb_tours,
        date_debut_tournoi,
        date_fin_tournoi,
        lieu,
        type_controle_temps,
    ):
        self.numero_tournoi = numero_tournoi
        self.nom = nom
        self.statut = statut
        self.nb_tours = nb_tours
        self.date_debut_tournoi = date_debut_tournoi
        self.date_fin_tournoi = date_fin_tournoi
        self.lieu = lieu
        self.type_controle_temps = type_controle_temps


class Round(Tournoi):
    def __init__(self, numero_round, liste_matchs, heure_debut_round, heure_fin_round):
        Tournoi.__init__(Round)
        self.numero_round = numero_round
        self.liste_matchs = liste_matchs
        self.heure_debut_round = heure_debut_round
        self.heure_fin_round = heure_fin_round


"""x = Joueur("aevzf", "zknkqzf", "31/04/2000", "ahdbd", 123)
print(x.nom)"""

"""test = Round(123, "ZF?KZF", 1029, 2944)
print(test.numero_round)"""


def affichage_menu_initial():
    print("Saisissez l'élément de menu :")
    print("1 : Création du tournoi")
    print("2 : Enregistrement des joueurs")
    print("3 : Modifier joueur")
    print("4 : Création des matchs par tour")
    print("5 : Saisie des scores")
    print("6 : Afficher classements")
    return True


def menu_1_creation_tournoi():
    saisie_nom_tournoi = input("Nom tournoi:")
    saisie_lieu_tournoi = input("Lieu du tournoi :")
    saisie_type_tournoi = input("Type tournoi (bullet/blitz/Coup rapide) :")
    saisie_statut = input("Statut tournoi :")
    saisie_nb_tours = input("Nombres de tours du tournoi:")
    saisie_debut_tournoi = input("Date début tournoi :")
    saisie_fin_tournoi = input("Date fin tournoi :")

    ts = int(time.time())

    ajout = Tournoi(
        numero_tournoi=ts,
        nom=saisie_nom_tournoi,
        lieu=saisie_lieu_tournoi,
        type_controle_temps=saisie_type_tournoi,
        statut=saisie_statut,
        nb_tours=saisie_nb_tours,
        date_debut_tournoi=saisie_debut_tournoi,
        date_fin_tournoi=saisie_fin_tournoi,
    )

    liste_tournois.append(ajout)

    print(f"Tournoi N°{ajout.numero_tournoi} créé !\n")


def menu_2_enregistrement_joueurs():
    saisie_nom = input("Nom :")
    saisie_prenom_joueur = input("Prénom :")
    saisie_naissance_joueur = input("Date naissance (format jour/mois/année) :")
    saisie_sexe_joueur = input("Sexe du joueur :")

    ajout = Joueur(
        id_joueur=saisie_nom[:3] + saisie_prenom_joueur[:3],
        nom=saisie_nom,
        prenom=saisie_prenom_joueur,
        date_naissance=saisie_naissance_joueur,
        sexe=saisie_sexe_joueur,
        classement=0,
    )

    liste_joueurs.append(ajout)

    print("joueur ajouté ! \n")


def menu_6_afficher_classements():
    print("1 : Afficher la liste totale des joueurs")

    print("2 : Afficher la liste des joueurs d'un tournoi")

    print("3 : Afficher la liste de tous les tournois")

    print("4 : Afficher la liste des rounds d'un tournoi")

    print("5 : Afficher la liste des matchs d'un tournoi")

    saisie_utilisateur = int(input("Mon choix :"))

    if saisie_utilisateur == 1:
        for i in liste_joueurs:
            print("Joueur :", i.nom)

    elif saisie_utilisateur == 3:
        for i in liste_tournois:
            print("Tournoi :", i.nom)

    return True


#################################################################### MAIN #############

try:

    print("Bienvenue sur EchecsEtMaths ! \nQue souhaitez-vous faire? ")

    while True:
        try:
            affichage_menu_initial()

            saisie_utilisateur = int(input("Mon choix :"))

            if saisie_utilisateur > nombre_choix_menu or saisie_utilisateur <= 0:
                print("Le nombre saisi n'est pas valide")
                continue

            elif saisie_utilisateur == 1:  # menu créer tournoi

                menu_1_creation_tournoi()

            elif saisie_utilisateur == 2:  # menu ajouter joueur

                menu_2_enregistrement_joueurs()
                continue

            elif saisie_utilisateur == 3:  # menu modifier joueur
                pass

            elif saisie_utilisateur == 6:

                menu_6_afficher_classements()

        except Exception as e:
            print("saisissez un nombre valide", e)
            continue

except Exception as e:
    print("sortie programme", e)


liste_test_joueurs = [""]


def creation_pools(numero_tour=None):
    if numero_tour == 1:
        pass
