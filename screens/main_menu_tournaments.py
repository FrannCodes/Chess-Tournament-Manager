from commands import ExitCmd, NoopCmd
from .base_screen import BaseScreen


class MainMenuTournament(BaseScreen):
    """Main menu screen"""

    # Screen displayed when viewing tournaments

    def __init__(self, tournaments):
        self.tournaments = tournaments

    def display(self):
        # Displays list of both completed and in-progress tournaments
        print("Completed and In-progress Tournaments")
        for count, tournament in enumerate(self.tournaments, 1):
            print(count, tournament["name"])

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            # If there are no tournaments, only have to option to make one
            if not self.tournaments:
                print("Select 'C' to create a new tournament or 'X' to quit.")
                value = self.input_string()

                if value.upper() == "C":
                    return NoopCmd("create-tournament")
                elif value.upper() == "X":
                    return ExitCmd()

            else:
                # If there are ongoing tournaments, have the option to make one or view one
                print("Select a tournament to view/manage it, or 'C' to create a new tournament, or 'X' to quit.")
                value = self.input_string()

                if value.isdigit():
                    value = int(value)
                    if value in range(1, len(self.tournaments) + 1):
                        return NoopCmd("tournament-view", tournament=self.tournaments[value - 1])
                elif value.upper() == "C":
                    return NoopCmd("create-tournament")
                elif value.upper() == "X":
                    return ExitCmd()
