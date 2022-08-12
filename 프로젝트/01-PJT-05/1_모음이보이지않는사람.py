import sys

sys.stdin = open("_모음이보이지않는사람.txt")
t = int(input())
for i in range(1, t + 1):
    word = input()
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for letter in aeiou:
        word = word.replace(letter, '')
    print('#{}'.format(i), word)