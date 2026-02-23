import re
txt = input()

x = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", txt)
print(len(x))