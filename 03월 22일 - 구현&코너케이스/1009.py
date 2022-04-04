import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    num = a**b
    if num%10 == 0:
        print(10)
    else:
        print(num%10)
