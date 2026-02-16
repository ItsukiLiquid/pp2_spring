import sys
input = sys.stdin.readline
print = sys.stdout.write

a = input().strip()

gen = (a[x] for x in range(len(a) - 1, -1, -1))

first = True
print("".join(gen))
# for i in gen:
#     if first:
#         print(i)
#         first = False
#     else:
#         print(f"{i}")