a = int(input())

def isPrime(b):
    if b == 1:
        return "YES"
    else:
        if a % b == 0:
            print("NO")
        else:
            isPrime(b - 1)
isPrime(a) 