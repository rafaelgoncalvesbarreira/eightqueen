import nqueen
import nqueen_genetico
if False: # __name__=="__main__":
    #print(nqueen.count_target_attack([1,3,0,2]))
    #print(nqueen.count_target_attack([1,0,3,2]))
    #print(nqueen.count_target_attack([1,2,3,4,5,6,7,0]))

    #nqueen.resolve([1,2,3,0])
    #print(nqueen.count_target_attack([1,0,3,2]))
    #print(nqueen.get_allcost_fromcolumn([1,0,3,2],2))
    
    # solution = nqueen.resolve([1,2,3,0])
    # solution = nqueen.resolve([1,0,3,2])
    solution = nqueen.resolve([1,2,3,4,5,6,7,0])
    for i in solution:
        print(i)
if __name__=="__main__":
    for i in range(10):
        result = nqueen_genetico.resolve(8,generation_limit =500,population_size=120,)
        if result is not None:
            print(result.board)
        else:
            print("sem resultados")