import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n) : 
    test = sys.stdin.readline().split()
    command = test[0]

    length = len(stack)
    if command == 'push' :
        value = test[1]
        stack.append(int(value))
    elif command == 'pop' :
        print(stack.pop() if len(stack) != 0 else -1)
    elif command == 'size' :
        print(len(stack))
    elif command == 'empty' :
        print(1 if len(stack) == 0 else 0)
    else : print(stack[length-1] if len(stack) != 0 else -1)
