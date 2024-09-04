for _ in range(int(input())):
    num = int(input())
    ans = num & - num

    while num == ans or num & ans == 0:
        ans += 1
    
    print(ans)
