from position import position

class human:

    def move(self, Pos):
        while(True):
            print("input x:")
            x = input()
            print("input y:")
            y = input()
            print("input z:")
            z = input()
            if(Pos.validMove(int(x), int(y), int(z))):
                Pos.move(int(x),int(y),int(z))
                return
            else:
                print("invalid move: (" + str(x) + ", " + str(y) + ", " + str(z) + ")")
