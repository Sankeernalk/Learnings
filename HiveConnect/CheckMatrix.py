from pythonds.basic.deque import Deque

def domath(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y


s1 = Deque()
s2 = Deque()
str = "(1+2)/3+4"
operators = ['+','-','/','*']
result = 0
for i in range(len(str)):
    if str[i] == '(':
        pass
    elif str[i].isdigit():
        s1.addFront(str[i])
        #print(s1.items)
    elif str[i] in operators:
        s2.addFront(str[i])
        #print(s2.items)
    elif str[i] == ')':
        x,y = s1.removeFront(),s1.removeFront()
        op = s2.removeFront()
        #print(x,y,op)
        result = domath(int(x),op,int(y))
        s1.addRear(result)

#print(s1.items,s2.items)

while not s1.isEmpty() and not s2.isEmpty():
    op = ''
    if '/' in s2.items or '*' in s2.items:
        op = s2.removeRear()
        if op in ['*','/']:
            x,y = s1.removeRear(),s1.removeRear()
            result = domath(int(x),op,int(y))
            s1.addRear(result)
        else:
            s2.addRear(op)
            op = ''
    elif '+' in s2.items or '-' in s2.items:
        op = s2.removeRear()
        if op in ['+','-']:
            x,y = s1.removeRear(),s1.removeRear()
            result = domath(int(x),op,int(y))
            s1.addRear(result)
        else:
            s2.addRear(op)
            op = ''

print(s2.items,s1.items)







