import sys
input = sys.stdin.readline

"""
 [나무 자르기]

 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값은?
 -> 절단기의 높이가 k(임의의 값)일 때, M미터의 나무를 집에 가져갈 수 있는가?

 left: 절단기의 최소 높이 -> 0
 right: 절단기의 최대 높이 -> 주어진 나무 중 가장 높은 나무 높이
"""

# 내림차순으로 정렬된 리스트에서 height보다 값이 큰 요소들에 대해 각 길이와 height의 차를 모두 더해서 리턴
def cut_tree(height, tree):     
    total = 0   #total 0으로 초기화 

    for h in tree:      #트리의 원소만큼 반복 
        if h <= height:     #높이가 나무의 높이보다 크거나 작은 경우 
            return total    #total 리턴 
        total += h - height         #total에다가 h-height 더하기 
    
    return total        #total 리턴 

def binary_search(target, tree):
    left = 1
    right = tree[0]

    while left <= right:    #최소 높이가 최대 높이보다 작은 경우 
        mid = (left + right) // 2   #그 중심 구하기 
        if cut_tree(mid, tree) >= target:   #만약 집에 가져가야하는 양이 cut_tree 값보다 작거나 같은 경우 
            left = mid + 1      #최소 높이는 중간+1 
        else:   #아닌 경우 
            right = mid - 1     #최대 높이는 중간-1

    return left - 1     #최소 높이-1 리턴 

# 입력
n, m = map(int, input().split())
tree = list(map(int, input().split())) # 나무의 높이를 tree에 저장 
tree.sort(reverse=True) # 내림차순 정렬
print(binary_search(m, tree))
