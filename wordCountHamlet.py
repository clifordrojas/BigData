#Cliford Rojas
#EnhanceIT



class main():
    """
    This program will read a file named "shakespeare-hamlet.txt" and count the words in the file.
    It will print out in the console the word and the number of times the word was used. The document
    will be read twice once to establish the dictionary of words used in the file and the second time
    to calculate the results. 
    """

    #Step 1: Build the dictionary of words used.
    f = open("shakespeare-hamlet.txt", "r")
    tel = {}
    counter =0
    for lines in f:
        line = f.readline().strip().split(" ")
        for x in line:
            y = x.lower()
            z = y.rstrip(",.;:")
            tel[z] = 1
    #Step 2: Count the amount of times the word was referenced.
    f2 = open("shakespeare-hamlet.txt", "r")
    for linesFiles in f2:
        line2 = f2.readline().strip().split(" ")

        for z in line2:
            y = z.lower()
            a = y.rstrip(",.;:")
            if a in tel:
                tel[a] += 1

    #Step 3: Display the results to the console.
    for key in tel:
        print(key,tel[key])


if __name__ == '__main__':
    main()