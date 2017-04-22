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

def resolve(board):
    solution = []
    solution.append(board)
    last_column=-1
    last_row=[]
    cost = count_target_attack(board)

    while not is_objective(cost):
        #pego o o que tiver maior custo e mudo
        c = 0 #custo da coluna
        i_c =0 #indice da coluna com maior cust
        forbiden_column = -1
        if len(last_row) == len(board):
            forbiden_column = last_column
            last_row=[]
        for i,item in enumerate(cost):
            if item > c and i != forbiden_column:
                c=item
                i_c =i

        column_cost = get_allcost_fromcolumn(board, i_c)
        index_row=0
        row_cost=len(board)
        for i, item in enumerate(column_cost):
            if item < row_cost and (i not in last_row or i_c != last_column):
                row_cost = item
                index_row = i

        #nao pode ser o mesmo da jogada passada
        board[i_c]=index_row
        if last_column == i_c:
            last_row.append(index_row)
        else:
            last_column = i_c
            last_row = [index_row]
        solution.append(board)
        cost = count_target_attack(board) 

    return solution
