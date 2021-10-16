# BOJ 2564 경비원

w, h = map(int, input().split())
n = int(input())

pos = [[0] * 2 for _ in range(n + 1)]
for i in range(n + 1):
    pos[i] = list(map(int, input().split()))

    total = 0
for j in range(n):
    if pos[n][0] == pos[j][0]:
        total += abs(pos[n][1] - pos[j][1])
    elif (pos[n][0] + pos[j][0]) == 3: # 상하 평행
        total += h
        if pos[n][1] + pos[j][1] < 2 * w - (pos[n][1] + pos[j][1]):
            total += pos[n][1] + pos[j][1]
        else:
            total += 2 * w - (pos[n][1] + pos[j][1])
    elif (pos[n][0] + pos[j][0]) == 7: # 좌우 평행
        total += w
        if pos[n][1] + pos[j][1] < 2 * h - (pos[n][1] + pos[j][1]):
            total += pos[n][1] + pos[j][1]
        else:
            total += 2 * h - (pos[n][1] + pos[j][1])
    else:   # 다른 인접한 경우들
        if pos[n][0] == 1:
            total += pos[j][1]
            if pos[j][0] == 3:
                total += pos[n][1]
            else:
                total += w - pos[n][1]
        elif pos[n][0] == 2:
            total += (h - pos[j][1])
            if pos[j][0] == 3:
                total += pos[n][1]
            else:
                total += w - pos[n][1]
        elif pos[n][0] == 3:
            total += pos[j][1]
            if pos[j][0] == 1:
                total += pos[n][1]
            else:
                total += h - pos[n][1]
        elif pos[n][0] == 4:
            total += (w - pos[j][1])
            if pos[j][0] == 1:
                total += pos[n][1]
            else:
                total += h - pos[n][1]
print(total)
