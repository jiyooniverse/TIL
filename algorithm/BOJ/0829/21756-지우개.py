N = int(input())

arr = list(range(N + 1))

while len(arr) > 2:
    new_arr = arr[::2]
    arr = new_arr[:]

print(arr[1])