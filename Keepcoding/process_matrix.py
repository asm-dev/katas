# Código escrito por Ana Salamanca Montero, espero que os guste :)

from functools import reduce

def process_matrix(matrix):

    """
    What does this function do?
    ---------------------------
    This function takes a matrix (a list of lists, such as [[1,2,3],[1,2,3],[1,2,3]]) and returns a new matrix with the same size and number of elements. 
    The initial matrix elements are transformed and added to the new matrix, which is the return product.


    How are the elements of the initial matrix transformed?
    -------------------------------------------------------
    This function uses two loops (one inside another) to iterate over the matrix. 
    It then transforms each element by calculating the average of this element and the adjacent ones (upwards, downwads, left and right).

    Following the example above, if we took the matrix [[1,2,3],[1,2,3],[1,2,3]] process_matrix() would transform 1 (the first element of the first list) into 
    (1 + adjacent element to the right + adjacent element downwards), as there are no elements before or above 1 in the matrix --> 1 + 2 + 1 = 4, 
    the average value is sum/num of elements, therefore 1 => 4/3 = 1.333333333 (approx) would be the new value of 1 in the new matrix.

    Other examples of transformations would be:
    --- The second one of the first list (2) would be 2 -- (1+2+2+3)/4
    --- The second one of the second list (2) would be 2 (1+2+2+3+2)/5
    --- The last element of the last list (3) would be 2.666666 (aprox) (3+2+3)/3


    What can we use this function for?
    ----------------------------------
    This funcion can be used to process images and apply a filter, as it makes the matrix elements more similar to the adjacent ones it can soften images.
    It can be applied time after time, and each time (due to how the averaging works) each matrix element (which could be a pixel) becomes more and more similar to the others.
    """

    new_matrix = []
    row = 0

    for li in range(len(matrix)):

        new_list = []
        col = 0

        for element in range(len(matrix[row])):

            element = matrix[row][col]
            adjacent_elements = [element,]

            # We get the element ABOVE, if there's any
            if row != 0 and col < len(matrix[row-1]):
                adjacent_elements.append(matrix[row-1][col])

            # We get the element AFTER, if there's any
            if col < len(matrix[row])-1:    
                adjacent_elements.append(matrix[row][col+1])

            # We get the element BELOW, if there's any
            if row < len(matrix)-1 and col < len(matrix[row+1]):
                adjacent_elements.append(matrix[row+1][col])

            # We get the element BEFORE, if there's any
            if col != 0: 
                adjacent_elements.append(matrix[row][col-1])
            
            # We can use these prints to understand what's going on here:
            # ***********************************************************
            # print(f"\Element: {element}")
            # print(f"Position/index: [{row}][{col}]")
            # print(f"Nearby elements: {adjacent_elements}")
            # print(f"Sum: {reduce(lambda a,b: a+b, adjacent_elements)}")
            # print(f"Average: {reduce(lambda a,b: a+b, adjacent_elements)/len(adjacent_elements)}")

            new_element = reduce(lambda a,b: a+b, adjacent_elements)/len(adjacent_elements)
            new_list.append(new_element)
            col += 1
        
        new_matrix.append(new_list)
        row += 1
    
    return new_matrix


# Potential tests:
# ****************
# matrix = [[],[1.1,1.2,1.3,1.4,1.5],[2.1,2.2,2.3,2.4,2.5],[3.1,3.2,3.3,3.4,3.5],[4.1,4.2,4.3,4.4,4.5],[5.1,5.2],[]]
# print(process_matrix(matrix))
# matrix_2 =  [[1,2,3],[4,5,6],[7,8,9]]
# print(process_matrix(matrix_2))
# print(process_matrix([[1],[2],[3],[4]]))