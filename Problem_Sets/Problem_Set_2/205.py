import math
a = int(input())
b = math.log2(a)
print("NO" if b-int(b) != 0 else "YES")