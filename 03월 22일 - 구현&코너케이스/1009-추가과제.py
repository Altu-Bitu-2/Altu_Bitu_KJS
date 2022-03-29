import sys
input = sys.stdin.readline

"""
[분산처리]
- a^b의 일의 자리를 구하는 문제
- 일의 자리는 0~9 중 하나 이므로, 어떤 수를 계속 곱해 나가면 일의 자리는 패턴을 가지게 되어 있음
    ex) 2 -> 4 -> 8 -> 6 -> 2 ... 
- 0~9까지 일의 자리 패턴을 미리 구한 후, (b % 패턴의 길이)번째 수를 출력하면 된다.
- 0이 나올 경우 10번 컴퓨터가 처리하므로, 0이 출력되지 않도록 예외처리
"""



last_digit = [[i] for i in range(10)]   # 0부터 9까지의 패턴
size = []                               # 패턴의 길이

for i in range(10):     #10가지의 수에 대한 일의 자리 패턴 구하기
    temp = i            #temp에 i 넣기 
    while i != (temp * i) % 10:     #temp에 i를 곱한 값의 일의 자리가 i가 아닐 경우 
        temp *= i                   #temp에 i를 곱하기 
        temp %= 10                  #temp의 일의 자리 구하기 
        last_digit[i].append(temp)  #맞는 패턴에 일의 자리를 넣기 
    size.append(len(last_digit[i])) #패턴의 길이 넣기 
        
# 입력
t = int(input())

# 입력 + 연산
for _ in range(t):                      #t만큼 반복 
    a, b = map(int, input().split())    
    a %= 10                             #a에 일의 자리 넣기 

    if a == 0:                          #0일 경우 10의 배수이므로 10 출력 
        print(10)
        continue

    print(last_digit[a][b%size[a] - 1]) #a의 패턴에서 (b%길이)번째 수를 출력 
