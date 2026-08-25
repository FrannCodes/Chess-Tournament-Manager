import json
from .tournament_attr import TournamentATTR

class Tournament:
    def __init__(self, filepath_tournament):
        # An instance of Tournament class will create a list of tournaments which each of them are dictionaries

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
            json.dump(self.tournaments_list, fp)

    def create_tournament(self, name, **kwargs):
        # Creates a new tournament

        tournament = TournamentATTR(name = name, **kwargs)
        self.tournaments_list.append(tournament.return_attributes())
        self.save()

        return tournament.return_attributes()

    def remove_tournament(self, name):
        for tournament in self.tournaments_list:
            if tournament["name"] == name:
                self.tournaments_list.remove(tournament)
        self.save()

    def register_player (self, player_num, tournament_name, filepath_club):
        # Registers a player for the tournament using already defined players in a club

        player_list = []

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
                        player_list = tournament["players"]

        except FileNotFoundError:
            print ("File not Found")

        except ValueError as e:
            print(e)

        self.save()

        return player_list

    def results (self, tournament_name, winners):
        # Submits the results of the tournament

        results = []

        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                for match, winner in zip(tournament["rounds"][-1], winners):
                    match["winner"] = winner

                    if match["winner"] not in  match["players"] and match["winner"] is not None:
                        raise ValueError("Winner must be one of the players in the match or a tie")
                    else:
                        match ["completed"] = True

        self.save()

        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                results = tournament["rounds"]

        return results

    def advance (self, tournament_name):
        # Advances tournament to the next round

        number_of_rounds = 1
        current_round = 1


        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:

                number_of_rounds = tournament["number_of_rounds"]
                current_round = tournament["current_round"]

                if number_of_rounds > current_round:
                    tournament["current_round"] += 1
                    current_round = tournament["current_round"]

                elif number_of_rounds == current_round:
                    current_round += 1

        self.save()
        return current_round, number_of_rounds

    def report (self, tournament_name):
        # Returns report of the tournament

        report = {}
        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                report = tournament
        return report

    def return_rounds(self, tournament_name):
        # Returns the rounds

        rounds = []

        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                rounds = tournament["rounds"]

        return rounds

    def return_players(self, tournament_name):
        # Returns the players in a round

        players = []

        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                players = tournament["players"]

        return players

    def add_round(self, tournament_name, matches):
        # Adds a round

        for tournament in self.tournaments_list:
            if tournament["name"] == tournament_name:
                tournament["rounds"].append(matches)
        self.save()
