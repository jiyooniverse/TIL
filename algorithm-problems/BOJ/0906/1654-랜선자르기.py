# BOJ 1654 랜선자르기
import sys
k, n = map(int, sys.stdin.readline().split())

rope = []
for i in range(k):
    rope.append(int(sys.stdin.readline()))

start = result = 1
end = max(rope)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        r = rope[i]
        cnt += r // mid
    if cnt >= n:
        if result < mid:
            result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
