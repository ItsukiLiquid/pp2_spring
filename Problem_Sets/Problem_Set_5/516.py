import re

txt = input()

x = re.search(r"Name:\s(.+?), Age:\s(.+)", txt)
print(x.group(1), x.group(2)) if x != None else None