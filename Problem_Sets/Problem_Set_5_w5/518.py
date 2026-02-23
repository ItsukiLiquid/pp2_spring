import re

txt = input()
try:
    p = input()
except EOFError:
    p = ""
pattern = re.escape(p)

x = re.findall(pattern, txt)

# if pattern == " ":
#     x = re.findall(r"\s", txt)
# else:
#     x = re.findall(pattern, txt)
print(len(x))