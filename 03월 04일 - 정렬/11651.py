import sys

input = sys.stdin.readline 
N = int(input())
array = []

for i in range(N):
    x, y = map(int, input().split())
    array.append([y,x])

array = sorted(array)

for i in range(N):
    print(array[i][1], array[i][0])
