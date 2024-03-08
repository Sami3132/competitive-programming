for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    ans = float('inf')
    for i in range(1, n):
        if abs(arr[i - 1] - arr[i]) < ans:
            ans = abs(arr[i - 1] - arr[i])
    
    print(ans)
