from django.shortcuts import render
from django.db.models import Q


from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # # Запрос:
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'description'
    #     ).filter(
    #         # Вернём только те объекты, у которых в поле is_on_main=True
    #         is_on_main=True
    #     ).exclude(
    #         # Исключим только те объекты, у которых is_published=False:
    #         is_published=False 
    #     )
    # # print(ice_cream_list)
    # # Полученный из БД QuerySet передаём в словарь контекста:

    # Контрольный тест
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        Q(is_published=True) &
        (Q(is_on_main=True) | Q(title__icontains='пломбир'))
    ).order_by('title')[1:4]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
