import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  cwdch = os.getcwd()
  file_path = os.path.join(cwdch, filename)
  with open(file_path, "w") as f:
   timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
   f.write(str(timestamp))
  # Convert the timestamp into a readable format, then into a string

  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(len(str(timestamp))))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd