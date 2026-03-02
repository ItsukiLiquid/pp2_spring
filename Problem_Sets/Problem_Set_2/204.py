a = int(input())
b = list(map(int, input().split()))
pos_count = 0
for i in b:
    if i > 0:
        pos_count += 1
print(pos_count)