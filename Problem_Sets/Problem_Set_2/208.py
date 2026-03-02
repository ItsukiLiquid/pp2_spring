powers_of_2 = []
def print_2pow(a, i): # < -- recursion used
    if pow(2, i) <= a:
        powers_of_2.append(pow(2, i))
        print_2pow(a, i + 1)

a = int(input())
print_2pow(a, 0)
for i in powers_of_2:
    print(i, end = " ")