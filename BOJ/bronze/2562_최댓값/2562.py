import sys
arr = list(map(int,sys.stdin.readlines()))
max = -1
index = 0
for i in range(len(arr)):
    if arr[i] >max:
        max,index = arr[i],i+1
print(max)
print(index)