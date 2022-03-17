import numpy as np 

class Position:
    player = 1
    board = np.ndarray((4,4,4), int)

    def __init__(self):
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    self.board[i][j][k] = 0

    def move(self, x, y, z):
        if(self.board[x][y][z] == 0):
            self.board[x][y][z] = self.player
            self.player *= -1
        else:
            print("invalid move: (" + str(x) + ", " + str(y) + ", " + str(z) + ")")
        
    def display(self):
        print(self.board)
        print("player " + str(self.player) + " to move")

    def win(self):
        for i in range(0,4):
            for j in range(0,4):
                counter_A = 0
                counter_B = 0
                counter_C = 0
                for k in range(0,4):
                    counter_A += self.board[i][j][k]
                    counter_B += self.board[i][k][j]
                    counter_C += self.board[k][i][j]
                if (counter_A == 4) or (counter_B == 4) or (counter_C == 4):
                    return 1
                if (counter_A == -4) or (counter_B == -4) or (counter_C == -4):
                    return -1
        for i in range(0,4):
            counter_A = 0
            counter_B = 0
            counter_C = 0
            counter_D = 0
            counter_E = 0
            counter_F = 0
            for j in range(0,4):
                counter_A += self.board[i][j][j]
                counter_B += self.board[j][i][j]
                counter_C += self.board[j][j][i]
                counter_D += self.board[i][j][3 - j]
                counter_E += self.board[j][i][3 - j]
                counter_F += self.board[j][3 - j][i]
                if (counter_A == 4) or (counter_B == 4) or (counter_C == 4) or (counter_D == 4) or (counter_E == 4) or (counter_F == 4):
                    return 1
                if (counter_A == -4) or (counter_B == -4) or (counter_C == -4) or (counter_D == -4) or (counter_E == -4) or (counter_F == -4):
                    return -1
        counter_A = 0
        counter_B = 0
        counter_C = 0
        counter_D = 0
        counter_E = 0
        counter_F = 0
        counter_G = 0
        counter_H = 0
        for i in range(0,4):
            counter_A += self.board[i][i][i]
            counter_B += self.board[i][i][3 - i]
            counter_C += self.board[i][3 - i][i]
            counter_D += self.board[i][3 - i][3 - i]
            counter_E += self.board[3 - i][i][i]
            counter_F += self.board[3 - i][i][3 - i]
            counter_G += self.board[3 - i][3 - i][i]
            counter_H += self.board[3 - i][3 - i][3 - i]
        if (counter_A == 4) or (counter_B == 4) or (counter_C == 4) or (counter_D == 4) or (counter_E == 4) or (counter_F == 4) or (counter_G == 4) or (counter_H == 4):
                    return 1
        if (counter_A == -4) or (counter_B == -4) or (counter_C == -4) or (counter_D == -4) or (counter_E == -4) or (counter_F == -4) or (counter_G == -4) or (counter_H== -4):
                    return -1
        return 0


    