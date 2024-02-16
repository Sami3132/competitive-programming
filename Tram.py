n = int(input())
maxVal = 0
count = 0

while n > 0:
    i, j = map(int, input().split())
    count += -i + j
    maxVal = max(maxVal, count)
    n -= 1

print(maxVal)
