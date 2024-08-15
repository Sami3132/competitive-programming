class Solution:
    def intToRoman(self, num: int) -> str:
        converts = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], 
        ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        ans = ""

        for roman, integer in reversed(converts):
            if num // integer:
                count = num // integer
                ans += (roman * count)

                num = num % integer
        
        return ans
