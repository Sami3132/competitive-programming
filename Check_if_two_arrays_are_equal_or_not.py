class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        if len(A) != len(B): return False
        
        newDict = dict()
        
        for a in A:
            if a in newDict:
                newDict[a] += 1
            else:
                newDict[a] = 1
        
        for b in B:
            if b in newDict and newDict[b] != 0:
                newDict[b] -= 1
            else:
                return False
        
        for el in newDict:
            if newDict[el] != 0:
                return False
        
        return True
