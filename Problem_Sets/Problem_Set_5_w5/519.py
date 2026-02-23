import re

txt = input()

pattern = re.compile(r"\w+")
x = pattern.findall(txt)
print(len(x))