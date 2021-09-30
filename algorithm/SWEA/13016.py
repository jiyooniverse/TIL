# 13016 이진수
def binary(n):
    if n == 0:
        res = 0
    else:
        res = ''
    while n:
        res = f'{n % 2}' + res
        n //= 2

    return int(res)


T = int(input())
for tc in range(T):
    N, num = input().split()

    result = ''
    for i in range(int(N)):
        result += f'{binary(int(num[i], 16)):04d}'

    print(f'#{tc + 1} {result}')

## 다른 코드
T = int(input().rstrip())

for tc in range(T):
    n, num_16 = input().split()
    n = int(n)
    for i in range(n):
        now = num_16[i]
        # 10 진수로 변환
        now_10 = 0
        if '0' <= now <= '9':
            now_10 = ord(now) - ord('0')
        else:
            # 'A' ~ 'F' = 10 ~ 15
            now_10 = ord(now) - ord('A') + 10

        # 2진수로 변경하기
        for j in range(3, -1, -1):
            # 'N & (1 << j)'는 j자리 비트 추출
            if now_10 & (1 << j) == 0:
                print(0, end='')
            else:
                print(1, end='')
    print()





## 다른 코드 1
T = int(input())
for tc in range(T):
    n, a = input().split()
    print(f'#{tc+1}', end=' ')
    for i in a:
        result = ''
        x = int(i, 16)
        for j in range(4):
            result += str(x % 2)
            x = x // 2
        print(result[::-1], end='')
    print()

## 다른 코드 2
def make_binary4(num):
    binary_rtn = ''
    while num > 0:
        if num % 2:
            binary_rtn = '1' + binary_rtn
        else:
            binary_rtn = '0' + binary_rtn
        num //= 2

    binary_rtn = '0' * (4 - len(binary_rtn)) + binary_rtn

    return binary_rtn


T = int(input())
for tc in range(1, T + 1):
    N, hexadecimal = input().split()
    N = int(N)
    hexadecimal_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    binary_str = ''
    print(f'#{tc} ', end='')
    for h in hexadecimal:
        if h.isdigit():
            h = int(h)
        else:
            h = hexadecimal_dict[h]
        print(make_binary4(h), end='')
    print()