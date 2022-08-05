import sys

sys.stdin = open("_조교의성적매기기.txt")
t = int(input())
for x in range(1, t + 1):
    n, k = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(n)]
    # score에 비율을 곱해서 계산한 값과 학생 넘버를 넣은 리스트
    total_score = []
    for i in range(n):
        total_score.append([i + 1, score[i][0] * 0.35 + score[i][1] * 0.45 + score[i][2] * 0.2])
    # total_score를 기준으로 정렬
    total_score.sort(key = lambda x : -x[1])
    # 학생들을 점수 순서대로 정렬한 새로운 리스트 생성
    rank = []
    for i in range(n):
        rank.append(total_score[i][0])
    # k의 등수는 랭크 인덱스에 1을 더한 것, 등수는 1등부터 시작
    rank_k = rank.index(k) + 1
    # k가 상위 몇 퍼센트에 속해있는지
    percentage = rank_k / n
 
    print('#{}'.format(x), end = ' ')
    if percentage <= 0.1:
        print('A+')
    elif percentage <= 0.2:
        print('A0')
    elif percentage <= 0.3:
        print('A-')  
    elif percentage <= 0.4:
        print('B+')    
    elif percentage <= 0.5:
        print('B0')  
    elif percentage <= 0.6:
        print('B-')  
    elif percentage <= 0.7:
        print('C+')  
    elif percentage <= 0.8:
        print('C0')  
    elif percentage <= 0.9:
        print('C-')  
    else:
        print('D0')  
    
    
            
    