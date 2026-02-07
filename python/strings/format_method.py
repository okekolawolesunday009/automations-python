        # Expr

        # Meaning

        # Example

        # {:d}

        # integer value

        # "{0:.0f}".format(10.5) → '10'

        # {:.2f}

        # floating point with that many decimals

        # '{:.2f}'.format(0.5) → '0.50'

        # {:.2s}

        # string with that many characters

        # '{:.2s}'.format('Python') → 'Py'

        # {:<6s}

        # string aligned to the left that many spaces

        # '{:<6s}'.format('Py') → 'Py    '

        # {:>6s}

        # string aligned to the right that many spaces

        # '{:>6s}'.format('Py') → '    Py'

        # {:^6s}

        # string centered in that many spaces

        # '{:^6s}'.format('Py') → '  Py  '

        # Print the receipt for the customer. The format string ":10,.2f" 

        
# works as follows:
#   - ":10" makes the output 10 characters wide.
#   - "," inserts thousands separators between groups of digits.
#   - ".2" limits the output to two digits after the decimal.
#   - "f" tells Python to expect a floating-point number.
#
print("Subtotal:     ${:10,.2f}".format(subtotal))
print("Sales Tax:    ${:10,.2f}".format(tax_amt))
print("Total:        ${:10,.2f}".format(total))