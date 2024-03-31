from django.contrib import admin

# Из модуля models импортируем модуль Category...
from .models import Category, IceCream, Topping, Wrapper

# Register your models here.

# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (
        # какие поля будут показаны на странице списка объектов;
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        # какие поля можно редактировать прямо на странице списка объектов;
        'is_published',
        'is_on_main',
        'category'
    )
    search_fielbs = (
        # кортеж с перечнем полей, по которым будет проводиться поиск.
        # Форма поиска отображается над списком элементов;
        'title',
    )
    list_filter = (
        # кортеж с полями, по которым можно фильтровать записи.
        # Фильтры отобразятся справа от списка элементов;
        'category',
    )
    list_display_links = (
        # поля, при клике на которые можно перейти на страницу просмотра и
        # редактирования записи. По умолчанию такой ссылкой служит первое
        # отображаемое поле.
        'title',
    )
    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выыодиться строка "Не задано"
    empty_value_display = 'Не задано'

    # Для Топпингов
    # Изменим интерфейс так, чтобы связанные записи можно было перекладывать из
    # одного окошка в другое. Такой интерфейс называется filter_horizontal
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (IceCreamInline,)
    list_display = ('title',)


# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'
# ...и регистрируем её в админке:
admin.site.register(Topping)
admin.site.register(Wrapper)
# admin.site.register(IceCream)
# admin.site.register(Category)
# Регистрируем новый класс:
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно использовать класс IceCreamAdmin
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
