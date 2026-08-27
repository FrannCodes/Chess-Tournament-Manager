from commands import ReportCmd, NoopCmd
from models import TournamentManager
from ..base_screen import BaseScreen

class TournamentReport(BaseScreen):

    display = "- Report -"

    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        print(f"Tournament: {self.tournament["name"].strip()}")
        print(f"From: {self.tournament["dates"]["from"]}")
        print(f"To: {self.tournament["dates"]["to"]}")
        print("- Player Rankings -")

        player_report = ReportCmd(self.tournament["name"])
        player_report()

        for player, points in player_report.ranks:
            print(f"{player} | {points}")

        print()

        print("ROUNDS")

        for i in range(len(player_report.rounds)):
            print(f"-- Round {i + 1} --:")
            for j in range(len(player_report.rounds[i])):
                print(f"- Match {j + 1} -:")
                print(f"Player 1 : {player_report.rounds[i][j]["players"][0]}")
                print(f"Player 2 : {player_report.rounds[i][j]["players"][1]}")
                if player_report.rounds[i][j]["winner"] is None and player_report.rounds[i][j]["completed"] is True:
                    print("Winner : TIE!")
                elif player_report.rounds[i][j]["winner"] is None and player_report.rounds[i][j]["completed"] is False:
                    print("Winner : Not Decided")
                else:
                    print(f"Winner : {player_report.rounds[i][j]["winner"]}!")

                if player_report.rounds[i][j]["completed"] is True:
                    print("Completed")
                else:
                    print("Ongoing")

                print()

        print()

        while True:
            button = self.input_string("Press 'B' to return to Tournament View").upper()
            if button == "B":
                return NoopCmd("tournament-view", tournament = self.tournament)