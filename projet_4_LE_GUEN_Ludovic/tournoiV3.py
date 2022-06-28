from tinydb import TinyDB, Query


db = TinyDB("db.json")

# insertion colonne & data
"""table.insert({"value": True})"""
# maj data
"""db.update({'count': 10}, Fruit.type == 'apple')"""
# afficher contenu table
"""print(table.all())"""


class Model:
    def __init__(self):

        # nettoyahe bdd
        db.drop_tables()

        # liste d'objets
        self.liste_tournois = []
        self.liste_joueurs = []
        self.liste_tours = []

        # bdd
        self.table_tournoi = db.table("Tournoi")
        self.table_joueurs = db.table("Joueur")
        self.table_tours = db.table("Tour")

    # ajouter objet dans liste tournois
    def ajouter_tournoi(self, tournoi):
        self.liste_tournois.append(tournoi)

    # enregistrer tournoi dans bdd
    def enregistrer_tournoi(self, nom_tournoi):
        self.table_tournoi.insert({"nom_tournoi": nom_tournoi})

    def extraction_tournoi(self):
        return self.table_tournoi.all()

    # ajouter objet dans liste joueur
    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    # enregistrer joueur dans bdd
    def enregistrer_joueur(self, nom_joueur):
        self.table_joueurs.insert({"nom_joueur": nom_joueur, "score_joueur": 0})

    def extraction_totalite_score(self):

        bdd = self.table_joueurs.all()

        for element in bdd:
            nom_joueur = element["nom_joueur"]
            score_joueur = element["score_joueur"]
            print(f"{nom_joueur}, score : {score_joueur}")

    def extraction_score_joueur(self, nom_joueur_cible):

        bdd = self.table_joueurs.all()

        for element in bdd:
            if element["nom_joueur"] == nom_joueur_cible:
                return element["score_joueur"]

    # ajouter objet dans liste tour
    def ajouter_tour(self, tour):
        self.liste_tours.append(tour)

    # enregistrer tournoi dans bdd
    def enregistrer_tour(self, numero_tour, match_1, match_2, match_3, match_4):
        self.table_tours.insert({"numero_tour": numero_tour, "match_1": match_1})
        self.table_tours.insert({"numero_tour": numero_tour, "match_2": match_2})
        self.table_tours.insert({"numero_tour": numero_tour, "match_3": match_3})
        self.table_tours.insert({"numero_tour": numero_tour, "match_4": match_4})


class View:
    def __init__(self):
        self.menu = "menu"

    def saisir_nom_tournoi(self):
        return input("entrez le nom du tournoi :")

    def choisir_gagnant(self):
        return input("le gagnant est le joueur 1 ou 2?")

    def saisir_nom_joueur(self):
        return input("entrez le nom du joueur :")

    def afficher_tournoi(self):
        # requete bdd table tournoi
        pass

    def afficher_liste_matchs(self, match_1, match_2, match_3, match_4):
        return print(
            f"\nLes matchs à jouer sont :\n\nMatch 1:{match_1}\nMatch 2:{match_2}\nMatch 3:{match_3}\nMatch 4:{match_4}"
        )

    def afficher_match(self, joueur_1, joueur_2):
        return print(f"\nDésignez le gagnant du match :\n1 :{joueur_1}\n2 :{joueur_2}")

    def afficher_saisie_score(self):
        question = int(input("\nSaisissez le numéro du joueur gagnant:"))
        if question == 1:
            return True
        elif question == 2:
            return False
        else:
            return None


