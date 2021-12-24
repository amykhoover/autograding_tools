import argparse
import os
import shutil

if __name__ == "__main__":

    needsEdit = False

    parser = argparse.ArgumentParser()
    parser.add_argument("javaFile", help="check that all methods are static")
    args = parser.parse_args()
    print(f"Reading from file: {args.javaFile}")
    
    
    linesFromFile = []
    
    try:
        file1 = open(f"{args.javaFile}", 'r+')
        linesFromFile = file1.readlines()
        editedLines = []

        count = 0
        # Strips the newline character
        for line in linesFromFile:
            count += 1
            if "public" in line and "static" not in line:
                needsEdit = True
                splitOnPublic = line.split("public")
                myLine="public static" + f" {splitOnPublic[1].strip()}"
                editedLines.append(myLine)
            else:
                editedLines.append(line)
    except Exception as e:
        raise e


    if needsEdit is True:
       
        shutil.copyfile(args.javaFile, f"{args.javaFile}_StudentOriginal.java")
        file2 = open(f"{args.javaFile}", 'w')
        for eline in editedLines:
            file2.write(eline)
        file2.close()