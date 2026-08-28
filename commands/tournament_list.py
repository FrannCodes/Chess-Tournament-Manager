from commands.context import Context
from models import TournamentManager
from .base import BaseCommand


class TournamentListCmd(BaseCommand):
    # Command to create a tournament

    def execute(self):
        # Command to get a list of tournaments

        tm = TournamentManager()

        return Context("main-menu", tournaments=tm.tournaments)
