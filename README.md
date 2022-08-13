![Am I Responsive](/assets/images/am-i-responsive.png)

# Connect4 Game
Code Institute Milestone Project 3
Written in python, developed on GitPod and Git Hub and deployed via Heroku.
## You can view a live version [here](https://connect4-mr.herokuapp.com/)
## How to play
Choose 'N' for a New Game then try to beat the computer.

After choosing 'X' to play first, or 'O' to play second; join four of your pieces in a row, either horizontally, vertically or diagonally.
## Contents
+ [UXD](#uxd)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
    + [Surface](#surface)
+ [Technologies Used](#technologies-used)
+ [Resources](#resources)
+ [Development](#development)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Issues](#known-issues)
+ [Deployment](#deployment)
+ [Acknowledgments](#acknowledgments)
## UXD
### Strategy
[Back to Top](#contents)
### User Stories
#### Game Player
The player wants to play a game of Connect4 against the computer, played from the terminal.
#### Site Owner
The site owner wants to present the Connect4 strategy game, written in python, deployed via Heruko, and played from the terminal, where the player plays against the computer which is using Artificial Intelligence.
## Scope
### Minimum Viable Product
[Back to Top](#contents)
#### Features
- Original code meets CI assessment criteria
- Complete code presents a working version of the game connect 4
- All external resources are clearly credited
- Computer AI is dumb : (random computer moves)
- Win State Checking Algorithm: 4 in a row
    - Horizontally
    - Vertically
    - Positive Slope Diagonals
    - Negative Slope Diagonals
- Player interaction with the computer is easily understood with screen feedback
- Player can choose to go first (X) or second (O)
- At the end of the game, the player can choose to play again or quit
- The game is deployed to Heroku for web-based play.
### Development Stage 2 : Game data stored in the cloud
[Back to Top](#contents)

Data for each game is stored on a remote Google Drive in a Google Spreadsheet, and is reviewable through the terminal program. The player, or a third party may review past game data.
### Development Stage 3: Screen Colour
[Back to Top](#contents)

The library ‘Colorama’ provides the user with colour in the terminal as the game is played.
The colorama library can be found at https://pypi.org/project/colorama/
### Development Stage 4: Computor AI
[Back to Top](#contents)

#### AI Requirements:
Whilst any form of AI other than the simplest random computer moves is beyond the scope of this project, such AI code is readily available to be used, with appropriate accreditation. Keith Galli explains the AI needed in his youtube video ‘How does a Board Game AI Work? (Connect 4, Othello, Chess, Checkers) - Minimax Algorithm Explained’ 
https://www.youtube.com/watch?v=y7AKtWGOPAE&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=5
Such AI needs the following:
- A scoring heuristic: A way for the computer to evaluate the ‘static state’ of the board at any given point in the game. Keith Galli’s scoring method counts the number of pieces (either 'X' or 'O') in a 4 space window in the board (horizontally, vertically and diagonally):
    - Number of MaximizingPlayer pieces in the Centre Column (prefer centre column)
    - 3 MaximizingPlayer pieces and 1 empty space (prefer next win move)
    - 2 MaximizingPlayer pieces and 2 empty space (prefer win in 2 moves)
    - 3 MinimizingPlayer pieces and 1 empty space (prefer blocking opponent win)
- An Algorithm for the computer to evaluate the future state of the board and decide how best to make a best move based on this evaluation.

#### Interim AI Stages
Initially the  AI randomly chose a column using the random python module:
```
 # """ Computer makes a random move """
    # col = random.randint(0, 6)
    # if len(columns[col]) < 6:
    #     columns[col].push(computer_xo)
    #     board[6 - len(columns[col])][col] = \
    #         columns[col].peek()
    #     if len(columns[col]) >= 6:
    #         column_full.append(True)
    # else:
    #     computer_move(board, columns, computer_xo, column_full)
    # col = pick_best_move(board, computer_xo)
```
For the next level of AI, the computer chose the best column given the scoring heuristic described above:
```
    # col = pick_best_move(board, computer_xo)
```
The pick_best_move() function was removed from the deployed code, since it was not being called in the deployed code:
```
# def pick_best_move(board, xo):  # Static Method only
#     """ Calculate the best column for next move """
#     valid_locations = get_valid_locations(board)
#     best_score = -10000
#     best_col = random.choice(valid_locations)
#     for col in valid_locations:
#         row = get_next_open_row(board, col)
#         temp_board = [x[:] for x in board]
#         drop_xo(temp_board, row, col, xo)
#         score = score_position(temp_board, xo)
#         if score > best_score:
#             best_score = score
#             best_col = col
#     return best_col
```
#### MiniMax Algorithm and Apha Beta Pruning
[Back to Top](#contents)

The traditional algorithm used for turn based games is known as the MiniMax algorithm. 
Keith Galli’s code for the MinMax algorithm suited our purpose.
Sebastian Lague’s explanation in Algorithms Explained – minimax and alpha-beta pruning proved very helpful.
https://www.youtube.com/watch?v=l-hh51ncgDI&t=14s

In summary:
- the MiniMax Algorithm evaluates the board for each next potential next choice of column, for each future turn, for a given number of turns. If it is the opponent's turn choices are made to minimise the outcome, otherwise they are made to maximise the outcome. At increasing depths the algorithm has to process exponentially increasing possibilities, and therefore has 'exponential time complexity'. This  means it takes exponentially more time to run.
- Alpha Beta pruning removes runtime choices which do not progress the Max or Min calculations, and therefore significantly reduce the runtime of the MiniMax Algorithm.

Sebastian Lague and Keith Galli both use the public domain pseudo code for the MiniMax algorithm and alpha beta pruning. A python version of this code is needed for implementation, and this was provided by Keith Galli, then modified by me, where needed. The pseudo code can also be found on the wikipedia links below.

Pseudocode links provided by Sebastian Lague:
- https://pastebin.com/VSehqDM3 - plain minimax
- https://pastebin.com/rZg1Mz9G - alpha beta

More info about the Minimax Algorithm, and Alpha Beta Pruning can be found here:
- https://en.wikipedia.org/wiki/MinimaxWhilst 
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
### Future Development
[Back to Top](#contents)

Future versions of the game can include:
- Choice of difficulty level:
    - AI level 1: random choice, AI level 2: Static Heuristic, AI level 3: minimax with alpha beta pruning
- A Leader board showing:
    - a league table sorted by player with most wins per difficulty level
    - player with the fastest win per difficulty level
    - player with the least moves per difficulty level
## Structure
[Back to Top](#contents)
### Flow Chart
![flow chart](/assets/images/flow-chart.png)

### Data Structures
[Back to Top](#contents)
#### Stacks
Oscar Nieves, in his article ‘Programming a Connect-4 game on Python’ https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf
recommends the  Stack Data Structure for holding the content of each column.
A stack is a simplified list, where the last data to be added is the first to be removed. Oscar Nieves create a class Stack with methods to return the length of the stack object, to add data to the object and to read the last data in the stack. This code is copied with accreditation into a separate stacks.py file and imported to the run.py file. I provided one additional function:
```
# Code by MR
def build_empty_cols(columns):
    """ Initialises empty column Stacks """
    for col in range(7):
        col = Stack()
        columns.append(col)
    return columns
```
#### List of Lists
[Back to Top](#contents)

Oscar Nieves used a list of lists to model the 6 * 7 board, where each row was a list of 7 'spaces' for string representations of 'X' and 'O' to be stored in.
This data structure was used.
However, Keith Galli (see below) used a different data structure.
Keith chose to use a Numpy Array to to represent the board, and the pieces were integers 1 and 2, whilst spaces were 0.
This difference in data structures caused many issues in development.
As development progressed, Keith's work was followed in preference to Oscars', but significant portions of Keith's code needed to be modified to accommodate my choice of data structure.
The single most significant issue was the difference in indexing between a Numpy Array and a native python list of lists.
#### Game Data: Game() Class
[Back to Top](#contents)

A class Game() is used to create and store data about each game. The class has methods facilitating the game flow, and reading, writing and file management of stored game data.
```
class Game:
    """ Game data storage """
    def __init__(self, board, player, xo):
        self._id = slugify(str(datetime.now()))
        self.player = player
        self.xo = xo
        self.winner = ""
        self.moves = 0
        self.start = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self._end = ""
        self._duration = 0.0
        self.board = board
```
Methods are:
```
def welcome(self):
        """ Initial Instructions """
```
```
def process_win(self, winner, PLAYER, draw):
        """ Displays winner message """
```
```
def final_update(self, board):
        """ Add final data in string form to game object:
        The final state of board,
        The end time of the game,
        The calculated duration of the game in minuets and seconds
        """
```
```
def display_game_data(self):
        """ Displays final game data in terminal"""
```
```
def write_game_data(self, SHEET):
        """
        Stores current game data in a
        google worksheet (connect4) on
        google drive. Solution to storing board
        list from Stack Overflow (https://stackoverflow.
        com/questions/34400635/
        how-to-write-a-table-list-of-lists-
        to-google-spreadsheet-using-gspread)
        """
```
```
def read_game_data(self, worksheet):
        """ Reads game data into game object """
```
Other functions in the game.py module were imported as needed.
#### Persistent Data
[Back to Top](#contents)

Data about each game is stored in worksheets on a remote Google Drive. The program writes game data to the remote googlesheets worksheet. It provides the user with a list of games played, and the facility to read game data for a chosen game.
The API gspread was used to write to and access the spreadsheet and worksheets on goolge drive. Each game was writen to a unique worksheet within the Connect4 Spreadsheet.
A unique Game ID was generated using the datetime.now() method. The start time of the game was captured, and converted to a slug( lowercase, hyphon-separated). This slug was used to name the worksheet ( and could also be used for file path generation later) since the slug form is 'file-path-friendly' for unix and windows operating systems. The Game ID was stored as one of the game record fields.
The game record fields stored were:
- game_id   [slug version of start]
- player    [player inputed name]
- xo        [Player choice of X or O: X playes first]
- winner    [the winner of the game]
- moves     [how many moves were made by the player]
- start     [the datetime.now() time-stamp for the start of the game]
- end       [the datetime.now() time-stamp for the end of the game]
- duration  [the duration of the game, calculated from start and end using the datetime.timedaelta()]
- board     [the content of the board list of lists in its win state]
The code to link the project to the external google worksheets was copied from the Code Institute 'Love Sandwiches' walkthrough.
One can review played games by choosing one from the menu before choosing to play a game. See the development section for a proceedure.
### Skeleton
[Back to Top](#contents)

#### Input Validation
All player inputs were validated to ensure that only acceptable values were passed inti the program.
Unacceptable inputs were:
- White space (the space bar being pressed any number of times, then enter)
- Enter pressed without any other key pressed
- Any value other than values in the required values
##### Features
The following features were built into input validation:
- Input instructions were clearly given
- Where an invalid input was made, the instructions were repeated and correct input invited.
- All input errors were caught using either a while loop or  Try/Except
- Feedback to the user was polite, usually by repetition of the clear input instructions.
### Game Flow 
#### Feedback
As the program progresses, the user is given appropriate feedback.
#### Screens
##### Welcome
The user is greeted and invited to enter their name:
![intro1](/assets/images/intro1.png)
##### Saved Games
The user is invited to review saved games , or continue to play a new game:
![intro2](/assets/images/intro2.png)
##### Game Screens
The game board is displayed as the game progresses until the game is over:
![win](/assets/images/win.png)
##### Display Game data
If the user chooses to display a past game, the data for that game is presented:
![game data](/assets/images/game_data.png)
### Surface
[Back to Top](#contents)

#### Colorama
The colorama library enables colour to be appied to text in the terminal.
https://pypi.org/project/colorama/
A text prefix was added before the desired colour text and a prefix was added if the same colour was not to be continued.
At the begining of the run.py file, colorama needed to be initated, and at the end in neded to be deinitiated.
## Technologies Used
[Back to Top](#contents)

### Language
The project was written in python version 3.8.11
### IDE
The development environment used was GitPod
### Virtual Environment
- A virtual environment was used to ensure compatibility in deployment. A template containing all standard project requirements was prepared by the Code Institute.
- The environment was updated with additional requirements by downloading them into the environment via the terminal, and the requirements.txt file was updated using the following code:
```
pip3 freeze > requirements.txt
```
### Git
Git was used for version control
### GitHub
GitHub was used for external project storage and display
### Libraries
The following libraries were used:
#### Slugify
https://pypi.org/project/python-slugify/

Slugify provided an easy way to convert a long string into a lowercase-and-hyphon string for use as an ID, a worksheet name and possibly a file path name in a form which was compatible with all operating systemns.
#### gspread
https://docs.gspread.org/en/latest/

gspread provided interaction with the remote spreadsheet via the Google Sheets API
```
import gspread
```
#### Google Auth
https://google-auth.readthedocs.io/en/master/

```
from google.oauth2.service_account import Credentials
```
#### Colorama
https://pypi.org/project/colorama/

The colorama library enabled terminal text to be coloured
```
from colorama import init, deinit, Fore
```
#### Python Libraries
The following internal python libraries were used:
- math
- random
- datetime
### API's
The following APIs were used:
- Google Drive
- Googe Sheets
## Resources
[Back to Top](#contents)

The following resources were used:
+ Code Institute Training Material
+ Walkthroughs
    + CI Love sandwiches
    + Oscar Neives: 'Programming a Connect-4 game on Python'
		+ https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf
    + Keith Galli: 'How to Program a Connect 4 AI (implementing the minimax algorithm)
		+ https://www.youtube.com/watch?v=MMLtza3CZFM&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=6
+ Python Documentation
    + DataTime: https://docs.python.org/3/library/datetime.html
+ Gspread Documentation: https://docs.gspread.org/en/latest/
+ Stack Overflow: https://stackoverflow.com/
+ Wikapedia: https://en.wikipedia.org/wiki/Main_Page
## Development
[Back to Top](#contents)

### Setting Up Development Environment
A gitHub repository was created using a required Code Institute template. This template created a virtual environment within the GitPod workspace which contained all the necessary requirements for the Milestone 3 project.

### Procedure for establishing a link to an external file
The procedure for establishing a link to an external file was exactly followed from the Code Institute 'Love Sandwiches' Walkthrough and is as follows:
- A Google Worksheet was created on my personal Google Drive (personal Google account)
- The worksheet was named appropriately and the name recored for later use.
- A bookmark of the link was stored for future reference
- From the Google Cloud Platform https://console.cloud.google.com/ Dashboard:
    - A new project was created
    ![new project](/assets/images/new-project.png)
    - The project was named
    ![name project](/assets/images/name-project.png)
    - The project was selected
    ![select project](/assets/images/select-project.png)
    NB: Creating a new project creates access credentials which are unique for each project.
    - From the hamburger menu select APIs and Services, then Library
    - search for, and select Google Drive
    - click on and enable the Google Drive API
    - Generate a Credentials file:
        - Steps to get your credentials file for users with the "new" form UI:
            - From the "Which API are you using?" dropdown menu, choose Google Drive API
            - For the "What data will you be accessing?" question, select Application Data
            - For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" question, select No, I'm not using them
            - Click Next
            ![credentials type](/assets/images/credentials-type.png)
            - Click Done
            ![your credentials](/assets/images/your-credentials.png)
            - Enter a Service Account name, you can call it anything you like - I will call mine "LoveSandwiches" - then click Create
            ![account service details](/assets/images/account-service-details.png)
            - In the Role Dropdown box choose Basic > Editor then press Continue
            ![editor role](/assets/images/editor-role.png)
            - These options can be left blank, click Done
            ![blank options](/assets/images/blank-options.png)
            - On the next page, click on the Service Account that has been created
            ![select service account](/assets/images/select-service-account.png)
            - On the next page, click on the Keys tab
            ![keys tab](/assets/images/keys-tab.png)
            - Click on the Add Key dropdown and select Create New Key
            -Select JSON and then click Create. This will trigger the json file with your API credentials in it to download to your machine. It will probably be stored in your downloads folder
            ![download json](/assets/images/download-json.png)
    - Steps to Enable Google Sheets API
        - From the hamburger menu, then Library menu, search for Google Sheets API
        - Select Google Sheets API and click Enable
    - IDE steps:
        - Drag the credentials json file to the IDE workshpace
        - rename this file to creds.json
        - open creds.json then copy the client email address (without quotes)
        - In the Google Spreadsheet crested for this project, the Share button was clicked
        - paste the client address, ensure editor is selected, unclick 'notify people', then click 'share'
        - add 'creds.json' to .gitignore then save, to prevent creds.json being uploaded to GitHub and being publicly available when git pushes are made. 
        - In gitpod workspace, pin the workspace to stop gitpod closing it after 14 days.
    - Install required Libraries
        - Google Auth https://google-auth.readthedocs.io/en/master/
        - gspreead https://docs.gspread.org/en/latest/
        - in the terminal:
        ```
        pip3 install gspread google-auth
        ```
    - Add the following imports:
    ```
    import gspread
    from google.oauth2.service_account import Credentials
    ```
    - Add the following code ('connect4' is the name of the spreadsheet to connect to)
    ```
    SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("connect4")
    ```
    - The spreadsheet is now connected
    - Worksheets within the spreadsheet are accessed using:
    ```
    SHEET.worksheet(worksheet_name)
    ```
### Full development of Minimum Viable Product
The Minimum Viable Product as defined in stage one of the development scope above was developed and deployed before progressing to stage two and beyond.

### Oscar Neives' Work
Since this is a terminal based project, it was decided to follow the work of Oscar Neives in his article 'Programming a Connect-4 game on Python'
- https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf

Oscar has very concise code for basic game play and his structure was followed closely.

Modifications were made appropriate to this project's scope.

### Keith Galli's Work
Neil Galli has produced a series of youtube walkthroughs for programming connect4.
The final one, 'How to Program a Connect 4 AI (implementing the minimax algorithm)' was followed closely.
https://www.youtube.com/watch?v=MMLtza3CZFM&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=6

Whilst the essence, structure and extensive sections of Keith's code are copied directly, there were also significant modifications which needed to be made. The reason for these modifications were:
- to match the scope of this project
- In this project, the user interacts with the game via the terminal, whereas in Keith's game, he uses pygame to draw a connect4 board on the screen
- My project (and Oscar Neives' version) use Stacks for column data and nested lists for board data, whereas Keith uses a Numpy Array for both. Keith uses integers to represent game pieces, and I use strings. The indexing for Numpy Arrays and python nests lists are very different.
## Testing
[Back to Top](#contents)

Testing was done constantly throughout development.
### Incremental Function Testing
As each function and logic code was added and adapted, the code was tested to ensure its functionality was as expected.
### Intelisence GitPod Python Linter
Within GipPod, which is a browser based version of the Virtual Studio Code IDE, the Intelisence linter showed code anomalies which were either:
- critical 'red'
- warning 'orange'
- advisory 'blue'
All critical and warning code was corrected.
### VSC Debugger
Extensive use of the built in debugger was used to test the more complex aspects of the code. Breakpoints were used to stop the code at particular points so that the values of particular variables could be examined.
#### Case Example: Checking the code for MiniMax
At first, it seemed to me that the Terminal Node Case code for the minimax algorithm was wrong.
```
if depth == 0 or is_terminal:
        if is_terminal:
            if win_com:  # Edgecase: Computor wins
                return (None, 10000000000000000)
            elif win_ply:  # Edgecase: Player wins
                return (None, -10000000000000000)
            else:  # Draw
                return (None, 0)
        else:  # depth is zero
            return (None, score_position(board, computer_xo, computer_xo))
```
I needed minimax to pass a value for column to the recieving function computer_move()
```
    col = minimax(board, 4, -math.inf, math.inf,
                  True, computer_xo)[0]
```
Initially I set the depth for minimax to zero and immediately the code rejected the returned value of 'None' to col in computer_move(), which needed to use an actual value to write to the column stack.
So I replaced the value for 'None' with the value generated by the now unused function pick_best_move()
```
# def pick_best_move(board, xo):  # Static Method only
#     """ Calculate the best column for next move """
#     valid_locations = get_valid_locations(board)
#     best_score = -10000
#     best_col = random.choice(valid_locations)
#     for col in valid_locations:
#         row = get_next_open_row(board, col)
#         temp_board = [x[:] for x in board]
#         drop_xo(temp_board, row, col, xo)
#         score = score_position(temp_board, xo)
#         if score > best_score:
#             best_score = score
#             best_col = col
#     return best_col
```
I wondered why minimax was not functioning properly.
After reflection, I realised that the depth of minimax was never going to be initialised as zero. It was going to be at least 1 and probably 3 or higher.
I set the depth to 1 and watched the output of minimax (col). It  returned an integer for the chosen column.
This showed me that the original code was correct.
### Manual Testing
Example: The Win_check() function was tested as it was built, but debugging required that it was retested later. All except 1 win scenario were commented out and that scenario was recreated during play, to manually test its functionality. This was repeated for all scenarios, under all circumstance eg player moves first, computer moves first, with some full columns etc.
### AI Parameters
These were set arbitrarily at first, then Keith Galli's preferred parameters were used. Then small adjustments were made.
### Game Play
The game play was tested under various scenarios, including forcing the AI to win in various ways
### Human Testing
Two other people tested the game play without issue.
### PEP8
The code was tested using PEP8 online http://pep8online.com/ and passed without issue.
![run](/assets/images/pep8run.png)
![game](/assets/images/pep8game.png)
![stacks](/assets/images/pep8stack.png)
![ai](/assets/images/pep8ai.png)
![utils](/assets/images/pep8utils.png)
## Bugs and Fixes
[Back to Top](#contents)

A variety of bugs were identified during development and testing.
Two were mentioned above.
Some others were:
- checkwin() for computer is not working properly
    - if player goes second, the computer does not show move on the board…
    - check_win outputs a tuple().
    - Fix: check_win[1] outputs win=True/False
- check_win() outputs False if not win (so far so good)
    - But : check_win outputs tuple (column, True) if True:
        - Fix: within if statements, boolean was assigned  tuple (col, Boolean)
            - return’ renamed to ‘win’
            - win only assigned Boolean
            - check_win() only returns tuple (col, win)
- when minimax is run: check_win with computer first gives false +ve win @ 3 in a row
    - The following combinations were tested
        - for either empty columns or some full columns
            - and for horizontal or vertical or +ve dia or -ve día
                - and for player first or computer first
                    -and for player vertical or computer vertical
    - the errors were:
        - computer first: -dia: does not return true
        - Fix: There were 5 conditionals instead of 4: The incorrect conditional was removed.
- Minimax was not behaving properly: When the maximizing_player was false, the 'computer_xo' was 'xo' instead of 'player_xo'
    - Fix: Match maximizing_player with appropriate piece i.e.
        - True: computer_xo
        - False: player_ox
## Known Issues
[Back to Top](#contents)

### There are occasional false +ve for a Computor win (AI plays X)
- eg. game ID: 2022-08-13-10-00-52-445210
### AI win choice not always taken when available (AI plays X )
- eg game ID: 2022-08-13-10-18-15-716327
## Deployment
[Back to Top](#contents)

### Freeze requirements
Before deployment, the imported libraries were frozen into the requirement.txt file so that they could be available in the deployed virtual environment. The following code was used:
```
pip3 freeze > requirements.txt
```
This is the contents of the project requirements.txt file:
```
cachetools==5.2.0
colorama==0.4.5
google-auth==2.10.0
google-auth-oauthlib==0.5.2
gspread==5.4.0
oauthlib==3.2.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
python-slugify==6.1.2
requests-oauthlib==1.3.1
rsa==4.9
text-unidecode==1.3

```
### Hiroku
The project was deployed to the Heroku platform using the following steps:
- Delete unused resources/libraries
- Add \n to input line
- pip3 freeze > requirements.txt
- commit & push to gitHub
- make Heroku account
- create new app (in Heroku)
- in dashboard : open settings
- in settings : open config vars
    - add config vars
        - creds.json to config vars (these are environment variables, not exposed to the public). Key: “CREDS”, Value: the contents of creds.json
        -  key: “PORT”, Value : “8000”
    - Add build packs:
        - Heroku/python
        - Heroic/nodejs
- in deploy
    - choose deployment method
        - GitHub
        - connect to GitHub
        - Authorise Heroic to access your gitHub
        - search for and connect to repository name
        - choose a deployment method (Enable Automatic Deploys)
        - master/main branch
        - click view to open a web page with the deployment in a browser
## Acknowledgments
[Back to Top](#contents)

Grateful acknowledgment is given to the following
- Mentor: Martina Terlevic for her amazing guidance and encouragement
- Code Institute: for training materials, training environment and specific code
- Oscar Neives: for his article ‘Programming a Connect-4 game on Python’ 
https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf
-  Keith Galli: 
	- for his youtube 'How to Program a Connect 4 AI (implementing the minimax algorithm)' 
	https://www.youtube.com/watch?v=MMLtza3CZFM&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=6
	- for his youtube 'How does a Board Game AI Work? (Connect 4, Othello, Chess, Checkers) - Minimax Algorithm Explained' 
	https://www.youtube.com/watch?v=y7AKtWGOPAE&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=5
- Sebastian Lague: for his youtube Algorithms Explained – minimax and alpha-beta pruning 
https://www.youtube.com/watch?v=l-hh51ncgDI&t=14s
- Sarah and Emily Rae: for their testing of the game

