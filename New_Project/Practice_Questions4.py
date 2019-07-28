import os
print(dir())
print(vars())
import math
print(math.sqrt(25))


def sum(n):
    sum =0
    for i in range(n):
        sum = sum+i*i
    print(sum)



sum(3)

def minmax(data):
    big = data[0]
    for i in data:
        if i > big:
            big = i
    print(big)



minmax([1,2,3,4,5,6])


def test_distinct(data):
    count = 0
    for k in data:
        for j in data:
            if  k == j:
                print(k)
                print(j)
                count+=1
                if count == 2:
                    return False
    return True

print(test_distinct([2,3,5,6]))


import re
s = "string.!!!! With. Punctuation?"
s = re.sub(r'[^\w\s]','',s)
print(s)

import re
phone_check = re.compile(r"[^0-9\s-]")
phone = input ("Please, enter your phone: ")
while re.search(r"[^0-9\s-]",phone):
    print("Please enter your phone correctly!")
    phone = input ("Please, enter your phone: ")




A = [1,2,3,4,5,6]
B = [10,12,13,1,41,15]
print(A+B)


