from commands import TournamentListCmd, NoopCmd
from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    def __init__(self, tournament):
        # Tournament view screen
        self.tournament = tournament

    def display(self):
        # Basic Tournament Info
        print("##", self.tournament["name"].strip())
        print("#-Dates-")
        print("From:", self.tournament["dates"]["from"])
        print("To:", self.tournament["dates"]["to"])
        print("Venue:", self.tournament["venue"])
        print("Number of Rounds:", self.tournament["number_of_rounds"])

        if not self.tournament["current_round"]:
            print("Completed")
        else:
            print("Current Round:", self.tournament["current_round"])

        print("#-Players-")
        if not self.tournament["players"]:
            print("[No Players Registered]")
        else:
            for player in self.tournament["players"]:
                print(player)



    def get_command(self):
        while True:
            if self.tournament["completed"] is True:
                print("##[Completed Tournament]")
                print("##Options:")
                print("Type 'V' to view tournament report")
                print("Type 'B' to return to list of tournaments")

                action = self.input_string()
                if action.upper() == "V":
                    return NoopCmd("tournament-report-view")
                elif action.upper() == "B":
                    return TournamentListCmd()
            else:
                if len(self.tournament["players"]) < 2 or len(self.tournament["players"]) % 2 != 0:
                    print("[Ongoing Tournament]")
                    print("##Options:")
                    print("Type 'P' to register player [You have less than two players or an odd amount of players!]")
                    print("Type 'V' to view tournament report")
                    print("Type 'B' to return to list of tournaments")

                    action = self.input_string()
                    if action.upper() == "P":
                        return NoopCmd("register-player-view")
                    elif action.upper() == "V":
                        return NoopCmd("tournament-report-view")
                    elif action.upper() == "B":
                        return TournamentListCmd()

                elif len(self.tournament["players"]) >= 2 and not self.tournament["rounds"]:
                    print("[Ongoing Tournament]")
                    print("##Options:")
                    print("Type 'P' to register player")
                    print("Type 'C' to create a round [You don't have any rounds!]")
                    print("Type 'V' to view tournament report")
                    print("Type 'B' to return to list of tournaments")

                    action = self.input_string()
                    if action.upper() == "P":
                        return NoopCmd("register-player-view", tournament = self.tournament)
                    elif action.upper() == "C":
                        return NoopCmd("tournament-create")
                    elif action.upper() == "V":
                        return NoopCmd("tournament-report-view")
                    elif action.upper() == "B":
                        return TournamentListCmd()

                else:
                    print("[Ongoing Tournament]")
                    print("##Options:")
                    print("Type 'P' to register player")
                    print("Type 'R' to enter results for current round")
                    print("Type 'A' to advance to the next round")
                    print("Type 'V' to view tournament report")
                    print("Type 'B' to return to list of tournaments")

                    action = self.input_string()
                    if action.upper() == "P":
                        return NoopCmd("register-player-view", tournament = self.tournament)
                    elif action.upper() == "R":
                        return NoopCmd("results-view")
                    elif action.upper() == "A":
                        return NoopCmd("advance-view")
                    elif action.upper() == "V":
                        return NoopCmd("tournament-report-view")
                    elif action.upper() == "B":
                        return TournamentListCmd()