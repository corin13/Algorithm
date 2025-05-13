def solution(sticks):
    answer = 1
    right = sticks.pop()

    for i in range(len(sticks)-1,-1,-1):
        if sticks[i] > right:
            answer +=1
            right = sticks[i]
        
    return answer

# 정답 코드
'''
def solution(stick):
    answer = 1
    maxN = stick[-1]
    for i in range(len(stick)-2, -1, -1):
        if stick[i] > maxN:
            maxN = stick[i]
            answer += 1
    return answer
'''
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(solution(arr))