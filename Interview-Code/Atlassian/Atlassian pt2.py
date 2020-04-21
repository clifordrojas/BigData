
def isA(input):
    return True if input == "A" else False
def isB(input):
    return True if input == "B" else False
def isC(input):
    return True if input == "C" else False

test_case = ["A","B","C"]

for x in test_case:
    print(isA(x),isB(x),isC(x))

input_string1 = "AABCABBA"

output = ""

for x in input_string1:
    if isA(x) and not isB(x) and not isC(x):
        output += x
for x in input_string1:
    if not isA(x) and isB(x) and not isC(x):
        output += x
for x in input_string1:
    if not isA(x) and not isB(x) and  isC(x):
        output += x

print("\nMy output: "+output)


