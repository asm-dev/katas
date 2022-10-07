# 'R', [3, 2, 1, 2]      ->  [1, 2, 2, 3]
# 'L', [1, 4, 5, 3, 5 ]  ->  [5, 5, 4, 3, 1]

list1 = [3, 2, 1, 2]
list2 = [3, 2, 1, 2]

def flip(dir, list):
    if dir == "R" or dir =="L":
        list.sort()
        if dir == "L":
            list.reverse()
    return list

print(flip(list1, "R"))
print(flip(list2, "L"))