import nqueen
import random
import math
import copy
from specimen import Specimen

def generate_inital_population(population_size, board_size):
    population=[]
    for i in range(population_size):
        subject = Specimen()
        for j in range(board_size):
            subject.board.append(random.randrange(board_size))
        population.append(subject)
    return population   

def calc_fitness(population):
    for subject in population:
        cost = nqueen.count_target_attack(subject.board)
        subject.cost = sum(cost)

def parent_selection(population, parents_size):
    '''
    roulette
    '''
    # max_cost = max([subject.cost for subject in specimen_costs])
    max_cost = population[-1].cost
    all_cost = sum([x.cost for x in population])
    roulette =[]
    for subject in population:
        for i in range(max_cost - subject.cost):
            roulette.append(subject)

    parents=[]
    for i in range(parents_size):
        bingo = random.randrange(len(roulette))
        parents.append(roulette[bingo])
    
    return parents

def reproduction(parents, population_size):
    newpopulation =[]
    while len(newpopulation)<population_size:
        p1_index =random.randrange(len(parents))
        p2_index =random.randrange(len(parents))
        children1, children2 = crossover(parents[p1_index],parents[p2_index])
        newpopulation.append(children1)
        newpopulation.append(children2)
    return newpopulation

def crossover(subject1, subject2):
    chromossome_size = len(subject1.board)
    crossover_point = random.randrange(0,chromossome_size)
    children1 = Specimen()
    children1.board = subject1.board[:crossover_point] + subject2.board[crossover_point:]
    children2 = Specimen()
    children2.board = subject1.board[crossover_point:] + subject2.board[:crossover_point]
    return children1, children2

def mutation(parents, mutation_size):
    mutated =[]
    for i in range(mutation_size):
        parent_index= random.randrange(len(parents))
        copied = copy.deepcopy(parents[parent_index])
        attr_index = random.randrange(len(copied.board))
        value = copied.board[attr_index]
        if random.randrange(2) == 1:
            value = value + 1
        else:
            value = value -1
        if value >= len(copied.board):
            value=0
        if value<0:
            value = len(copied.board)-1

        copied.board[attr_index] = value
        mutated.append(copied)
    
    return mutated

def found(population):
    return population[0].cost == 0

def resolve(board_size, generation_limit = 150, population_size=50):
    population = generate_inital_population(population_size, board_size)
    # cost = nqueen.count_target_attack(board)
    calc_fitness(population)
    population.sort(key = lambda x:x.cost)
    i = 0

    while not found(population) and i < generation_limit:
        parents = parent_selection(population, int(population_size/2))
        population = reproduction(parents, population_size)
        mutation_size = math.ceil(population_size / 20) # 5%
        mutated = mutation(parents,mutation_size)
        population.extend(mutated)
        costs = calc_fitness(population)
        population.sort(key = lambda x:x.cost)
        i = i+1
    
    if population[0].cost==0:
        print("found in {0} generation".format(i))
        return population[0]
    return None