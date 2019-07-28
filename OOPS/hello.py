def CreateStack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    if len(stack) == 0:
        return True

def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack): return
    return stack.pop()


def reverseString(mystr):
    n = len(mystr)

    stack = CreateStack()
    for i in range(0,n,1):
        push(stack,mystr[i])

    mystr = ''
    for i in range(0,n,1):
        mystr+=pop(stack)

    return mystr


print(reverseString('apple'))