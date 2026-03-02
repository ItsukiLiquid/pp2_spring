n = int(input())
my_list = map(int, input().split())
result = 0
for i in my_list:
    result += i**2

print(result)