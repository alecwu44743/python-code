def Continuous_LCS(x, y):
    m = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    maxLength_Subsequence = 0
    lastPosition = 0

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                m[i+1][j+1] = m[i][j] + 1
                if m[i+1][j+1] > maxLength_Subsequence:
                    maxLength_Subsequence = m[i+1][j+1]
                    lastPosition = i + 1

    return x[lastPosition - maxLength_Subsequence : lastPosition]



def strProcessing(str, subStr, subStrPositions):
    endPosition = subStrPositions + len(subStr)
    cnt = 0
    for pos in range(len(str)):
        if pos == subStrPositions:
            print("[[", end="")
            cnt+=1
        elif pos == endPosition:
            print("]]", end="")
            cnt+=1
        print(str[pos], end="")

    if cnt > 0 and cnt == 1:
        print("]]", end="")

    print("", end="\n")



def outputRequest(x, y, subStr):
    subStrLength = len(subStr)
    if len(subStr) == 0:
        print("Oops!", end=" ")
        print(x + " and " + y + " have no common subsequence.")
    else:
        strProcessing(x, subStr, x.find(subStr))
        strProcessing(y, subStr, y.find(subStr))
        print("The common subsequence for <" + x + "> and <" + y + "> is {" + subStr + "}.", end="")
        print("\n( Length is ", end="")
        print(subStrLength, end="") 
        print(". )")
        


# try it !
# x = "People's Republic of China" -> People's [[Republic of China]] 
# y = "Republic of China" -> [[Republic of China]]

x = input()
y = input()

outputRequest(x, y, Continuous_LCS(x, y))