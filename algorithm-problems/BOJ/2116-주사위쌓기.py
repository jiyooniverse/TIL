# 주사위 쌓기
N = int(input())

# 이중배열로 input 받기
dice_list = []
for _ in range(N):
    dice = list(map(int, input().split()))
    dice_list.append(dice)

def check_max(top, bottom):
    num_list = list(range(1, 7))
    num_list.remove(top)
    num_list.remove(bottom)

    return max(num_list)

max_sum = 0
opposite_side = [5, 3, 4, 1, 2, 0]  #  (0, 5), (1, 3), (2, 4)
# 맨 아래 주사위의 6면을 돌아가며 계산한다.
for i in range(6):
    sum = 0  
    # top, bottom 제외하고 가장 큰 수를 옆면으로 놓는다.
    top_side = dice_list[0][i]
    bottom_side = dice_list[0][opposite_side[i]]
    sum += check_max(top_side, bottom_side)
    for count in range(1, N):
        bottom_side = top_side 

        bottom_side_index = dice_list[count].index(bottom_side)
        top_side_index = opposite_side[bottom_side_index]
        top_side = dice_list[count][top_side_index]
        sum += check_max(top_side, bottom_side)
    
    if max_sum < sum:
        max_sum = sum

print(max_sum)

