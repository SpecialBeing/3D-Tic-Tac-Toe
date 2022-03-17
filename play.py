from position import Position
from copy import copy, deepcopy

game = Position()

while(True):
    game.display()
    res = game.win()
    if(res != 0):
        print("player " + str(res) + " has won!")
        break
    print("input x:")
    x = input()
    print("input y:")
    y = input()
    print("input z:")
    z = input()
    game.move(x,y,z)
