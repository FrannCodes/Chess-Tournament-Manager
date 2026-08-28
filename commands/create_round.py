from commands.context import Context
from .base import BaseCommand
from models import TournamentManager

class CreateRoundCmd(BaseCommand):
    # Command to create a round

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):

        tm = TournamentManager()

        tm.matchmaking(self.tournament)

        tournament_details = {}
        for t in tm.tournaments:
            if t["name"] == self.tournament:
                tournament_details = t

        return Context("tournament-view", tournament = tournament_details)