# BOJ 14696 딱지놀이

# 별 - 동그라미 - 네모 - 세모 순으로 비교
n = int(input())    # 라운드 수

for i in range(n):
    a_cnt = [0] * 5
    b_cnt = [0] * 5

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for aa in a[1::]:
        a_cnt[aa] += 1
    for bb in b[1::]:
        b_cnt[bb] += 1

    result = 'D'
    for m in range(4, 0, -1):
        if a_cnt[m] > b_cnt[m]:
            # A가 이긴다.
            result = 'A'
            break
        elif a_cnt[m] < b_cnt[m]:
            # B가 이긴다.
            result = 'B'
            break
        else:
            continue
    print(result)