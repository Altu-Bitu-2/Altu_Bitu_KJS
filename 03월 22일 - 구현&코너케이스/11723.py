import sys
input = sys.stdin.readline

"""
[집합] - 단순 구현 문제
ver1. 리스트 사용
set()을 사용해서 매번 연산을 하면 시간이 굉장히 오래 걸려요.
입력되는 x의 값이 1~20으로 범위가 매우 작기 때문에, 각 숫자가 집합에 들어있는 여부를 저장하는 리스트를 이용합니다.
1. 크기가 21인 리스트 선언
2. add는 True, remove는 false
"""
SIZE = 21
m = int(input())
s = [False]*SIZE
value = {"all":True, "empty":False}

def update(cmd):                #update : cmd에 따라 모든 s를 값을 바꾸기
    for i in range(1, 21):
        s[i] = value[cmd]

def check(num):                 
    if s[num]:                  #만약 s[num]가 True일 경우 1 리턴, 아니면 0 리턴 
        return 1
    return 0

for _ in range(m):              #m만큼 반복 
    cmd = input().split()       #[0] : 연산, [1] : 숫자 

    if len(cmd) == 1:           #길이가 하나일 경우 : all / empty
        update(cmd[0])          #update
        continue                
    else:
        num = int(cmd[1])       #다른 연산일 경우, num에 [1]의 정수형 넣기 

    if cmd[0] == "add":         #만약 add 연산이라면 
        s[num] = True           #s[num]을 True 
    elif cmd[0] == "remove":    #만약 remove 연산이라면 
        s[num] = False          #s[num]을 Flase 
    elif cmd[0] == "check":     #만약 check 연산이라면 
        print(check(num))       #check 출력 
    elif cmd[0] == "toggle":    #만약 toggle 연산이라면 
        s[num] = not s[num]     #s의 값들을 반전시키기 
