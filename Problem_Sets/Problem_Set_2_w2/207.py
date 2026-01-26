a = int(input())
b = list(map(int, input().split()))
c = max(b)
print(b.index(c) + 1)