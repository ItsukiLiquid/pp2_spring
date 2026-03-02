n = int(input())
my_list = list(map(int, input().split()))
filtered_list = [i >= 0 for i in my_list]
print("Yes" if all(filtered_list) else "No")