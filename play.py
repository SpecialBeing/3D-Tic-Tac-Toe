from position import position
from player import human
from copy import copy, deepcopy

game = position()

playerA = human()
playerB = human()

while(True):
    game.display()
    if(game.player == 1):
        playerA.move(game)
    else:
        playerB.move(game)
    res = game.win()
    if(res != 0):
        print("player " + str(res) + " has won!")
        break
