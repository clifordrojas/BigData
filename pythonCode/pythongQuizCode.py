"""
Cliford Rojas
1/25/2020
EnhanceIT Python Quiz Code

"""

import random
import copy
class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __str__(self):
        return "Name: {} Id: {}".format(self.name,self.id)


#Task generate a random integer list
randomNumberList = []

for x in range(30):

    addTo = random.randint(1,10000)
    randomNumberList.append(addTo)


print(randomNumberList, "\n","The size of the list is: {}".format(len(randomNumberList)))

#Creates an object with the overriding method str to display the name and id of the object.
#Currently ID assigned 0 for demonstration purpose
personObject = Person("Cliford R.", 0)
print(personObject)

#Given an unsorted list of numbers find the smallest positive missing number
unSortedNums = [1,9,3,4,7,8,2,0]
counter = 0
flag = True
while (flag):
    if counter in unSortedNums:
        counter +=1
    else:
        flag = False
print("Lowest Number is:"+str(counter))

"""
Difference between Yield and Return
Yield returns generators that you can then use methods to call next. Doens't destroy the variables
Return terminates the programs and destroys the variables

"""

#Remove duplicated from a list
newList = []
weekdays = ['sun','mon','tue', 'sun','mon','tue','wed','thu','fri','wed','thu','fri','sat']
for x in weekdays:
    if x not in newList:
        newList.append(x)
    else:
        pass
weekdays = copy.deepcopy(newList)
print(weekdays)

