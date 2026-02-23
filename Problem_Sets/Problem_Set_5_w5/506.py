import re
txt = input()

x = re.findall(r"\S+@\S+\.+\S+", txt)
print(x[0] if len(x) != 0 else "No email")