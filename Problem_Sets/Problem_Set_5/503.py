import re
s = input()
subs = input()
list_patterns = re.findall(subs, s)
print(len(list_patterns))