n = int(input())
my_list = list(map(int, input().split()))
uniq_set = set(my_list)
uniq_list = [i for i in uniq_set]
print(*sorted(uniq_list))