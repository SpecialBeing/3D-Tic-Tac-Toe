import position

class evaluator:

    def winrate(self, pos):
        if(pos.win() == pos.player):
            return 1.00
        if(pos.win() == -1 * pos.player):
            return 0.00
        return 0.50