# python reading files (.txt, .json, .csv)

# 1. reading .txt docs

file_path1 = "Documents/test.txt"

try:
  with open(file_path1, "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")

# 2. reading .json docs

import json

file_path2 = "Documents/write-output-employee.json"

try:
  with open(file_path2, "r") as file:
    content = json.load(file)
    print(content)                        # used to read everything in json file
    print(content["name"])                # used to read a particular part of json file
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")


# 3. reading .csv files

import csv

file_path3 = "Documents/write-output-employee.csv"

try:
  with open(file_path3, "r") as file:
    content = csv.reader(file)
    for line in content:
      print(line)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")