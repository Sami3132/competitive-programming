class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Dict = defaultdict(int)
        s2Dict = defaultdict(int)

        for c in s1:
            s1Dict[c] += 1
        
        for i in range(len(s1)):
            s2Dict[s2[i]] += 1
        
        if s1Dict == s2Dict:
            return True
        
        for i in range(len(s1), len(s2)):
            s2Dict[s2[i]] += 1
            s2Dict[s2[i - len(s1)]] -= 1

            if s2Dict[s2[i - len(s1)]] == 0:
                del s2Dict[s2[i - len(s1)]]
            
            if s1Dict == s2Dict:
                return True

        return False
