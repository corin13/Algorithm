'''
내 코드
'''
# from collections import defaultdict, Counter
# def solution(participant, completion):
#     sH1 = Counter(participant) # 참가사 수 세기
#     sH2 = defaultdict(int)  # 이것도 카운터로 해도 될 듯
#     for x in completion:
#         sH2[x]+=1   #완주자 추가

#     for key in sH1: # 참가자 순회하면서 비교
#         if key not in completion:   #완주자 목록에 없냐?
#             return key
#         else:
#             if(sH1[key]-sH2[key]!=0):   # 중복 참가자가 있을 경우
#                 return key

'''
답안
'''
from collections import defaultdict, Counter
def solution(participant, completion):
    answer = ''
    sH = Counter(participant)
    for x in completion:
        sH[x] -= 1
    for key in sH:
        if sH[key] == 1:
            return key
    return answer

n = int(input())
a = []
for i in range(n):  # 참가자 목록 생성
    a.append(input())
b = []
for i in range(n-1):    # 완주자 목록 생성
    b.append(input())
print(solution(a, b))