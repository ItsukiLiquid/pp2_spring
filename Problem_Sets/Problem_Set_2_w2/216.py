a = int(input())
b = list(map(int, input().split()))
c = []
for i in b:
    print("YES" if i not in c else "NO")
    c.append(i)


# another example

# a = int(input())
# b = list(map(int, input().split()))
# c = []
# for i in b:
#     print("NO" if i in c else "YES")
#     c.append(i)

