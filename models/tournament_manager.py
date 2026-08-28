import json
import random
from pathlib import Path
from .tournament import Tournament
from datetime import datetime

class TournamentManager:
    def __init__(self, data_folder = "data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tournaments = []
        self.refresh()

    def refresh(self):
        list_tournaments = []

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

        self.tournaments.sort(
            key = lambda x: datetime.strptime(x["dates"]["from"], "%d-%m-%Y")
        )

    def completed(self, name):
        #Moves completed tournaments from "in-progress.json" to "completed.json" file when marked as completed

        for t in self.tournaments:
            if t["name"] == name:
                in_progress = Tournament("data/tournaments/in-progress.json")
                completed = Tournament("data/tournaments/completed.json")

                for i in in_progress.tournaments_list:
                    if i["name"] == name:
                        in_progress.remove_tournament(name)
                        completed.create_tournament(name, dates = i["dates"], venue = i["venue"],
                                                    number_of_rounds = i["number_of_rounds"],
                                                    current_round = None, completed = True,
                                                    players = i["players"], rounds = i["rounds"])

        self.refresh()

    def get_scores(self, name):
        tournament = Tournament("data/tournaments/in-progress.json")
        rounds = tournament.return_rounds(name)
        player_points = {}

        if rounds:
            for i in rounds[0]:
                for chess_id in i["players"]:
                    player_points[chess_id] = 0

            for r in rounds:
                for i in r:
                    if i ["completed"]:
                        for chess_id in i["players"]:
                            if i["winner"] == chess_id:
                                player_points[chess_id] += 1
                            elif i["winner"] is None:
                                player_points[chess_id] += 0.5

            return player_points

        else:
            return player_points

    def return_rankings(self, player_points):
        # Returns ranking of players

        ranking = list(player_points.items())
        ranking.sort(key=lambda x: x[1], reverse=True)

        return ranking


    def matchmaking(self, name):
        # Matches players

        tournament = Tournament("data/tournaments/in-progress.json")
        rounds = tournament.return_rounds(name)
        players = tournament.return_players(name)
        matches = []
        group1 = []
        group2 = []

        if not rounds:
            # Splits the players in half, must be an even amount
            # If there is one extra player, they are excluded

            random.shuffle(players)
            for i in range((len(players)) // 2):
                group1.append(players[i])

            for i in range(1, (len(players)) // 2 + 1):
                group2.append(players[-i])

            for player1, player2 in zip(group1, group2):
                pairs = {"players": [player1, player2],
                         "completed": False,
                         "winner": None}

                matches.append(pairs)

            tournament.add_round(name, matches)

        else:
            # Pairs players based on scores

            player_points = self.get_scores(name)

            # Randomize pairs if they have the same points

            point_groups = {}
            for player, points in player_points.items():
                if points not in point_groups:
                    point_groups[points] = []
                point_groups[points].append(player)

            for points in point_groups.keys():
                random.shuffle(point_groups[points])

            # Convert the point_groups back into dictionary
            player_points_updated = {}
            for points, player in point_groups.items():
                for p in player:
                    player_points_updated[p] = points

            # Turns player_points_updated into a list of tuples (Ranked highest to lowest)
            ranking = self.return_rankings(player_points_updated)

            # Pairs the players based on ranking
            for i in range(0, len(ranking), 2):
                players = [ranking[i][0], ranking[i+1][0]]
                pairs = {"players": players,
                         "completed": False,
                         "winner": None}

                matches.append(pairs)

            tournament.add_round(name, matches)

        self.refresh()