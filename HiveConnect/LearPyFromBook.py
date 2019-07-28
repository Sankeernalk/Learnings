def StringReplace(str1,str2):
    m = len(str1)
    n = len(str2)
    i = 0
    j = 0
    if m < n:
        for i in range(n):
            if i < m:
                if str1[i]==str2[i]:
                    pass
            else:
                str1+=str2[i]
    else:
        for i in range(m):
            if i < n:
                if str1[i]==str2[i]:
                    pass
            else:
                str2+=str1[i]
    return (str1,str2)


str2 = "San"
str1 = "SanLK"
print(StringReplace(str1,str2))