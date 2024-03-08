n = int(input())
arr = list(map(int, input().split()))

if n == 2:
    arr.sort()
    print(*arr)
    exit()

arr.sort()
i = 0
j = n - 1

ans = []

while i < j:
    ans.append(arr[i])
    ans.append(arr[j])
    i += 1
    j -= 1

if n % 2 != 0:
    ans.append(arr[i])

print(*ans)
