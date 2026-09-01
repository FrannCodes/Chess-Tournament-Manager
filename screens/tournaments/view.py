import json
from pathlib import Path
from commands import TournamentListCmd, NoopCmd
from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    def __init__(self, tournament):
        # Tournament view screen
        self.tournament = tournament

    def display(self):
        # Basic Tournament Info
        print(f"-- {self.tournament["name"].strip()} --")
        print("-Dates-")
        print("From:", self.tournament["dates"]["from"])
        print("To:", self.tournament["dates"]["to"])
        print("Venue:", self.tournament["venue"])
        print("Number of Rounds:", self.tournament["number_of_rounds"])

        if not self.tournament["current_round"]:
            print("Completed")
        else:
            print("Current Round:", self.tournament["current_round"])

        print("-Players-")
        if not self.tournament["players"]:
            print("[No Players Registered]")
        else:
            data_folder = Path("data/clubs")
            players = []

            for chess_id in self.tournament["players"]:
                for filepath in data_folder.iterdir():
                    if filepath.is_file() and filepath.suffix == ".json":
                        try:
                            with open(filepath) as fp:
                                data = json.load(fp)

                                for player in data["players"]:
                                    if player["chess_id"] == chess_id:
                                        players.append((player["name"], player["chess_id"]))

                        except json.JSONDecodeError:
                            print("Invalid File")

            for player in players:
                print(f"{player[0]} ({player[1]})")

    def get_command(self):

        while True:
            if self.tournament["completed"] is True:
                print("[Completed Tournament]")
                print("Options:")
                print("Type 'V' to view tournament report")
                print("Type 'B' to return to list of tournaments")

                action = self.input_string()
                if action.upper() == "V":
                    return NoopCmd("tournament-report-view", tournament=self.tournament)
                elif action.upper() == "B":
                    return TournamentListCmd()
            else:
                if len(self.tournament["players"]) < 2 or len(self.tournament["players"]) % 2 != 0:
                    print("[Ongoing Tournament]")
                    print("Options:")
                    print("Type 'P' to register player [You have less than two players or an odd amount of players!]")
                    print("Type 'V' to view tournament report")
                    print("Type 'B' to return to list of tournaments")

                    action = self.input_string()
                    if action.upper() == "P":
                        return NoopCmd("register-player-view", tournament=self.tournament)
                    elif action.upper() == "V":
                        return NoopCmd("tournament-report-view", tournament=self.tournament)
                    elif action.upper() == "B":
                        return TournamentListCmd()

                elif len(self.tournament["players"]) >= 2 and not self.tournament["rounds"]:
                    print("[Ongoing Tournament]")
                    print("Options:")
                    print("Type 'P' to register player")
                    print("Type 'C' to create a round [You don't have any rounds!]")
                    print("Type 'V' to view tournament report")
                    print("Type 'B' to return to list of tournaments")

                    action = self.input_string()
                    if action.upper() == "P":
                        return NoopCmd("register-player-view", tournament=self.tournament)
                    elif action.upper() == "C":
                        return NoopCmd("create-round-view", tournament=self.tournament)
                    elif action.upper() == "V":
                        return NoopCmd("tournament-report-view", tournament=self.tournament)
                    elif action.upper() == "B":
                        return TournamentListCmd()

                else:
                    print("[Ongoing Tournament]")
                    print("Options:")
                    print("Type 'P' to register player")
                    print("Type 'R' to enter results for current round")
                    print("Type 'A' to advance to the next round")
                    print("Type 'V' to view tournament report")
                    print("Type 'B' to return to list of tournaments")

                    action = self.input_string()
                    if action.upper() == "P":
                        return NoopCmd("register-player-view", tournament=self.tournament)
                    elif action.upper() == "R":
                        return NoopCmd("results-view", tournament=self.tournament)
                    elif action.upper() == "A":
                        return NoopCmd("advance-view", tournament=self.tournament)
                    elif action.upper() == "V":
                        return NoopCmd("tournament-report-view", tournament=self.tournament)
                    elif action.upper() == "B":
                        return TournamentListCmd()
