import sys
input = sys.stdin.readline

"""
[행운의 바퀴]

- 바퀴가 돌아갈 필요 X
- 화살표가 가르키는 인덱스를 회전 정보에 따라 바꿔줌

1. 화살표가 가르키는 칸이 결정되지 않았으면 알파벳을 바퀴에 적는다.
2. 이미 알파벳이 써 있는 경우, 같은 알파벳이 아닌 경우 조건에 해당하는 바퀴 만들 수 없다.
3. 바퀴에 쓰여있는 알파벳은 중복되지 않으므로 동일한 알파벳이 여러 자리에 있을 수 없다.
"""

def make_wheel(n, record):
    wheel = ['?'] * n   # 바퀴의 상태
    is_available = dict()   # 해당 알파벳을 새로 쓸 수 있는지 확인하는 딕셔너리

    # 모든 알파벳에 대해 우선 True로 저장
    # ord(문자) = 아스키코드
    # chr(아스키코드) = 문자
    ord_a = ord('A')
    for i in range(26):     #26번 반복 
        is_available[chr(i + ord_a)] = True #is_available의 딕셔너리에 알파벳에 맞춰 트루를 넣어준다. 

    idx = 0 # 화살표가 가르키는 인덱스

    for rot, alpha in record:       #기록에서, 알파벳과 회전 정보를 저장 
        idx = (idx - int(rot)) % n      #인덱스에서 회전만큼 돌려줌 
        
        # 같은 경우
        if wheel[idx] == alpha:
            continue
        # 다른 알파벳이 써 있거나, 이미 알파벳을 다른 자리에 사용한 경우
        if wheel[idx] != '?' or not is_available[alpha]:
            return '!'      #!리턴 
        wheel[idx] = alpha  #바퀴의 해당 인덱스를 알파벳으로 변경 
        is_available[alpha] = False     #is_available의 해당 부분을 false처리 
                
    return ''.join(wheel[idx:]+wheel[:idx]) #연결해서 인덱스부터 바퀴 전체 출력 

# 입력
n, k = map(int, input().split())
record = [input().split() for _ in range(k)]
    
print(make_wheel(n, record))
