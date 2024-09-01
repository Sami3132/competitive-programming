class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []
        
        ans = []

        for i in range(m):
            col = []

            for j in range(n):
                col.append(original[j + i * n])
            
            ans.append(col)
        
        return ans
