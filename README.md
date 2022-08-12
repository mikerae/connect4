![win](/assets/images/win.png)

# Connect4 Game

Code Institute Milestine Project 3
Written in python, developed on GitPod and Git Hub and deployed via Heroku.

## You can view a live version [here](https://connect4-mr.herokuapp.com/)

## How to play
Choose 'N' for a New Game then try to beat the computer.

After choosing 'X' t oplay first, or 'O' to play second; join four of your pieces in a row, either horizontally, vertically or diagonally.

## Saved Games
Game data is stored remotely.
You can review played games by choosing one from the menu before choosing to play a game.
![saved games](/assets/images/intro.png) 

![m](/assets/images/game_data.png)

## Scope
### Minimum Viable Product
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
Should the player, or a third party wish to evaluate game performance, data for each game is stored in the cloud, and is reviewable through the terminal program.
### Developmet Stage 3: Screen Colour
The library ‘Colorama’ provides the user with colour in the terminal as the game is played.
The colorama library can be found at https://pypi.org/project/colorama/
### Developmet Stage: Computor AI
Whilst any form of AI other than the simplest random computer moves is beyond the scope of this project, such AI code is readily available to be used, with appropriate accreditation. Keith Galli explains the AI needed in his youtube video ‘How does a Board Game AI Work? (Connect 4, Othello, Chess, Checkers) - Minimax Algorithm Explained’ 
Such AI needs the following:
- A scoring heuristic: A way for the computer to evaluate the ‘static state’ of the board at any given point in the game
Keith Galli’s scoring method is used
- An Algorithm for the computer to evaluate the future state of the board and decide how best to make a best move based on this evaluation.

#### MiniMax Algorithm and Apha Beta Pruning
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

## Structure: Flow Chart
![flow chart](/assets/images/connect4-flow-chart.png)

## Data Structures
### Stacks
Oscar Nieves, in his article ‘Programming a Connect-4 game on Python’ https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf  recommends the  Stack Data Structure for holding the content of each column. A stack is a simplified list, where the last data to be added is the first to be removed. Oscar Nieves create a class Stack with methods to return the length of the stack object, to add data to the object and to read the last data in the stack. This code is copied with accreditation into a separate python file and imported as a library 
into the project code.
### List of Lists
He used a list of lists to model the 6 * 7 board, where each row was a list of 7 'spaces' for string representations of 'X' and 'O' to be stored.
This data structure was used.
However, Keith Galli (see below) used a different data structure.
Keith chose to use a Numpy Array to to represent the board, and the pieces were integers 1 and 2, whilst spaces were 0.
This difference in data strucures caused many issues in development.
As develpment progressed, Keith's work was followed in preference to Oscars, but significant portions of Keiths code needed to be modified to accomodate my choice of data structurs.
The single most significant issue was the diference in indexing between a Numpy Array and a native python list of lists.
There were other differences.
### Persistent Data
Data about each game is stored in worksheets in the cloud. The program writes game data to the remote googlesheets worksheet. It provides the user with a list of games played, and the facility to read game data for a chosen game.
The API gspread was used to access the spreadsheet and worksheets on goolge drive.
### Game Data: Game Class
A class Game() is used to create and store data about each game. The class has methods facilitating the reading, writing and file management of stored game data. 

