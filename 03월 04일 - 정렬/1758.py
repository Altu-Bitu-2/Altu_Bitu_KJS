import sys

input = sys.stdin.readline
N = int(input())
array = []
sum = 0

for i in range(N):
    array.append(int(input().strip()))


array.sort(key=lambda x:(-x))

for i in range(N):
    money = array[i]-(i)
    if money > 0 :
        sum += money

print(sum)
