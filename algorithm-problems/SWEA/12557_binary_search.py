# SWEA 이진 탐색
T = int(input())

for test_case in range(T):
    # 전체 페이지 수, a가 찾을 페이지, b가 찾을 페이지
    n, pa, pb = map(int, input().split())
    start_a = start_b = 1
    end_a = end_b = n

    result = '0'
    while start_a <= end_a or start_b <= end_b:
        middle_a = (start_a + end_a) // 2
        middle_b = (start_b + end_b) // 2

        if middle_a == pa and middle_b == pb:
            result = '0'
            break
        elif middle_a == pa:
            result = 'A'
            break
        elif middle_b == pb:
            result = 'B'
            break

        if middle_a > pa:
            end_a = middle_a
        else:
            start_a = middle_a

        if middle_b > pb:
            end_b = middle_b
        else:
            start_b = middle_b

    print(f"#{test_case + 1} {result}")
#      middle - 1/ middle + 1로 계산하면 오답인지 ??????
#      -> 문제에서 middle에서부터 시작/ 끝으로 지정하여서 그럼.