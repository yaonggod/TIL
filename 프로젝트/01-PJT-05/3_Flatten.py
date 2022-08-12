import sys

sys.stdin = open("_Flatten.txt")
for i in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))
    for _ in range(n):
        # 이미 평탄화된 상태
        if len(set(boxes)) == 1:
            print('#{}'.format(i), 0)
            break
        # 평탄화
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        
    else:
        print('#{}'.format(i), max(boxes) - min(boxes))