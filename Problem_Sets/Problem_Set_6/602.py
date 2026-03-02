n = int(input())
original_list = list(map(int, input().split()))
even_list = list(filter(lambda x: x % 2 == 0, original_list))
print(len(even_list))