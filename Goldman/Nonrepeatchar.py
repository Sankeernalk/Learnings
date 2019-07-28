from collections import OrderedDict
test_string = "GeeksfoorrGeeks"
dict_test = OrderedDict()
for i in test_string:
    if i in dict_test.keys():
        dict_test[i]+=1
    else:
        dict_test[i]=1
#print(dict_test)

for k,v in dict_test.items():
    if v == 1:
        print("The first non repeating character is " +k)
        break



# test_string1 = "GeeksfoorrGeeks"
# while test_string1 != "":
#     org_len = len(test_string1)
#     ch = test_string1[0]
#     test_string1 = test_string1.replace(ch,"")
#     mod_len = len(test_string1)
#     if org_len == mod_len-1:
#         print(ch)
#         break
