import random
import socket
import threading

from client import client

main_server = (socket.gethostname(),3000)
template = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]


def connect_player(port):
    try:
        server = socket.socket()
        server.bind(main_server)
        server.listen()
        conn,addr=server.accept()
        conn.send(int.to_bytes(port,"little"))
        conn.close()

        player = socket.socket()
        player.bind(port)
        player.listen()
        conn,addr=player.accept()
        return conn
    finally:
        server.close()


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
def get_data(conn):
    data = conn.recv(1024)
    if data:
        return data.decode("utf-8")
    else:
        raise Exception("FAIL")
        exit(1)



def valid_move(move):
    if grid[move[0]][move[1]]==" ":
        return True
    else:
        return False


def print_grid():
    for y in grid:
        row=""
        for x in grid:
            row.join(x)
        print(row)
    return False


# Setup game
grid = template.copy()
test=client("player1")
test.start()
player1_move = []
player2_move = []

# Connect to clients
player1_socket=connect_player(4001)
player1_socket.send("Player1, Crosses")

player2_socket=connect_player(4002)
player1_socket.send("Player2, Noughts")

# Start game
turn = bool(random.getrandbits(1))
player1_socket.send("Game Start")
player2_socket.send("Game Start")
while check_win(grid) == " ":
    # Get move from player
    if turn:
        player1_socket.send("Your move")
        player1_move = get_data(player1_socket).split(",")
        if valid_move(player1_move):
            grid[player1_move[0],player1_move[1]]="X"
            player1_socket.send("Success")
            player2_socket.send(player1_move)
            turn = not turn
        else:
            player1_socket.send("Failed move")
    else:
        player2_socket.send("Your move")
        player2_move = get_data(player2_socket).split(",")
        if valid_move(player2_move):
            grid[player2_move[0], player2_move[1]] = "O"
            player2_socket.send("Success")
            player1_socket.send(player2_move)
            turn = not turn
        else:
            player2_socket.send("Failed move")
    print_grid()
