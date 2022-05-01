import sys
input = sys.stdin.readline

"""
 [좋다]

 1. 각 수마다 양 쪽 끝에서 포인터를 시작해서 좁혀오면서 어떤 '다른 두 수'가 현재 수를 만들 수 있는지 검사
 2. 포인터를 차례로 옮기며 검사하기 위해 미리 수를 오름차순 정렬함
 3. 현재 만드려는 수의 위치와 left, right 포인터 위치가 겹칠 경우 처리 주의
 4. left와 right의 초기화 주의 -> 음수가 존재하므로, 지금 검사하는 수 보다 큰 수도 포함될 수 있음
"""

# 좋은 수의 개수를 세는 함수(투 포인터)
def count_good_numbers(n, nums):
    count = 0                       #count = 0 초기화 

    for i in range(n):              #'각 수의 개수'만큼 반복 
        p1 = 0                      #p1 = 0로 초기화 
        p2 = n - 1                  #p2 = n-1로 초기화 

        while p1 < p2:              #p1가 p2보다 작으면 반복 
            if p1 == i:             #만약 p1이 i와 같으면 p1가 1 증가 이후 다시 반복 
                p1 += 1
                continue
            if p2 == i:             #만약 p2가 i와 같으면 p2가 1 감소 이후 다시 반복 
                p2 -= 1
                continue

            if nums[p1] + nums[p2] == nums[i]:  #만약 p1와 p2의 인덱스를 가진 nums를 더한 것이 i의 인덱스를 가진 nums와 동일하다면 count 1 증가 이후 멈춤  
                count += 1                  
                break                           
            if nums[p1] + nums[p2] < nums[i]:   #만약 p1와 p2의 인덱스를 가진 nums를 더한 것이 i의 인덱스를 가진 nums보다 작다면 p1 1 증가 
                p1 += 1
            else:                               #만약 p1와 p2의 인덱스를 가진 nums를 더한 것이 i의 인덱스를 가진 nums보다 크다면 p2 1 감소
                p2 -= 1

    return count                    #count 리턴 

# 입력
n = int(input())
nums = list(map(int, input().split()))
nums.sort() # 오름차순 정렬

# 연산 + 출력
print(count_good_numbers(n, nums))
