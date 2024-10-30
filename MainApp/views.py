from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]

def home(request):
    # print(f'{vars(request)=}')

    # text = """
    # <h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>
    # """

    # name = "Ходылева О.И."
    # text = f'<h1>"Изучаем django"</h1><p><strong>Автор</strong>: <i>{name}</i>'
    # return HttpResponse(text)

    # return render(request, "index.html")

    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    author = {
    "name": "Иван",
    "middle_name": "Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
    }
    # text = f"""
    # Имя: <b>{autor["Имя"]}</b><br>
    # Отчество: <b>{autor["Отчество"]}</b><br>
    # Фамилия: <b>{autor["Фамилия"]}</b><br>
    # телефон: <b>{autor["телефон"]}</b><br>
    # email: <b>{autor["email"]}</b><br>
    # """
    # return HttpResponse(text)

    return render(request, "about.html", {"author": author})


def get_item(request, item_id:int):
    # """ По указанному id возвращаем имя элемента"""
    # find = False
    # for it in items:
    #     if it['id'] == item_id:
    #         find = True
    #         name = it['name']
    #         quantity = it['quantity']
    # if find:
    #     #text = str(n)
    #     text = f'<strong>Название: </strong> <i>{name}</i><br>'
    #     text += f'<strong>Количество: </strong> <i>{quantity}</i>'
    #     text += f'<p><a href="/items">Назад к списку товаров</a></p>'
    # else:
    #     text = f'Товар с id={item_id} не найден'
    #     #HttpResponseNotFound
    # return HttpResponse(text)

    # item = next((item for item in items if item['id'] == item_id), None)
    # if item is not None:
    #     context = {
    #         "item": item
    #     }
    #     return render(request, "item_page.html", context)
    # return HttpResponseNotFound(f'Товар с id={item_id} не найден')

    # """ По указанному id возвращаем элемент из БД"""
    # item = Item.objects.filter(pk=item_id)
    # if item is not None:
    #     item = Item.objects.get(pk=item_id)
    #     context = {
    #         "item": item
    #     }
    #     return render(request, "item_page.html", context)
    # return HttpResponseNotFound(f'Товар с id={item_id} не найден')

    """ По указанному id возвращаем элемент из БД"""
    try:
        item = Item.objects.get(pk=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар с id={item_id} не найден')
    else:
        context = { "item": item }
        return render(request, "item_page.html", context)


def items_list(request):
    # text = '<ol>'
    # for it in items:
    #     n = it['id']
    #     name = it['name']
    #     quantity = it['quantity']
    #     text += f'<li><a href="/item/{n}">{name}</a> : <strong>{quantity}</strong></li>'
    # text += '</ol>'  
    # return HttpResponse(text)

    # context = {
    #     "items": items
    # }
    # return render(request, "items_list.html", context)

    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "items_list.html", context)

