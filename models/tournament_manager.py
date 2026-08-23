import json
from pathlib import Path
from .tournament import Tournament

class TournamentManager:
    def __init__(self, data_folder = "data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tournaments = []

        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    with open(filepath) as fp:
                        # Appends all tournaments from both completed and in-progress files to the same list
                        data = json.load(fp)
                        for tournament in data:
                            self.tournaments.append(tournament)

                except json.JSONDecodeError:
                    print(filepath, "is an invalid JSON file.")

    def completed(self, name):
        #Moves completed tournaments from "in-progress.json" to "completed.json" file when marked as completed
        list_tournaments = []

        for t in self.tournaments:
            if t["name"] == name:
                in_progress = Tournament("data/tournaments/in-progress.json")
                completed = Tournament("data/tournaments/completed.json")

                for i in in_progress.tournaments_list:
                    if i["name"] == name:
                        in_progress.remove_tournament(name)
                        completed.create_tournament(name, dates = i["dates"], venue = i["venue"],
                                                    number_of_rounds = i["number_of_rounds"],
                                                    current_round = i["current_round"],
                                                    players = i["players"], rounds = i["rounds"])

        for filepath in self.data_folder.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    with open(filepath) as fp:
                        # Appends all tournaments from both completed and in-progress files to the same list
                        data = json.load(fp)
                        for tournament in data:
                            list_tournaments.append(tournament)

                    self.tournaments = list_tournaments

                except json.JSONDecodeError:
                    print(filepath, "is an invalid JSON file.")