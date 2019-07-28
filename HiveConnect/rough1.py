operations = ['push 4','pop','push 3','push 5','push 2','inc 2 1']
#op = ['push 4']
L1 = []
for i in operations:
    if i.split(' ')[0] == 'push':
        L1.append(int(i.split(' ')[1]))
    elif i == 'pop':
        L1.pop()
    elif i.split(' ')[0] == 'inc':
        for j in range(int(i.split(' ')[1])):
            L1[j]+=int(i.split(' ')[2])
    if len(L1) == 0:
        print('EMPTY')
    else:
        print(L1[-1])

#a = [3,2,1,2,7]
arr = [1,2,2]
sort_a = sorted(arr)
#print(sort_a)
len_a = len(arr)
temp = 0
sum_a = 0
for i in range(1,len_a):
    if sort_a[i-1] == sort_a[i]:
        temp = sort_a[i]+1
        while True:
            if temp not in sort_a[i+1::]:
                sort_a[i] = temp
                break
            else:
                temp+=1
sum_a = sum(sort_a)
print(sum_a)