from commands.register_player import RegisterPlayerCmd
from ..base_screen import BaseScreen

class RegisterPlayers:
    display = "- Register Player -"

    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        print("Enter player name or Chess ID")

        RegisterPlayerCmd(self.tournament["name"])
