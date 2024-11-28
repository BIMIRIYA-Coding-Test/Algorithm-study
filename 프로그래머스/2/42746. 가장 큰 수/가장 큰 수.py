def solution(numbers):
    answer = ''
    
#     # 1 ~ 1000까지
#     array = [[int(i) if int(i) != 0 else -1 for i in str(num)] + [0] * (4 - len(str(num))) for num in numbers]
    
#     array.sort(key=lambda x: x*3 reverse=True)
    
    
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] == 0:
#                 pass
#                 # continue ㄴㄴ 한 번 0 나오면 나머지 또한 0이기 때문
#             elif array[i][j] == -1:
#                 array[i][j] = 0
#                 if str(array[i][j]) == '0' and answer == '':
#                     answer = ''
#                 else:
#                     answer += str(array[i][j])
#             else:
#                 if str(array[i][j]) == '0' and answer == '':
#                     answer = ''
#                 else:
#                     answer += str(array[i][j])
    
#     if answer == '':
#         answer = '0'
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return answer[0]
    
    return answer