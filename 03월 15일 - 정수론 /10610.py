N = list(input())
N.sort(reverse=True)       #리스트를 역순으로 정렬 (30의 배수여야 하니, 0이 맨 뒷자리여야 해서) 

sum = 0
ans = 0

for i in N :
    sum += int(i)

if sum % 3 == 0 and '0' in N:    #3의 배수 체크와 10의 배수 체크 
    for i in N:
        print(str(i), end='')
    
else :
    print(-1)

