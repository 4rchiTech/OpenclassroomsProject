import time

from tinydb import TinyDB

from controllers import controleur_principal
from views import view_main


player_database = TinyDB("models/players.json")


class Player:
    def __init__(
        self,
        last_name=None,
        first_name=None,
        birthdate=None,
        gender=None,
        ranking=None,
        tournament_score=0,
        player_id=0,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.tournament_score = tournament_score
        self.player_id = player_id

    def serialized(self):
        player_infos = {}
        player_infos["Nom"] = self.last_name
        player_infos["Prenom"] = self.first_name
        player_infos["Date de naissance"] = self.birthdate
        player_infos["Sexe"] = self.gender
        player_infos["Classement"] = self.ranking
        player_infos["Score"] = self.tournament_score
        player_infos["Id du joueur"] = self.player_id
        return player_infos

    def unserialized(self, serialized_player):
        last_name = serialized_player["Nom"]
        first_name = serialized_player["Prenom"]
        birthdate = serialized_player["Date de naissance"]
        gender = serialized_player["Sexe"]
        ranking = serialized_player["Classement"]
        tournament_score = serialized_player["Score"]
        player_id = serialized_player["Id du joueur"]
        return Player(
            last_name,
            first_name,
            birthdate,
            gender,
            ranking,
            tournament_score,
            player_id,
        )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}, classement : {self.ranking}"

    def add_to_database(self, player_values):
        player = Player(
            player_values[0],
            player_values[1],
            player_values[2],
            player_values[3],
            player_values[4],
        )
        player_id = player_database.insert(player.serialized())
        player_database.update({"Id du joueur": player_id}, doc_ids=[player_id])
