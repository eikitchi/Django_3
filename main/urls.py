from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import home, info, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionListView, CategoriesListView
from main.apps import MainConfig
from config import settings

app_name = MainConfig.name
urlpatterns = [

    path('', cache_page(60)(home), name='home'),
    path('contacts/', info, name='contacts'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('categories/', cache_page(60)(CategoriesListView.as_view()), name='categories_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_item'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/versions/<int:pk>/', VersionListView.as_view(), name='version'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)