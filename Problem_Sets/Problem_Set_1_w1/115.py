a = list(map(str, input().split()))
b = input()
isExist = False
for i in a:
    if b in i:
        isExist = True
        break

print(isExist)