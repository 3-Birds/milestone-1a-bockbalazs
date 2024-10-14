# Write a Python function that takes a string as input and counts the frequency of each character 
# in the string. The function should return the character frequencies in a dictionary 
# where keys should be the characters of input string and values represent the number of occurences of each characters.

# In this exercise, the function `character_frequency_counter` takes a string as input, 
# counts the frequency of each character, and then returns the character frequencies. 
# You can run the function with any string you'd like to test.

# Requirements:
# - Returns number of umber of occurences of each characters in a dictionary like in the following sample:
#     {'a': 1, 'b': 2, 'c':3}
# - In case of None input returns None
# - In case of Empty input string, returns None
# - Space characters are missing from output


def get_frequency(input_string):
    try:    
        input_string = str(input_string).replace(' ', '')
        result = {}
        for i in input_string:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        return result
    except ValueError:
        None
    except None:
        None
    except:
        None