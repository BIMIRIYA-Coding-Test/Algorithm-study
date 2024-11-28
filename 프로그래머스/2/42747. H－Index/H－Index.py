def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    for i, c in enumerate(citations):  # i는 논문의 순서, c는 인용 횟수
        if i + 1 > c:  # i+1은 현재 논문 수 (1-indexed)
            return i  # 이전 논문의 순서가 H-Index
    return len(citations)  # 모든 논문이 조건을 만족하면 전체 논문 수가 H-Index
