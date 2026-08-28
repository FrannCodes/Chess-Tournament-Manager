from commands import RegisterPlayerCmd, ClubListCmd
from ..base_screen import BaseScreen

class RegisterPlayers(BaseScreen):
    display = "- Register Player -"

    def __init__(self, tournament):
        self.tournament = tournament

    def get_command(self):
        print("CLUBS")

        cm = ClubListCmd()
        cm()

        for count, c in enumerate(cm.clubs, 1):
            print(f"{count}. {c.name}")

        club = self.input_club()

        print("PLAYERS")

        for c in cm.clubs:
            if c.name == club:
                for player in c.players:
                    print(f"{player.name}, {player.chess_id}")

        player = self.input_player(club)

        return RegisterPlayerCmd(player, self.tournament["name"], club)
