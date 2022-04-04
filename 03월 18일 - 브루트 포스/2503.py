import sys

input = sys.stdin.readline

N = int(input())
arr = [True]*1000           #~999이므로 1000가지의 칸 만들기
count = 0

for i in range(111,1000):   #3자리 수에서 중복, 0포함 경우 제외하기 
    i=str(i)
    if i[0] == i[1]or i[1] == i[2] or i[2] == i[0]:
        arr[int(i)] = False
    if i[0]== '0' or i[1] == '0' or i[2] == '0':
        arr[int(i)] = False

for i in range(N):
    num, s, b = map(int,input().split())
    num = str(num)
    for j in range(111,1000):   #주어진 수와 칸에 있는 수에서 s와 b의 수가 동일하면 남겨두고, 동일하지 않은 경우 제외하기
        ss = 0
        bb = 0
        j = str(j)
        if num[0] in j:
            if num[0] == j[0]:
                ss += 1
            else :
                bb += 1
        if num[1] in j:
            if num[1] == j[1]:
                ss += 1
            else :
                bb += 1
        if num[2] in j :
            if num[2] == j[2]:
                ss += 1
            else :
                bb += 1
        if s == ss and b == bb :
            continue
        else :
            arr[int(j)] = False

for i in range(111,1000):       #제외된 경우(False)를 빼고 나머지 True(조건에 맞는 숫자들)의 수 세기 
    if arr[i]:
        count += 1
print(count)
    
                
        
        
