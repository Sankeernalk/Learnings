def binarySearch(list1,item1):
    first = 0
    last = len(list1)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item1 == list1[mid]:
            found = True
        else:
            if item1 < list1[mid]:
                last = mid-1
            else:
                first = mid+1
    return found

print(binarySearch(['bye','hi','hello'],'hi'))


from pythonds.basic.stack import Stack
def balSymbols(str1):
    i = 0
    balanced = True
    s1 = Stack()
    while i < len(str1) and balanced:
        if str1[i] in '[{(':
            s1.push(str1[i])
        else:
            if s1.isEmpty():
                balanced = False
            else:
                top = s1.pop()
                if not matches(top,str1[i]):
                    balanced = False
        i = i+1
    if balanced and s1.isEmpty():
        return True
    else:
        return False


def matches(open,close):
    opens = '[{('
    closes = ']})'
    return opens.index(open) == closes.index(close)



# list1 = [10,20,40,30,5,8,15]
# new_list = []
# min = list1[0]
# while list1:
#     for i in list1:
#         if i < min:
#             min = i
#     new_list.append(min)
#     list1.remove(min)
# print(new_list)

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)


data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
for i in range(len(data_list)):
    for j in range(len(data_list)-i-1):
        if data_list[j] > data_list[j+1]:
            data_list[j],data_list[j+1] = data_list[j+1],data_list[j]

print(data_list)


str1 = 'abcdefgh'
result = ''
for i in str1:
    result = i+result

print(result)


list1 = [3,2,4,1,1]
list2 = ['three','two','four','one','one1']
list1,list2 = zip(*sorted(zip(list1,list2)))
print(list1,list2)


import re
with open("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\empph.txt") as f:
    for i in f:
        print(re.findall('\D+',i.strip()))



t1 = (1,2,3,4)
l1 = list(t1)
print(type(l1))