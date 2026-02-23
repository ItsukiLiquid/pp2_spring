import re

txt = input()

x = re.findall(r"\d{2,}", txt)
print(*x)