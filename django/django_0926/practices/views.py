from django.shortcuts import render
from random import randint, choice
# Create your views here.

def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # name = request.GET.get('ball')
    # context = {'name' : name}
    return render(request, 'pong.html', context={'ball' : request.GET.get('ball')})

def nct(request):
    return render(request, 'nct.html')

def nctmatch(request):
    random_num = randint(0, 100)
    name = request.GET.get('name')
    if name == '':
        name = request.GET.get('nct')
    print(name)
    context = {
        'num' : random_num,
        'name' : name,
        'me' : request.GET.get('me')
    }
    return render(request, 'nctmatch.html', context)

def is_odd_even(request, number):
    result = '짝수'
    if number % 2 == 1:
        result = '홀수'
    context = {
        'num' : number,
        'result' : result
    }
    return render(request, 'is_odd_even.html', context)

def calculate(request, n1, n2):
    context = {
        'n1' : n1,
        'n2' : n2,
        'plus' : n1 + n2,
        'minus' : n1 - n2,
        'mult' : n1 * n2,
        'divide' : n1 // n2
    }
    return render(request, 'calculate.html', context)

def lorem(request):
    return render(request, 'lorem.html')

def lorem_result(request):
    text_lst = ['태일', '쟈니', '태용', '유타', '쿤', '도영', '텐', '재현', '윈윈', '정우', '루카스', '마크', '샤오쥔', '헨드리', '런쥔', '제노', '해찬', '재민', '양양', '쇼타로', '성찬', '천러', '지성']
    texts = []
    n1 = int(request.GET.get('n1'))
    n2 = int(request.GET.get('n2'))
    for _ in range(n1):
        text_part = ''
        for _ in range(n2):
            text_part += choice(text_lst)
            text_part += " "
        texts.append(text_part)
    context = {
        'n1' : n1, 
        'n2' : n2,
        'texts' : texts
    }
    return render(request, 'lorem_result.html', context)


