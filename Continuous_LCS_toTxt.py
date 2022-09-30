import os
import sys
# from colorama import init, Fore, Back -> look better

def Continuous_LCS(x, y):
    m = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    maxLength_Subsequence = 0
    lastPosition = 0

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                m[i+1][j+1] = m[i][j] + 1
                if m[i+1][j+1] > maxLength_Subsequence:
                    maxLength_Subsequence = max(maxLength_Subsequence, m[i+1][j+1])
                    # maxLength_Subsequence = m[i+1][j+1]
                    lastPosition = i + 1

    return x[lastPosition - maxLength_Subsequence : lastPosition]

# sum of two numbers
def add(x, y):
    return x + y

def strProcessing(str, subStr, subStrPositions):
    endPosition = subStrPositions + len(subStr)
    cnt = 0
    for pos in range(len(str)):
        if pos == subStrPositions:
            txtFile.write("[[")
            cnt+=1
        elif pos == endPosition:
            txtFile.write("]]")
            cnt+=1
        txtFile.write(str[pos])

    if cnt > 0 and cnt == 1:
        txtFile.write("]]")

    txtFile.write("\n")



def outputRequest(x, y, subStr):
    subStrLength = len(subStr)
    if len(subStr) == 0:
        outputTheNotFoundSubsqemessage()
        txtFile.write("Oops! ")
        seq = (x + " and " + y + " have no common subsequence.")
        txtFile.write(seq)
    else:
        outputWeFoundSubsqemessage()
        strProcessing(x, subStr, x.find(subStr))
        strProcessing(y, subStr, y.find(subStr))
        seq = ("The common subsequence for <" + x + "> and <" + y + "> is {" + subStr + "}.")
        txtFile.writelines(seq)
        txtFile.write("\n( Length is ")
        txtFile.write(str(subStrLength))
        txtFile.write(". )")



def txtDisplay(fileName):
    disFile = open(fileName)
    cntLine = 0
    print("\n[+ File:" + fileName + "]")
    for line in disFile:
        seq = "[+ Line:" + str(cntLine) + " +>   "
        print(seq, end=line)
        cntLine+=1
    disFile.close()



def outputTheNotFoundSubsqemessage():
    print("[+] We NOT Found Any Subsequence. QAQ")

def outputWeFoundSubsqemessage():
    print("[+] We Found the Subsequence. xD")



# try it !
# x = "People's Republic of China" -> People's [[Republic of China]] 
# y = "Republic of China" -> [[Republic of China]]

if __name__ == "__main__":
    fileName = input("[>] Enter the specified file name (MUST include the Extension)> ")

    x = input("[>] First String> ")
    y = input("[>] Second String> ")

    txtFile = open(fileName, 'w')

    outputRequest(x, y, Continuous_LCS(x, y))

    print("[+] Done !")

    fileLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), fileName)

    txtFile.close()

    while True:
        action = input("[>] Open it? [Y/N]: ")
        if action.lower() == 'y' or action.lower() == "yes" or action.lower() == 'n' or action.lower() == "no":
            if action.lower() == 'y' or action.lower() == "yes":
                txtDisplay(fileName)
                print("\n\n[+] File Location: ", end="")
            else:
                print("[+] Open it in ", end="")
            
            print(fileLocation)
            break