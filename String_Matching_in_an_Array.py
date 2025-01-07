class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        mySet = set()

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[j] in words[i] and words[j] not in mySet:
                        ans.append(words[j])
                        mySet.add(words[j])
        
        return ans
