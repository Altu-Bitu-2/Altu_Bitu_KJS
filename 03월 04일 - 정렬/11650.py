import sys

input = sys.stdin.readline 
N = int(input())
array = []

for i in range(N):
    x, y = map(int, input().split())
    array.append([x,y])

array.sort(key=lambda x:(x[1]))

for x, y in array:
    print(x,y)
    
