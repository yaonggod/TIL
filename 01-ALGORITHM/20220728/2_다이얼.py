# https://www.acmicpc.net/problem/5622

word = input()
number_lst = []

for i in range(len(word)):
    if word[i] == "A" or word[i] == "B" or word[i] == "C":
        number_lst.append(3)
    elif word[i] == "D" or word[i] == "E" or word[i] == "F":
        number_lst.append(4)
    elif word[i] == "G" or word[i] == "H" or word[i] == "I":
        number_lst.append(5)
    elif word[i] == "J" or word[i] == "K" or word[i] == "L":
        number_lst.append(6)
    elif word[i] == "M" or word[i] == "N" or word[i] == "O":
        number_lst.append(7)
    elif word[i] == "P" or word[i] == "Q" or word[i] == "R" or word[i] == "S":
        number_lst.append(8)
    elif word[i] == "T" or word[i] == "U" or word[i] == "V":
        number_lst.append(9)
    else:
        number_lst.append(10)
        
print(sum(number_lst))