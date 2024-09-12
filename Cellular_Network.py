n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

ans = 0

def binarySearch(city, towers):
    left, right = 0, len(towers) - 1

    while left <= right:
        mid = (left + right) // 2

        if towers[mid] == city:
            return mid
        elif towers[mid] < city:
            left = mid + 1
        else:
            right = mid - 1
        
    return left

for city in cities:
    r = float("inf")
    index = binarySearch(city, towers)

    left = float("inf") if index == 0 else abs(city - towers[index - 1])
    right = float("inf") if index == len(towers) else abs(city - towers[index])

    r = min(left, right)

    ans = max(ans, r)

print(ans)
