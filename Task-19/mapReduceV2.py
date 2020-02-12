import string
import subprocess


def cleanWord(word):
    '''
    This method will take a word and remove all leading and trailing symbols i.e. ,.$
    :param word:
    :return: Returns a lowercase the word with no leading/trailling chars
    '''
    cleanWord = word.translate(str.maketrans("","",string.punctuation))
    cleanWord = cleanWord.rstrip()
    cleanWord = cleanWord.lower()

    return cleanWord

def mapper(wordList):
    '''
    This will create a duple of given a list of strings. These tuples will be assigned 1.

    :param wordList: A list of strings to be tupleized
    :return: A list of tuples for all words in the list (string, 1)
    '''
    list_of_tuples = []
    for words in wordList:
        list_of_tuples.append((words,1))
    return list_of_tuples

def reducer(mapped_tuples):
    """
    This will reduce the tuples and add the dictionary so they string keys aren't duplicated but will increment the
    value of the key when it already exist. Example (name,1)(name,1) the return will be (name,2)
    :param mapped_tuples:
    :return: returns a dictions where the strings are keys and the value is equal to the amount of time the words
    show up.
    """
    reducedDictionary = {}
    for tuples in mapped_tuples:
        if tuples[0] in reducedDictionary:
            reducedDictionary[tuples[0]] += 1
        else:
            reducedDictionary[tuples[0]] = 1

    return reducedDictionary

def main():
    #Starting list of strings
    mapList = []

    with open("caesar.txt") as file:
        for line in file:
            line_split = line.split(" ")
            for x in line_split:
                mapList.append(cleanWord(x))
    mapped_tuples = mapper(mapList)

    print(mapped_tuples)
    recudedDictionary = reducer(mapped_tuples)
    print(recudedDictionary)


    printerWriter = open('caesar.csv', 'w')
    # Step 3: Display the results to the console.
    stop = 0
    printerWriter.writelines("Word ,  Count \n")
    for key in recudedDictionary:
        # print(key, recudedDictionary[key])
        printerWriter.writelines("{} , {}\n".format(key, recudedDictionary[key]))

    bash_command = 'hadoop fs -copyFromLocal caesar.csv /data'
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    #output,error = process.communicate()

if __name__ == '__main__':
    main()
