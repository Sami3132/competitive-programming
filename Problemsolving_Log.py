for _ in range(int(input())):
    time = int(input())
    string = input()

    wordTime = dict()

    for i in range(1, 27):
        wordTime[chr(64 + i)] = i

    for c in string:
        if wordTime[c] > 0:
            wordTime[c] -= 1

    ans = 0

    for key in wordTime:
        if wordTime[key] == 0:
            ans += 1

    print(ans)
