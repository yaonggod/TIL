import sys

sys.stdin = open("_민석이의과제체크하기.txt")
t = int(input())
for x in range(1, t + 1):
    n, k = map(int, input().split())
    # 전체 학생 리스트
    student = [i for i in range(1, n + 1)]
    # 숙제 제출한 학생 리스트
    homework = list(map(int, input().split()))
    
    print('#{}'.format(x), end = ' ')
    # homework에 학생 번호가 없으면 제출 안함
    for i in range(1, n + 1):
        if i not in homework:
            print(i, end = ' ')
    print()