import sys
from math import gcd        #최대공약수를 구해주는 함수 

n,m = map(int, sys.stdin.readline().split(':'))      #:을 기점으로 두 수를 정수로 저장 
gcd_nm = gcd(n,m)                   # 두 수의 최대공약수 구하기 

print(str(int(n//gcd_nm))+":"+str(int(m//gcd_nm)))  #최대공약수로 나눈 수 출력 
