MAX_TEMP = 200000
n, k, q = map(int, input().split())

rec = [0] * (MAX_TEMP + 2)

for _ in range(n):
    l, r = map(int, input().split())
    rec[l] += 1
    rec[r + 1] -= 1

currRec = 0
admissible = [0] * (MAX_TEMP + 1)

for i in range(1, MAX_TEMP + 1):
    currRec += rec[i]
    if currRec >= k:
        admissible[i] = 1

rec = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    rec[i] = rec[i - 1] + admissible[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(rec[b] - rec[a - 1])
