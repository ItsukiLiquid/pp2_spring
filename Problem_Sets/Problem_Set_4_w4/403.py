def thr_four_div(number: int):
    init_val = 0
    while init_val <= number:
        if init_val % 3 == 0 and init_val % 4 == 0:
            yield init_val
        init_val += 1

n = int(input())
lst = thr_four_div(n)

for i in lst:
    print(i, end = " ")