import sys

sys.stdin = open("_문자열의거울상.txt")

t = int(input())
for i in range(1, t + 1):
    word = input()
    # 문자열의 순서를 뒤집은 상태에서 거울 뒤집기
    word_reverse = word[::-1]
    # 거울 뒤집기 한 후 word_mirror에 더하기
    word_mirror = ''
    for j in range(len(word_reverse)):
        if word_reverse[j] == 'q':
            word_mirror += 'p'
        elif word_reverse[j] == 'p':
            word_mirror += 'q'
        elif word_reverse[j] == 'b':
            word_mirror += 'd'
        else:
            word_mirror += 'b'
    print("#{}".format(i), word_mirror)