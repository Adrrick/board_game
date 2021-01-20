from case import Case
from player import Player
from board import Board
from time import sleep
from random import randint, randrange

def initBoard(size, board):
    for i in range(size):
        if i % 2 == 0:
            c = Case(randrange(-400, -50, 50))
        else:
            c = Case(randrange(50, 400, 50))
        board.cases.append(c)

def game(player):
    print(f"It's {player.name} turn!")
    move = randint(1,6) + randint(1,6)
    print(f"It's a {move}.")
    if move == 12:
        print("It's a double!!")
        movement(player, move)
        if player.balance <= 0:
            return None
        sleep(1.0)
        print("----------DOUBLE----------")
        move = randint(1,6) + randint(1,6)
        print(f"It's a {move}.")
        movement(player, move)
    else:
        movement(player, move)
    print("\n")
    sleep(2.0)

def movement(player, move):
    print(f"{player.name} is at position {player.pos}/{b.size}.")
    if (player.pos + move) >= b.size:
        player.pos += move
        player.pos = (player.pos - b.size) - 1
        if player.pos < 0:
            player.pos = 0
    else:
        player.pos += move
    print(f"{player.name} moved to position {player.pos}/{b.size}.")
    print(f"It's a {b.cases[player.pos].value} € case.")
    player.balance += b.cases[player.pos].value
    print(f"{player.name} is now at {player.balance} €.")

if __name__ == "__main__":

    b = Board(40)
    p1 = Player("Player 1")
    p2 = Player("Player 2")

    initBoard(b.size, b)

    turn = randint(1,2)

    while p1.balance > 0 and p2.balance > 0:
        if turn == 1:
            game(p1)
            turn = 2
        else:
            game(p2)
            turn = 1
    
    if p1.balance <= 0:
        print(f"{p2.name} has won ! He had {p2.balance} €.")
    else:
        print(f"{p1.name} has won ! He had {p1.balance} €.")