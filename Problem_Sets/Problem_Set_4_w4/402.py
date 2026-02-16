import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
lst = (x for x in range(0, n + 1, 2))

first = True
for i in lst:
    if first:
        print(str(i))
        first = False
    else:
        print(f",{i}")