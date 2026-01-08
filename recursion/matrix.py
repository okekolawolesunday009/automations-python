# This function uses a set of nested for loops with the range() function 
# to create a matrix of numbers. The upper range value in the range() 
# function should be included in the matrix. The matrix should consist 
# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):


    # It is an optional code style to assign the long variable names in the
    # function parameters to shorter variable names. 
    n1 = initial_number 
    n2 = end_of_first_row+1  # include the upper range value with +1

    # The first for loop will create the rows.
    for row in range(n1, n2):1, 5

        # The nested for loop will create the columns.
        for column in range(n1, n2):1, 5

            # To make the matrix of numbers easier to read, include a space
            # between each number in the rows until the loop reaches the 
            # end of the row. You can override the default behavior of the 
            # print() function (which inserts a new line character after 
            # the print command runs) by using the "end=" "" parameter 
            # inside the print() function.  
              print(column * row, end=" ")

        # The row ends when the inner loop (the columns) is finished.
        # The outer (row) for loop should insert a new line
        # to create the next row. Use the print() function new line default 
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters. 
    # row = 1 ( 1 *1, 1* 2, 1* 3, 1* 4)
    # row = 2 ( 2 *1, 2* 2, 2* 3, 2* 4)
    # row = 3 ( 3 *1, 3* 2, 3*    3, 3* 4)
    # row = 4 ( 4 *1, 4* 2, 4* 3, 4* 4)

matrix(1, 4)
# Should print:
# 1 2 3 4 
# 2 4 6 8 
# 3 6 9 12 
# 4 8 12 16 
