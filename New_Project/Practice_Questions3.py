try:
    with open('C:\\Users\\611419222\\Documents\\Python\\SP_PRICED_NOT_IN_BILLED.sql','r') as input:
        read1 = input.readlines()
        print(read1)
except ValueError as e:
    print('Unable to open the file:',e)


def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')


sqrt(1)

def counter(x):
    for i in range(x):
        #print(i)
        yield i


m = counter(5)
for i in m:
    print(i)


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        future = a+b
        a = b
        b = future
        print(a,b,end='/n')


for i in fibonacci():
    print(i)

