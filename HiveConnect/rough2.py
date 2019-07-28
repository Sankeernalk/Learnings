def getMinimumUniqueSum(arr):
    # Write your code here
    sort_a = sorted(arr)
    # print(sort_a)
    len_a = len(arr)
    temp = 0
    sum_a = 0
    for i in range(1, len_a):
        if sort_a[i - 1] == sort_a[i]:
            temp = sort_a[i] + 1
            while True:
                if temp not in sort_a[i + 1::] and temp not in sort_a[i - 1::-1]:
                    sort_a[i] = temp
                    break
                else:
                    temp += 1
    sum_a = sum(sort_a)
    print(sort_a)
    return sum_a

arr = [2,2,2]
result = getMinimumUniqueSum(arr)
print(result)

def anagramoptimize(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos]+1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos]+1

    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j = j+1
        else:
            stillOk = False
    return stillOk

print(anagramoptimize('apple','pleap'))


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

from timeit import Timer
t1 = Timer("test1()","from __main__ import test1")
print("concat ",t1.timeit(number=1000),"milliseconds")

t2 = Timer("test2()","from __main__ import test2")
print("append ",t2.timeit(number=1000),"milliseconds")

t3 = Timer("test3()","from __main__ import test3")
print("comprehension ",t3.timeit(number=1000),"milliseconds")

t4 = Timer("test4()","from __main__ import test4")
print("list range ",t4.timeit(number=1000),"milliseconds")


from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))


from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))


from pythonds.basic.deque import Deque

def palcheck(palstr):
    q1 = Deque()
    stilBal = True
    for i in palstr:
        q1.addFront(i)

    while q1.size() > 1 and stilBal:
        first = q1.removeFront()
        last = q1.removeRear()
        if first != last:
            stilBal = False
    return stilBal

print(palcheck('ahkfhfc'))
print(palcheck('madam'))

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))


def binarySerach(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and found == False:
        midpoint = (first+last)/2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

alist  = [0,1,2,5,6,7,10,13,16,17]
print(binarySerach(alist,5))