from datetime import datetime

class TournamentATTR:
    # A class that contains all tournament information
    # each tournament creates a TournamentATTR object

    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, name, dates, venue, number_of_rounds,
                 current_round = 1, players = None, rounds = None):

        self.name = name
        self.dates = dates
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = False
        self.players = players
        self.finished = False
        self.rounds = rounds

        self.dates_attr = {}

    def __str__(self):
        return f"<{self.name}>"

    def serialize_dates(self):
        # Serializes the dates as a dictionary to be converted to JSON

        self.dates["from"] = self.dates_attr["from"].strftime(self.DATE_FORMAT)
        self.dates["to"] = self.dates_attr["to"].strftime(self.DATE_FORMAT)
        return self.dates

    def set_dates(self, from_date, to_date):
        # Sets the dates as a dictionary

        try:
            self.dates_attr["from"] = datetime.strptime(from_date, self.DATE_FORMAT)
            self.dates_attr["to"] = datetime.strptime(to_date, self.DATE_FORMAT)

            if self.dates_attr["from"] > self.dates_attr["to"]:
                raise ValueError(" \"From\" date is later than \"To\" date")

        except ValueError as e:
            print(e)