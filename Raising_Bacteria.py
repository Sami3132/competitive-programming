n = int(input())
ans = 1

while n != 1:
    if n % 2:
        ans += 1
    
    n //= 2

print(ans)
