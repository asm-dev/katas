
from functools import reduce


def process_list(elements):
    """
    Gets a numerical list and returns a new one, with those elements changed. Each element of the new list
    would be the average of the old value and the neighbouring values
    """
    processed_list = []
    if len(elements) == 0:
        processed_list = elements
    else:
        for index, element in enumerate(elements):
            new_element = process_element(index, elements)
            processed_list.append(new_element)
        return processed_list


def process_element(index, elements):
    """
    Gets the index of an element and its list, calculates its average with their neighbouring values and returns 
    that average
    """
    indexes = get_neighbours_indexes(index, elements)
    values = get_neighbours_values(indexes, elements)
    averages = get_average(values)
    return averages


def get_neighbours_indexes(index, elements):
    """
    REturns the list of indexes of neighbouring items. It includes the element itself
    """
    indexes = []
    if index == 0:
        # First element
        indexes.append(index + 1)
    elif index == len(elements) - 1:
        # Last element
        indexes.append(index - 1)
    else:
        # Middle element
        indexes.append(index + 1)
        indexes.append(index - 1)

    # We add the element as neibour of itself
    indexes.append(index)

    return indexes


def get_neighbours_values(indexes, elements):
    values = []
    for index in indexes:
        values.append(elements[index])
    return values


def get_average(values):
    """
    Gets a list of numbers and returns their average
    """
    return reduce(lambda a,b: a+b, values, 0) / len(values)


print(process_list([0,1,2,3]))
print(process_list([1,2,1,2,3,2]))