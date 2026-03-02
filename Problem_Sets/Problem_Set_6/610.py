n = int(input())
my_list = list(map(int, input().split()))
filtered_list = list(filter(lambda x: x != 0, my_list))

print(len(filtered_list))