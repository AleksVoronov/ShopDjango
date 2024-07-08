from django.shortcuts import render

from items.models import Category
# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Широкий асортимент продукції українських та зарубіжних виробників горілки часто вводить в оману навіть найдосвідченіших любителів спиртних напоїв'
    }
    return render(request, 'main/about.html', context)
