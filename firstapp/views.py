from django.shortcuts import render
from random import randint
import random
list=["Живопись XVIII – первой половины XIX вв." , "Живопись второй половины XIX века - начала XXI века" , "Живопись первой половины XIX века " , "Искусство новейших течений" , "Скульптура XX – XXI вв." , "Декоративно-прикладное искусство" , "Скульптура XVIII – начала XX вв." , "Народное искусство" , "Галерея портретов Романовых" , "Древнейшие памятники культуры и искусства Евразии" , "Залы Невской парадной анфилады, Малахитовый зал, Ротонда" , "Живопись Испании" , "Искусство Дневнего Рима" , "Культура и искусство России второй половины XVIII в." , "Живопись Фландрии" , "Древние письменности Ближнего и Среднего Востока" ,
      "Готторпский (Большой Академический) глобус" , "Петровская Кунсткамера, или Башня знаний" , "Имперский зал: Многонародная Россия" , "Первая астрономическая обсерватория Академии наук" , "Ближний и Средний Восток" , "Китай" , "Монголия" , "Северная Америка" , "Пасхальное яйцо Курочка" , "Пасхальное яйцо «Ландыши»" , "Табакерка презентационная с портретом императора Николая II" , "Пасхальное яйцо «Ренессанс»" , "Пасхальное яйцо «Лавровое дерево»" , "Пасхальное яйцо «Бутон розы»" , "Зажигалка настольная «Волк»" , "Настольные часы-календарь"]
rusmuzmuseam="Русский музей"
ermitajmuseam="Эрмитаж"
kuntskameramuseam="Кунтскамера"
faberjemuseam="Музей Фаберже"
def art(list):
    num=randint(0,31)
    artifact=list[num]
    if artifact=="Живопись XVIII – первой половины XIX вв." or artifact=="Живопись второй половины XIX века - начала XXI века" or artifact=="Живопись первой половины XIX века "or artifact=="Искусство новейших течений" or artifact=="Скульптура XX – XXI вв." or artifact=="Декоративно-прикладное искусство" or artifact=="Скульптура XVIII – начала XX вв." or artifact=="Народное искусство":
     museam="Русский музей"
    elif artifact=="Галерея портретов Романовых" or artifact=="Древнейшие памятники культуры и искусства Евразии" or artifact=="Залы Невской парадной анфилады, Малахитовый зал, Ротонда" or artifact=="Живопись Испании" or artifact=="Искусство Дневнего Рима" or artifact=="Культура и искусство России второй половины XVIII в." or artifact=="Живопись Фландрии" or artifact=="Древние письменности Ближнего и Среднего Востока" :
     museam="Эрмитаж"
    elif artifact=="Готторпский (Большой Академический) глобус" or artifact=="Петровская Кунсткамера, или Башня знаний" or artifact=="Имперский зал: Многонародная Россия" or artifact=="Первая астрономическая обсерватория Академии наук" or artifact=="Ближний и Средний Восток" or artifact=="Китай" or artifact=="Монголия" or artifact=="Северная Америка":
     museam="Кунтскамера"
    elif  artifact=="Пасхальное яйцо Курочка" or artifact=="Пасхальное яйцо «Ландыши»" or artifact=="Табакерка презентационная с портретом императора Николая II" or artifact=="Пасхальное яйцо «Ренессанс»" or artifact=="Пасхальное яйцо «Лавровое дерево»" or artifact=="Пасхальное яйцо «Бутон розы»" or artifact=="Зажигалка настольная «Волк»" or artifact=="Настольные часы-календарь":
     museam="Музей Фаберже"
    return museam,artifact
def index(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request,'main/catalog.html' , data)

def about(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request,'main/about.html' , data)
def catalog(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request , 'main/catalog.html' , data)
def game(request):
    return render(request, 'main/game.html')
def cuntscamera(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/cuntscamera.html' , data)
def ermitaj(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/ermitaj.html' , data)
def faberje(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/faberje.html' , data)
def rusmuz(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/rusmuz.html' , data)
def peter(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/peter.html' , data)
def era(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/era.html' , data)
def fortress(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/fortress.html' , data)
def pushkin(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/pushkin.html' , data)
def mramor(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/mramor.html' , data)
def zapovednik(request):
    mus,arti=art(list)
    data={
        "museam": mus,
        'artifact': arti,
    }
    return render(request, 'main/zapovednik.html' , data)