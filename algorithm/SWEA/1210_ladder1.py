# SWEA Ladder1
T = 10
size = 100
for test_case in range(T):
    num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(size)]

    curr_i = size - 1
    for row in range(size):   # 출발점 (0 ~ 99)
        curr_j = row
        if ladder[curr_i][curr_j] == 2:
            break

    while curr_i >= 0:
        # 옆에 길이 있나 확인하고 움직임
        if 0 <= (curr_j + 1) < size and ladder[curr_i][curr_j + 1] == 1:
            next_ladder = ladder[curr_i][curr_j + 1]
            ladder[curr_i][curr_j] = 0 # 지나온 곳 사다리 끊어
            curr_j += 1
        elif 0 <= (curr_j - 1) < size and ladder[curr_i][curr_j - 1] == 1:
            ladder[curr_i][curr_j] = 0 # 지나온 곳 사다리 끊어
            curr_j -= 1
        else:   # 옆에 길이 없으면 위로 이동
            curr_i -= 1

    print(f"#{test_case + 1} {curr_j}")
