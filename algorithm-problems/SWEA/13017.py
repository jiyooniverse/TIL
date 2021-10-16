# 13017 이진수2

T = int(input())
for tc in range(T):
    # 0 < N < 1
    _, N = input().split('.')
    decimal_num = 10**len(N)    # 소수점 자리수
    N = int(N)

    # 2진수 자리수 13개 넘으면 overflow 출력
    num_10 = 0
    for i in range(1, 14):
        _N = (2**i) * N
        if _N % decimal_num == 0:
            num_10 = _N // decimal_num
            break

    if i > 12:
        print(f'#{tc + 1} overflow')
    else:
        num_2 = ''
        while num_10:
            num_2 = f'{num_10 % 2}'+num_2
            num_10 //= 2

        print(f'#{tc + 1} {int(num_2):0{i}d}')


## 다른 풀이
# 이진수2
t = int(input())

for tc in range(t):
    num = float(input())
    bi = 1 # bi : 확인할 자릿수
    cnt = 1
    ret = ""
    while num:
        bi /= 2 # 자릿수를 1개 내려줌
        if num >= bi :
            # 확인할 자릿수가 존재한다면
            ret += "1"
            num -= bi
        else :
            ret += "0"
        if cnt > 12:
            ret = "overflow"
            break
        cnt += 1
    print(f"#{tc + 1} {ret}")
"""
실수 2가지 32bit, 64bit용
-유효자릿수 6자리, 12자리
"""