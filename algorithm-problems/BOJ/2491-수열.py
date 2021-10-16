# BOJ 2491 수열
n = int(input())
arr = list(map(int, input().split()))

max_cnt = 1
cnt = 1
for i in range(n - 1):
    if arr[i] <= arr[i + 1]:
        cnt += 1
    else:
        cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt


arr2 = arr[::-1]
cnt2 = 1
for i in range(n - 1):
    if arr2[i] <= arr2[i + 1]:
        cnt2 += 1
    else:
        cnt2 = 1
    if max_cnt < cnt2:
        max_cnt = cnt2

print(max_cnt)
