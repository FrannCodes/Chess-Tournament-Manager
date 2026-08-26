from commands.create_tournament import CreateTournamentCmd
from ..base_screen import BaseScreen

class TournamentCreate(BaseScreen):

    display = "## Create Tournament"

    def get_command(self):
        print("Enter tournament information: ")
        kwargs = {"name": self.input_string("Name"),
                  "dates": self.input_dates(),
                  "venue": self.input_string("Venue"),
                  "number_of_rounds": self.input_rounds(),
                  "current_round": self.input_rounds("Enter the current round"),
                  "players": [],
                  "rounds" : []}

        return CreateTournamentCmd(**kwargs)
