for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    i = j = 0
    ans = 0

    while i < n:
        while j < n and arr[j] >= j - i + 1:
            j += 1

        ans += (j - i)

        i += 1
    
    print(ans)
