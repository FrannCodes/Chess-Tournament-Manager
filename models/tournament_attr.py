from datetime import datetime

class TournamentATTR:
    # A class that contains all tournament information
    # each tournament creates a TournamentATTR object

    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, name, dates, venue, number_of_rounds = 1,
                 current_round = 1, completed = False, players = None, rounds = None):

        self.name = name
        self.dates = dates
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = completed
        self.players = players
        self.finished = False
        self.rounds = rounds

        self.dates_attr = {}

    def __str__(self):
        return f"<{self.name}>"

    def __hash__(self):
        # Returns the hash of the object - useful to use the instance as a key in a dictionary or in a set

        return hash((self.name, self.dates, self.venue, self.number_of_rounds,
                     self.current_round, self.players, self.rounds))

    def __eq__(self, other):
        # Required when __hash__ is defined

        if type(other) is not type(self):
            raise TypeError("'==' is not supported with type %s" % type(other))

        return (self.name,
                self.dates,
                self.venue,
                self.number_of_rounds,
                self.current_round,
                self.players,
                self.rounds) == (
            other.name,
            other.dates,
            other.venue,
            other.number_of_rounds,
            other.current_round,
            other.players,
            other.rounds
        )

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

    def return_attributes (self):
        attributes = {"name": self.name, "dates": self.dates, "venue": self.venue,
                      "number_of_rounds": self.number_of_rounds, "current_round": self.current_round,
                      "completed": self.completed, "players": self.players, "rounds": self.rounds}

        return attributes
