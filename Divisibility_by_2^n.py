for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    factorTwo = 0

    for el in arr:
        while el % 2 == 0:
            factorTwo += 1
            el //= 2
    
    if factorTwo >= n:
        print(0)
        continue
    
    indexFactorTwo = []

    for i in range(1, n + 1):
        if i % 2:
            continue
        count = 0

        while i % 2 == 0:
            count += 1
            i = i // 2
        
        indexFactorTwo.append(count)
    
    indexFactorTwo.sort(reverse=True)
        
    operations = 0

    for index in indexFactorTwo:
        factorTwo += index
        operations += 1

        if factorTwo >= n:
            break
    
    if factorTwo >= n:
        print(operations)
    else:
        print(-1)
