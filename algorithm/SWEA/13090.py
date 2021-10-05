# 13090 베이비진 게임
T = int(input())
for tc in range(T):
    cards = list(map(int, input().split()))
    player1 = cards[0::2]
    player2 = cards[1::2]

    winner = 0
    check1 = [0] * 12
    check2 = [0] * 12
    for i in range(len(player1)):
        num1 = player1[i]
        num2 = player2[i]

        check1[num1] += 1
        if check1[num1] == 3:
            winner = 1
            break
        if check1[num1] >= 1 and check1[num1 + 1] >= 1 and check1[num1 + 2] >= 1:
            winner = 1
            break
        if num1 > 0 and check1[num1] >= 1 and check1[num1 + 1] >= 1 and check1[num1 - 1] >= 1:
            winner = 1
            break
        if num1 > 1 and check1[num1] >= 1 and check1[num1 - 1] >= 1 and check1[num1 - 2] >= 1:
            winner = 1
            break

        check2[num2] += 1
        if check2[num2] == 3:
            winner = 2
            break
        if check2[num2] >= 1 and check2[num2 + 1] >= 1 and check2[num2 + 2] >= 1:
            winner = 2
            break
        if num2 > 0 and check2[num2] >= 1 and check2[num2 + 1] >= 1 and check2[num2 - 1] >= 1:
            winner = 2
            break
        if num2 > 1 and check2[num2] >= 1 and check2[num2 - 1] >= 1 and check2[num2 - 2] >= 1:
            winner = 2
            break

    print(f'#{tc + 1} {winner}')
