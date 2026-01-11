def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for x in text.lower(): 
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if x.isalpha():
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if x not in dictionary:
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[x] = 0 
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[x] += 1
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}