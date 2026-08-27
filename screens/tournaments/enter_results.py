from commands.results import ResultsCmd
from ..base_screen import BaseScreen

class EnterResults(BaseScreen):

    display = "## Enter Results"

    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        print("Enter the Winners for Each round:")
        winners = []

        for i, match in enumerate(self.tournament["rounds"][-1], 1):
            print("1.) ", match["players"][0])
            print("2.) ", match["players"][1])
            print("3.) TIE")

            winner = 0

            while  winner < 1 or winner > 3:
                winner = self.input_digit(prompt = f"Winner for match {i}")

            match winner:
                case 1: winners.append(match["players"][0])
                case 2: winners.append(match["players"][1])
                case 3: winners.append(None)

        return ResultsCmd(self.tournament["name"], winners)
