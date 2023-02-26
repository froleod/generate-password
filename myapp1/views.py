from django.shortcuts import render
import random
from myapp1.models import Worker


def index_page(request):
    # worker_to_change = Worker.objects.get(id=2)
    # worker_to_change.second_name = 'New_second'
    # worker_to_change.save()
    # all_workers = Worker.objects.all()
    # Worker.objects.get(id=1).delete()
    # for i in all_workers:
    #     print(i.second_name, i.name, i.salary)

    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    num = list('0123456789')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters + num)

    return render(request, 'password.html', {'password': thepassword})


