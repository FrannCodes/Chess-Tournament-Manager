from commands.context import Context
from .base import BaseCommand
from models.tournament import Tournament


class Results(BaseCommand):
    # Command to input results

    def __init__(self, tournament, file):
        self.tournament = tournament
        self.file = file # Could be asking for the tournaments in progress or completed

    def execute(self):
        # The command uses the results method from the Tournament model

        t = Tournament(self.file)
        results = t.results(self.tournament)

        return Context("results-view", results = results)
