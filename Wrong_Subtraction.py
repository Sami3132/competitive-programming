num, n = map(int, input().split())

while n > 0:
    if num % 10 != 0:
        num -= 1
    else:
        num //= 10

    n -= 1
print(num)
