def squares(a: int, b: int) -> int:
    init_val = a
    while init_val <= b:
        yield init_val ** 2
        init_val += 1

a, b = map(int, input().split())
gen = squares(a, b)
for x in gen:
    print(x)