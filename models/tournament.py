import json
from .player import Player

class Tournament:
    def __init__(self):
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
        pass

    def create_tournament (self, filepath_club):
        pass

    def register_player (self, filepath_club):
        pass

    def results (self):
        pass

    def advance (self):
        pass

    def report (self):
        pass