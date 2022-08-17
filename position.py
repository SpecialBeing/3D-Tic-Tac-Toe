import numpy as np 

class position:
    player = 1
    board = np.ndarray((4,4,4), int)

    def __init__(self):
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    self.board[i][j][k] = 0

    def validMove(self, x, y, z):
        return (self.board[x][y][z] == 0)

    def validMoves(self):
        moves = []
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    if(validMove(i,j,k)):
                        moves.append([i, j, k])
        return moves

    def move(self, x, y, z):
        if(self.validMove(x,y,z)):
            self.board[x][y][z] = self.player
            self.player *= -1

    def display(self):
        print(self.board)
        print("player " + str(self.player) + " to move")

    def win(self):
        for i in range(0,4):
            for j in range(0,4):
                x = 0
                y = 0
                z = 0
                for k in range(0,4):
                    x += self.board[i][j][k]
                    y += self.board[i][k][j]
                    z += self.board[k][i][j]
                if (x == 4) or (y== 4) or (z == 4):
                    return 1
                if (x == -4) or (y == -4) or (z == -4):
                    return -1
        for i in range(0,4):
            xy = 0
            zx = 0
            yz = 0
            yx = 0
            xz = 0
            zy = 0
            for j in range(0,4):
                xy += self.board[i][j][j]
                zx += self.board[j][i][j]
                yz += self.board[j][j][i]
                yx += self.board[i][j][3 - j]
                xz += self.board[j][i][3 - j]
                zy += self.board[j][3 - j][i]
                if (xy == 4) or (zx == 4) or (yz == 4) or (yx== 4) or (xz == 4) or (zy == 4):
                    return 1
                if (xy == -4) or (zx == -4) or (yz == -4) or (yx == -4) or (xz == -4) or (zy == -4):
                    return -1
        fff = 0
        ffb = 0
        fbf = 0
        fbb = 0
        bff = 0
        bfb = 0
        bbf = 0
        bbb = 0
        for i in range(0,4):
            fff += self.board[i][i][i]
            ffb += self.board[i][i][3 - i]
            fbf += self.board[i][3 - i][i]
            fbb += self.board[i][3 - i][3 - i]
            bff += self.board[3 - i][i][i]
            fbf += self.board[3 - i][i][3 - i]
            bbf += self.board[3 - i][3 - i][i]
            bbb += self.board[3 - i][3 - i][3 - i]
        if (fff == 4) or (ffb == 4) or (fbf == 4) or (fbb == 4) or (bff == 4) or (bfb == 4) or (bbf == 4) or (bbb == 4):
                    return 1
        if (fff == -4) or (ffb == -4) or (fbf == -4) or (fbb == -4) or (bff == -4) or (bfb == -4) or (bbf == -4) or (bbb == -4):
                    return -1
        return 0


    