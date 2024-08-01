n, t = map(int, input().split())
arr = list(map(int, input().split()))

i = j = 0
ans = 0
total = 0

while j < n:
    if total + arr[j] <= t:
        total += arr[j]
        j += 1
        ans = max(ans, j - i)
    else:
        total -= arr[i]
        i += 1

print(ans)
