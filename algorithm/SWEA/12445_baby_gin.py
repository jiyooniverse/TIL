# Baby Gin
T = int(input())

for test_case in range(T):
    numbers = list(map(int, input().strip()))
    counts_list = [0]*12
    result = 'Lose'

    for number in numbers:
        counts_list[number] += 1
    # 1. 2개의 triplet
    if counts_list.count(3) == 2 or counts_list.count(6) == 1:
        result = 'Baby Gin'
    # 2. 1개의 triplet
    if counts_list.count(3) == 1:
        if counts_list.count(1) == 3:
            start_number = counts_list.index(1)
            if counts_list[start_number+1] == 1 and counts_list[start_number+2] == 1:
                result = 'Baby Gin'
    elif counts_list.count(4) == 1:
        if counts_list.count(1) == 2:
            start_number = counts_list.index(1)
            count_four_number = counts_list.index(4)
            if count_four_number < start_number:
                if counts_list[count_four_number+1] == 1 and counts_list[count_four_number+2] == 1:
                    result = 'Baby Gin'
            else:
                if (start_number+1 == count_four_number) and counts_list[count_four_number+1] == 1:
                    result = 'Baby Gin'
                elif counts_list[start_number+1] == 1:
                    result = 'Baby Gin'
    # 3. 2개의 run
    run_count = 0
    tmp_list = counts_list[:]
    for i in range(len(counts_list)-2):
        if counts_list[i] == 0:
            continue

        while tmp_list[i] > 0:
            if tmp_list[i+1] != 0 and tmp_list[i+2] != 0:
                tmp_list[i] -= 1
                tmp_list[i + 1] -= 1
                tmp_list[i + 2] -= 1
                run_count += 1
            else:
                break

    if run_count == 2:
        result = 'Baby Gin'

    print(f'#{test_case+1} {result}')
