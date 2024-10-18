n = int(input())

if n < 6:
    print(0)
    exit()

ans = 0

for i in range(6, n + 1):
    curr = i
    count = 0

    j = 2

    while j * j <= curr:
        prev = curr
        while curr % j == 0:
            curr //= j
        
        if curr != prev:
            count += 1
        
        if count > 2:
            break

        j += 1
    
    if curr > 1:
        count += 1
    
    if count == 2:
        ans += 1

print(ans)
