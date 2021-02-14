import random

# Our Board
theBoard = {'Top L': ' ', 'Top M': ' ', 'Top R': ' ',
            'Mid L': ' ', 'Mid M': ' ', 'Mid R': ' ',
            'Low L': ' ', 'Low M': ' ', 'Low R': ' '}

# Placeholders
def printBoard(board):
    print(board['Top L'] + ' | ' + board['Top M'] + ' | ' + board['Top R'])
    print('--+---+--')
    print(board['Mid L'] + ' | ' + board['Mid M'] + ' | ' + board['Mid R'])
    print('--+---+--')
    print(board['Low L'] + ' | ' + board['Low M'] + ' | ' + board['Low R'])
    
printBoard(theBoard)

# Rules
def ruleO():
    if theBoard['Top L'] == 'O' and theBoard['Top M'] == 'O' and theBoard['Top R'] == 'O':
        print("Congratulations you won the game")
    elif theBoard['Mid L'] == 'O' and theBoard['Mid M'] == 'O' and theBoard['Mid R'] == 'O':
        print("Congratulations you won the game")
    elif theBoard['Low L'] == 'O' and theBoard['Low M'] == 'O' and theBoard['Low R'] == 'O':
        print("Congratulations you won the game")
    elif theBoard['Top L'] == 'O' and theBoard['Mid L'] == 'O' and theBoard['Low L'] == 'O':
        print("Congratulations you won the game")
    elif theBoard['Top M'] == 'O' and theBoard['Mid M'] == 'O' and theBoard['Low M'] == 'O':
        print("Congratulations you won the game")
    elif theBoard['Top R'] == 'O' and theBoard['Mid R'] == 'O' and theBoard['Low R'] == 'O':
        print("Congratulations you won the game")
    elif theBoard['Top L'] == 'O' and theBoard['Mid M'] == 'O' and theBoard['Low R'] == 'O':
        print("Congratulations you won the game")
    elif theBoard['Top R'] == 'O' and theBoard['Mid M'] == 'O' and theBoard['Low L'] == 'O':
        print("Congratulations you won the game")

def ruleX():
    if theBoard['Top L'] == 'X' and theBoard['Top M'] == 'X' and theBoard['Top R'] == 'X':
        print("Congratulations you won the game")
    elif theBoard['Mid L'] == 'X' and theBoard['Mid M'] == 'X' and theBoard['Mid R'] == 'X':
        print("Congratulations you won the game")
    elif theBoard['Low L'] == 'X' and theBoard['Low M'] == 'X' and theBoard['Low R'] == 'X':
        print("Congratulations you won the game")
    elif theBoard['Top L'] == 'X' and theBoard['Mid L'] == 'X' and theBoard['Low L'] == 'X':
        print("Congratulations you won the game")
    elif theBoard['Top M'] == 'X' and theBoard['Mid M'] == 'X' and theBoard['Low M'] == 'X':
        print("Congratulations you won the game")
    elif theBoard['Top R'] == 'X' and theBoard['Mid R'] == 'X' and theBoard['Low R'] == 'X':
        print("Congratulations you won the game")
    elif theBoard['Top L'] == 'X' and theBoard['Mid M'] == 'X' and theBoard['Low R'] == 'X':
        print("Congratulations you won the game")
    elif theBoard['Top R'] == 'X' and theBoard['Mid M'] == 'X' and theBoard['Low L'] == 'X':
        print("Congratulations you won the game")

# Get who picks a value first
randomChoice1 = "Player1"
randomChoice2 = "Player2"
choice = random.choice([randomChoice1, randomChoice2])
print(choice)

player1 = ''
player2 = ''
valueX = 'X'
valueO = 'O'

# get player value
value = input('Pick and use a value between X and O: ').capitalize()
if value  == 'X':
    player1 = valueX
    player2 = valueO
    print(f"{choice} gets the value {value}")
else:
    player2 = valueX
    player1 = valueO
    print(f"{choice} gets the value {value}")

while True:
    place1 = input('Player1, please pick a place in the board: ').title()
    if place1 in theBoard.keys():
        theBoard[place1] = player1
        printBoard(theBoard)
        if ruleO():
            break
        elif ruleX():
            break
    else:
        print("Place not found.")
        place1 = input('Last chance, pick a place in the board: ').title()
        if place1 in theBoard.keys():
            theBoard[place1] = player1
            printBoard(theBoard)
            if ruleO():
                break
            elif ruleX():
                break
        else:
            print('Chance forfeited.')
    print("Player2 your turn")
    place2 = input('Player2, please pick a place in the board: ').title()
    if place2 in theBoard.keys():
        theBoard[place2] = player2
        printBoard(theBoard)
        if ruleO():
            break
        elif ruleX():
            break
    else:
        print("Place not found.")
        place2 = input('Last chance, pick a place in the board: ').title()
        if place2 in theBoard.keys():
            theBoard[place2] = player2
            printBoard(theBoard)
            if ruleO():
                break
            elif ruleX():
                break
        else:
            print('Chance forfeited.')
    print("Player1 your turn")


