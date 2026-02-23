import re
txt = input()

def double_values(match: re.Match) -> str:
    return match.group() * 2
x = re.sub(r"\d", double_values, txt)
print(x)