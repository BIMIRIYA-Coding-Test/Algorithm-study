def solution(s):

    stack = []
    for i in s:
        if i == "(":
            stack.append(0)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False