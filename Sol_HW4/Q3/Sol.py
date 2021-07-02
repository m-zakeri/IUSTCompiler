import os
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter parser script's filename : ")
    if filename == "":
        current_dir_filemames = os.listdir(".")
        for name in current_dir_filemames:
            if name.endswith("Parser.py"):
                filename = name
                break
        if filename == "":
            print("Couldn't find parser in this directory")
            exit()
        else:
            print("solve " + filename + ".")


file = open(filename, "r")
lines = file.readlines()
file.close()


for i in range(len(lines)):
    spaceNum = 0
    while spaceNum < len(lines[i]) and lines[i][spaceNum] == ' ':
        spaceNum += 1
    if spaceNum > 10 and spaceNum % 4 == 2:
        lines[i] = lines[i][10:]


file = open(filename, "w")
file.writelines(lines)
file.close()

