# python writing files (.txt, .json, .csv)

#1. writing .txt

txt_data = "I like pizza!"

file_path ="Documents/file-write-output.txt"               # relative path
file_path2 = "C:/Users/Ved Dhake/Desktop/write-output.txt" # absolute path

with open(file_path, "w") as file:                # open returns a file object and with closes the file, w is for writing a new file and if it already exists, it will overwrite a file
  file.write(txt_data)
  print(f"Text file {file_path} was created")

try:
  with open(file_path, "x") as file:                # x means write a file only if it does not exist already
    file.write(txt_data)
    print(f"Text file {file_path} was created")
except FileExistsError:
  print("File already exists")


try:
  with open(file_path, "a") as file:                # a means appending a text to a file
    file.write(txt_data)
    print(f"Text file {file_path} was created")
except FileExistsError:
  print("File already exists")

employees = ["Eugene", "squidward", "Spongebob", "Patrick"]

file_path3="Documents/write-output-employees.txt"

try:
  with open(file_path3, "a") as file:                # a means appending a text to a file
    for employee in employees:
      file.write(employee + "\n")
    print(f"Text file {file_path3} was created")
except FileExistsError:
  print("File already exists")

# writing .json

import json

employee = {"name":"Spongebob",
            "age": 30,
            "job":"cook"
            }

file_path4 = "Documents/write-output-employee.json"

try:
  with open(file_path4, "w") as file:
    json.dump(employee, file, indent = 4)               # indent indents the file contents with requried spaces
    print(f"json file {file_path4} was created")
except FileExistsError:
  print("File already exists")


# writing .csv

import csv

employees = [["Name", "Age", "Job"],
            ["Ved", 20, "Student"],
            ["Jack", 30, "unemployeed"]]

file_path5 = "Documents/write-output-employee.csv"

try:
  with open(file_path5, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
      writer.writerow(row)               
    print(f"json file {file_path5} was created")
except FileExistsError:
  print("File already exists")