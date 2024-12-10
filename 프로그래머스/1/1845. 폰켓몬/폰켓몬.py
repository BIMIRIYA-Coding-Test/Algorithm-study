def solution(nums):
    type_count = len(set(nums)) # 폰켓몬 종류 수
    length = len(nums)/2 # N/2 폰켓몬 선택하는 수
    
    if(type_count <= length): # 폰켓몬의 종류가 선택해야 하는 수보다 작을 시
        answer = type_count
    else: answer = length
    
    return answer