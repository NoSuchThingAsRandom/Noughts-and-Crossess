import random

template = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]


def check_win(grid):
    if grid[0][0] != " " and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[2][0] != " " and grid[2][0] == grid[1][1] == grid[0][2]:
        return grid[2][0]
    for i in range(3):
        if grid[i][0] != " " and grid[i][0] == grid[i][1] == grid[i][2]:
            return grid[i][0]
        if grid[0][i] != " " and grid[0][i] == grid[1][i] == grid[2][i]:
            return grid[0][i]
    return " "


def valid_move(move):
    if grid[int(move[1])][int(move[0])] == " ":
        return True
    else:
        return False


def print_grid(grid):
    for y in grid:
        row = "|"
        for x in y:
            row += (x)
            row += ("|")
        print(row)
    return False


# Setup game
grid = template.copy()
player1_move = []
player2_move = []

# Connect to clients
print("Player1, Crosses")
print("Player2, Noughts")

# Start game
turn = bool(random.getrandbits(1))
print("Game Start")
print_grid(grid)
moves = 0
while check_win(grid) == " ":
    if turn:
        print("Player 1 move")
        player1_move = input("Enter location in form x,y (Starting from 0)").split(",")
        if valid_move(player1_move):
            grid[int(player1_move[1])][int(player1_move[0])] = "X"
            print("Valid move")

            turn = not turn
        else:
            print("Invalid move")
    else:
        print("Player 2 move")
        player2_move = input("Enter location in form x,y (Starting from 0)").split(",")
        if valid_move(player2_move):
            grid[int(player2_move[1])][int(player2_move[0])] = "O"
            print("Valid move")
            turn = not turn
        else:
            print("Failed move")
    moves += 1
    if moves == 9:
        print("DRAW")
        exit(0)
    print_grid(grid)
print(str(check_win(grid)) + " won!")
