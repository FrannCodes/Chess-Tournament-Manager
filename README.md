# Chess Tournament Manager

This repository contains the completed work of the tournament program along with the starter code made by OpenClassrooms

### Data files

There are data files provided:
- JSON files for the chess clubs of Springfield and Cornville
- JSON files for two tournaments: one completed, and one in progress

### Models

This package contains the models already defined by the application:
* `Player` is a class that represents a chess player
* `Club` is a class that represents a chess club (including `Player`s)
* `ClubManager` is a manager class that allows to manage all clubs (and create new ones)
* `TournamentATTR` is a class that represents the attributes of a single tournament
* `Tournament` is a class that represents all tournaments in a single file
* `TournamentManager` is a class that manages all tournaments

### Screens

This package contains classes that are used by the application to display information from the models on the screen.
Each screen returns a Command instance (= the action to be carried out).

### Commands

This package contains "commands" - instances of classes that are used to perform operations from the program.
Commands follow a *template pattern*. They **must** define the `execute` method.
When executed, a command returns a context.

### Main application

* The club application is controlled by `manage_clubs.py`

* The tournament application is controlled by `manage_tournaments.py`

* Based on the current Context instance, it instantiates the screens and runs them. The command returned by the screen is then executed to obtain the next context.

* The application is an infinite loop and stops when a context has the attribute `run` set to False.

### Run
* When running the tournament application, the user starts at the main menu which lets them choose a tournament to view
  * If there are no tournaments, the user will only have the option to create a tournament
* When the user is in tournament view for an ongoing tournament, the user can choose the following options:
  * For a tournament that has at least one active round and even amount of registered players:
  * `Type 'P' to register player`
  * `Type 'R' to enter results for current round`
  * `Type 'A' to advance to the next round`
  * `Type 'V' to view tournament report`
  * `Type 'B' to return to list of tournaments`
  * For a tournament without an active round:
  * `Type 'P' to register player`
  * `Type 'C' to create a round [You don't have any rounds!]`
  * `Type 'V' to view tournament report`
  * `Type 'B' to return to list of tournaments`
  * For a tournament with no/odd players:
  * `Type 'P' to register player [You have less than two players or an odd amount of players!]`
  * `Type 'V' to view tournament report`
  * `Type 'B' to return to list of tournaments`

* The register player option allows the user to register a player
* The create round option allows the user to create a round(Cannot create a round without players)
* The view report option allows the user to view the report of a selected tournament which displays the following information:
  * Name 
  * Start and end date
  * List of Players
  * Player rankings
  * List of rounds and matches in that round
* The advance option allows the user to move on to the next round, prompting the user with a confirmation message (Cannot advance without rounds)
* The results option allows the user to enter results for the current match (Cannot do this without rounds)
* The user can return to the list of tournaments

### flake8-html

To create a new flake8-html report:
* In terminal, enter:
* `python3 -m pip install flake8 flake8-html`
* Then, from the project root, enter:
* `python3 -m flake8 . --format=html --htmldir=flake8-report`
* Finally, enter:
* `open flake8-report/index.html`