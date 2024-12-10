from collections import defaultdict

def solution(clothes):
    clothes_type = defaultdict(int)
    
    # 의상 종류별 개수 파악
    for _, category in clothes:
        clothes_type[category] += 1
    
    # 각 의상 종류별 (의상 수 + 1)을 곱함 => +1은 해당 종류의 옷을 입지 않았을 경우의 수
    total_combinations = 1
    for count in clothes_type.values():
        total_combinations *= (count + 1)
    
    # 모든 의상을 입지 않는 경우를 제외
    return total_combinations - 1
