def Longest_Common_Subsequence(x, y, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    Index = L[m][n]

    LCS = [""] * (Index+1)
    LCS[Index] = ""

    i = m
    j = n

    while i > 0 and j > 0:
        
        if x[i-1] == y[j-1]:
            LCS[Index-1] = x[i-1]
            i-=1
            j-=1
            Index-=1
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
    
    ans_str = ("".join(LCS))

    return ans_str
    
x = input()
y = input()

print(Longest_Common_Subsequence(x, y, len(x), len(y)))