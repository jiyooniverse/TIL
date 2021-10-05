# 13070 컨테이너 운반
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    weight.sort(reverse=True)
    truck.sort(reverse=True)
    # 트럭 1개당 1개의 짐을 옮길 수 있음
    check = [0] * N
    total = 0
    for t in truck:
        for i in range(len(weight)):
            if check[i] != 0:
                continue
            if t >= weight[i]:
                # 담을 수 있는 가장 무거운 짐을 담는다.
                total += weight[i]
                check[i] = 1
                break

    print(f'#{tc + 1} {total}')