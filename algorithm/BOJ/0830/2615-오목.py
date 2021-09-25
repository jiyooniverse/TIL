# BOJ 2615 오목

# 19*19 맵
MAP = [list(map(int, input().split())) for _ in range(19)]

#
winner = 0
pos = []
# 가로 방향 탐색: 같은 수가 5개 연속하여 있는가, 6개가 되지 않는지 추가 확인
for i in range(19):
    if winner != 0:
        break
    for j in range(15):
        # i, j가 시작 point
        if MAP[i][j] == 0:
            continue
        arr = MAP[i]
        if arr[j:j+5].count(MAP[i][j]) == 5:
            # 앞뒤의 번호가 연속하지 않는지 확인
            if j - 1 >= 0:
                if arr[j -1] == MAP[i][j]:
                    continue
            if j + 5 < 19:
                if arr[j + 5] == MAP[i][j]:
                    continue
            winner = MAP[i][j]
            pos = [i, j]
            break


# 세로 방향 탐색
MAP2 = [[0] * 19 for _ in range(19)]
for ii in range(19):
    for jj in range(19):
        MAP2[ii][jj] = MAP[18 - jj][ii]
for i in range(19):
    if winner != 0:
        break
    for j in range(15):
        # i, j가 시작 point
        if MAP2[i][j] == 0:
            continue
        arr = MAP2[i]
        if arr[j:j+5].count(MAP2[i][j]) == 5:
            # 앞뒤의 번호가 연속하지 않는지 확인
            if j - 1 >= 0:
                if arr[j -1] == MAP2[i][j]:
                    continue
            if j + 5 < 19:
                if arr[j + 5] == MAP2[i][j]:
                    continue
            winner = MAP2[i][j]
            # 가로로 회전했기 때문에 맨 끝 점을 가지고 좌표 변환
            pos = [18 - (j + 4), i]
            break

# 좌상향 우하향 대각선
for i in range(19):
    if winner != 0:
        break
    for j in range(19):
        if MAP[i][j] == 0:
            continue
        cnt = 0
        for k in range(5):
            if (i + k) < 19 and (j + k) < 19:
                if MAP[i + k][j + k] == MAP[i][j]:
                    cnt += 1
        if cnt == 5:
            # 앞, 뒤 확인
            if (i - 1) >= 0 and (j - 1) >= 0:
                if MAP[i - 1][j - 1] == MAP[i][j]:
                    continue
            if (i + 5) < 19 and (j + 5) < 19:
                if MAP[i + 5][j + 5] == MAP[i][j]:
                    continue
            winner = MAP[i][j]
            pos = [i, j]
            break

# 우상향 좌하향 대각선
for i in range(19):
    if winner != 0:
        break
    for j in range(19):
        if MAP[i][j] == 0:
            continue
        cnt = 0
        for k in range(5):
            if (i + k) < 19 and (j - k) >= 0:
                if MAP[i + k][j - k] == MAP[i][j]:
                    cnt += 1
        if cnt == 5:
            # 앞, 뒤 확인
            if (i - 1) >= 0 and (j + 1) < 19:
                if MAP[i - 1][j + 1] == MAP[i][j]:
                    continue
            if (i + 5) < 19 and (j - 5) >= 0:
                if MAP[i + 5][j - 5] == MAP[i][j]:
                    continue
            winner = MAP[i][j]
            pos = [i + 4, j - 4]
            break

print(winner)
if winner != 0:
    print(pos[0] + 1, pos[1] + 1)