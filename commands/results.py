from commands.context import Context
from .base import BaseCommand
from models import Tournament, TournamentManager

class ResultsCmd(BaseCommand):
    # Command to input results

    def __init__(self, tournament, winners):
        self.tournament = tournament
        self.winners = winners

    def execute(self):
        # The command uses the results method from the Tournament model

        t = Tournament("data/tournaments/in-progress.json")
        results = t.results(self.tournament, self.winners)

        tm = TournamentManager()
        tournament_details = {}
        for t in tm.tournaments:
            if t["name"] == self.tournament:
                tournament_details = t

        return Context("tournament-view", tournament = tournament_details)
