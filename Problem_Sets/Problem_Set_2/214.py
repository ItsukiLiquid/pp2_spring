a = int(input())
b = list(map(int, input().split()))

def count(list_name, value):
    result = 0
    for i in list_name:
        if i == value:
            result += 1
    return result

c = list(set(b))

max_count = 0
max_val = 0

max_counts = []

for i in c:
    i_count = count(b, i)
    if (i_count > max_count):
        max_count = i_count
        max_val = i
for i in c:
    i_count = count(b, i)
    if i_count == max_count:
        max_counts.append(i)

print(min(max_counts))

