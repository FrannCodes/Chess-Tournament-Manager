from commands.context import Context
from .base import BaseCommand
from models import TournamentManager


class ReportCmd(BaseCommand):
    # Command to show tournament report

    def __init__(self, tournament):
        self.tournament = tournament
        self.ranks = []
        self.rounds = []

    def execute(self):
        # The command uses the report method from the Tournament model

        tm = TournamentManager()
        player_points = tm.get_scores(self.tournament)
        self.ranks = tm.return_rankings(player_points)
        self.rounds = tm.return_rounds(self.tournament)

        tournament_details = {}
        for t in tm.tournaments:
            if t["name"] == self.tournament:
                tournament_details = t

        return Context("report-view", tournament=tournament_details)
