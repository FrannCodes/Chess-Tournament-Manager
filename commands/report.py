from commands.context import Context
from .base import BaseCommand
from models.tournament import Tournament


class ReportCmd(BaseCommand):
    # Command to show tournament report

    def __init__(self, tournament, file):
        self.tournament = tournament
        self.file = file # Could be asking for a report of a completed/in-progress tournament

    def execute(self):
        # The command uses the report method from the Tournament model

        t = Tournament(self.file)
        report = t.report(self.tournament)

        return Context("report-view", report = report)
