import sys

sys.stdin = open("_퍼펙트셔플.txt")
t = int(input())
for i in range(1, t + 1):
    n = int(input())
    lst = list(map(str, input().split()))
    # 홀수인 경우 첫 번째 리스트를 두 번째 리스트보다 하나 더 길게
    lst1 = lst[:(n + 1) // 2]
    lst2 = lst[(n + 1) // 2:]
    print('#{}'.format(i), end = ' ')
    # 짧은 리스트 길이 기준 순서대로 일단 출력
    for j in range(len(lst2)):
        print(lst1[j], lst2[j], end = ' ')
    # 긴 리스트에 남아있으면 그것도 마저 출력
    if n % 2 == 1:
        print(lst1[-1], end = ' ')
    print()
    