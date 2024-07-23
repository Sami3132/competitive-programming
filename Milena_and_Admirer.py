for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    last = arr[len(arr) - 1]
    ans = 0

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > last:
            times = arr[i] // last

            if arr[i] % last:
                times += 1

            last = arr[i] // times
            ans += times - 1
        else:
            last = arr[i]
    
    print(ans)
