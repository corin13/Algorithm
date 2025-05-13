def solution(array):

    n = len(array)
 
    for i in range(n):
        l1 = list(array[i][1])
        l2 = []
        for j in range(len(l1)):
            l2.append(str(l1[j]*array[i][0]))
        print(''.join(l2))

n = int(input())
arr = []
for i in range(n):
    a,b = input().split()
    arr.append([int(a),b])

solution(arr)