n = int(input())
keys = list(map(str, input().split()))
values = list(map(str, input().split()))

x = list(zip(keys, values))
my_dict = {}
for items in x:
    key = items[0]
    value = items[1]
    my_dict[key] = value

key = input()
try:
    print(my_dict[key])
except KeyError:
    print("Not found")