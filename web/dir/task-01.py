import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename) as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))


Error on line 16:
    print(new_directory("PythonPrograms", "script.py"))
Error on line 10:
    with open (filename) as file:
FileNotFoundError: [Errno 2] No such file or directory: 'script.py'