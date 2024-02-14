n = int(input())
newDict = dict()

for _ in range(n):
    namePhone = input().split()
    newDict[namePhone[0]] = namePhone[1]
    
name = input()

while name:
    if name in newDict:
        print(f"{name}={newDict[name]}")
    else:
        print("Not found")
    try:
        name = input()
    except EOFError:
        break
