n = int(input())
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

x = zip(list_1, list_2)
result = 0
for numbers in x:
    num1 = numbers[0]
    num2 = numbers[1]
    result += num1 * num2
print(result)