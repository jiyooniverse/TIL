# SWEA 1244 최대 상금
T = int(input())
for tc in range(T):
    num, cnt = input().split()

    num_list = set()
    num_list.add(num)
    for _ in range(int(cnt)):
        new_list = set()
        for n in num_list:
            # 한 번씩 바꿔서 모든 수 new_list에 넣기
            n_arr = list(n)
            for i in range(len(n) - 1):
                for j in range(i + 1, len(n)):
                    tmp = n_arr[:]
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    tmp_n = ''.join(s for s in tmp)
                    new_list.add(tmp_n)
        num_list = new_list

    res = max(num_list)
    print(f'#{tc + 1} {res}')


## 다른 사람 코드
def dfs(now, cnt=0):
    # 길이끝났는데 아직 교환 횟수가 남았을 때를 위해서
    # 미리 가능한 경우들 확인하기
    if (k - cnt) % 2 == 0:
        # 짝수번 남았으면 지금 수도 가능한 경우 수이므로 미리 비교
        num = int("".join(map(str, num_list)))
        ans = max(ans, num)

    # now번까지 오는데, cnt번 교환
    global ans
    if cnt == k:
        # 정확히 k번 사용 끝.
        num = int("".join(map(str, num_list)))
        ans = max(ans, num)
        return
    if now >= len(num_list):
        return

    # 1. now번째 교환 x
    dfs(now + 1, cnt)

    for i in range(now + 1, len(num_list)):
        # i : now번째랑 교환해 줄 위치
        num_list[now], num_list[i] = num_list[i], num_list[now]
        dfs(now + 1, cnt + 1)
        # 복구
        num_list[now], num_list[i] = num_list[i], num_list[now]


t = int(input())
for tc in range(t):
    num, k = input().split()
    num_list = list(map(int, str(num)))
    ans = -1
    dfs(0)
    print(f'{tc + 1} {ans}')
