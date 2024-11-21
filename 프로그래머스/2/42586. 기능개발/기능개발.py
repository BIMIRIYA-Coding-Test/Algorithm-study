def solution(progresses, speeds):
    li = []
    answer = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            li.append((100 - progresses[i]) // speeds[i])
        else:
            li.append((100 - progresses[i]) // speeds[i] + 1)
    print(li)
    
    value = li[0]
    cnt = 0
    for i in li:
        if i <= value:
            cnt += 1
        else:
            answer.append(cnt)
            value = i
            cnt = 1
    answer.append(cnt)
    
    return answer