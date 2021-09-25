# BOJ 13458 시험 감독
import sys
N = int(input())    # 시험장
students = list(map(int, sys.stdin.readline().split()))  # 응시자
B, C = map(int, sys.stdin.readline().split())    # 총, 부

cnt = N # 총 감독관 한명씩 배치
for i in range(N):
    students[i] -= B
    if students[i] <= 0:
        continue

    if students[i] % C == 0:
        cnt += students[i] // C
    else:
        cnt += students[i] // C + 1


print(cnt)