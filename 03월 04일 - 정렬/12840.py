import sys

input = sys.stdin.readline

h, m, s = map(int, input().split())

q = int(input())

for i in range(q):
    array = list(map(int, input().split()))
    if array[0] == 3:
        print(h, m, s)

    else :
        time = 60*60*h + 60*m + s
        if array[0] == 1:
            time += array[1]
        else :
            time -= array[1]
            if time < 0:
                time += 24*60*60
        time = time%(24*60*60)
        h = time//3600
        m = (time%3600)//60
        s = time%60
