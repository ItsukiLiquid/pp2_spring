def squares(a: int):
    init_val = 1
    while init_val <= a:
        yield init_val ** 2
        init_val += 1

n = int(input())
lst = squares(n)

for i in lst:
    print(i)