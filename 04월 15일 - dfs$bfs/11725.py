import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

"""
[트리의 부모 찾기]

- 1번 노드에서 출발해서 탐색
- 루트 노드에서 출발 했기 때문에, 현재 노드의 부모는 이전 노드가 된다.
- (주의) 트리 노드의 최대 수가 100,000이므로, 가능한 트리의 최대 깊이는 100,000번이 된다. 즉, 재귀 깊이 또한 100,000번이 되므로 재귀 깊이 제한을 재설정 해야한다.
"""

def dfs_recursion(prev, curr):
    if parent[curr]:       #만약 curr 인덱스의 부모가 true일 때 리턴 
        return
    
    parent[curr] = prev    #curr 인덱스의 부모는 prev로 바꿈 

    for next in adj_list[curr]:        #adj_list[curr]에서 반복 
        dfs_recursion(curr, next)      #dfs_recursion(curr,next) 실행 후 리턴 
    return

n = int(input())       # n의 노드의 개수 
adj_list = [list() for _ in range(n+1)]    #adj_list 입력 
parent = [0] * (n + 1)     #parent 리스트 n+1개 생성 [0]로 

for _ in range(n-1):               #n-1 반복 
    a, b = map(int, input().split()) #a,b dlqfur 
    adj_list[a].append(b)  3 ajd_list[a]는 b 추가, adj_list[b]는 a 추가 
    adj_list[b].append(a)

dfs_recursion(1, 1)   # 1번 노드는 루트노드이므로, 부모를 자기 자신으로 설정
print(*parent[2:], sep='\n')    #parent의 2 인덱스부터 끝까지의 포인터 출력 
