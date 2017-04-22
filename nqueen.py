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
    solution.append(list(board))
    last_column=-1
    last_row=[]
    last_row_cost={}
    cost = count_target_attack(board)
    forbiden_column = -1

    while not is_objective(cost):
        #pego o o que tiver maior custo e mudo
        c = 0 #custo da coluna
        i_c =0 #indice da coluna com maior cust
        
        #if len(last_row) == len(board):
        #    forbiden_column = last_column
        #    last_row=[]
        for i,item in enumerate(cost):
            if item > c and i != forbiden_column:
                c=item
                i_c =i

        column_cost = get_allcost_fromcolumn(board, i_c)
        index_row=0
        row_cost=len(board)
        #aqui é que o bixo pega
        for i, item in enumerate(column_cost):
            #is_last_row_ok = i not in last_row
            #if not is_last_row_ok:
            #    pass
            if item < row_cost: #and (is_last_row_ok or i_c != last_column): #esse "or" meio que limpa o last_row
                row_cost = item
                index_row = i

        #nao pode ser o mesmo da jogada passada
        if board[i_c] != index_row:
            board[i_c]=index_row
            forbiden_column = -1
        else:
            #segue a vida
            forbiden_column = i_c
        # if last_column == i_c:
        #     last_row.append(index_row)
        #     last_row_cost[index_row]=row_cost
        # else:
        #     last_column = i_c
        #     last_row = [index_row]
        #     last_row_cost= {index_row:row_cost}
        solution.append(list(board))
        cost = count_target_attack(board) 

    return solution
