# unsolved

a = int(input())
b = []
d = dict()
for i in range(a):
    temp_list = list(map(str, input().split()))
    if temp_list[0] == "set":
        key = temp_list[1]
        value = temp_list[2]
        d[key] = value
    elif temp_list[0] == "get":
        key = temp_list[1]
        try:
            print(d[key])
        except KeyError:
            print(f"KE: no key {key} found in the document")
