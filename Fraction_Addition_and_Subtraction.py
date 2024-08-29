class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)
        
        numerator = 0
        denominator = 1
        
        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] in "+-":
                if expression[i] == '-':
                    sign = -1
                i += 1
            
            j = i
            while expression[j] != '/':
                j += 1
            num = sign * int(expression[i:j])
            i = j + 1
            
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            denom = int(expression[i:j])
            i = j
            
            commonDenominator = lcm(denominator, denom)
            numerator = numerator * (commonDenominator // denominator) + num * (commonDenominator // denom)
            denominator = commonDenominator
        
        commonDivisor = gcd(abs(numerator), denominator)
        numerator //= commonDivisor
        denominator //= commonDivisor
        
        return f"{numerator}/{denominator}"
