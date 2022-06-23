# puits de données
class Model:
    def __init__(self):
        self.liste_tournois = []
        self.liste_joueurs = []
        # creation des tables tiny ex self.table_tour = commande tiny

    def ajouter_tournoi(self, tournoi):
        self.liste_tournois.append(tournoi)

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)


class Tournoi:
    def __init__(self, nom):
        self.nom = nom


class Joueur:
    def __init__(self, nom):
        self.nom = nom


class Tour:
    def __init__(self, numero):
        self.numero = numero
        self.liste_match_tour_1 = []


class View:
    def __init__(self):
        self.menu = "menu"

    def saisir_tournoi(self):
        return input("entrer nom tournoi")

    def saisir_joueur(self):
        return input("entrer nom joueur")

    def afficher_tournoi(self):
        # requete bdd table tournoi
        pass

    def afficher_liste_matchs(self):
        # boucle sur liste matchs si non vide
        # boucle sur bdd table tour
        pass

    def afficher_classements(self):
        # requete sur table classement (MAJ à chaque sauvegarde d'un score)
        pass


class Controller:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue

    def creer_tournoi(self):
        self.model.ajouter_tournoi()

    def creer_joueur(self):
        self.model.ajouter_tournoi()

    def generer_tour(self):
        # retourne liste de match, tant que nb liste < 4
        pass

    def saisir_scores(self):
        # sur derniere liste des match
        pass

    def calculer_classement(self):
        # calculer le classement après saisie d'un score
        pass

    def enregistrer_element_bdd(self):
        # enregistrer dans bdd - aka fonction sauvegarde
        # enregistre scores, tournoi, tour, classement
        pass

    def run(self):
        running = True

        while running:
            # si table tournoi BDD vide, créer un tournoi, enregistrement bdd

            self.model.ajouter_tournoi(Tournoi(nom=self.vue.saisir_tournoi()))

            # boucle créer 8 joueurs, enregistrement bdd a chaque saisie complete d'un joueur
            self.model.ajouter_joueur(Joueur(nom=self.vue.saisir_joueurk()))

            # créer 4 tours
            # pour chaque tour saisi, afficher liste de match suivant regles, enregistrement bdd
            # pour chaque que tour saisi, saisir les scores suivant liste matchs, enregistrement bdd
            # pour chaque tour fini (100% saisies), calculer et afficher classement provisoire, enregistrement bdd
            # on ne peut pas créer nouveau tour tant que 100% scores pas saisis

            # afficher le classement final, enregistrement bdd, sortie de boucle

            # si table tournoi non vide, charger le dernier tournoi (ou choix?)
            # si nb joueurs < 8, créer joueur, ..
            # si tour < 4, créer tour, ..
            # si scores non full remplis, ajouter scores, ..
            running = False


if __name__ == "__main__":
    # instancier les classes
    model = Model()
    vue = View()
    controleur = Controller(model, vue)

    # run du controller
    controleur.run()
