from collections import defaultdict

n = int(input())
pokemons = input()

mySet = set(pokemons)

i = 0
myDict = defaultdict(int)
ans = float('inf')

for j in range(n):
    myDict[pokemons[j]] += 1

    while len(mySet) == len(myDict):
        ans = min(ans, j - i + 1)
        myDict[pokemons[i]] -= 1

        if not myDict[pokemons[i]]:
            del myDict[pokemons[i]]

        i += 1

print(ans)
