class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        numbers = {i for i in range(1, n + 1)}

        for i in range(n - 1, -1, -1):
            length = len(numbers)

            if A[i] in numbers:
                numbers.remove(A[i])
            if B[i] in numbers:
                numbers.remove(B[i])
            
            A[i] = length
            
        return A
