n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
sum = 0
longest = 0

while right < n:
    while sum + arr[right] > m:
        sum -= arr[left]
        left += 1

    sum += arr[right]
    right += 1        
    longest = max(longest, right - left)

print(longest)
