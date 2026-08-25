from commands.context import Context
from .base import BaseCommand
from models.tournament import Tournament
from models.tournament_manager import TournamentManager


class Advance(BaseCommand):
    # Command to advance a round

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):

        t = Tournament("data/tournaments/in-progress.json")
        tm = TournamentManager()

        advance = t.advance(self.tournament)

        if advance[0] > advance[1]:
            tm.completed(self.tournament)
        else:
            tm.matchmaking(self.tournament)

        return Context("advance-view", prompt = None)