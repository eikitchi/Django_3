import os

from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView

from config import settings
from main.forms import ProductForm, VersionForm
from main.models import Product, Version


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
    form_class = ProductForm
    template_name = 'main/product_form_with_formset.html'
    # fields = ('name', 'description', 'preview', 'category', 'price', 'date_create', 'date_change')
    success_url = reverse_lazy('main:product_list')

    def get_success_url(self, *args, **kwargs):
        return reverse('main:product_update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('main:product_list')


class VersionListView(ListView):
    model = Version


def info(request):
    context = {
        'title': 'Контакты',

    }
    return render(request, 'main/info.html')
