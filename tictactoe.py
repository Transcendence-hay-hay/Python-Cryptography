# Tic-Tac-Toe Game with Python
from os import system
from time import sleep
from random import choice

# This will be the list that stores all the input values of the user (Ignore the '0' element of the array)
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Just a function to print out some information while starting the game
def initializing():
    print("""
Hello!, Let's play some Tic Tac Toe!
Player 1 = X
Player 2 = O

Please wait...
    """)
    from time import sleep
    sleep(0.5)
    system('cls')

# Just a function that prints out a sample board to show the corresponding numbers to the player
def sampleBoard():
    print('''
 7 | 8 | 9
___|___|___
 4 | 5 | 6
___|___|___
 1 | 2 | 3
   |   |

This is a sample board, the numbers corresponds to each of the box.
Please type the corresponding number later on during the game.
    ''')

# Making use of the elements in the array, we print out the current state of the board while the player is playing
def printBoard():
    print(' {7} | {8} | {9}'.format(*board))
    print("___|___|___ ")
    print(' {4} | {5} | {6}'.format(*board))
    print("___|___|___ ")
    print(' {1} | {2} | {3}'.format(*board))
    print("   |   |    ")

# The function that allows the user's input for which position he wants
def playerMove():
    turn = True
    while turn:
        move = input('Please select a position now: ')
        try:
            move = int(move)
            if move > 0 and move < 10: # Just to make sure that the input is valid
                if board[move] == ' ': # Makes sure that the position is not already filled up before filling it up
                    turn = False
                    board[move] = playerMarker
                else:
                    print('Position is already occupied!')
            else:
                print('Please enter a valid position!')
        except:
            print('Please enter a valid number!')

# Function to check whether any of the players have won
def winCondition(board):
    #Horizontal
    if board[7] == board[8]  and board[8] == board[9] and board[7] != ' ':
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        return True
    elif board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return True
    #Diagonal
    elif board[7] == board[5] and board[5] == board[3] and board[7] != ' ':
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[1] != ' ':
        return True
    #Vertical
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        return True

# Function to check if the board is full, to check for tie condition
def fullBoard(board):
    if board.count(' ') > 1: # Checks for any elements that has not been filled up in the array
        return False
    else:
        return True

# Used for Single Player mode, this is how the computer will execute its moves
def computerMove():
    global computerMarker
    computerMarker = 'O'
    possibleMoves = []
    for i in range(len(board)):
        if (board[i] == ' ') and (i != 0):
            possibleMoves.append(i)
    if (board[5] == ' '): # The 'computer' will always prioritize the box in the middle
        board[5] = computerMarker
        print('Player 2 has chosen position 5 as its move!')
    else:
        move = choice(possibleMoves) # If the box in the middle is filled, then pick any other empty boxes randomly
        board[move] = computerMarker
        print('Player 2 has chosen position ' + str(move) + ' as its move!')

def main():
    initializing()
    sampleBoard()
    print('-' * 100)
    global playerMarker # Probably the only way that I know that allows me to make use of this variable in all the different functions
    turnNumber = 0
    inputCheck = True # This is here to just keep the loop going when the player has typed in a wrong input when choosing the mode
    while inputCheck:
        print('''
Do you wish to play in Single Player Mode or Multiplayer mode?
Type "S" or "M" for either Single or Multi player modes
        ''')
        playerMode = str(input())
        if playerMode.lower() == 's': # Checking for which mode they want
            playerMarker = 'X'
            inputCheck = False # Setting this value to False to stop the loop from continuing after a valid input has been given
            print("You will be starting first and will be using the 'X' player Marker.")
            while not fullBoard(board):
                if not winCondition(board):
                    if turnNumber % 2 == 0: # It will always start from turn 0, if the turn is on an even number, then it means it is the player's turn
                        printBoard()
                        print('It is now your turn!')
                        playerMove()
                        turnNumber += 1
                    else:
                        computerMove() # If the turn is on an odd number, then it means it is the computer's turn
                        turnNumber += 1
                else:
                    if turnNumber % 2 == 0: # Same way to check which player has won the game
                        printBoard()
                        print('Games Over! You lost unfortunately')
                        break
                    else:
                        printBoard()
                        print('Games Over! You Won!')
                        break
            else:
                if not winCondition(board):
                    print('Games Over! It is a Tie!')
        elif playerMode.lower() == 'm':
            inputCheck = False
            while not fullBoard(board):
                if not winCondition(board):
                    if turnNumber % 2 == 0:
                        playerMarker = 'X'
                        printBoard()
                        print("It is Player 1 with the marker 'X' turn!")
                        playerMove()
                        turnNumber += 1
                    else:
                        playerMarker = 'O'
                        printBoard()
                        print("It is Player 2 with the marker 'O' turn!")
                        playerMove()
                        turnNumber += 1
                else:
                    if turnNumber % 2 == 0:
                        printBoard()
                        print("Games Over! Player 2 with the marker 'O' won!")
                        break
                    else:
                        printBoard()
                        print("Games Over! Player 1 with the marker 'X' won!")
                        break
            else:
                if not winCondition(board):
                    print('Games Over! It is a Tie!')
main()
