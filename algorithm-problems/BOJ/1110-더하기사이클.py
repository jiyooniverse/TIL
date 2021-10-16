# BOJ 1110 더하기 사이클
N = int(input())

a = N // 10     # 10의 자리
b = N % 10      # 1의 자리
k = a + b

M = b * 10 + k % 10

cnt = 1
while N != M:
    cnt += 1
    X = M
    a = X // 10  # 10의 자리
    b = X % 10  # 1의 자리
    k = a + b
    M = b * 10+ k % 10

print(cnt)