from functools import reduce

def is_narcissistic(num):
    
    """
    This function allows us to determine wether a number is narcissistic or not - it returns a boolean (True/False)
    It creates a list with the number's digit (e.g. 153 would be [1, 5, 3]).
    It then we uses map() and reduce() to transform and reduce this list. 
    Map() takes each digit and retuns a list with this number/digit powered by the total digits in the original number (e.g. 153 len == 3).
    Reduce() gives us the sum of all of them.
    If the sum == number (e.g. 153 == 153) then this function will return True, and if  sum != number, it will return False.
    """

    digits = []
    for n in range(0, len(str(num))):
        digits.append(int(str(num)[n]))
    # print(f"num_list: {digits}")

    sum = reduce(lambda x, y: x + y, map(lambda x: x ** len(str(num)), digits), 0)
    # print(sum)

    if num == sum:
        return True
    else:
        return False

# print(is_narcissistic(153)) # --> True
# print(is_narcissistic(1652)) # --> False