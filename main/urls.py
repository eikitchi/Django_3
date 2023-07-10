from django.conf.urls.static import static
from django.urls import path
from main.views import home, info
from main.apps import MainConfig
from config import settings

app_name = MainConfig.name
urlpatterns = [

    path('', home, name='home'),
    path('contacts/', info, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)