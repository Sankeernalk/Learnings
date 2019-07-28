from __future__ import division
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
counter = 0
k = 3
list_temp = []
list_tar = []
list2 = []
for i in list1:
    list2.append(i)
for i in list2:
    list_temp = list1[counter:k+counter]
    if len(list_temp) == 3:
        sum_temp = sum(list_temp)/k
        list_tar.append(round(sum_temp,2))
    counter +=1
print(list_tar)


def gen_time(list1):
    list1.sort(reverse=True)
    for i in list1:
        if i <=2 :
            str1 = i
            list1.remove(i)
            break
    for i in list1:
        if str1 == 2 and i <= 3:
            str1=str(str1)+str(i)
            list1.remove(i)
            break
        elif str1 < 2:
            str1=str(str1)+str(i)
            list1.remove(i)
            break
    for i in list1:
        if i <= 5:
            str1=str(str1)+':'+str(i)
            list1.remove(i)
            break
    str1=str1+str(list1[0])
    if len(str1) == 5:
        print(str1)
    else:
        print('NA')

list1 = [1,7,7,7]
gen_time(list1)

import datetime

print(datetime.date.today())

import hashlib
hashlib.
result = hashlib.md5('GeeksForGeeks')
print(result.digest())