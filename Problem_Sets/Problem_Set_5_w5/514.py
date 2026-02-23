import re

pattern = re.compile(r"^\d{0,}$")
txt = input()
x = pattern.search(txt)

print("Match" if x != None else "No match")