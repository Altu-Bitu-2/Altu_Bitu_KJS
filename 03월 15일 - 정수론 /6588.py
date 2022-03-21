import sys

array = [True for i in range(1000001)]      #1000001개의 칸을 가진 배열 만들기 : 소수판별을 위해 

for i in range(2,1001):
    if array[i]:
        for j in range(i+i, 1000001, i):
            array[j] = False               #앞에 수의 배수는 지우기 

while True:
    N = int(sys.stdin.readline())

    if N == 0 :
        break

    for i in range(3, 1000001):        
                   if array[i] and array[N-i]:      #i, N-1 번째가 True(소수)이면 통과 
                       print(N, "=", i, "+", N-i)
                       break
