import math
def count_target_attack(board):
    '''
    Return the cost from every column
    '''
    cost = []
    for item_index,item in enumerate(board):
        cost_item=0
        for another_index,another in enumerate(board):
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

def get_allcost_fromcolumn(board, item_index):
    '''
    Retorn the cost from all row in the column
    '''
    max = len(board)
    item = board[item_index]
    cost = []
    for item in range(max):
        cost_item=0
        for another_index,another in enumerate(board):
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

def is_objective(cost):
    return all(x == 0 for x in cost)

def get_lowest(board, costs, current_row_index):
    index_row=0
    row_cost=len(board)
    for i, item in enumerate(costs):
        if item < row_cost:
            row_cost = item
            index_row = i
    
    if index_row == current_row_index:
        copy=list(costs)
        copy[current_row_index]=len(board)
        index = get_lowest(board, copy, current_row_index)
        if costs[index] <= costs[current_row_index]:
            return index
        else:
            return current_row_index
    else:
        return index_row

def resolve(board):
    solution = []
    solution.append(list(board))
    #last_column=-1
    # last_row=[]
    # last_row_cost={}
    cost = count_target_attack(board)
    forbiden_column = -1

    current_column=0

    while not is_objective(cost):
        column_costs = get_allcost_fromcolumn(board, current_column)
        lowest_row = get_lowest(board,column_costs,current_column)
        board[current_column] = lowest_row
        solution.append(list(board))

        current_column = current_column + 1

        cost = count_target_attack(board) 

    return solution
