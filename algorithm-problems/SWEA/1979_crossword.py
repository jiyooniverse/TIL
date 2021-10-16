# SWEA 단어 어디 들어가

T = int(input())

for test_case in range(T):
    # n: 가로세로 길이, k: eksdj rlfdl
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    blank_list = []
    for i in range(n):
        # 한 줄씩 읽으면서 연속인 빈칸 개수 세기

        blank_row = blank_col = 0
        for j in range(n):
            # 가로로 읽기
            if puzzle[i][j] == 1:
                blank_row += 1
            elif blank_row != 0:
                blank_list += [blank_row]
                blank_row = 0
            # 세로로 읽기
            if puzzle[j][i] == 1:
                blank_col += 1
            elif blank_col != 0:
                blank_list += [blank_col]
                blank_col = 0

        if blank_row != 0:
            blank_list += [blank_row]
        if blank_col != 0:
            blank_list += [blank_col]

    for b in blank_list:
        if b == k:
            count += 1

    print(f"#{test_case + 1} {count}")