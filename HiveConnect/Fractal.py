list1 = [1,2,1,2,2]
list2 = [3,2,1,3,3]
list_temp = []
len_1 = len(list1)
for i in range(len_1):
    if list1[i] == list2[i]:
        list_temp.append(list1[i])
    else:
        for i in range(list1[i],list2[i]+1):
            if i in list_temp:
                pass
            else:
                list_temp.append(i)

print(len(set(list_temp)))


