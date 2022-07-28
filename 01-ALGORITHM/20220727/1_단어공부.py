# https://www.acmicpc.net/problem/1157
word = input()
alphabet = [0 for _ in range(26)]

# 알파벳을 소문자로 통일, 아스키코드로 바꾸기
for i in word:
    i = i.lower()
    alphabet[ord(i) - 97] += 1
   
max_alphabet = max(alphabet)
# 알파벳 개수의 최대값이 여러개이면 ? 출력
if alphabet.count(max_alphabet) != 1:
    print("?")
# 알파벳의 아스키코드를 대문자 알파벳으로 변환
else:
    max_alphabet_index = alphabet.index(max_alphabet)
    print(chr(max_alphabet_index + 97).upper())