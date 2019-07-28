import datetime
list1 = []
dict1 = {}
with open ("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\sample.txt") as f:
    for line in f:
        line = line.strip()
        list1.append(line)
    for i in list1:
        #list_tmp = i.split(',')
        sell_id = i.split(',')[1]
        date_1 = i.split(',')[3]
        dt = datetime.datetime.strptime(date_1,'%d-%m-%Y')
        #print(dt.month)
        if sell_id in dict1:
            if dt.month == 2:
                dict1[sell_id] +=1
        else:
            dict1[sell_id] = 1
sort_dict = sorted(dict1.items(),key=lambda kv:-kv[1])
print(sort_dict)
