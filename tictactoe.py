#  Imports
import random
import time

# Variables
board =[[" "," "," "],[" "," "," "],[" "," "," "]]
playStatus = True
userPos = []
cpPos = []
count = 0


# User Functions
def printGameBoard():
    global board
    print("\n")
    print(f"     |     |     ")
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ")
    print(f"     |     |     ")


def checkIfSomeoneWon(player):
    global playStatus
    global userPos
    global cpPos
    arr = []
    winningConditions = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],
        [1,4,7],[2,5,8],[0,4,8],[2,4,6]
    ]

    if player == 1:
        arr = userPos
    else:
        arr = cpPos

    for i in winningConditions:
        check =  all(item in arr for item in i)
        if check is True:
            playStatus = False
            break
    
    if playStatus == False:
        if player == 1:
            print("\nYou won the game. Congratulations !!")
        else:
            print("\nComputer won the game. Good game !!")

        printGameBoard()


def machineTurn():
    global board
    global userPos
    global cpPos
    loop = True
    row = 0
    pos = 0

    s = random.randint(0,8)

    while loop:
        if s in userPos:
            s = random.randint(0,8)
        elif s in cpPos:
            s = random.randint(0,8)
        else:
            loop = False

    if s > 5:
        row = 2
        pos = s-6
    elif s > 2:
        row = 1
        pos = s-3
    else:
        row = 0
        pos = s

    board[row][pos] = "O"
    cpPos.append(s)

    return s+1


def GameTurn(sq):
    global board
    global playStatus
    global userPos
    global cpPos
    global count
    row = 0
    pos = 0

    # Check if the square id is valid
    if (0 < sq < 10):
        s = sq-1

        if s > 5:
            row = 2
            pos = s-6
        elif s > 2:
            row = 1
            pos = s-3
        else:
            row = 0
            pos = s

        # Check if the square is empty
        if board[row][pos] == " ":
            board[row][pos] = "X"
            userPos.append(s)
            checkIfSomeoneWon(1)

            # Continue with computer's turn
            if playStatus:
                print("\nComputer's turn...")

                machineSquare = machineTurn()
                time.sleep(2)
                print(f"\nComputer played {machineSquare}...")
                checkIfSomeoneWon(2)

                count += 1

                if count == 5:
                    printGameBoard()
                    print("\nGame draw...")
                    playStatus = False
                
        else:
            print("\nSquare is already taken. Please select an empty square...")

    else:
        print("\nInvalid Square...")


# Main body
if __name__ == "__main__":
    print("Starting new game...........\n")
    print("Select a square and enter the position Of the Square. Computer will be playing O and Player will be playing X")
    
    while playStatus:
        time.sleep(1)
        printGameBoard()
        print("\n")
        userInput = int(input("Enter your position : "))
        GameTurn(userInput)