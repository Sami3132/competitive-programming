class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def vowelK(k):
            vowel = {"a", "e", "i", "o", "u"}
            myDict = defaultdict(int)
            ans = l = constant = 0

            for r in range(len(word)):
                if word[r] not in vowel:
                    constant += 1
                else:
                    myDict[word[r]] += 1
                
                while len(myDict) == 5 and constant >= k:
                    ans += (len(word) - r)

                    if word[l] not in vowel:
                        constant -= 1
                    else:
                        if myDict[word[l]] == 1:
                            del myDict[word[l]]
                        else:
                            myDict[word[l]] -= 1
                    
                    l += 1
            
            return ans
        
        return vowelK(k) - vowelK(k + 1)
