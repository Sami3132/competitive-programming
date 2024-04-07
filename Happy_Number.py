class Solution(object):
    def isHappy(self, n):
        mySet = set()
        while n != 1:
            if n in mySet: return False
            mySet.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True
