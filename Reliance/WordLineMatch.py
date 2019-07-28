import re
with open("C:\\Users\\611419222\\PycharmProjects\\Reliance\\SearchName") as f:
    read_line = f.readlines()
    print(read_line)
    #print(len(read_line))
    for i,j in enumerate(read_line):
        if re.match(r'^.*Sankeerna.*$',j,re.I):
            print(i,j)


def rev(str):
    str1 = ""
    for i in range(len(str)-1,-1,-1):
        str1=str1+str[i]
    print(str1)

rev("Sankeerna")

def revstring(str):
    list1 = []
    for i in str:
        list1.append(i)
    str_fin = ""
    for j in range(len(list1)):
        print("".join(list1.pop()))

revstring("Sankeerna")

def numString():
    with open("C:\\Users\\611419222\\PycharmProjects\\Reliance\\SearchName") as f:
        line = f.readlines()
        #print(line)
        for l in line:
           #print(l)
            return((re.findall(r'\d+',l)),(re.findall(r'\D+',l)))

print(numString())

str11 = "Retailer country,Order method type,Retailer type,Product line,Product type,Product,Year,Quarter,Revenue,Quantity,Gross margin"
str12 = (x.replace(' ','_') for x in str11.split(','))
print(str12)
