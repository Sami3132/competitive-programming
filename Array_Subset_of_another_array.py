def isSubset( a1, a2, n, m):
    if len(a1) < len(a2): return False
    
    newDict = dict()
    
    for a in a1:
        if a in newDict:
            newDict[a] += 1
        else:
            newDict[a] = 1
    
    for a in a2:
        if a not in newDict or newDict[a] == 0:
            return False
        else:
            newDict[a] -= 1
    
    return True
