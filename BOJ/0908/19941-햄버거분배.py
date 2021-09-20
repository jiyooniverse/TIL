# BOJ 19941 햄버거 분배
n, k = map(int, input().split())
arr = list(input())
check = [0] * n
check1 = [0] * n
cnt = cnt1 = 0
for i in range(n):
    if arr[i] == 'P':
        for j in range(-k, k + 1):
            if 0 <= i + j < n and arr[i + j] == 'H' and check[i + j] == 0:
                check[i + j] = 1
                cnt += 1
                break
        for jj in range(-k, k + 1):
            if 0 <= i - jj < n and arr[i - jj] == 'H' and check1[i - jj] == 0:
                check1[i - jj] = 1
                cnt1 += 1
                break

if cnt > cnt1:
    print(cnt)
else:
    print(cnt1)

