# 14719 빗물
R, C = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
left = arr[0]
right = arr[-1]

i = j = 1
while i + j < C:
    if left < right:
        if left > arr[j]:
            total += left - arr[j]
        else:
            left = arr[j]
        j += 1

    else:
        if right > arr[C-1-i]:
            total += right - arr[C-1-i]
        else:
            right = arr[C-1-i]
        i += 1

print(total)


