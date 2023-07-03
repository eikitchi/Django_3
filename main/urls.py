from django.urls import path
from main.views import home, info
from main.apps import MainConfig
app_name = MainConfig.name
urlpatterns = [

    path('', home),
    path('contacts/', info),
]