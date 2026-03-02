n = int(input())
my_list = list(map(str, input().split()))
x = enumerate(my_list)
for object in x:
    print(f"{object[0]}:{object[1]}", end = " ")