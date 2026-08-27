from commands.context import Context
from models import Tournament, TournamentManager
from .base import BaseCommand

class CreateTournamentCmd(BaseCommand):
    # Command to create a tournament
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def execute(self, **kwargs):
        # Uses a Tournament instance to create a tournament and add it to the list of created tournaments
        t = Tournament("data/tournaments/in-progress.json")
        t.create_tournament(**self.kwargs)

        tm = TournamentManager()
        tournament_details = {}
        for t in tm.tournaments:
            if t["name"] == self.kwargs["name"]:
                tournament_details = t

        return Context("tournament-view", tournament = tournament_details)