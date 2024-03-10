class Solution:
    def compress(self, chars: List[str]) -> int:
        left = len(chars) - 1
        right = len(chars) - 1

        while left > 0:
            counter = 0

            while left != - 1 and chars[left] == chars[right]:
                counter += 1
                left -= 1
            
            if counter != 1:
                chars[left + 1:right + 1] = [chars[right]]
                chars[left + 2:left + 2] = str(counter)
            
            right = left
    
        return len(chars)
