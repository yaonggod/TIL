from django.shortcuts import render
from random import randint, sample

# Create your views here.
def index(request):
    return render(request, "index.html")

def template(request):
    numbers = [1, 2, 3, 4, 5]
    context = {
        'numbers' : numbers   
    }
    return render(request, 'template.html', context)

def todaydinner(request):
    foods = ['라면', '떡볶이', '곱창', '삼겹살', '피자', '치킨', '햄버거']
    images = ['https://health.chosun.com/site/data/img_dir/2021/10/26/2021102601968_0.jpg',
              'https://doewxs707ovkc.cloudfront.net/v3/prod/image/item/mainpage/907/ad4474bef39c4167b84477eaa7a5052f20210708171733.',
              'https://ai.esmplus.com/foodjang01/images/221700262_b_1.jpg',
              'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201702/27/117f5b49-1d09-4550-8ab7-87c0d82614de.jpg',
              'https://cdn.dominos.co.kr/admin/upload/goods/20200311_x8StB1t3.jpg',
              'https://t1.daumcdn.net/cfile/tistory/2403BA485896A5C829',
              'http://www.thekpm.com/news/photo/202201/106072_86332_1730.jpg'
              ]
    random_number = randint(0, len(foods) - 1)
    context = {
        'foods' : foods,
        'images' : images,
        'random_number' : random_number
    }
    return render(request, 'todaydinner.html', context)

def lotto(request):
    lottos = []
    for i in range(5):
        lottos.append(sample(range(1, 45), 7))
    win = [3, 11, 15, 29, 35, 44, 10]
    for lotto in lottos:
        count = 0
        bonus = 0
        for i in range(6):
            if lotto[i] in win:
                count += 1
        if lotto[6] == win[6]:
            bonus = 1
        if count == 6:
            lotto.append('1등')
        elif count == 5 and bonus == 1:
            lotto.append("2등")
        elif count == 5:
            lotto.append("3등")
        elif count == 4:
            lotto.append('4등')
        elif count == 3:
            lotto.append('5등')
        else:
            lotto.append('꽝')
                    
    context = {
        'lottos' : lottos
    }
    return render(request, 'lotto.html', context)