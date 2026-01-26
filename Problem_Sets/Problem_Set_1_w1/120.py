def cout_larger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "equal"

a = int(input())
b = int(input())
print(cout_larger(a, b))