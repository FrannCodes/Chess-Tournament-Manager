import json
from .tournament_attr import TournamentATTR

class Tournament:
    def __init__(self, filepath_tournament):
        # An instance of Tournament class will create a dictionary of each tournament

        self.filepath_tournament = filepath_tournament
        self.tournaments_list = []

        with open(self.filepath_tournament) as fp:
            data = json.load(fp)
            for d in data:
                self.tournaments_info = {
                    "name" : d["name"],
                    "dates": d["dates"],
                    "venue": d["venue"],
                    "number_of_rounds": d["number_of_rounds"],
                    "current_round": d["current_round"],
                    "completed": d["completed"],
                    "players": d["players"],
                    "rounds": d["rounds"]
                }
                self.tournaments_list.append(self.tournaments_info)

    def save(self):
        # Saves JSON file everytime a change is made

        with open(self.filepath_tournament, "w") as fp:
            json.dump(self.tournaments_list)

    def create_tournament (self, name, **kwargs):
        # Creates a new tournament

        tournament = TournamentATTR(name = name, **kwargs)
        self.tournaments_list.append(tournament.return_attributes())
        self.save()

    def register_player (self, player_num, tournament_name, filepath_club):
        # Registers a player for the tournament using already defined players in a club

        try:
            players = []

            with open(filepath_club) as fp:
                data = json.load(fp)

                for d in data["players"]:
                    players.append(d["chess_id"])

                if player_num not in players:
                    raise ValueError("Player not Found")

                for tournament in self.tournaments_list:
                    if tournament["name"] == tournament_name:
                        tournament["players"].append(player_num)


        except FileNotFoundError:
            print ("File not Found")

        except ValueError as e:
            print(e)

        self.save()

    def results (self, tournament_name):
        # Returns the results of the tournaments

        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                results = tournament["rounds"]

        return results

    def advance (self, tournament_name):
        # Advances tournament to the next round

        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                if tournament["number_of_rounds"] > tournament["current_round"]:
                    tournament["current_round"] += 1

                else:
                    raise ValueError("Tournament cannot advance past the final round")

        self.save()

    def report (self, tournament_name):
        # Returns report of the tournament

        report = {}
        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                report = {
                    "name": tournament["name"],
                    "dates": tournament["dates"],
                    "venue": tournament["venue"],
                    "number_of_rounds": tournament["number_of_rounds"],
                    "current_round": tournament["current_round"],
                    "completed": tournament["completed"],
                    "players": tournament["players"],
                    "rounds": tournament["rounds"]
                }
        return report