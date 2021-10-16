# 1931 회의실 배정
import sys
N = int(sys.stdin.readline())

schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 끝나는 순서로 정렬해준다.
schedule.sort()
schedule.sort(key=lambda x:x[1])
# 내가 직접 sort하면 시간초과 발생함

cnt = 1 # 회의 수, 0번 회의는 무조건 한다.
end = schedule[0][1]    # 0번 회의 끝나는 시간

for i in range(1, N):
    if end <= schedule[i][0]:
        cnt += 1
        end = schedule[i][1]

print(cnt)