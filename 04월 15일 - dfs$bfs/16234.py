import sys
from collections import deque
input = sys.stdin.readline

"""
[인구이동]

0. 인구이동이 일어날 수 있는 나라(처음에는 모든 나라)의 좌표를 좌표 큐에 저장
1. bfs 탐색을 통해 연합을 확인하고, 연합에 포함된 나라의 인구이동을 진행한다.
2. 인구 이동이 있었던 나라는 다음 날에도 인구이동이 시작될 수 있으므로 좌표 큐에 다시 넣어준다.
    -> 직전 이동이 있었던 나라에 대해서만 bfs 탐색 진행
    - 인구 이동이 일어나지 않은 두 나라 사이에서는 다음 날에도 인구이동이 일어날 수 없음
3. 인구이동이 전혀 일어나지 않을 때까지 반복

"""

def bfs(n, left, right, i, j, day):
    dr = [-1, 1, 0, 0] 
    dc = [0, 0, -1, 1]

    que = deque()              #que = deque() 생성
    que.append((i, j))         #que에 (i,j) 추가 
    total = 0   # 연합의 인구 수 합계
    count = 0   # 연합에 포함된 나라의 수
    cord = []   # 연합에 포함된 나라의 좌표
    
    while que:                 #que가 NULL면 
        r, c = que.popleft()   #r,c 를 que에서 빼서 가져오기 
        count += 1             #count 1 증가 
        total += board[r][c]   #total에 [r][c] 나라의 인원 수 추가 
        cord.append((r, c))    #corddp (r,c) 추가 

        for x in range(4):     #4만큼 반복 
            new_r = r + dr[x]  #new_r = r+dr의 x인덱스
            new_c = c + dc[x]  #new_c = c+dc의 x인덱스 
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c] == day:
                continue       d#만약 new_r과 new_c가 0보다 크거나 같고 n보다 작거나 [new_r][new_c]가 day와 동일하지 않을 경우 countinue  

            # 이 때 여기서 visited에 표기를 하면 안됨
            # 현재는 조건에 맞지 않지만, 이후에 연합에 있는 다른 나라에 의해 연합에 들어올 수 있음

            if left <= abs(board[new_r][new_c] - board[r][c]) <= right:
                que.append((new_r, new_c))
                visited[new_r][new_c] = day
            #만약 두 나라의 인구수의 차이가 left와 right의 사이일 경우, que에 (new_r, new_c)를 추가하고 visited[new_r][new_c]에  day 입력 

    # 적어도 나라 2개 이상이 모여야 연합을 이루었다고 볼 수 있음
    if count > 1:      #만약 count 가 1 이상일 경우 평균 = total // count 
        avg = total // count
        # 인구 이동
        for r, c in cord:  # corddml r,c 반복 
            board[r][c] = avg #[r][c]의 나라의 인구수는 agv로 바뀜 
            # 인구의 이동이 있는 나라는 다음 이동이 시작될 가능성이 있음
            countries.append((r, c))   #contries에 (r,c)를 추가 
    
    return count > 1   #count>1 일 경우(연합 존재) ture 리턴, 아닐 경우 Flase 리턴 

def simulation(n, left, right):
    day = 0        # day = 0 
    while True: # 무한 반복 
        size = len(countries)   # 이번에 탐색할 수 있는 나라의 수
        flag = False   #flag가 false 라면 day 1 증가 
        day += 1
        for _ in range(size): #탐색할 수 있는 나라의 수 만큼 반복 
            i, j = countries.popleft()     # contries에서 i,j 빼오기 
            if visited[i][j] == day:       #만약 visited[i][j]가 day와 동일하다면 continue 
                continue
            visited[i][j] = day            #visited[i][j]를 day로 바꾸기 
            if bfs(n, left, right, i, j, day):   # bfs 결과 true면 연합을 이루었다는 의미이므로 flag 표시
                flag = True                # flag는 ture로 설정 

        if not flag:               #만약 flag가 false 일 때 day -1 리턴 
            return day - 1

# 입력
n, left, right = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 방문배열
visited = [[0]*n for _ in range(n)]
# 나라
countries = deque([(i, j) for i in range(n) for j in range(n)])

# 연산 + 출력
print(simulation(n, left, right))
