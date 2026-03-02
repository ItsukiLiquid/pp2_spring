a = int(input())
b = list(map(int, input().split()))
c = sorted(b, reverse = True)
print(*c)