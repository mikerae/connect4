![Am I Responsive](/assets/images/am-i-responsive.png)

# Connect4 Game
Code Institute Milestine Project 3
Written in python, developed on GitPod and Git Hub and deployed via Heroku.
## You can view a live version [here](https://connect4-mr.herokuapp.com/)
## How to play
Choose 'N' for a New Game then try to beat the computer.

After choosing 'X' t oplay first, or 'O' to play second; join four of your pieces in a row, either horizontally, vertically or diagonally.
## Contents
+ [UXD](#uxd)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
	+ [Skelteton](#skelteton)
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


## Saved Games
Game data is stored remotely.
You can review played games by choosing one from the menu before choosing to play a game.


## Scope
### Minimum Viable Product
[Back to Top](#contents)
Original code meets CI assessment criteria
Complete code presents a working version of the game connect 4
All external resources are clearly credited
Computer AI is dumb : (random computer moves)
Win State Algorithm checking
Player interaction with the computer is easily understood with screen feedback
Player can choose to go first (X) or second (O)
At the end of the game, the player can choose to play again or quit
The game is deployed to Heroku for web-based play.

Since this is a terminal based project, it was decided to follow the work of Oscar Neives in his article 'Programming a Connect-4 game on Python'
- https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf

Oscar has very concise code for basic game play and his structure was followed closely.

### Development Stage 2 : Game data stored in the cloud
[Back to Top](#contents)
Should the player, or a third party wish to evaluate game performance, data for each game is stored in the cloud, and is reviewable through the terminal program.
### Developmet Stage 3: Screen Colour
[Back to Top](#contents)
The library ‘Colorama’ provides the user with colour in the terminal as the game is played.
The colorama library can be found at https://pypi.org/project/colorama/
### Developmet Stage: Computor AI
[Back to Top](#contents)
Whilst any form of AI other than the simplest random computer moves is beyond the scope of this project, such AI code is readily available to be used, with appropriate accreditation. Keith Galli explains the AI needed in his youtube video ‘How does a Board Game AI Work? (Connect 4, Othello, Chess, Checkers) - Minimax Algorithm Explained’ 
Such AI needs the following:
- A scoring heuristic: A way for the computer to evaluate the ‘static state’ of the board at any given point in the game
Keith Galli’s scoring method is used
- An Algorithm for the computer to evaluate the future state of the board and decide how best to make a best move based on this evaluation.

#### MiniMax Algorithm and Apha Beta Pruning
[Back to Top](#contents)
The traditional algorithm used for this is known as the MiniMax algorithm. 
Keith Galli’s code for the MinMax algorithm suited our purpose.
Sebastian Lague’s explanation of Algorithms Explained – minimax and alpha-beta pruning proved very helpful.
Sebastian Lague draws on pseudo code for the MinMax algorithm and alpha beta pruning the links below. A python version of this code is needed for implementation, and this was provided by Keith Galli, then modified by me, where needed. The pseudo code can also be found on the wikipedia links below.

Pseudocode:
- https://pastebin.com/VSehqDM3 - plain minimax
- https://pastebin.com/rZg1Mz9G - alpha beta

More info about the Minimax Algorithm, and Alpha Beta Pruning can be found here:
- https://en.wikipedia.org/wiki/MinimaxWhilst 
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
### Future Development
[Back to Top](#contents)
## Structure
[Back to Top](#contents)
### Flow Chart
![flow chart](/assets/images/flow-chart.png)

### Data Structures
[Back to Top](#contents)
#### Stacks
Oscar Nieves, in his article ‘Programming a Connect-4 game on Python’ https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf  recommends the  Stack Data Structure for holding the content of each column. A stack is a simplified list, where the last data to be added is the first to be removed. Oscar Nieves create a class Stack with methods to return the length of the stack object, to add data to the object and to read the last data in the stack. This code is copied with accreditation into a separate python file and imported as a library 
into the project code.
#### List of Lists
[Back to Top](#contents)
He used a list of lists to model the 6 * 7 board, where each row was a list of 7 'spaces' for string representations of 'X' and 'O' to be stored.
This data structure was used.
However, Keith Galli (see below) used a different data structure.
Keith chose to use a Numpy Array to to represent the board, and the pieces were integers 1 and 2, whilst spaces were 0.
This difference in data strucures caused many issues in development.
As develpment progressed, Keith's work was followed in preference to Oscars, but significant portions of Keiths code needed to be modified to accomodate my choice of data structurs.
The single most significant issue was the diference in indexing between a Numpy Array and a native python list of lists.
There were other differences.
#### Persistent Data
[Back to Top](#contents)
Data about each game is stored in worksheets in the cloud. The program writes game data to the remote googlesheets worksheet. It provides the user with a list of games played, and the facility to read game data for a chosen game.
The API gspread was used to access the spreadsheet and worksheets on goolge drive.
The code to link the project to the external google worksheets was copied from the Code Institue 'Love Sandwiches' walkthrough.
#### Game Data: Game Class
[Back to Top](#contents)
A class Game() is used to create and store data about each game. The class has methods facilitating the reading, writing and file management of stored game data. 
### Skelteton
[Back to Top](#contents)
		+ Input Validation
			+ Features
			+ Methods
				+ Try/Except
				+ While Loops
				+ White Space/No input
			+ Error Feedback
		+ Game Flow 
			+ Feedback
			+ Screens
				+ Welcome
				+ Name Input
				+ Saved Games
				+ Start Choice
				+ Screen Alternating
				+ Game End
				![win](/assets/images/win.png)
				+ Again/End
				+ Screen Shots
				![saved games](/assets/images/intro.png) 

				![m](/assets/images/game_data.png)
### Surface
[Back to Top](#contents)
		+ Colorama
## Technologies Used
[Back to Top](#contents)
+ Language
	+ IDE
	+ Virtual Environment
		+ Preprepared: Code Institute
		+ Updated: Requirements freeze
	+ Git
	+ GitHub
	+ Libraries
		+ slugify
		+ gspread
		+ google docs auth
		+ slugify
		+ math
		+ random
	+ API's
## Resources
[Back to Top](#contents)
+ CI Training Material
	+ Walkthroughs
		+ CI Love sandwiches
		+ Oscar Neives
		+ Keith Galli
		+ 
	+ Python Documantation
		+ DataTime
	+ Gspread Documentation
	+ Stack Overflow
	+ Wikapedia
## Development
[Back to Top](#contents)

+ Full dev of MVP
	+ Walk-throughs and Modification
	+ Requiremnts Freeze
	+ Link to remote Google Spreadsheet
	+ Deply before dev stage 2
+ Testing
	+ Incremental Function Testing
		+ Walkthrough
		+ Code Adaptatation
	+ Intelisence VSC Python Linter
	+ VSC Debugger
		+ Method
		+ Breakpoints
		+ Watch Variable
		+ Case Examples
	+ Manual Testing
		+ Win+check()
		+ Scoring ()
		+ AI
		+ Game Play
	+ Human Testing
	+ PEP8
### Testing
[Back to Top](#contents)
## Bugs and Fixes
[Back to Top](#contents)
	+ inc conidered modification to minimax() thrugh lack of understanding: test to learn
checkwin() for computer is not working properly	
if player goes second, the computer does not show move on the board…
	check_win outputs a tuple().
	check_win[1] outputs win=True/False 

	check_win outputs False if not win
	check_win outputs tuple (column, True) if True:
		Fix: within if statements, boolean was assigned  tuple (col, Boolean)
			return’ renamed to ‘win’
			win only assigned Boolean
			check_win() only returns tuple (col, win)

when minimax:
	check_win with computer first gives false +ve win @ 3 in a row
	empty columns, some full columns
		horizontal, vertical, +ve dia, -ve día
			player first, computer first
				player vertical , computer vertical
				
	errors:
	computer first: -dia: does not return true
		fix: 5 conditionals instead of 4: removed wrong one

Minimax terminal node bugs
	confirmed that with depth not zero, column is output with score
	therefore providing a column value if terminal is not right. removed code and reverted to Neil Galli code
Minimax: Match maximizing_player with approptiate piece i.e.
- True: computer_xo
- False: player_ox
## Known Issues
[Back to Top](#contents)
	+ Ocasional False +ve for Computor win (AI plays X)
		+ eg. game ID: 2022-08-13-10-00-52-445210
	+ AI win choice not taken when availavle (AI plays X )
		+ eg game ID: 2022-08-13-10-18-15-716327
## Deployment
[Back to Top](#contents)
	+ MVP Deployemnt
	+ Hiroku
		+ Method
		+ Auto Update on push
## Acknowledgments
[Back to Top](#contents)
	+ Mentor
	+ CI
	+ Oscar Neives
	+ Keith Galli
	+ Sebastian Lague
	+ Sarah and Emily Rae
