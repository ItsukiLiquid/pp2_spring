import re
txt = input()
x = re.findall(r"\w+", txt)
# y = re.split(r"\s", txt)
print(len(x))