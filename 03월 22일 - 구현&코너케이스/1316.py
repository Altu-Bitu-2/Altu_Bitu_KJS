import sys
input = sys.stdin.readline

"""
[그룹 단어 체커] - 단순 구현 문제
- 이미 등장한 알파벳 저장할 set() 선언 (탐색 O(1))
- 처음 등장하는 알파벳은 set에 추가하고, 무리에서 떨어졌는데 이미 등장한 알파벳이면 그룹 단어가 아니다.
"""

def is_group_word(word):        #
    checked = set()             #checked set 생성 
    prev = None

    for c in word:              #단어의 알파벳
        if c == prev:           #바로 전에 있던 알파벳이라면 continue 
            continue
        
        if c in checked:        #checked에 있는 (전에 나왔었던) 알파벳이라면 False 리턴
            return False

        checked.add(c)          #checked에 c 추가 
        prev = c                #바로 전 알파벳에 넣기 

    return True                 #True 리턴 


# 입력
n = int(input())

# 입력 + 연산
count = 0                       #그룹단어 개수 세기 

for _ in range(n):              #n번 반복 
    word = input().rstrip()     #word를 넣어주기 
    if is_group_word(word):     #만약 그룹 단어라면 (리턴값이 True라면)
        count += 1              #그룹단어 개수 +1 

# 출력
print(count)                    #그룹 단어 개수 출력 
