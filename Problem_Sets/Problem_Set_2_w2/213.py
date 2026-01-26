a = int(input())
b = a - 1
isPrime = True
while (b > 1):
    if a % b == 0:
        isPrime = False
        break
    else:
        b -= 1
print("YES" if isPrime else "NO")