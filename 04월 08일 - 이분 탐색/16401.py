Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import sys
input = sys.stdin.readline

"""
 [과자 나눠주기]

 n개의 과자가 있을 때 m명의 조카에게 각각 같은 길이로 줄 수 있는 과자의 최대 길이를 구하는 문제
 -> 특정 과자 길이에 대하여 m명의 조카에게 나누어 줄 수 있는가?

 left: 과자 길이의 최솟값 -> 1
 right: 과자 길이의 최댓값
"""

# 내림차순 정렬된 snacks 리스트에서 length 길이의 과자를 몇개 만들 수 있는지 개수를 세어 리턴하는 함수
def split_snack(length, snacks):
    count = 0   #count 0 초기화 
    for l in snacks:    #snacks의 길이에서 
        if l < length:   #만약 과자의 길이가 length보다 작으면 
            return count    #count 리턴 
        count += l // length    #카운트에 l//length 값 추가 

    return count    #count 리턴 

def binary_search(m, snacks):
    left = 1        #최솟값은 1 
    right = snacks[0]   #최대값은 snacks[0] 
    while left <= right:    #최댓값이 최솟값보다 크거나 같은 경우 
        mid = (left + right) // 2   #중간값 구하기 
        if split_snack(mid, snacks) >= m:    #split_snack 값이 조카의 수보다 같거나 클 때 
            left = mid + 1  #최솟값은 중간+1 
        else:   #아닐 경우 
            right = mid - 1     #최댓값은 중간 -1 
    return left - 1     #최솟값 -1 리턴 

m, n = map(int, input().split())        
snacks = list(map(int, input().split()))    #과자의 길이를 snacks에 저장 
snacks.sort(reverse=True)   # 내림차순 정렬

print(binary_search(m, snacks))