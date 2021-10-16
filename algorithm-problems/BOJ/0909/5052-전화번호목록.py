# BOJ 5052 전화번호 목록
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    res = 0
    n = int(sys.stdin.readline())
    # 길이로 정렬하고 짧은 길이부터 비교 패턴으로 사용해서 비교
    numbers = [sys.stdin.readline().rstrip() for _ in range(n)]
    numbers.sort()

    for i in range(n-1):
        if res == 1:
            break
        for j in range(i + 1, n):
            # 접두어인지만 확인
            if numbers[i] == numbers[j][:len(numbers[i])]:
                res = 1
                break
    if res == 1:
        print('NO')
    else:
        print('YES')

