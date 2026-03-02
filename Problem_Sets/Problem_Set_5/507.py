import re
txt = input()
pattern = input()
replace_word = input()

x = re.sub(pattern, replace_word, txt)
print(x)