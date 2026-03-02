def fibonacci_generator(a: int):
    if a >= 1:
        yield 0
    if a >= 2:
        yield 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
        yield b

n = int(input())
gen = fibonacci_generator(n)

first = True

print(*gen, sep = ",")