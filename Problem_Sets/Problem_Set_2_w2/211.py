a, l, r = map(int, input().split())
b = list(map(int, input().split()))

l -= 1
r -= 1

for i in range(l, (l + r + 1) // 2):
    b[i], b[l + r - i] = b[l + r - i], b[i]

print(*b)