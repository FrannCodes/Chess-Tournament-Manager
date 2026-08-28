from commands import AdvanceCmd, NoopCmd
from ..base_screen import BaseScreen


class Advance(BaseScreen):

    display = "- Advance -"

    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        print("    Are you sure you want to advance?   ")
        print("----------------------------------------")
        print("- Press 'N' to return to Tournament View")
        print("- Press 'Y' to advance tournament")

        choice = ""

        while choice != "N" and choice != "Y":
            choice = self.input_string().upper()

        if choice == "Y":
            return AdvanceCmd(self.tournament["name"])
        else:
            return NoopCmd("tournament-view", tournament=self.tournament)
