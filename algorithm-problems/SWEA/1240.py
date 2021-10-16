# 1240 bit 연산 및 진수
DAT = {int('0001101', 2): '0',
       int('0011001', 2): '1',
       int('0010011', 2): '2',
       int('0111101', 2): '3',
       int('0100011', 2): '4',
       int('0110001', 2): '5',
       int('0101111', 2): '6',
       int('0111011', 2): '7',
       int('0110111', 2): '8',
       int('0001011', 2): '9'
}

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data_list = [input().rstrip() for _ in range(N)]
    for data in data_list:
        if int(data) != 0:
            break

    i = 1
    while M - i and data[M - i] == '0':
        i += 1

    result = ''
    for j in range(M-i+1-56, M-i+1, 7):
        now = int(data[j: j+7], 2)
        if now in DAT:
            result += DAT[now]

    sum = 0
    sum1 = 0
    for k in range(8):
        sum1 += int(result[k])
        if k % 2 == 0:
            sum += int(result[k]) * 3
        else:
            sum += int(result[k])

    if sum % 10 == 0:
        print(f'#{tc + 1} {sum1}')
    else:
        print(f'#{tc + 1} 0')


