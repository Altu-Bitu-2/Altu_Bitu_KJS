import sys
from collections import deque
input = sys.stdin.readline

"""
[숨바꼭질]

 x좌표 위에서 x-1, x+1, 2*x의 위치로 계속 이동하며 탐색
 가장 빠른 시간을 찾아야 하므로 주변 노드부터 탐색하는 풀이로 풀어서 k에 도달하면 바로 탐색 종료 (bfs)
"""
SIZE = 10**5 #size는 100000 

def bfs(n, k):
    time = [-1] * (SIZE + 1)   #size+1만큼 [-1]생성 
    que = deque()  # que = deque() 생성 
    que.append(n)  #que에 수빈이의 위치인 n 추가 
    time[n] = 0    #time[n] = 0 초기화 

    while que:         #que가 null일 때까지 반복 
        curr = que.popleft()   #curr = que에서 뺀 값 
        if curr == k:          #만약 curr이 k와 동일하다면 time[curr] 리턴 
            return time[curr]
        
        for next in (curr * 2, curr + 1, curr - 1):        #curr의 제곱, curr+1, curr-1 을 넣어서 총 3번 반복 
            if next < 0 or next > SIZE or time[next] > -1: #만약 next가 0보다 작거나, size보다 크거나, time[next]가 -1보다 클 경우 countiue  
                continue
            time[next] = time[curr] + 1        #time[next]에 time[curr]+1 입력 
            que.append(next)           #que에 next 추가 

# 입력
n, k = map(int, input().split())
# 연산 + 출력
print(bfs(n, k))
