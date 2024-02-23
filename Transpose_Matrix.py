class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = [[] * len(matrix) for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed[j].append(matrix[i][j])
        
        return transposed
