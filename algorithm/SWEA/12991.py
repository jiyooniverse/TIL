# 12991 이진수 3의 배수
def factorial(n):
    res = 1
    for k in range(1, n + 1):
        res *= k
    return res


T = int(input())
for tc in range(T):
    result = 0
    N, K = map(int, input().split())

    # i개 만큼 짝수 선택
    factorial(0)
    for i in range(K + 1):
        if (2 * i - K) % 3 == 0:
            even = factorial(N//2) // factorial(i) // factorial((N//2 - i))
            odd = factorial(N - N//2) // factorial(K - i) // factorial(N - N//2 - K + i)
            result += even * odd

    print(f'#{tc + 1} {result}')


## DP 사용하기

combi = [([-1] * 51) for _ in range(51)]    # 50자리 수에서 i선택개수 0 ~ 50
def calc_combi(nn, kk):
    if nn < kk: return 0
    if kk == 0: return 1
    if kk == nn: return 1
    if kk == 1: return nn

    if combi[nn][kk] != -1:
        return combi[nn][kk]
    #combi[nn][kk] = combi[nn - 1][kk] + combi[nn -1][kk - 1]
    now = calc_combi(nn - 1, kk) + calc_combi(nn - 1, kk - 1)
    combi[nn][kk] = now
    return now

T = int(input())
for tc in range(T):
    result = 0
    N, K = map(int, input().split())

    # i개 만큼 짝수 선택
    for i in range(K + 1):
        if (2 * i - K) % 3 == 0:
            result = calc_combi(N//2, i) * calc_combi(N - N//2, K - i)

    print(f'#{tc + 1} {result}')