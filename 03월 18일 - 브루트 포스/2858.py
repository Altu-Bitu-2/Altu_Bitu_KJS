R, B = map(int, input().split())        #R,B 입력받기 

area = R+B                      #R과 B을 더한 값 = 넓이 

for i in range(3,area//2):      #넓이를 어떤 수를 나눴을 때 나머지가 0인 수들을 구하기 
    if area % i == 0:
        if (i-2)*(area//i-2) == B:  #갈색 부분의 넓이를 구한 후 B와 같은지 확인 
            print(area//i, i)
            break
