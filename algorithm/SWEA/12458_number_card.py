# 숫자 카드

T = int(input())

for test_case in range(T):
    N = int(input())
    cards = list(map(int, input().strip()))

    # 카드의 개수를 셉니다.
    card_count = [0]*10
    for card in cards:
        card_count[card] += 1

    # 개수가 많은 인덱스를 구합니다.
    max_count = -1
    max_num = 0
    for i in range(10):
        if card_count[i] >= max_count:
            max_count = card_count[i];
            max_num = i
    print(f'#{test_case + 1} {max_num} {max_count}')

    # 다른 풀이
    # #####################
    # N = int(input())
    # cards = int(input())
    # card_li = [0] * 10 # 각 카드가 몇개 있는가?
    # while cards > 0:
    #     card = cards % 10   # 추출
    #     cards //= 10         # 뽑고 남은 수
    #     card_li[card] += 1
    #     ## 밑의 코드를 아예 여기서 갱신 가능
    #     if card_li[card] >= max_value:
    #           max_value = card_li[card]
    #           max_index = card
    # 
    # max_value = -1  # 제일 많은 개수
    # max_index = -1  # 제일 많은 개수를 갖는 카드 번호
    # for i in range (10):
    #     if card_li[i] > max_value:
    #         max_value = card_li[i]
    #         max_index = i
    # print("#{} {} {}".format(test_case + 1, max_index, max_value))