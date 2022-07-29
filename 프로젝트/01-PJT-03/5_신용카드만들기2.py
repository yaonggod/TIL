import sys

sys.stdin = open("_신용카드만들기2.txt")

t = int(input())
for i in range(1, t + 1):
    # 문자열 인덱싱을 하기 위해 문자열 형태로 입력받음
    card = input()
    # 카드 번호가 -로 나눠져 있을 시 split 후 card_num이라는 문자열로 새로 합성해줌
    # - 없는 문자열일 시 card를 그대로 card_num으로 입력
    if '-' in card:
        card_num = ''
        card_list = card.split('-')
        for j in range(len(card_list)):
            card_num += card_list[j]
    else:
        card_num = card
    
    # 숫자의 개수가 16개가 아닐 시 불가능
    # 숫자의 개수가 16개일 시 맨 앞자리 수 검증 필요
    if len(card_num) == 16:
        # 문자열로 받았으므로 문자열로 일치 여부 확인
        if card_num[0] in ['3', '4', '5', '6', '9']:
            print("#{}".format(i), 1)
        else:
            print("#{}".format(i), 0)
    else:
        print("#{}".format(i), 0)