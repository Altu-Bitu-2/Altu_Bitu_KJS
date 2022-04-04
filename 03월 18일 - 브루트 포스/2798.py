N, M = map(int, input().split())        #N, M 입력받기

nums = list(map(int, input().split()))  #숫자들 입력받기
ans = []                                #정답 후보들

for i in range(N):                      #숫자들에서 3개씩 더한 값을 M과 비교해서 넘지 않는 숫자들을 ans에 입력
    for j in range(i+1,N):
        for k in range(j+1,N):
            if nums[i]+nums[j]+nums[k] <= M:
                ans.append(nums[i]+nums[j]+nums[k])
                
ans.sort(reverse=True)      #정답후보 내림차순으로 정렬 
print(ans[0])               #정렬한 값 중 첫번째 값 출력 (가장 큰 값)
