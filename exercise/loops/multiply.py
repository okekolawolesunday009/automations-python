def multiplication_table(start, stop):
    # Complete the outer loop range

    for x in range(start, stop+1): 
         # Complete the inner loop range
        for y in range(start, stop+1):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
