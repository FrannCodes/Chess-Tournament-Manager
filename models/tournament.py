import json
from .player import Player

class Tournament:
    def __init__(self, name = None, filepath_tournament = None):
       self.name = name
       self.filepath_tournament = filepath_tournament

    def save (self):
        pass

    def create_tournament (self, filepath_club):
        pass

    def register_player (self, filepath_club):
        pass

    def results (self):
        pass

    def advance (self):
        pass

    def report (self):
        pass