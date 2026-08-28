from commands import CreateRoundCmd, NoopCmd
from ..base_screen import BaseScreen

class CreateRound(BaseScreen):

    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        print()
        print("Round Created")
        print()

        return CreateRoundCmd(self.tournament["name"])