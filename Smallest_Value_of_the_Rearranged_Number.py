class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            arr = list(str(num))
            arr.sort()

            if arr[0] == "0":
                for i in range(len(arr)):
                    if arr[i] != "0":
                        arr[i], arr[0] = arr[0], arr[i]
                        break
            
            return int("".join(arr))
        
        else:
            num = abs(num)
            arr = list(str(num))
            arr.sort(reverse = True)

            return -int("".join(arr))
