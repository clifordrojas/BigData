file = open("testScript.txt", "r+")
counter = 1
line = file.readlines()
if len(line) == 0:
    print("No value, add value")
    file.write(str(counter)+"\n")
else:
    print("Last value is:\t",line[-1])
    counter = int(line[-1]) + 1
    file.write(str(counter) + "\n")

print(line)
file.close()
