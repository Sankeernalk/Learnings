from datetime import datetime,timedelta
date_today = datetime.now()+timedelta(days=1)
print(date_today.strftime('%A'))


seats = [['|','|','|'],['|','|','|'],['|','|','|']]
print(seats)


from collections import OrderedDict
def RemoveDupWithoutOrder(str1):
    return ''.join(set(str1))

def RemoveDupWithOrder(str1):
    return ''.join(OrderedDict.fromkeys(str1))

str_dup = 'geeksforgeeks'
print(RemoveDupWithoutOrder(str_dup))
print(RemoveDupWithOrder(str_dup))

str_tar = ''
for i in str_dup:
    if i not in str_tar:
        str_tar+=i
        #print(id(str_tar))
print(str_tar)

strDate = '07/02/2019'
date_in = datetime.strptime(strDate,'%d/%m/%Y')
print(date_in.strftime('%b %d %Y'))






string_xml = """
<nodes>
<cnode desc ="" name="xyz">
<pnode name="word1"/>
<pnode name="word2"/>
<pnode name="word3"/>
</cnode>
<cnode desc="" name="abc">
<pnode name="word4"/>
<pnode name="word5"/>
<pnode name="word6"/>
</cnode>
</nodes>
"""

import xml.etree.ElementTree as etree
xyz=[]
abc=[]
tree = etree.fromstring(string_xml)
result = {}
for node in tree.findall('cnode'):
    name = node.get('name')
    if name not in result.items():
        result[name] = []

    for child in node.findall('pnode'):
        child_name = child.get('name')
        result[name].append(child_name)

print(result)

from datetime import date,timedelta
from dateutil.relativedelta import relativedelta
def month_range(d1, d2):
    return [d1 + relativedelta(months=+x) for x in range((d2.year - d1.year)*12 + d2.month - d1.month + 1)]


d1 = date(2008,8,15)
d2 = date(2008,10,15)
print(month_range(d1,d2))


def compound_interest(principle,rate,time):
    CI = principle*(pow((1+rate/100),time))
    print(CI)

compound_interest(1200,5.4,2)

k = 4


def main():
    list1 = []

    def add():
        for x in xrange(k):
            list1.append(x)
        print("hi "+str(list1))

    add()


main()