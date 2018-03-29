from random import randint
import time

board = []
run_true = ['yes', 'y', 'yeah']

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print("".join(row))


print("Welcome to the Battleships application!")
time.sleep(1)
confirm_input = input("Would you like to play a game? ")


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


if confirm_input in run_true:
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(4):
        print("Turn", turn + 1)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        if int(guess_row) == ship_row and int(guess_col) == ship_col:
            print("Congratulations! You sunk my battleship!")
            time.sleep(5)
            break;
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
                time.sleep(1)
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
                time.sleep(1)
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
                time.sleep(1)
            if turn == 3:
                print("Game Over")
                time.sleep(5)
        print_board(board)
else:
    print("Okay, have a nice day.")
    time.sleep(5)
