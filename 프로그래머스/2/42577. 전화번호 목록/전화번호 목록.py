def solution(phone_book):
    
    # 전화번호 목록 정렬
    phone_book.sort()
    
    # 인접한 번호들 비교
    for i in range(len(phone_book) - 1):
        # 현재 번호가 다음 번호의 접두사인지 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    return True

