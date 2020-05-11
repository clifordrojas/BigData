
counter = 0
odd = []
even = []
#Using string resolve 2 * 2 = 4
#Printf

for x in range(0,11,2):
    even.append(x**2)
    print("{} * {} = {}".format(x,x,x**2))
for x in range(1,11,2):
    odd.append(x**2)
    print("{} * {} = {}".format(x, x, x ** 2))

print("Even List: " + str(even))
print("Odd List: " + str(odd))
