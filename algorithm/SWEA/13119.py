# 4366 정식이의 은행업무

T = int(input())
for tc in range(T):
    a = input()    # 2진수
    b = input()    # 3진수

    # a 무조건 한자리 틀리다
    # b 무조건 한자리 틀리다
    a_10 = int(a, 2)
    for i in range(len(a)):
        # a 한자리씩 바꿔서
        new_a = a_10 ^ (1 << i)
        ans = new_a
        cnt = 0   # b 자리수랑 비교하기
        index = len(b) - 1
        while new_a:
            if cnt > 1:
                # 자리수 다른 부분이 1개 넘으면 그냥 종료
                break
            if index < 0 or new_a % 3 != int(b[index]):
                cnt += 1
            new_a //= 3
            index -= 1

        if cnt == 1 and index < 0:
            # 얘가 답이다
            print(f'#{tc + 1} {ans}')


