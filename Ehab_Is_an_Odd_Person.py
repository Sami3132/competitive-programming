n = int(input())
arr = list(map(int, input().split()))

odd = [num for num in arr if num % 2 != 0]
even = [num for num in arr if num % 2 == 0]

if len(odd) and len(even):
    print(*sorted(arr))
else:
    print(*arr)
