class Solution:
    operation = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []

        for i in range(len(expression)):
            op = expression[i]

            if op in self.operation:
                num1 = self.diffWaysToCompute(expression[:i])
                num2 = self.diffWaysToCompute(expression[i + 1:])
            
                for n1 in num1:
                    for n2 in num2:
                        ans.append(self.operation[op](n1, n2))
        
        if ans == []:
            ans.append(int(expression))
        
        return ans
