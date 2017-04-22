import nqueen
if __name__=="__main__":
    #print(nqueen.count_target_attack([1,3,0,2]))
    #print(nqueen.count_target_attack([1,0,3,2]))
    #print(nqueen.count_target_attack([1,2,3,4,5,6,7,0]))

    #nqueen.resolve([1,2,3,0])
    #print(nqueen.count_target_attack([1,0,3,2]))
    #print(nqueen.get_allcost_fromcolumn([1,0,3,2],2))
    solution = nqueen.resolve([1,2,3,0])
    for i in solution:
        print(i)
