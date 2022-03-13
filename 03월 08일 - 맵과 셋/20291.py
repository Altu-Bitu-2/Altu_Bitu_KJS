import sys

input = sys.stdin.readline

N = int(input())
file = dict()       #딕셔너리 생성

for i in range(N):
    name = (input().split('.'))[1]      #확장자 체크
    if name in file:            #확장자가 딕셔너리에 있으면 value +1
        file[name] += 1
    else :                      #확장자가 딕셔너리에 없으면 추가하고 value =1
        file[name] = 1

file = sorted(file.items())         #확장자 기준으로 정렬

for key, value in file:
    print(key.rstrip(), value)
