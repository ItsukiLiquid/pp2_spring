def rounding(a, b):
    if (a % b == 0):
        return int(a / b)
    else:
        if (a / b > 0):
            return int(a / b)
        elif (a / b < 0):
            return int(a / b) - 1
        else:
            return 0

a = int(input())
b = int(input())
print(rounding(a, b))
print(a / b)