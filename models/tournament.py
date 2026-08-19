import json
from .player import Player

class Tournament:
    def __init__(self):
        # An instance of Tournament class will create a dictionary of each tournament,
        # with the tournament name as the key and the other data as values

        self.filepath_tournament = "data/tournaments/in-progress.json"
        self.tournaments = {}

        with open(self.filepath_tournament) as fp:
            data = json.load(fp)
            for d in data:
                self.tournaments[d["name"]] = {
                    "dates": d["dates"],
                    "venue": d["venue"],
                    "number_of_rounds": d["number_of_rounds"],
                    "current_round": d["current_round"],
                    "completed": d["completed"],
                    "players": d["players"],
                    "rounds": d["rounds"]
                }

    def save(self):
        with open(self.filepath_tournament, "w") as fp:
            json.dump(

            )

    def create_tournament (self, name, **kwargs):
        self.tournaments[name] = {

        }


    def register_player (self, player_num, tournament_name, club_name):

        try:
            players = []
            with open("data/clubs/" + club_name + ".json") as fp:
                data = json.load(fp)

                for d in data["players"]:
                    players.append(d["chess_id"])

                if player_num not in players:
                    raise ValueError("Player not Found")
                self.tournaments[tournament_name]["players"].append(player_num)

        except FileNotFoundError:
            print ("File not Found")

        except ValueError as e:
            print(e)


    def results (self):
        return self.tournaments

    def advance (self, tournament_name):
        self.tournaments[tournament_name]["current_round"] += 1

    def report (self):
        pass