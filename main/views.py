from django.shortcuts import render
from main.models import Product


# Create your views here.
def home(request):
    context = {
        'product_list': Product.objects.all()[:4],
        'title': 'Список продуктов'
    }
    return render(request, 'main/home.html', context)


def info(request):
    return render(request, 'main/info.html')