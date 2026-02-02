a = input()

def check_valid(a):
    isValid = True
    for char in a:
        if (int(char) % 2 != 0):
            isValid = False
            return "Not valid"
            break
    if isValid:
        return "Valid"
print(check_valid(a))