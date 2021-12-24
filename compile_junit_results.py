
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("junitlog_dir", help="contains a text file for each function tested")
    args = parser.parse_args()

    files = os.listdir(args.junitlog_dir)

    reportHeader = "List of Test Cases per Problem"
    testCasesResults = {}

    for file in files:
        print(file)
        if ".DS_Store" not in file:
            fileObj = open(f"{args.junitlog_dir}/{file}", 'r')
            lines = fileObj.readlines()
            print()
            myTuplesList = []
            testCase = ""
            result = ""
            doubleCheckYourAnswer = ""
            doubleCheckTCAnswer = ""
            for l in lines:
                if "Test Case" in l:
                    testCase = l
                elif "Correct" in l:
                    result = l
                elif "Incorrect" in l:
                    result = l
                elif "Your Answer" in l:
                    doubleCheckYourAnswer = l
                elif "TestCase Answer" in l:
                    doubleCheckTCAnswer = l
        
            
                if testCase is not "" and result is not "" and doubleCheckYourAnswer is not "" and doubleCheckTCAnswer is not "":
                    mytuple = (testCase.strip(), result.strip(), doubleCheckYourAnswer.strip(), doubleCheckTCAnswer.strip())
                    myTuplesList.append(mytuple)
                    testCase = ""
                    result = ""
                    doubleCheckYourAnswer = ""
                    doubleCheckTCAnswer = ""
            testCasesResults[file] = myTuplesList
      

       
    """"
    fileheaderforeightbulk=f"Description:\n"
    fileheaderforeightbulk+="For Homework Two, you were to complete eight common problems that"
    fileheaderforeightbulk+=" were assigned to everyone, and select two additional problems to solve from the website: codingbat.\n"

    eightCommon = "The eight common problems had a variable number of test cases. Scores for each question depended on the percentage of test cases that you got correct answers for."
    eightCommon += "Note: I did not take off credit if your code did not run because you forgot the static keyword.\n"
    
    problem1 = f"1. public static boolean scoresIncreasing(int[] scores)\n"
    eightCommon += f"\t Six Cases\n"
    problem2 = f"2. public static int wordsCount(String[] words, int len)\n"
    eightCommon += f"\t Six Cases\n"
    problem3 = f"3. public static String[] mergeTwo(String[] a, String[] b, int n)\n"
    eightCommon += f"\t Nine Cases\n"
    problem4 = f"4. public static boolean dividesSelf(int n)\n"
    eightCommon += f"\t Eleven Cases\n"
    problem5 = f"5. public static int userCompare(String aName, int aId, String bName, int bId)\n" 
    eightCommon += f"\t Eight Cases\n"
    problem6 = f"6. public static int matchUp(String[] a, String[] b)\n" 
    eightCommon += f"\t Thirteen Cases\n"
    problem7 = f"7. public static int sumHeights(int[] heights, int start, int end)\n"
    eightCommon += f"\t Twelve Cases\n"
    problem8 = f"8. public static int[] copyEvens(int[] nums, int count)\n"
    eightCommon += f"\t Thirteen Cases\n"
    
    scorePerProblem = {}
"""
    #Write to Screen Test
    try:
        fileAll = open(f"{args.junitlog_dir}/0.eightCommonScores.txt", 'w')
    except Exception as e:
        raise e
    fileAll.write(args.junitlog_dir)
    fileAll.write("\n")
    for myKey in testCasesResults.keys():
        totalCorrect = 0
        totalIncorrect = 0
        correctResults = []
        incorrectResults = []
        for myresultTuple in testCasesResults[myKey]:
            if "Correct" in myresultTuple[1]:
                totalCorrect = totalCorrect + 1
                correctResults.append(myresultTuple)
            elif "Incorrect" in myresultTuple[1]:
                totalIncorrect = totalIncorrect + 1
                incorrectResults.append(myresultTuple)
           
        #print(testCasesResults[myKey])
        print(f"Function Test: {myKey}")
        fileAll.write(f"Function Test: {myKey}\n")
        percentageCorrectTop = totalCorrect
        percentageCorrectBottom = totalCorrect + totalIncorrect
        #scorePerProblem[myKey] = (totalCorrect,totalIncorrect)
        print(f"\tScore: {percentageCorrectTop}/{percentageCorrectBottom}")
        fileAll.write(f"\tScore: {percentageCorrectTop}/{percentageCorrectBottom}\n")
        print (f"\tTotal Correct: {totalCorrect}, Total Incorrect: {totalIncorrect}")
        fileAll.write(f"\tTotal Correct: {totalCorrect}, Total Incorrect: {totalIncorrect}\n")
        if len(incorrectResults) > 0:
            print("\t-------------")
            fileAll.write(f"\t-------------\n")
            print("\tDetails about incorrect answers: \n")
            fileAll.write("\tDetails about incorrect answers: \n")
            for r in incorrectResults:
                print(f"\t\t{r[0]}: {r[1]}")
                fileAll.write(f"\t\t{r[0]}: {r[1]}\n")
                print(f"\t\t{r[2]}")
                fileAll.write(f"\t\t{r[2]}\n")
                print(f"\t\t{r[3]}")
                fileAll.write(f"\t\t{r[3]}\n")
    fileAll.close()
    """
    #Write to File Test
    problem1 = f"1. public static boolean scoresIncreasing(int[] scores)\n"
    problem2 = f"2. public static int wordsCount(String[] words, int len)\n"
    problem3 = f"3. public static String[] mergeTwo(String[] a, String[] b, int n)\n"
    problem4 = f"4. public static boolean dividesSelf(int n)\n"
    problem5 = f"5. public static int userCompare(String aName, int aId, String bName, int bId)\n" 
    problem6 = f"6. public static int matchUp(String[] a, String[] b)\n" 
    problem7 = f"7. public static int sumHeights(int[] heights, int start, int end)\n"
    problem8 = f"8. public static int[] copyEvens(int[] nums, int count)\n"


    #fileAll.write(fileheaderforeightbulk)
    keys = testCasesResults.keys()
    for key in keys:
        print(f"key: {key} \n")
        scoreForKey = scorePerProblem[key]
        print(f"\t score for key: {scoreForKey} \n")
        if "scoresIncreasing" in key:
            print(problem1)
            fileAll.write(problem1)
        elif "wordsCount" in key:
            print(problem2)
            fileAll.write(problem2)
        elif "mergeTwo":
            print(problem3)
            fileAll.write(problem3)
        elif "dividesSelf":
            print(problem4)
            fileAll.write(problem4)
        elif "userCompare":
            print(problem5)
            fileAll.write(problem5)
        elif "matchUp":
            print(problem6)
            fileAll.write(problem6)
        elif "sumHeights":
            print(problem7)
            fileAll.write(problem7)
        elif "copyEvens":
            print(problem8)
            fileAll.write(problem8)
        #fileAll.write(str(scoreForKey))
        #fileAll.write(f"\n")
        fileAll.write(f"\t Total: {scoreForKey[0]}/{scoreForKey[0] + scoreForKey[1]}")
        fileAll.write(f"\n")
      
        

    fileAll.close()
    """