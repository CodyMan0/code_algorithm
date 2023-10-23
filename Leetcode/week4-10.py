# Valid Parentheses
def isValid(s):
    stack = []
    pairs = {"(": ")", "{": "}", "[": "]"}
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)

        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False

    return len(stack) == 0


isValid("()")
isValid("()[]{}")
isValid("(]")

## Stack?
## 과거에 풀었는데 기억이 안남(외워서 그런듯)
## (와 [ 와 { 면 append 아니면 pop

## IDEA : LIFO principle. therefore a stack is a good choice here
