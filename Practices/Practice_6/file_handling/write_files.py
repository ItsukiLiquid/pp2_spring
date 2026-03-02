# ex 1: appending text to the file
with open("write.txt", "a") as f1:
    f1.write("Now it has appended from the code")
x = open("write.txt", "r")
print(x.read())
x.close()