"""
Connect4 game for player v. computer
"""

PLAYER = ""
PLAYER_POSITION = ""

print("\n********************")
print(" Welcome to Connect4")
print("********************\n")

while PLAYER.isspace() or PLAYER == "":
    PLAYER = input("Please tell me your name...\n")

print(f'Hello {PLAYER}, you can choose to play first (X) or second (O)...\n')
valid = False
while (PLAYER_POSITION.isspace() or PLAYER_POSITION == "") or valid is False:
    PLAYER_POSITION = input("Type X to play first, or O to play second: ")
    if PLAYER_POSITION.upper() == "X":
        print(f'You go first {PLAYER}, Make your first move...\n')
        valid = True
    elif PLAYER_POSITION.upper() == "O":
        print(f"I'll  go first then, {PLAYER}...\n")
        valid = True
    else:
        valid = False
