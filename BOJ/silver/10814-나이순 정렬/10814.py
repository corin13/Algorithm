def solution(people):
    people.sort(key=lambda v:int(v[0]))
    for i in range(len(people)):
        print(people[i][0], people[i][1])

n = int(input())
arr = []
for i in range(n):
    a,b = input().split()
    arr.append([a,b])
solution(arr)