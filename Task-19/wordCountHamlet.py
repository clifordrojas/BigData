#Cliford Rojas
#EnhanceIT

import subprocess

"""
This program will read a file named "shakespeare-hamlet.txt" and count the words in the file.
It will print out in the console the word and the number of times the word was used. The document
will be read twice once to establish the dictionary of words used in the file and the second time
to calculate the results.
"""


def mapper():
    # Step 1: Build the dictionary of words used.
    f = open("shakespeare-hamlet.txt", "r")
    tel = {}
    counter = 0
    for lines in f:
        line = f.readline().strip().split(" ")
        for x in line:
            y = x.lower()
            z = y.rstrip(",.;:")
            tel[z] = 1
    # Step 2: Count the amount of times the word was referenced.
    f2 = open("shakespeare-hamlet.txt", "r")
    for linesFiles in f2:
        line2 = f2.readline().strip().split(" ")

        for z in line2:
            y = z.lower()
            a = y.rstrip(",.;:")
            if a in tel:
                tel[a] += 1
    return tel

def reducer(dictToReduce):
    printerWriter = open('HamletCount.csv', 'w')
    # Step 3: Display the results to the console.
    stop = 0
    for key in dictToReduce:
        print(key, dictToReduce[key])
        if stop == 0:
            printerWriter.writelines("Word , Count\n".format(key, dictToReduce[key]))
            stop += 1
        else:
            printerWriter.writelines("{} , {}\n".format(key, dictToReduce[key]))


dictionary = mapper()
reducer(dictionary)

bash_command = 'hadoop fs -copyFromLocal HamletCount.csv /data'
process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
output,error = process.communicate()





