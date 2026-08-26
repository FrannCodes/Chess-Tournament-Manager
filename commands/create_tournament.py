from commands.context import Context
from models.tournament import Tournament
from .base import BaseCommand

class CreateTournamentCmd(BaseCommand):
    # Command to create a tournament
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def execute(self, **kwargs):
        # Uses a Tournament instance to create a tournament and add it to the list of created tournaments
        t = Tournament("data/tournaments/in-progress")
        tournament = t.create_tournament(**self.kwargs)

        return Context("tournament-view", tournament = tournament)