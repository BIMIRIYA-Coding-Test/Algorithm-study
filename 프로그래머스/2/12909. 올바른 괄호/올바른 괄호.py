def solution(s):
    if s[0] == ")": False
    
    stack = []    
    for text in s:
        if text == "(":
            stack.append(text)
        else:
            if stack:
                stack.pop()
            else: return False
    
    if not stack:
        return True
    return False
        
