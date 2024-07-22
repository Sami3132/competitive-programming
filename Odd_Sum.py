n = int(input())
arr = list(map(int, input().split()))

maxOdd = float('-inf')
maxEven = 0

for num in arr:
    if num % 2 == 0:  
        newEven = max(maxEven + num, maxEven, num)
        newOdd = max(maxOdd + num, maxOdd)
    else: 
        newEven = max(maxOdd + num, maxEven)
        newOdd = max(maxEven + num, maxOdd, num)
    
    maxEven, maxOdd = newEven, newOdd

print(maxOdd)
