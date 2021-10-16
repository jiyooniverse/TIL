# BOJ 10610 30
numbers = list(map(int, input()))

# 1) 3으로 안 나눠지면 30으로 안 됨.
if sum(numbers) % 3 != 0:
    print(-1)
else:
    numbers.sort(reverse=True)  # 내림차순 정렬
    # 2) 0이 없으면 30 배수 불가
    if numbers[-1] != 0:
        print(-1)
    else:
        print("".join(str(s) for s in numbers))