N, M = map(int, input().split())        #N,M 입력 
arr=[]
ans=[]

for i in range(N):              #체스판 입력받기 
    arr.append(input())


for i in range(N-7):        #8x8 체스판 자르기(후보 생성)
    for j in range(M-7):
        casew = 0           #첫 번째가 w일 케이스 
        caseb = 0           #첫 번째가 b일 케이스 
        for p in range(i, i+8):     #잘라낸 체스판에서 w,b가 잘못 되어있을 경우 각 케이스에서 1추가 
            for q in range(j, j+8):
                if (p+q)%2 == 0:
                    if arr[p][q] != 'W' :
                        casew += 1
                    if arr[p][q] != 'B' :
                        caseb += 1
                else :
                    if arr[p][q] != 'B' :
                        casew += 1
                    if arr[p][q] != 'W' :
                        caseb += 1
        check = min(casew, caseb)   #두 케이스에서 더 적은 수 가져오기 
        ans.append(check)       #8x8잘라 놓은 것에서 더 적은 수들 모으기 

print(min(ans))     #제일 작은 수 출력 
