def toPostfix(prefix):
    stack = []
    postfix = []
    op = ['+', '-', '*', '(']
    for s in prefix:
        if s in op:
            if len(stack) == 2:
                postfix.append(stack.pop())
                postfix.append(stack.pop())
                stack.append(s)
            if stack and stack[len(stack) - 1]:
                break
            break
        else:
            postfix.append(int(s))

def getFirst(arr):
    # [+, +, +, -, *]
    for i in range(len(arr)//2):
        getArr(arr, i)

def getArr(arr, i):
    r = []
    for a in range(i):
        
