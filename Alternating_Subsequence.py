for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    l = 0
    count = 0

    while l != n:
        val = float('-inf')
        if arr[l] < 0:
            while l != n and arr[l] < 0:
                val = max(val, arr[l])
                l += 1
        else:
            while l != n and arr[l] > 0:
                val = max(val, arr[l])
                l += 1
        count += val
            
    print(count)
