import re
txt = input()
pattern = input()

x = re.split(pattern, txt)
print(*x, sep = ",")