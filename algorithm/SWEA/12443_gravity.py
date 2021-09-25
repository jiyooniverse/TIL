# Gravity

test_case = int(input())
for t in range(test_case):
    N = int(input())
    Height = list(map(int, input().split()))
    max_count = 0   # 최대 낙차를 넣을 변수
    for i in range(N-1):    # 마지막 column은 오른쪽으로 뒤집으면 바닥이 된다.
        count = 0
        for j in range(i+1, N):
            if Height[i] > Height[j]:
                count += 1

        if count > max_count:
            max_count = count

    print(f'#{t+1} {max_count}')