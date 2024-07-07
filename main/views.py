from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Широкий асортимент продукції українських та зарубіжних виробників горілки часто вводить в оману навіть найдосвідченіших любителів спиртних напоїв'
    }
    return render(request, 'main/about.html', context)
