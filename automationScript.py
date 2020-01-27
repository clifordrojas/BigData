

file = open("testScript.txt", "w+")
counter = 0
for x in file:
    counter = x
if file.readline() == "":
    print("Empty")
else:
    file.writelines(counter)
    print("Note empty: Adding")
file.close()