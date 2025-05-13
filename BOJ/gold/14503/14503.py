'''
내 코드
'''
# def solution(x, y, d, board,n,m):  
    # dx = [-1, 0, 1, 0]
    # dy = [0, 1, 0, -1]
    # answer = 0
    
    # while(True):
    #     flag = False
    #     # 1. 현재 칸이 청소되지 않은 경우, 현재 칸을 청소한다
    #     if board[x][y] == 0:    # 현재 위치 청소
    #         board[x][y] = 2
    #         answer += 1
        
    #     for k in range(4):
    #         nx = x + dx[k]
    #         ny = y + dy[k]

    #         # 3-1.청소할 곳이 있는 경우 flag를 True로 변경
    #         if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] == 0:# 청소 안 했냐?
    #             flag = True
    #             break

    #     # 2. 4칸 중 청소되지 않은 빈 칸이 없는 경우 -> 청소할 곳이 없냐?
    #     if not flag:   # 청소할 곳이 없으면 True
    #             # 그대로 뒤로 이동
    #             if board[x-dx[d]][y-dy[d]]==2:
    #                 x,y = (x-dx[d]), (y-dy[d])
    #             else:   # 뒤에가 벽이면 청소 종료
    #                 return answer

    #     # 3-2. 4칸 중 청소되지 않은 빈 칸이 있는 경우 -> 청소할 곳이 있냐?
    #     else:    # 청소할 곳이 있으면 True
    #         for _ in range(4):
    #             d = (d-1)%4 #반시계로 회전
    #             nx = x + dx[d]
    #             ny = y + dy[d]
    #             if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] == 0:
    #                 x,y = nx, ny    # 위치 이동
    #                 break

'''
강사님 코드
'''
def solution(x, y, d, board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    board[x][y] = 2
    answer = 1
    while True:
        flag = False
        for _ in range(4):
            d = (d+3) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if board[nx][ny] == 0:
                x = nx
                y = ny
                board[x][y] = 2
                answer += 1
                flag = True
                break
        if flag == False:
            if board[x-dx[d]][y-dy[d]] == 1:
                return answer
            else:
                x = x - dx[d]
                y = y - dy[d]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 내 코드
# print(solution(r, c, d, arr,n,m))
# 원본
print(solution(r, c, d, arr))