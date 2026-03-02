import re
txt = input()

x = re.search("^[a-zA-Z].*\d$", txt)
print("Yes" if x != None else "No")