import sys

sys.stdin = open("_최빈수구하기.txt")

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    score_lst = list(map(int, input().split()))
    # 학생들의 점수 분포를 딕셔너리로 만듬
    score_dict = {k : 0 for k in range(101)}
    for j in range(len(score_lst)):
        score_dict[score_lst[j]] += 1
    
    # 최빈수의 빈도수를 max_count에, 최빈수를 max_key에 저장
    # 최빈수가 여러 개면 뒤에 나오는 점수를 출력하므로 break를 걸 필요가 없이 끝까지 순회하면 됨
    max_count = 0
    max_key = 0
    for key in score_dict:
        if score_dict[key] >= max_count:
            max_count = score_dict[key]
            max_key = key
    print("#{}".format(i), max_key)
