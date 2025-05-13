'''
내 코드 - Counter 사용
'''
from collections import Counter
def solution(n, m, name):
    # print(n,m,arr)
    person = Counter(name)  # 카운터로 세고
    arr = []
    for key in person:
        if person[key]%2==0:    # 듣도 + 보도 못한 놈들 추가
            arr.append(key)
    print(len(arr)) # 듣보잡 수 출력
    arr.sort()  # 정렬 후
    for x in arr:
        print(x)


'''
강사님 답 - defaultdict 사용
'''
# from collections import defaultdict
# def solution(n,m,name):
#     answer = []
#     sH = defaultdict(int)   # 기본값 0
#     for x in name:  #반복하면서 이름 나오는 수 세기
#         sH[x] += 1

#     for key in sH:
#         if sH[key] == 2:    #듣도 + 보도 못한 놈이냐?
#             answer.append(key) # 듣보잡 리스트에 추가
#     print(len(answer))  # 2명
#     # 정렬순으로 이름 출력
#     for x in sorted(answer):  # 바로 정렬하기
#         print(x)





arr = []
n, m = map(int, input().split())
for i in range(n+m):
    arr.append(input())
solution(n, m, arr)