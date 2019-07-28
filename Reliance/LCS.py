def Subsequence(X, Y, m, n):
    T = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    index = T[m][n]
    lcs = [""]*(index+1)
    lcs[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
        elif T[i-1][j] > T[i][j-1]:
            i-=1
        else:
            j-=1

    print("Subsequence of "+ X +" and "+ Y + " is "+"".join(lcs))

X = "jfhdsf"
Y = "flkdsf"
m = len(X)
n = len(Y)
Subsequence(X, Y, m, n)