# 18185 라면사기 (small)
import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a += [0, 0]
i = 0
cost = 0
while i < N:
    # 값을 빼면서도 주르륵 연결이 유지될 수 있도록
    # 가운데 값이 크면 먼저 앞에 두개부터 처리해준다.
    if a[i + 1] > a[i + 2]:
        if 0 <= i < N - 1 and a[i] >= 1 and a[i + 1] >= 1:
            a[i] -= 1
            a[i + 1] -= 1
            # 5원 추가
            cost += 5
        elif 0 <= i < N - 2 and a[i] >= 1 and a[i + 1] >= 1 and a[i + 2] >= 1:
            a[i] -= 1
            a[i + 1] -= 1
            a[i + 2] -= 1
            # 7원 추가
            cost += 7
        elif a[i] >= 1:
            a[i] -= 1
            # 3원 추가
            cost += 3

    else:
        if 0 <= i < N - 2 and a[i] >= 1 and a[i + 1] >= 1 and a[i + 2] >= 1:
            a[i] -= 1
            a[i + 1] -= 1
            a[i + 2] -= 1
            # 7원 추가
            cost += 7
        elif 0 <= i < N - 1 and a[i] >= 1 and a[i + 1] >= 1:
            a[i] -= 1
            a[i + 1] -= 1
            # 5원 추가
            cost += 5
        elif a[i] >= 1:
            a[i] -= 1
            # 3원 추가
            cost += 3

    if a[i] == 0:
        i += 1

print(cost)