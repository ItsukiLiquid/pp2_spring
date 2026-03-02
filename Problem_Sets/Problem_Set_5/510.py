import re
txt = input()

x = re.search(r"cat|dog", txt)
print("Yes" if x != None else "No")