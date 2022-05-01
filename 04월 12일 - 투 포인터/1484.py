import sys
input = sys.stdin.readline

"""
 [다이어트]

 left: 성원이가 기억하고 있던 몸무게
 right: 성원이의 현재 몸무게

 같은 위치에서 시작해서 점점 증가하는 투 포인터로 풀이
 대신, left ~ right를 모두 고려하는 것이 아니라 left, right 포인터 값 자체만 고려

 !주의! 몸무게의 범위가 딱히 정해져 있지 않으므로, 종료 조건을 잘 세우는 것이 중요!
       -> 두 몸무게가 같아지는 순간 종료!
       -> left가 right와 같은 값을 가진다면, 직전 상황은 두 몸무게가 1차이 나는 상황
       -> 이 때 몸무게 차이가 g 이상이었다는 것은 이후로 나올 수 있는 차이는 무조건 g 이상이 된다. (제곱수의 간격은 수가 커질 수록 늘어나기 때문)
"""

def get_possible_weight(g):
    left = 1                            #성원이가 기억하고 있던 몸무게 = 1로 초기화 
    right = 2                           #성원이의 현재 몸무게 = 2로 초기화 
    ans = []                            #ans 리스트 생성 
    while left < right:                 #right가 left 보다 클 때,
        diff = right ** 2 - left ** 2   #diff = right의 제곱 - left의 제곱 
        if diff > g:                    #diff가 g(성원이가 말한 무게) 보다 크다면 left 1 증가 
            left += 1
        else:                           #diff가 g보다 크지 않다면 
            if diff == g:               #diff가 g와 같다면 ans 리스트에 right 값 추가 
                ans.append(right)
            right += 1                  #diff가 g보다 작다면 right 1 증가 
    return ans                          #ans 리턴 

# 입력
g = int(input())        #g값 입력 

# 연산
ans = get_possible_weight(g)    #ans 값 저장 

# 출력
if ans:                         #만약 ans의 값이 0이 아니면 
    print(*ans, sep='\n')       #ans의 포인터 출력 
else:
    print(-1)                   #아닌 값은 -1 출력 
