"""
Connect4 game for player v. computer
"""

PLAYER = ""

print("\n********************")
print(" Welcome to Connect4")
print("********************\n")

while PLAYER.isspace() or PLAYER == "":
    PLAYER = input("Please tell me your name...\n")

print(f'Hello {PLAYER} , Lets play Connect4\n')
