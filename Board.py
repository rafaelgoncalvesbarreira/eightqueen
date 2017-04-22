import math
class Board:
    def __init__(self, board):
        self.board=board
    def count_attack_target(self):
        cost = []
        for item_index,item in enumerate(self.board):
            cost_item=0
            for another_index,another in enumerate(self.board):
                if item_index == another_index:
                    continue
                dif = math.fabs(item_index - another_index)
                dif = int(dif)
                if item == another:
                    cost_item = cost_item + 1
                if item + dif == another:
                    cost_item = cost_item + 1
                if item - dif == another:
                    cost_item = cost_item + 1
            cost.append(cost_item)
        
        return cost
