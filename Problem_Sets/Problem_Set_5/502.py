import re
s = input()
subs = input()
isSubstring = re.search(subs, s)
print("Yes" if isSubstring != None else "No")