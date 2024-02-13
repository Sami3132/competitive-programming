if __name__ == '__main__':
    coll = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        coll.append([name, score])
    
    runner_up = float('inf')
    loser = coll[0][1]
    
    for i in range(1, len(coll)):
        if coll[i][1] < loser:
            runner_up = loser
            loser = coll[i][1]
        elif coll[i][1] < runner_up and coll[i][1] != loser:
            runner_up = coll[i][1]
            
    new_coll = []
    
    for i in range(len(coll)):
        if coll[i][1] == runner_up:
            new_coll.append(coll[i])
    
    new_coll.sort()
    for i in range(len(new_coll)):
        print(new_coll[i][0])
