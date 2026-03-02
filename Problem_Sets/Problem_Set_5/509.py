import re
txt = input()

x = re.findall(r"\b\S{3}\b", txt)
print(len(x))