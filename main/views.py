import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from config import settings
from main.models import Product


# Create your views here.
def home(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context = {
        'product_list': Product.objects.all()[:3],
        'title': 'Главная',
        'images': img_list
    }
    return render(request, 'main/home.html', context)


class ProductListView(generic.ListView):
    model = Product
    extra_context = {'title': 'Список продукции'}


def products(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context = {
        'product_list': Product.objects.all(),
        'title': 'Список продукции',
        'images': img_list
    }
    return render(request, 'main/product_list.html', context)


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item
    }
    return render(request, 'main/product_detail.html', context)


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price', 'date_create', 'date_change')
    success_url = reverse_lazy('main:product_list')


class ProductUpdateView(generic.UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price', 'date_create', 'date_change')
    success_url = reverse_lazy('main:product_list')


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('main:product_list')


def info(request):
    context = {
        'title': 'Контакты',

    }
    return render(request, 'main/info.html')
