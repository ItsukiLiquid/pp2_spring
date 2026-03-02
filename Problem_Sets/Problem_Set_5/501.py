import re
txt = input()

x = re.match("Hello", txt)
print("Yes" if x != None else "No")