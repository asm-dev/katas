arr = [1, 8, 9, 9, 9, 5, 2]

def remove_number(list, n):
    new_arr = [num for num in list if num != n]
    return new_arr

new_arr = remove_number(arr, max(arr))
print(max(new_arr))
