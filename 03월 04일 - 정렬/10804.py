import sys

input = sys.stdin.readline

array = []

for i in range(22):
    array.append(i)

for i in range(10):
    x, y = map(int, input().split())
    array = array[:x]+list(reversed(array[x:y+1]))+array[y+1:]

for i in range(20):
    print(array[i+1])


