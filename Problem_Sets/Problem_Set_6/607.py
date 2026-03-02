n = int(input())
my_list = list(map(str, input().split()))
max_word = max(my_list, key = len)
print(max_word)