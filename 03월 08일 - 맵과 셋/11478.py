S = str(input())  #문자열 입력

con = set()         #세트 생성

for i in range(len(S)):             #부분 문자열의 시작 지점
    for j in range(i, len(S)):      #부분 문자열의 끝 지점
        con.add(S[i:j+1])

        

print(len(con))         #세트 길이 출력 = 세트에 추가된 부분 문자열의 개수 출력
