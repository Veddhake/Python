
import os

file_path = "Documents/test.txt"                                # you can use relative or absolute file paths
file_path2="C:/Users/Ved Dhake/Desktop/test.txt.txt"  # you can either use backslash or double forward slash 

if os.path.exists(file_path):                         # you should be in the folder containing both these current py file and test.txt file to work
  print(f"The location {file_path} exists")

  if os.path.isfile(file_path):
    print("That is a file")
  elif os.path.isdir(file_path):
    print("That is a directory")
else:
  print(f"The location {file_path} does not exists")




