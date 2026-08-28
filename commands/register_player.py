from commands.context import Context
from .base import BaseCommand
from models import Tournament, TournamentManager


class RegisterPlayerCmd(BaseCommand):
    # Command to register a player

    def __init__(self,chess_id, tournament, club):
        self.club = club
        self.chess_id = chess_id
        self.tournament = tournament

    def execute(self):
        # The command uses the register_player method from the Tournament model

        t = Tournament("data/tournaments/in-progress.json")
        t.register_player(self.chess_id, self.tournament, self.club)

        tm = TournamentManager()
        tournament_details = {}
        for t in tm.tournaments:
            if t["name"] == self.tournament:
                tournament_details = t

        return Context("tournament-view", tournament = tournament_details)
