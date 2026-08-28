from commands.context import Context
from .base import BaseCommand
from models import Tournament, TournamentManager


class AdvanceCmd(BaseCommand):
    # Command to advance a round

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):

        t = Tournament("data/tournaments/in-progress.json")
        advance = t.advance(self.tournament)

        tm = TournamentManager()

        if advance[0] > advance[1]:
            tm.completed(self.tournament)
        else:
            tm.matchmaking(self.tournament)

        tournament_details = {}
        for t in tm.tournaments:
            if t["name"] == self.tournament:
                tournament_details = t

        return Context("tournament-view", tournament=tournament_details)
