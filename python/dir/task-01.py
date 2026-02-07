import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  
  os.path.join(directory, filename)
  with open (filename, "r") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))