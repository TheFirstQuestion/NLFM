import sys
import os
import re
import json


# Show usage if incorrect
if (len(sys.argv) != 2):
    print("Usage: python3 RunMe.py /path/to/dir")
    sys.exit()


# Read blacklist and file definitions
with open("blacklist.txt") as f:
    blacklist = f.read().splitlines()
with open("definitions.json") as j:
    definitions=json.load(j)


# Checks file extension, etc. for how to convert file
def convertFile(thisFile):
    # TODO: make extension lower case
    #print(thisFile)
    filename = thisFile.split("/")[-1]
    # Skip hidden files
    if filename[0] is ".":
        return

    # Classify the file based on its extension
    extension = thisFile.split(".")[-1]
    try:
        filetype = definitions[extension]
    except:
        # If no extension, skip it
        if filename in extension:
            return
        print("FILE IDENTIFICATION ERROR")
        return

    # Conver the file
    if (filetype == "programming" or filetype == "video" or filetype == "audio" or filetype == "archive" or filetype == "misc."):
        # Don't convert it
        return
    elif (filetype == "image"):
        # Use OCR to get text
        # Create plain tiddler
        # Create tiddler with text and transclude plain tiddler
        return
    elif (filetype == "document"):
        # Convert it using the shell script
        os.system("cd PanTidDoc-master && ./RunMe.sh \"{}\"".format("../" + thisFile))
        return


# Converts files and returns directories
def convertDirectory(startingDirectory):
    containedFiles = []
    containedDirs = []
    # Get directories and files
    for (dirpath, dirnames, filenames) in os.walk(startingDirectory):
        containedFiles.extend(filenames)
        containedDirs.extend(dirnames)
        break

    # Convert the files
    for thisFile in containedFiles:
        convertFile(startingDirectory + thisFile)

    # Add path to directories
    for i in range(len(containedDirs)):
        thisDir = containedDirs[i]
        # Check directory against blacklist
        isBlacklisted = False
        for term in blacklist:
            if term in thisDir:
                isBlacklisted = True
                break
        if(not isBlacklisted):
            # If none of the above...
            containedDirs[i] = startingDirectory + containedDirs[i] + "/"

    return containedDirs



if __name__ == "__main__":
    # Get command line argument for starting directory
    dirs = []
    dirs.extend(convertDirectory(sys.argv[1]))
    # Loop until all directories have been entered
    while len(dirs) > 0:
        dirs.extend(convertDirectory(dirs[0]))
        del dirs[0]