class Controller:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue

    def creer_tournoi(self):
        # input utilisateur
        saisie_nom_tournoi = self.vue.saisir_nom_tournoi()
        # enregistrement objet
        self.model.ajouter_tournoi(Tournoi(nom_tournoi=saisie_nom_tournoi))
        # enregistrement bdd
        self.model.enregistrer_tournoi(nom_tournoi=saisie_nom_tournoi)

    def creer_joueur(self):
        # input utilisateur
        saisie_nom_joueur = self.vue.saisir_nom_joueur()
        # enregistrement objet
        self.model.ajouter_joueur(Joueur(nom_joueur=saisie_nom_joueur))
        # enregistrement bdd
        self.model.enregistrer_joueur(nom_joueur=saisie_nom_joueur)

    def creer_tour(self):
        match_1 = (self.model.liste_joueurs[0].nom, self.model.liste_joueurs[4].nom)
        match_2 = (self.model.liste_joueurs[1].nom, self.model.liste_joueurs[5].nom)
        match_3 = (self.model.liste_joueurs[2].nom, self.model.liste_joueurs[6].nom)
        match_4 = (self.model.liste_joueurs[3].nom, self.model.liste_joueurs[7].nom)
        # enregistrement objet
        numero_tour = len(self.model.liste_tours) + 1

        # enregistrement bdd

        self.model.enregistrer_tour(numero_tour, match_1, match_2, match_3, match_4)

        instance_tour = Tour(numero_tour, match_1, match_2, match_3, match_4)
        self.model.ajouter_tour(instance_tour)

        # affichage des matchs

        self.vue.afficher_liste_matchs(match_1, match_2, match_3, match_4)
        # retour de l'objet pour saisie score
        return instance_tour

    def maj_score_gagnant(self, joueur_gagnant):
        score_actuel = self.model.extraction_score_joueur(joueur_gagnant)

        # incrémentation score
        nouveau_score = int(score_actuel) + 1

        # maj bdd
        requete = Query()
        self.model.table_joueurs.update(
            {"score_joueur": nouveau_score}, requete.nom_joueur == joueur_gagnant
        )

    def saisir_scores(self, tour):

        # premier match du tour
        match_1 = tour.match_1
        self.vue.afficher_match(joueur_1=match_1[0], joueur_2=match_1[1])

        if self.vue.afficher_saisie_score():
            self.maj_score_gagnant(joueur_gagnant=match_1[0])
        self.maj_score_gagnant(joueur_gagnant=match_1[1])

        # second match du tour
        match_2 = tour.match_2
        self.vue.afficher_match(joueur_1=match_2[0], joueur_2=match_2[1])

        if self.vue.afficher_saisie_score():
            self.maj_score_gagnant(joueur_gagnant=match_2[0])
        self.maj_score_gagnant(joueur_gagnant=match_2[1])

        # troisieme match du tour
        match_3 = tour.match_3
        self.vue.afficher_match(joueur_1=match_3[0], joueur_2=match_3[1])

        if self.vue.afficher_saisie_score():
            self.maj_score_gagnant(joueur_gagnant=match_3[0])
        self.maj_score_gagnant(joueur_gagnant=match_3[1])

        # quatrième match du tour
        match_4 = tour.match_4
        self.vue.afficher_match(joueur_1=match_4[0], joueur_2=match_4[1])

        if self.vue.afficher_saisie_score():
            self.maj_score_gagnant(joueur_gagnant=match_4[0])
        self.maj_score_gagnant(joueur_gagnant=match_4[1])

    def run(self):
        running = True

        while running:
            if len(self.model.liste_tournois) < 1:
                self.creer_tournoi()

                while len(self.model.liste_joueurs) < 8:
                    self.creer_joueur()

                self.saisir_scores(tour=self.creer_tour())  # TOUR 1
                self.model.extraction_totalite_score()

                self.saisir_scores(tour=self.creer_tour())  # TOUR 2
                self.model.extraction_totalite_score()


class Tournoi:
    def __init__(self, nom_tournoi):
        self.nom = nom_tournoi


class Joueur:
    def __init__(self, nom_joueur):
        self.nom = nom_joueur
        self.score = 0


class Tour:
    def __init__(self, numero_tour, match_1, match_2, match_3, match_4):
        self.numero_tour = numero_tour
        self.match_1 = match_1
        self.match_2 = match_2
        self.match_3 = match_3
        self.match_4 = match_4


if __name__ == "__main__":

    # instanciation des classes
    model = Model()
    vue = View()
    controleur = Controller(model, vue)

    # run du controller
    controleur.run()
