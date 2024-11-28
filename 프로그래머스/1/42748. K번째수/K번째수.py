def solution(array, commands):
    answer = []
    li = []
    for command in commands:
        
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1
        
        li = array[i:j]
        
        li.sort()
        
        if len(li) >= k + 1:
            answer.append(li[k])
        else:
            answer.append(li[-1])
        
    return answer