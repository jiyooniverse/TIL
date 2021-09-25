# BOJ 2578 빙고

N = 5
# 내 보드판 숫자를 입력 받는다.
my_board = [list(map(int, input().split())) for _ in range(N)]

# 사회자가 부를 숫자를 입력 받는다.
count = result = 0
for line_num in range(N):
    numbers = list(map(int, input().split()))   # 5개씩 한줄에 입력받는다.
    for index in range(N):  # 입력받은 5개를 하나씩 my_board와 비교
        num_flag = 0    # 숫자를 찾을 경우 이중 for문을 나오기 위해 사용한다.
        for i in range(N):
            if num_flag == 1:
                break
            for j in range(N):
                if my_board[i][j] == numbers[index]:
                    num_flag = 1
                    my_board[i][j] = -1
                    # column, row, 대각선1, 대각선2 빙고인지 확인
                    sum_x = sum_y = sum_1 = sum_2 = 0
                    for k in range(N):
                        sum_x += my_board[i][k]
                        sum_y += my_board[k][j]
                        if i == j:
                            sum_1 += my_board[k][k]
                        if (i + j) == N - 1:
                            sum_2 += my_board[k][N-1-k]
                    if sum_x == -5:
                        count += 1
                    if sum_y == -5:
                        count += 1
                    if sum_1 == -5:
                        count += 1
                    if sum_2 == -5:
                        count += 1

        # 선이 세개 이상이면 빙고
        if count >= 3:
            result = (line_num * N) + (index + 1)
            break
    if result != 0:
        break

print(result)
