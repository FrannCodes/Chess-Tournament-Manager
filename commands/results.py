from commands.context import Context
from .base import BaseCommand
from models.tournament import Tournament

class Results(BaseCommand):
    # Command to input results

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        # The command uses the results method from the Tournament model

        t = Tournament("data/tournaments/in-progress.json")
        results = t.results(self.tournament)

        return Context("results-view", results = results)
