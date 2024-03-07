n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

el1 = 0
el2 = 0
mergedArr = []

while el1 < n and el2 < m:
    if arr1[el1] < arr2[el2]:
        mergedArr.append(arr1[el1])
        el1 += 1
    else:
        mergedArr.append(arr2[el2])
        el2 += 1

mergedArr.extend(arr1[el1:])
mergedArr.extend(arr2[el2:])

print(*mergedArr)
