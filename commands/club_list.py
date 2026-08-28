from commands.context import Context
from models import ClubManager

from .base import BaseCommand


class ClubListCmd(BaseCommand):
    """Command to get the list of clubs"""
    def __init__(self):
        self.clubs = []

    def execute(self):
        cm = ClubManager()
        self.clubs = cm.clubs
        return Context("main-menu", clubs=cm.clubs)
