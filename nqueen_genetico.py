import nqueen
import random
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

def reproduction(parents):
    '''
    reprodução gera 25%
    cross over 50%
    elitismo 25%
    '''
    

def mutation(population, mutation_tax):
    pass

def found(population):
    for subject in population:
        if subject.cost == 0:
            return True
    
    return False

def founded_solution(population, costs):
    pass

def resolve(board_size, generation_limit = 150, population_size=50):
    population = generate_inital_population(population_size, board_size)
    # cost = nqueen.count_target_attack(board)
    calc_fitness(population)
    i = 0

    while not found(population) and i < generation_limit:
        population.sort(key = lambda x:x.cost)
        parents = parent_selection(population, int(population_size/2))
        population = reproduction(parents)
        mutation(population)
        costs = calc_fitness(population)
        i = i+1
    
    return founded_solution(population, costs)