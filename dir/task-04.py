import os
def parent_directory():
  relative_path = "~"
  current_path = os.path.abspath(relative_path)
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(relative_path, current_path)

  # Return the absolute path of the parent directory
  return current_path

print(parent_directory())