import re
txt = input()

dig_list = re.findall("\d", txt)
print(*dig_list) 