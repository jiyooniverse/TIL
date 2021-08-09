switch_count = int(input())
switch_status = list(map(int, input().split()))
switch_status.insert(0,100)
N = int(input())
for i in range(N):
    student, pos = map(int, input().split())
    if student == 1:    # 남자이면
        for m in range(pos, switch_count+1, pos):
            switch_status[m] = (switch_status[m] + 1) % 2
    else:   # 여자이면
        switch_status[pos] = (switch_status[pos] + 1) % 2
        for n in range(1, switch_count):
            if (pos - n) > 0 and (pos + n) < switch_count + 1:
                if switch_status[pos - n] == switch_status[pos + n]:
                    switch_status[pos - n] = (switch_status[pos - n] + 1) % 2
                    switch_status[pos + n] = switch_status[pos - n]
                else:
                    break
            else:
                break

# 20개씩 print
for i in range(1, switch_count+1):
    print(switch_status[i], end=' ')
    if (i % 20) == 0 and i != switch_count:
        print()