from commands.context import Context
from .base import BaseCommand
from models.tournament import Tournament


class RegisterPlayerCmd(BaseCommand):
    # Command to register a player

    def __init__(self,chess_id, tournament, club):
        self.club = club
        self.chess_id = chess_id
        self.tournament = tournament

    def execute(self):
        # The command uses the register_player method from the Tournament model

        t = Tournament("data/tournaments/in-progress.json")
        players = t.register_player(self.chess_id, self.tournament, self.club)

        return Context("register-player-view", tournament = self.tournament, players = players)
