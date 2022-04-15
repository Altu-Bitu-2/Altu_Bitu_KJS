import sys
from itertools import permutations
input = sys.stdin.readline

"""
[야구]

1. 가능한 모든 배치를 구한다.
    - 이때, 4번 타자는 항상 1번 선수(0번 인덱스)여야 함을 주의
2. 구한 배치에 대해 점수를 계산
    - out이 3번을 기록하여 이닝이 바뀔 때, 이전에 베이스에 있던 선수들을 비워주어야 함
    - 선수 인덱스를 갱신하는 과정에서 인덱스 에러가 나지 않도록 모듈러 연산 해주기
"""

# 구한 순서에 대해 점수를 계산
def calc_score(order, result):
    player = 0
    score = 0

    # result의 한 행이 inning이 되고, 
    for inning in result:
        out = 0     #out은 0으로 초기화 
        base1 = base2 = base3 = 0   #모든 base도 0으로 초기화 
        while out < 3:      #아웃이 3회 이하일 때 
            p = inning[order[player]] # 이번 타자의 포인트
            if p == 0:          #포인트가 0이면 
                out += 1        #아웃 1회 추가 
            elif p == 1:        #포인트가 1이면 
                score += base3  #base3은 점수로 추가  
                base3 = base2   #base 2s는 3로 이동 
                base2 = base1   #base 1은 2로 이동 
                base1 = 1       #base 1으로 이동 
            elif p == 2:        #포인트가 2이면 
                score += base3 + base2  #base 2와 3이 점수로 추가 
                base3 = base1       #base1이 3으로 이동 
                base2 = 1       #base2로 이동 
                base1 = 0       #base1에는 아무도 없음 
            elif p == 3:        #포인트가 3이면 
                score += base3 + base2 + base1  #모든 base에 있는 것이 점수로 추가 
                base3 = 1       #base3으로 이동 
                base2 = base1 = 0   #base1과 2는 아무도 없음 
            else:   #홈런일 경우 
                score += base3 + base2 + base1 + 1 #모든 베이스와 타자가 점수로 추가 
                base3 = base2 = base1 = 0   #이후 모든 베이스는 비어있음 
            # 다음 타자로 바꿔 줌
            player = (player + 1) % 9                        

    return score


# 입력
n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]    # 각 이닝별 득점결과
answer = 0


# 가능한 모든 배치를 구하되, 1번타자(0번 인덱스)는 고정되어 있음을 주의
for order in permutations(range(1, 9), 8):  
    order = list(order)     #order 리스트화 
    order.insert(3, 0)      #(3, 0) 인서트 
    # 최댓값 갱신
    answer = max(answer, calc_score(order, result))     #answer와 스코어 중 최대값을 answer에 저장 

print(answer)       #answer 출력   
