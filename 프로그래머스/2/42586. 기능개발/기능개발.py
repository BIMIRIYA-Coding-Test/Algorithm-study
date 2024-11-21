import math

def solution(progresses, speeds):
    # 제일 앞에 기능이 개발 될 때까지 기다린다. => 작업률을 + 시킨다.
    # 제일 앞에 기능이 100이 된다 => 뺀다. -> 그 수를 세서 배열에 넣는다.
    # 반복
    
    answer = []
    index = 0
    
    while(index < len(progresses)):
        count = 0
        remain = math.ceil((100 - progresses[index]) / speeds[index])

        for i in range(index, len(progresses)):
            progresses[i] = progresses[i] + speeds[i] * remain
        
        for i in range(index, len(progresses)):
            if progresses[i] >= 100:
                index += 1
                count += 1
            else: break
        
        answer.append(count)
    
    return answer