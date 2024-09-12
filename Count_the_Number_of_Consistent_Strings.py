class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mySet = set()
        for letter in allowed:
            if letter not in mySet:
                mySet.add(letter)
        
        ans = 0
        
        for word in words:
            flag = True

            for char in word:
                if char not in mySet:
                    flag = False
                    break
            
            if flag: ans += 1
        
        return ans
