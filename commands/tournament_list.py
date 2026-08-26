from commands.context import Context
from models.tournament_manager import TournamentManager
from .base import BaseCommand

class TournamentListCmd(BaseCommand):
    # Command to create a tournament

    def execute(self):
        # Command to get a list of tournaments

        t = TournamentManager()

        return Context("main-menu", tournaments = t.tournaments)