# min max

T = int(input())

for test_case in range(T):
    N = int(input())
    list_a = list(map(int, input().split()))
    min_val = list_a[0]
    max_val = list_a[0]

    for element in list_a:
        if element < min_val:
            min_val = element

        if element > max_val:
            max_val = element

    result = max_val - min_val
    print(f'#{test_case+1} {result}')
