'''
반례
-----입력----
2
0 1
1 0
-----답(출력)----
0 1
1 0
'''

def solution(xy):
    xy.sort(key=lambda v:(v[0],v[1]))
    for i in range(len(xy)):
        print(xy[i][0], xy[i][1])

arr = []
n = int(input())
for i in range(n):
    arr.append(list(map(int,input().split())))
solution(arr)