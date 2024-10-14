#Write a Python function to find the maximum element in a list of numbers without using the built-in `max()` function.
#If the input list is None or it is empty list, the return value must be None.

# Requirements:
# - Returns greatest element of a list of numbers
# - In case of None input returns None
# - In case of Empty input string, returns None

numbers = (1,2,3,4,7,5,3,9,13,3,5,7)

def get_max(numbers):
    try:
        result = numbers[0]
        for i in numbers:
            if result < i:
                result = i
        return result
    except ValueError:
        return None
    except:
        return None

print (get_max(numbers))

