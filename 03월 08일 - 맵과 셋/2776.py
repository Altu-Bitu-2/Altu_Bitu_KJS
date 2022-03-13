import sys

input = sys.stdin.readline
T = int(input()) 
for i in range(T):      #테스트 케이스만큼 반복
    N = int(input())
    note1 = set(map(int, input().split()))      #수첩 1에 있는 숫자들을 set에 입력
    M = int(input())
    note2 = list(map(int, input().split()))     #수첩 2에 있는 숫자들을 list에 입력
    for j in note2:         #수첩 2에 있는 숫자가 1에도 있으면 1 출력 없으면 0 출력
        if j in note1:
            print(1)
        else :
            print(0)
