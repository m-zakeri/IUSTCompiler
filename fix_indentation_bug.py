"""
This module fix the Python indentation
 for ANTLR generated codes

"""


import os
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter parser script's filename (Leave empty to automatically find in the current directory): ")
    if filename == "":
        current_dir_filemames = os.listdir(".")
        for name in current_dir_filemames:
            if name.endswith("Parser.py"):
                filename = name
                break
        if filename == "":
            print("Couldn't find any parser in this directory.\nAborting.")
            exit()
        else:
            print("Fixing " + filename + ".")

print("Reading...")
file = open(filename, "r")
lines = file.readlines()
file.close()

print("Processing...")
for i in range(len(lines)):
    space_count = 0
    while space_count < len(lines[i]) and lines[i][space_count] == ' ':
        space_count += 1
    if space_count > 10 and space_count % 4 == 2:
        lines[i] = lines[i][10:]

print("Writing...")
file = open(filename, "w")
file.writelines(lines)
file.close()

print("Done.")
