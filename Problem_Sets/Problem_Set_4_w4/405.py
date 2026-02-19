def countdown(number: int):
    init_val = number
    while init_val >= 0:
        yield init_val
        init_val -= 1

n = int(input())
gen = countdown(n)

for i in gen:
    print(i)