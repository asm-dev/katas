def same_case(char1, char2):
    """
    This function compares two characters, if either of them isn't a letter it returns -1, when they're both either capitalised or not capitalised
    (capitalised and capitalised, or not capitalised and not capitalised) it returns 1, and for other cases (taking this as "one is capitalised and the other 
    isn't, or viceversa) it returns -1
    """
    if char1.isalpha() != True or char2.isalpha() != True:
        return -1
    elif (char1.islower() and char2.islower()) or (char1.isupper() and char2.isupper()):
        return 1
    else:
        return 0

# print(f"{same_case('a', 'g')}) # == 1")
# print(f"{same_case('A', 'C')}) # == 1")
# print(f"{same_case('b', 'G')}) # == 0")
# print(f"{same_case('B', 'g')}) # == 0")
# print(f"{same_case('0', '?')}) # == -1")