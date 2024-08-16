class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, string):
            if len(string) == len(digits):
                ans.append(string)
                return
            
            for char in phoneMap[digits[i]]:
                backtrack(i + 1, string + char)

        if digits:
            backtrack(0, "")
        
        return ans
