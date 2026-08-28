from commands import TournamentListCmd
from screens.main_menu_tournaments import MainMenu
from screens.tournaments import Advance, CreateRound, EnterResults, RegisterPlayers, TournamentReport, TournamentView, TournamentCreate


class TournamentApp:
    """The main controller for the club management program"""

    SCREENS = {
        "main-menu": MainMenu,
        "create-tournament": TournamentCreate,
        "tournament-view": TournamentView,
        "register-player-view": RegisterPlayers,
        "tournament-report-view": TournamentReport,
        "advance-view": Advance,
        "create-round-view": CreateRound,
        "results-view": EnterResults,
        "exit": False,
    }

    def __init__(self):
        command = TournamentListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            # Get the screen class from the mapping
            screen = self.SCREENS[self.context.screen]
            try:
                # Run the screen and get the command
                command = screen(**self.context.kwargs).run()
                # Run the command and get a context back
                self.context = command()
            except KeyboardInterrupt:
                # Ctrl-C
                print("Bye!")
                self.context.run = False

if __name__ == "__main__":
    app = TournamentApp()
    app.run()
