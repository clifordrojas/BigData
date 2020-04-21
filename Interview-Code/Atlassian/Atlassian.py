#Start
def string_problem(string_iniput):
    '''
    This method will map the string input value and associated count
    for the numbers of times a character is used.
    :param string_iniput: This is an input string that you need to map for the frequency
    of the characters used.
    :return: dictionary of keys used A-Z
    '''
    keys = {}
    for chars in string_iniput:
        # Increment the keys value for duplicates. I.e 'aaa' map to 'a:3'
        if chars in keys and keys[chars]:
            keys[chars] += 1
        else:
            keys[chars] = 1
    return keys


def string_encode(dict_keys):
    '''
    This method will encode the keys based on the dictionary keys passed to it.
    :param dict_keys: Keys to be encoded (compressed)
    :return: A compressed output of the keys
    '''
    output = ""
    for key in dict_keys:
        if dict_keys[key] > 3:
            output += str(dict_keys[key]) + "X" + key
        else:
            output += key * dict_keys[key]

    return output


def main(value="uuuuuuuuuuuu", value2="abbccccuiiiiii"):
    '''
    This class will compress string with number of times a character
    is repeated only if the character is repeated more than three times consecutively.
    The output will be displayed in terminal/console.
    :return: None
    '''
    value = "uuuuuuuuuuuu"
    value2 = "abbccccuiiiiii"

    key_value1 = string_problem(value)
    key_value2 = string_problem(value2)

    encode_keys = string_encode(key_value1)
    encode_keys2 = string_encode(key_value2)

    print(encode_keys)
    print(encode_keys2)


if __name__ == '__main__':
    main()

