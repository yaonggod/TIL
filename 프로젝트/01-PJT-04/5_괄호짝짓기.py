import sys

sys.stdin = open("_괄호짝짓기.txt")
for x in range(1, 11):
    length = int(input())
    gwalho = input()
    # 스택을 4개 만들어서 4가지 종류의 괄호 관리
    # ()
    stack_1 = []
    # []
    stack_2 = []
    # {}
    stack_3 = []
    # <>
    stack_4 = []
    result = False
    for i in range(length):
        if gwalho[i] == '(':
            stack_1.append('(')
        elif gwalho[i] == '[':
            stack_2.append('[')
        elif gwalho[i] == '{':
            stack_3.append('{')
        elif gwalho[i] == '<':
            stack_4.append('<')
        # 닫는 괄호는 pop이 가능하면 pop하고 그렇지 않으면 break
        elif gwalho[i] == ')':
            try:
                stack_1.pop()
            except:
                break
        elif gwalho[i] == ']':
            try:
                stack_2.pop()
            except:
                break
        elif gwalho[i] == '}':
            try:
                stack_3.pop()
            except:
                break
        else:
            try:
                stack_4.pop()
            except:
                break
    # 모든 스택이 비어있을 시에만 True로 설정
    if len(stack_1) == len(stack_2) == len(stack_3) == len(stack_4) == 0:
        result = True
    if result:
        print('#{}'.format(x), 1)
    else:
        print('#{}'.format(x), 0)  