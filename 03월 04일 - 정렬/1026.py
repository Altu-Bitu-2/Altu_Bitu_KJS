import sys

input = sys.stdin.readline
N = int(input())
S = 0


A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(key=lambda x:(-x))
B.sort(key=lambda x:(x))

for i in range(N):
    S += A[i]*B[i]

print(S)

