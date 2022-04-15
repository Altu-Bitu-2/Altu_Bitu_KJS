import sys
input = sys.stdin.readline

"""
[주유소]

최대한 가격이 싼 곳에서 많은 기름을 넣어야 한다.
따라서 첫번째 도시부터 현재까지 가장 싼 가격을 저장하고, 이동에 필요한만큼만 기름을 채운다.
이렇게 하면 지금까지 지나 온 도시 중 가장 싼 곳에서 최대한 많이 살 수 있다.
"""

def calc_min_cost(n, road, price):
    cost = 0
    min_price = price[0]
    dist = 0

    for city in range(n - 1):  #n-1번 반복 
        cost += min_price * road[city]     #코스트에 최소 가격과 도시를 가는 도로의 길이를 곱한 값을 더하기 
        if price[city + 1] < min_price:    #만약 최소 가격보다 그 다음 도시의 주유소 리터당 가격이 크면 
            min_price = price[city + 1]    #최소 가격이 그 가격으로 바뀐다.

    return cost        #코스트 리턴 

# 입력
n = int(input())   #도시 개수 저장 
road = list(map(int, input().split()))     #도로의 길이 저장 
price = list(map(int, input().split()))    #리터당 가격 저장 

# 연산 + 출력
print(calc_min_cost(n, road, price))        #최소 코스트 출력 
