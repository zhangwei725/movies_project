from django.shortcuts import render

from apps.home.models import Film


def index(request):
    films = Film.objects.values('id', 'name', 'image', 'type_name', 'update_time')
    return render(request, 'index.html', locals())


# http://127.0.0.1:8000/home/detail/45/
def detail(request, id):
    film = Film.objects.get(id=int(id))
    return render(request, 'detail.html', locals())
