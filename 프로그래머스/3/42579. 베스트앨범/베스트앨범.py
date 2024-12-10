from collections import defaultdict

def solution(genres, plays):
    answer = []
    count = defaultdict(int) # 각 장르별 총 재생 횟수
    song = {} # 각 장르별 수록곡
    
    for i in range(len(genres)):
        count[genres[i]] += plays[i]
        
        song.setdefault(genres[i], [])
        song[genres[i]].append((i, plays[i]))
    
    # 각 장르별 총 재생 횟수를 내림차순으로 정렬
    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    print(sorted_count)
    
    for key in sorted_count:
        # 첫 번째 기준: 재생 횟수, 두 번째 기준: 고유번호가 낮은 순서 -인 이유는 내림차순이기 때문
        sorted_song = sorted(song[key], key=lambda tup: (tup[1], -tup[0]), reverse=True)
        
        if len(sorted_song) < 2:
            answer.append(sorted_song[0][0])
        
        else:
            answer.append(sorted_song[0][0])
            answer.append(sorted_song[1][0])
    return answer