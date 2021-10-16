# 4311 오래된 스마트폰
# from collections import deque

def dfs(path=[]):
    # 중복 순열
    if 0 < len(path) <= 3:
        new_num = ''.join(str(s) for s in path)
        new_nums.add(int(new_num))
        if len(path) == 3:
            return

    for i in range(N):
        dfs(path + [nums[i]])


T = int(input())
for tc in range(T):
    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    op_nums = list(map(int, input().split()))    # 1: +, 2: -, 3: *, 4: //
    target_num = int(input())

    new_nums = set(nums[:])
    dfs()
    new_nums = list(new_nums)
    new_nums = sorted(new_nums)
    nums2 = []
    v = [-1] * 1000
    # numcombi(0, 0)
    # if nums2.sort() == new_nums.sort():
    #     de = 1
    # de = 1

    # 1. 숫자 조합으로만 가능한 경우
    cnt1 = -1
    if target_num in new_nums:
        cnt1 = len(str(target_num))
        print(f'#{tc + 1} {cnt1}')
        continue

    # 2. 연산자 이용
    q = [] #deque()
    check = [0] * 1000

    # 초기값
    for i in range(len(new_nums)):
        q.append([new_nums[i], len(str(new_nums[i]))])  # 숫자 누르는 것 1회
        # nums들로 만드는 숫자 , 횟수는 nums의 길이
        check[new_nums[i]] = len(str(new_nums[i]))

    cnt2 = -1
    while q:
        now = q.pop(0)
        if now[0] == target_num:    # 원하는 숫자
            # 최소 횟수 구하기
            cnt2 = check[target_num] + 1
            break

        for n in new_nums:  # 누를 수 있는 번호
            for op_num in op_nums:  # 누를 수 있는 연산자
                if op_num == 1:
                    next = now[0] + n
                elif op_num == 2:
                    next = now[0] - n
                elif op_num == 3:
                    next = now[0] * n
                elif op_num == 4 and n != 0:    # 0으로 못 나눔
                    next = now[0] // n

                # next는 0~999사이 숫자이고 이미 계산했던거면 중복되니까 빼
                # ++++아니면 있는데 지금 계산 한 것이 더 빨리 구한거야 그럼 넣어
                if 0 <= next < 1000 and (check[next] == 0 or check[next] > check[now[0]] + 1 + len(str(n))):
                    check[next] = check[now[0]] + 1 + len(str(n))
                    if check[next] > M:
                        continue
                    q.append([next, now[1] + 1 + len(str(n))])

    if cnt2 > M:
        cnt2 = -1

    print(f'#{tc + 1} {cnt2}')


