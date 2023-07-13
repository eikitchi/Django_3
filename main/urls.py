from django.conf.urls.static import static
from django.urls import path
from main.views import home, info, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from main.apps import MainConfig
from config import settings

app_name = MainConfig.name
urlpatterns = [

    path('', home, name='home'),
    path('contacts/', info, name='contacts'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_item'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)