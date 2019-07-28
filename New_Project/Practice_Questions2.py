def count(data,target):
    n = 0
    for val in data:
        if val == target:
            n+=1
    return n


m = count([1,2,3,4,5,6,1,2,3,4,2,2],2)
print(m)


print('a','b','c',sep=':')

year = int(input('In which year were you born?'))
print(year)

reply = input('Enter x and y separated by spaces')
pieces = reply.split()
print(pieces[0])