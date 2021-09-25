# 간단한 소인수 분해

T = int(input())

for test_case in range(T):
    N = int(input())
    a = b = c = d = e = 0   # 초기화

    # a 구하기
    while N % 2 == 0:
        N //= 2
        a += 1

    while N % 3 == 0:
        N //= 3
        b += 1

    while N % 5 == 0:
        N //= 5
        c += 1

    while N % 7 == 0:
        N //= 7
        d += 1

    while N % 11 == 0:
        N //= 11
        e += 1

    print(f'#{test_case + 1} {a} {b} {c} {d} {e}')


# T = int(input())
# for tc in range(T):
#     N = int(input())
#     divide = [2, 3, 5, 7, 11]
#     cnt = [0] * 5
#     # divide : 소인수 분해를 위해 나눠줄 소수
#     # 2로 나눠본다
#     for i in range(len(divide)):
#         while N > 0 and N % divide[i] == 0 :
#             N //= divide[i] # <- / 소수점까지 계산, float : 데이터 처리 속도가 느린
#             cnt[i] += 1
#     print("#{} ".format(tc + 1), end = '')
#     for i in cnt:
#         print("{} ".format(i), end='')
#     print("")